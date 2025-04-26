import json
import random
from time import sleep
from typing import Dict, List, Optional, Union, Any, TypeVar

from jsonschema import validate
from requests import Response, Session
from requests.exceptions import RequestException, Timeout, ConnectionError

from config.config import TestConfig as test_config
from utils.common import CommonUtils as common_utils


T = TypeVar("T")


class EndpointsException(Exception):
    """Base exception for all endpoint-related errors"""


class EndpointConnectionError(EndpointsException):
    """Exception raised for connection errors"""


class EndpointTimeoutError(EndpointsException):
    """Exception raised for timeout errors"""


class EndpointResponseError(EndpointsException):
    """Exception raised for invalid responses"""


class EndpointsBase:
    """
    EndpointsBase - The base class for all endpoint classes.

    This class provides a standardized interface for making API requests and handling responses.
    It supports various HTTP methods, response validation, and pagination.

    Attributes:
        session (Session): HTTP session for making requests
        url (str): Base URL for API requests
        endpoint_base (str): Base path for endpoints
        data (Dict): Request data/payload
        timeout (int): Request timeout in seconds
    """

    # Default trailing slash behavior for different API types
    trailing_slash_map = {"rest": {"get": "", "post": "/", "put": "/", "patch": "/", "delete": ""}, "json": {"get": "", "post": "", "put": "", "patch": "", "delete": ""}}

    def __init__(self, session: Session, url: str, endpoint_base: str = ""):
        """
        Initialize the EndpointsBase instance.

        Args:
            session (Session): HTTP session for making requests
            url (str): Base URL for API requests
            endpoint_base (str, optional): Base path for endpoints. Defaults to "".
        """
        self.session = session
        self.url = url
        self.endpoint_base = endpoint_base
        self.data = None
        self.url_for_request = None
        self.timeout = test_config.REQUEST_TIMEOUT if hasattr(test_config, "REQUEST_TIMEOUT") else 30
        self.max_retries = test_config.MAX_RETRIES if hasattr(test_config, "MAX_RETRIES") else 3

    # region main api calls

    def _request(
        self,
        method: str,
        id_=None,
        expected_status_code=200,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        data=None,
        log_results=False,
        return_json_response=False,
        verify=True,
    ) -> Union[Dict, List, Response]:
        """
        Generic request method that handles all HTTP methods with retry logic.

        Args:
            method (str): HTTP method (get, post, put, patch, delete)
            id_ (Optional): ID for the resource being accessed
            expected_status_code (int): Expected HTTP status code
            params (Optional[Dict]): Query parameters
            headers (Optional[Dict]): HTTP headers
            url (Optional[str]): URL override
            expected_response: Expected response data
            schema: JSON schema for validation
            count_above (int): Minimum count for response items
            count_exactly (int): Exact count for response items
            data (Optional[Dict]): Request payload
            log_results (bool): Flag to log results
            return_json_response (bool): Flag to force JSON response
            verify (bool): Flag to verify response
            return_raw_response (bool): Flag to return raw response

        Returns:
            Union[Dict, List, Response]: Response data or raw response
        """
        self._before_request(method=method, url=url, id_=id_, data=data, params=params)

        # Initialize retry count
        retry_count = 0
        backoff_time = 1  # Start with 1 second backoff

        while retry_count <= self.max_retries:
            try:
                # Make the request with timeout
                if method == "get":
                    raw_response = self.session.get(url=self.url_for_request, params=params, headers=headers, timeout=self.timeout)
                elif method == "post":
                    raw_response = self.session.post(url=self.url_for_request, headers=headers, data=self.data, params=params, timeout=self.timeout)
                elif method == "put":
                    raw_response = self.session.put(url=self.url_for_request, headers=headers, data=self.data, params=params, timeout=self.timeout)
                elif method == "patch":
                    raw_response = self.session.patch(url=self.url_for_request, headers=headers, data=self.data, params=params, timeout=self.timeout)
                elif method == "delete":
                    raw_response = self.session.delete(url=self.url_for_request, headers=headers, data=data, params=params, timeout=self.timeout)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                # Process response
                self._after_request(
                    response=raw_response,
                    log_results=log_results,
                    verify_results=verify,
                    expected_status_code=expected_status_code,
                    expected_response=expected_response,
                    schema=schema,
                    count_above=count_above,
                    count_exactly=count_exactly,
                )

                if return_json_response:
                    return self._construct_response_json(raw_response, return_json_response=return_json_response)
                return raw_response

            except Timeout as e:
                if retry_count == self.max_retries:
                    error_msg = f"Request timed out after {self.max_retries} retries: {str(e)}"
                    common_utils.log(f"ERROR: {error_msg}")
                    raise EndpointTimeoutError(error_msg) from e

            except ConnectionError as e:
                if retry_count == self.max_retries:
                    error_msg = f"Connection error after {self.max_retries} retries: {str(e)}"
                    common_utils.log(f"ERROR: {error_msg}")
                    raise EndpointConnectionError(error_msg) from e

            except RequestException as e:
                if retry_count == self.max_retries:
                    error_msg = f"Request failed after {self.max_retries} retries: {str(e)}"
                    common_utils.log(f"ERROR: {error_msg}")
                    raise EndpointsException(error_msg) from e

            # Increment retry count and log retry attempt
            retry_count += 1
            if retry_count <= self.max_retries:
                common_utils.log(f"Retrying request ({retry_count}/{self.max_retries}) in {backoff_time}s...")
                sleep(backoff_time)
                backoff_time *= 2  # Exponential backoff

    def get(
        self,
        id_=None,
        expected_status_code=200,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        log_results=False,
        return_json_response=True,
        verify=True,
        total_pages_to_get=None,
        filter_name=None,
    ):
        """
        Perform an HTTP GET request.

        Args:
            id_ (Optional): ID for the resource being accessed
            expected_status_code (int): Expected HTTP status code
            params (Optional[Dict]): Query parameters
            headers (Optional[Dict]): HTTP headers
            url (Optional[str]): URL override
            expected_response: Expected response data
            schema: JSON schema for validation
            count_above (int): Minimum count for response items
            count_exactly (int): Exact count for response items
            log_results (bool): Flag to log results
            return_json_response (bool): Flag to force JSON response
            verify (bool): Flag to verify response
            return_raw_response (bool): Flag to return raw response
            total_pages_to_get (Optional[int]): Number of pages to retrieve
            filter_name (Optional[str]): Filter name to append to URL

        Returns:
            Union[Dict, List, Response]: Response data or raw response
        """
        if filter_name:
            url = f"{self.url}?{filter_name}"
        if total_pages_to_get is not None:
            return self._get_multi_page_records(url=url, total_pages_to_get=total_pages_to_get, log_results=log_results)

        return self._request(
            method="get",
            id_=id_,
            expected_status_code=expected_status_code,
            params=params,
            headers=headers,
            url=url,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
            data=None,
            log_results=log_results,
            return_json_response=return_json_response,
            verify=verify,
        )

    def post(
        self,
        id_=None,
        expected_status_code=201,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        data=None,
        log_results=False,
        return_json_response=True,
        verify=True,
    ):
        """Perform an HTTP POST request."""
        return self._request(
            method="post",
            id_=id_,
            expected_status_code=expected_status_code,
            params=params,
            headers=headers,
            url=url,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
            data=data,
            log_results=log_results,
            return_json_response=return_json_response,
            verify=verify,
        )

    def put(
        self,
        id_=None,
        expected_status_code=200,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        data=None,
        log_results=False,
        return_json_response=True,
        verify=True,
    ):
        """Perform an HTTP PUT request."""
        return self._request(
            method="put",
            id_=id_,
            expected_status_code=expected_status_code,
            params=params,
            headers=headers,
            url=url,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
            data=data,
            log_results=log_results,
            return_json_response=return_json_response,
            verify=verify,
        )

    def patch(
        self,
        id_=None,
        expected_status_code=200,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        data=None,
        log_results=False,
        return_json_response=True,
        verify=True,
    ):
        """Perform an HTTP PATCH request."""
        return self._request(
            method="patch",
            id_=id_,
            expected_status_code=expected_status_code,
            params=params,
            headers=headers,
            url=url,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
            data=data,
            log_results=log_results,
            return_json_response=return_json_response,
            verify=verify,
        )

    def delete(
        self,
        id_=None,
        expected_status_code=204,
        params=None,
        headers=None,
        url=None,
        expected_response="",
        schema="",
        count_above=-1,
        count_exactly=-1,
        data=None,
        log_results=False,
        return_json_response=True,
        verify=True,
    ):
        """Perform an HTTP DELETE request."""
        return self._request(
            method="delete",
            id_=id_,
            expected_status_code=expected_status_code,
            params=params,
            headers=headers,
            url=url,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
            data=data,
            log_results=log_results,
            return_json_response=return_json_response,
            verify=verify,
        )

    # endregion

    # region getting records

    def get_random_record_id(self) -> int:
        random_record = self.get_random_record()
        if random_record:
            # Try to get the 'id' field from the record
            record_id = random_record.get("id")
            if record_id:
                return int(record_id)
        return None

    def get_random_record(self, log_results=False) -> Dict:
        response = self.get(log_results=log_results)
        response_json = response.json()
        if self.session.api_type == "rest":
            pages = response_json["num_pages"]
            random_page = random.randint(1, pages)
            response_json = self.get(url=self.url + f"?page={random_page}", log_results=log_results)
        else:
            pages = response_json["meta"]["pagination"]["pages"]
            random_page = random.randint(1, pages)
            response_json = self.get(url=self.url + f"?page[number]={random_page}&page[size]=50", log_results=log_results)
        if len(response_json) == 0:
            return None
        return random.choice(response_json)

    def _get_multi_page_records(self, url=None, total_pages_to_get=3, log_results=False):
        """
        Fetches multiple pages of records from paginated API responses.

        This method handles different pagination formats:
        1. APIs using "num_pages" and "results" (REST style)
        2. APIs using "meta.pagination" and "data" with HATEOAS links (JSON:API style)

        Args:
            url (Optional[str]): URL to fetch data from
            total_pages_to_get (Union[int, str]): Number of pages to get, or "all" for all pages
            log_results (bool): Whether to log results

        Returns:
            List: Combined records from all retrieved pages
        """
        if url is None:
            url = self.url

        # Get first page to determine pagination structure and total pages
        response_json = self.get(return_json_response=True, url=url, log_results=log_results)

        # Initialize collection of all results
        all_records = []

        # Determine pagination format and extract data and pagination info
        if "num_pages" in response_json:
            # REST style pagination
            pagination_style = "rest"
            total_pages = response_json["num_pages"] + 1
            all_records = response_json["results"]
            page_param = "page"

        elif "meta" in response_json and "pagination" in response_json["meta"]:
            # JSON:API style pagination
            pagination_style = "json_api"
            total_pages = response_json["meta"]["pagination"]["pages"] + 1
            all_records = response_json["data"]
            # We'll use the next link directly for JSON:API

        else:
            # No pagination info found, return as is
            return response_json

        # Determine how many pages to fetch
        pages_to_fetch = total_pages
        if total_pages_to_get != "all" and isinstance(total_pages_to_get, (int, float)):
            pages_to_fetch = min(int(total_pages_to_get) + 1, total_pages)

        # Fetch additional pages
        for page_num in range(2, pages_to_fetch):
            try:
                if pagination_style == "rest":
                    # REST style uses page parameter
                    page_part = f"/?{page_param}={page_num}"
                    if "?" in url:
                        page_part = f"&{page_param}={page_num}"
                    next_url = f"{url}{page_part}"

                    response = self.get(url=next_url, log_results=log_results, return_json_response=True)
                    all_records.extend(response["results"])

                elif pagination_style == "json_api":
                    # JSON:API style uses HATEOAS links
                    next_url = response_json["links"]["next"]
                    response_json = self.get(url=next_url, log_results=log_results, return_json_response=True)
                    all_records.extend(response_json["data"])

                # Add a small delay to prevent overwhelming the API
                sleep(0.1)

            except Exception as e:
                error_msg = f"Error fetching page {page_num}: {str(e)}"
                common_utils.log(f"ERROR: {error_msg}")
                # Continue with partial data rather than failing completely

        return all_records

    # endregion

    # region assertions

    def assert_response_count(self, response_json, expected_above, expected_exactly):
        if expected_above > -1:
            error_msg = f"{len(response_json) =} <= {expected_above =}"
            assert len(response_json) > expected_above, error_msg
        if expected_exactly > -1:
            error_msg = f"{len(response_json) =} != {expected_exactly =}"
            assert len(response_json) == expected_exactly, error_msg

    def assert_schema(self, response_json, expected_schema):
        if expected_schema:
            validate(response_json, expected_schema)

    def assert_data(self, expected_data, actual_data):
        assert_message = "expected_data != actual_data"

        if test_config.LOG_RESPONSE:
            assert_message = f"\nexpected_data={json.dumps(expected_data, indent=2)} \
                        \nactual_data={json.dumps(actual_data, indent=2)}"

        assert expected_data == actual_data, assert_message

    def assert_status_code(self, expected_status_code, raw_response):
        response_status_code = raw_response.status_code
        assert_message = f"{expected_status_code =} != {response_status_code =}"
        if expected_status_code != response_status_code:
            assert_message += f"\n {raw_response.text}"
        assert expected_status_code == response_status_code, assert_message

    # endregion

    # region -> for internal use

    def _construct_url_for_request(self, url: str, method: str, record_id: int = None) -> None:
        """Constructs the URL for the request based on the provided URL, method, and optionally an ID"""

        if not url:
            url = self.url

        if record_id:
            url += f"{'' if url.endswith('/') else '/'}{str(record_id)}"

        # Determine the trailing slash based on API type and method
        trailing_slash = self.trailing_slash_map[self.session.api_type][method]
        self.url_for_request = url.rstrip("/") + trailing_slash

    def _prepare_body_for_request(self, data: Optional[Dict]) -> None:
        """Prepares the request body data for the HTTP request."""
        if data:
            self.data = json.dumps(data, indent=2)
            if test_config.LOG_INPUT_DATA:
                common_utils.log(f"\ninput data = {data}")

    def _before_request(self, method: str, url: str, id_: int, data: Optional[Dict], params: Optional[Dict]) -> None:
        """Performs pre-processing tasks before making an HTTP request."""
        self._construct_url_for_request(url, method, id_)
        self._prepare_body_for_request(data)
        self._log_before_request(method, params)

    def _after_request(self, response: Response, log_results: bool, verify_results: bool, expected_status_code: int, expected_response: str, schema: str, count_above: int, count_exactly: int) -> None:
        """Performs post-processing tasks after receiving an HTTP response."""
        if verify_results:
            self._verify_response(
                raw_response=response,
                expected_status_code=expected_status_code,
                expected_response=expected_response,
                schema=schema,
                count_above=count_above,
                count_exactly=count_exactly,
                log_results=log_results,
                return_json_response=False,
            )
        if log_results:
            self._log_after_request(response)

    def _get_actual_response(self, expected_response, actual_response):
        """gets the actual response to compare against the expected response"""
        if isinstance(expected_response, (dict, list)):
            return actual_response
        if expected_response:
            if isinstance(actual_response, dict):
                if "message" in actual_response:
                    return actual_response["message"]
            elif isinstance(actual_response, list):
                if "message" in actual_response[0]:
                    return actual_response[0]["message"]
        return ""

    def _verify_response(
        self,
        raw_response: Response,
        expected_status_code: int = 200,
        expected_response: Any = "",
        schema: Any = "",
        count_above: int = -1,
        count_exactly: int = -1,
        return_json_response: bool = False,
        log_results: bool = False,
    ) -> None:
        """
        Verifies the response against expectations.

        Args:
            raw_response (Response): The raw HTTP response
            expected_status_code (int): Expected HTTP status code
            expected_response: Expected response data
            schema: JSON schema for validation
            count_above (int): Minimum count for response items
            count_exactly (int): Exact count for response items
            return_json_response (bool): Flag to force JSON response
            log_results (bool): Flag to log results

        Raises:
            EndpointResponseError: When response validation fails
        """
        try:
            # Parse the response
            response_json = self._construct_response_json(raw_response, return_json_response=return_json_response)
            actual_response = self._get_actual_response(expected_response, response_json)

            # Log response details if requested
            self._log_response(response_json, raw_response.status_code, expected_status_code, count_above, count_exactly, log_results)

            # Perform assertions
            try:
                self.assert_data(expected_response, actual_response)
                self.assert_status_code(expected_status_code, raw_response)
                self.assert_response_count(response_json, count_above, count_exactly)
                self.assert_schema(response_json, schema)
            except AssertionError as e:
                # Convert assertion errors to EndpointResponseError for better error handling
                error_detail = {
                    "status_code": raw_response.status_code,
                    "expected_status": expected_status_code,
                    "response_text": raw_response.text[:500] + ("..." if len(raw_response.text) > 500 else ""),
                }
                raise EndpointResponseError(f"Response validation failed: {str(e)}\nDetails: {error_detail}")

        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON response: {str(e)}"
            common_utils.log(f"ERROR: {error_msg}")
            raise EndpointResponseError(error_msg) from e

        except Exception as e:
            if not isinstance(e, EndpointsException):
                error_msg = f"Unexpected error during response verification: {str(e)}"
                common_utils.log(f"ERROR: {error_msg}")
                raise EndpointResponseError(error_msg) from e
            raise

    def _construct_response_json(self, response: Response, return_json_response: bool = False) -> Union[Dict, List, str]:
        """
        Constructs the JSON response from the raw HTTP response.

        This method handles different response formats and extracts the relevant data.

        Args:
            response (Response): The raw HTTP response
            return_json_response (bool): Flag to force JSON response parsing

        Returns:
            Union[Dict, List, str]: Parsed response data
        """
        # Always return raw JSON when requested
        if return_json_response:
            try:
                return response.json()
            except json.JSONDecodeError as e:
                common_utils.log(f"WARNING: Could not parse JSON response: {str(e)}")
                return {"error": "Invalid JSON response", "raw_content": response.text}

        # For error responses, return empty string
        if response.status_code > 204:
            return ""

        # Try to parse JSON response
        try:
            response_json = response.json()

            # Extract data from common response formats
            if isinstance(response_json, dict):
                # Standard REST API format
                if "results" in response_json:
                    return response_json["results"]
                # JSON:API format
                elif "data" in response_json:
                    return response_json["data"]
                # No extraction needed
                return response_json
            # If response is already a list, return it directly
            elif isinstance(response_json, list):
                return response_json
            # Unexpected format
            return response_json

        except json.JSONDecodeError as e:
            common_utils.log(f"WARNING: JSON parsing failed: {str(e)}")
            if response.text.strip():
                return response.text
            return []
        except Exception as e:
            common_utils.log(f"ERROR: Response processing failed: {str(e)}")
            return []

    def _log_response(self, response_json, status_code, expected_status_code, expected_count_above, expected_count_exactly, log_results):

        if test_config.LOG_DETAIL is False or log_results is False:
            return

        log_message = ""
        log_message += f"expected status = {expected_status_code} actual status = {status_code}\n"
        log_message += self._construct_count_log(response_json, expected_count_above, expected_count_exactly)
        common_utils.log(log_message)

    def _construct_count_log(self, response_json, expected_count_above, expected_count_exactly):
        log_message = ""
        if test_config.LOG_COUNTS:
            if expected_count_above > -1:
                log_message += f"expected count above = {expected_count_above} actual count = {len(response_json)} \n"
            if expected_count_exactly > -1:
                log_message += f"expected count exactly = {expected_count_exactly} actual count = {len(response_json)} \n"
        return log_message

    def _log_before_request(self, method: str, params: Optional[Dict]) -> None:
        """Logs details before making an HTTP request."""
        if test_config.LOG_REQUEST_URL:
            if params:
                common_utils.log(f"{method}: {self.url_for_request} {params}")
            else:
                common_utils.log(f"{method}: {self.url_for_request}")

    def _log_after_request(self, response: Response) -> None:
        """Logs details after receiving an HTTP response."""
        if test_config.LOG_RESPONSE:
            try:
                log_message = f"\nresponse = {json.dumps(response.json(), indent=2)}\n"
            except Exception:
                log_message = f"\nresponse = {response}\n"
            common_utils.log(log_message)

    # endregion
