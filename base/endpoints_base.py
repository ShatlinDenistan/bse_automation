import json
import random
import re
from time import sleep
from typing import Dict, Optional

from jsonschema import validate
from requests import Response, Session

from config.config import TestConfig as test_config
from utils.common import CommonUtils as common_utils


class EndpointsBase:
    """EndpointsBase - The base class for all the endpoints classes"""

    # region - properties
    session: Session
    url: str
    data: Dict = None
    trailing_slash_map = {"rest": {"get": "", "post": "/", "put": "/", "patch": "/", "delete": ""}, "json": {"get": "", "post": "", "put": "", "patch": "", "delete": ""}}
    endpoint_base: str

    # endregion

    # region main api calls

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
        force_json_response=False,
        verify=True,
        return_raw_response=False,
        total_pages_to_get=None,
    ):
        if total_pages_to_get is not None:
            return self.get_multi_page_records(url=url, total_pages_to_get=total_pages_to_get, log_results=log_results)
        self._before_request(method="get", url=url, id_=id_, data=None, params=params)
        raw_response = self.session.get(url=self.url_for_request, params=params, headers=headers)
        self._after_request(
            response=raw_response,
            log_results=log_results,
            verify=verify,
            expected_status_code=expected_status_code,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
        )
        if return_raw_response:
            return raw_response
        return self._construct_response_json(raw_response, force_json_response=force_json_response)

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
        force_json_response=False,
        verify=True,
        return_raw_response=False,
    ):
        self._before_request("post", url, id_, data=data, params=params)
        raw_response = self.session.post(url=self.url_for_request, headers=headers, data=self.data, params=params)
        self._after_request(
            response=raw_response,
            log_results=log_results,
            verify=verify,
            expected_status_code=expected_status_code,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
        )
        if return_raw_response:
            return raw_response
        return self._construct_response_json(raw_response, force_json_response=force_json_response)

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
        force_json_response=False,
        verify=True,
        return_raw_response=False,
    ):
        self._before_request("put", url, id_, data=data, params=params)
        raw_response = self.session.put(url=self.url_for_request, headers=headers, data=self.data, params=params)
        self._after_request(
            response=raw_response,
            log_results=log_results,
            verify=verify,
            expected_status_code=expected_status_code,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
        )
        if return_raw_response:
            return raw_response
        return self._construct_response_json(raw_response, force_json_response=force_json_response)

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
        force_json_response=False,
        verify=True,
        return_raw_response=False,
    ):
        self._before_request("patch", url, id_, data=data, params=params)
        raw_response = self.session.patch(url=self.url_for_request, headers=headers, data=self.data, params=params)
        self._after_request(
            response=raw_response,
            log_results=log_results,
            verify=verify,
            expected_status_code=expected_status_code,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
        )
        if return_raw_response:
            return raw_response
        return self._construct_response_json(raw_response, force_json_response=force_json_response)

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
        force_json_response=False,
        verify=True,
        return_raw_response=False,
    ):
        self._before_request("delete", url, id_, data=None, params=params)
        raw_response = self.session.delete(url=self.url_for_request, headers=headers, data=data, params=params)
        self._after_request(
            response=raw_response,
            log_results=log_results,
            verify=verify,
            expected_status_code=expected_status_code,
            expected_response=expected_response,
            schema=schema,
            count_above=count_above,
            count_exactly=count_exactly,
        )
        if return_raw_response:
            return raw_response
        return self._construct_response_json(raw_response, force_json_response=force_json_response)

    # endregion

    # region getting records

    def get_random_record_id(self) -> int:
        random_record = self.get_random_record()
        if random_record:
            # Try to get the 'id' field from the record
            record_id = random_record.get("id")
            if record_id:
                return int(record_id)

            # Log the absence of the 'id' field and attempt to extract it from the URL
            common_utils.log("No 'id' field in response. Trying to get id from url..")
            match = re.search(rf"{self.endpoint_base}/(\d*)/", random_record.get("url", ""))
            if match:
                return int(match.group(1))
            else:
                common_utils.log("Problem with getting id from url field from the response.")

        return None

    def get_random_record(self, log_results=False) -> Dict:
        response = self.get(log_results=log_results, return_raw_response=True)
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

    def get_by_filter(self, filter_name, log_results=False, return_raw_response=False, expected_status_code=200, force_json_response=False):
        url = f"{self.url}?{filter_name}"
        response = self.get(url=url, log_results=log_results, return_raw_response=return_raw_response, expected_status_code=expected_status_code, force_json_response=force_json_response)
        return response

    def get_multi_page_records(self, url=None, total_pages_to_get=3, log_results=False):
        if url is None:
            url = self.url
        response_json = self.get(force_json_response=True, url=url, log_results=log_results)

        if "num_pages" in response_json:
            pages = response_json["num_pages"] + 1
            response_json_all: list = response_json["results"]

            for i in range(2, pages):
                if total_pages_to_get != "all" and i >= total_pages_to_get:
                    break
                page_part = f"/?page={i}"
                if "?" in url:
                    page_part = f"&page={i}"
                response = self.get(url=f"{url}{page_part}", log_results=log_results, force_json_response=True)
                response_json_all.extend(response["results"])
            return response_json_all

        elif "meta" in response_json and "pagination" in response_json["meta"]:
            pages = response_json["meta"]["pagination"]["pages"] + 1
            response_json_all: list = response_json["data"]

            for i in range(2, pages):
                if total_pages_to_get != "all" and i >= total_pages_to_get:
                    break
                url = f"{response_json['links']['next']}"
                response_json = self.get(url=url, log_results=log_results, force_json_response=True)
                response_json_all.extend(response_json["data"])
            return response_json_all

        else:
            return response_json

    def get_records_to_test_performace(self, record_type):
        params = {}
        response_json = self.get(force_json_response=True)

        if self.session.api_type == "rest":
            pages = response_json["num_pages"]
        else:
            pages = response_json["meta"]["pagination"]["pages"]

        steps = int(pages / 20)
        if steps == 0:
            return
        for page in range(1, pages, steps):
            params["page"] = page
            start_time = common_utils.start_tracking_time(f"Getting {record_type}s from page {page}")
            response = self.get(params=params, return_raw_response=True)
            records = response.json()["results"]
            record = random.choice(records)
            common_utils.log(record)
            common_utils.end_tracking_time(start_time)
            sleep(2)

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

    def _construct_url_for_request(self, url: str, method: str, id_: int = None) -> None:
        """Constructs the URL for the request based on the provided URL, method, and optionally an ID.

        Parameters
        ----------
        url : str, optional
            The base URL for the request. If not provided, the default URL associated with the session will be used.
        method : str, required
            The HTTP method for the request (e.g., 'get', 'post', 'put', 'patch').
        id_ : int, optional
            The ID to be appended to the URL. Defaults to None.

        Returns
        -------
        None

        Notes
        -----
        This method constructs the URL for the request by appending an ID (if provided) to the base URL and ensuring
        the proper formatting (e.g., adding or removing trailing slashes) based on the HTTP method and the
        session's API type.
        """

        # If no URL provided, use the default URL associated with the session
        if not url:
            url = self.url

        # Append ID to the URL if provided
        if id_:
            url += f"{'' if url.endswith('/') else '/'}{str(id_)}"

        # Determine the trailing slash based on API type and method
        trailing_slash = self.trailing_slash_map[self.session.api_type][method]

        # Construct the final URL for the request
        self.url_for_request = url.rstrip("/") + trailing_slash

    def _prepare_body_for_request(self, data: Optional[Dict]) -> None:
        """Prepares the request body data for the HTTP request.

        Parameters
        ----------
        data : Optional[Dict], optional
            The data to be included in the request body. Defaults to None.

        Returns
        -------
        None

        Notes
        -----
        This method prepares the request body data by converting it to JSON format and storing it in the `data`
        attribute of the session. If logging of input data is enabled, it logs the input data to the console.
        """
        if data:
            self.data = json.dumps(data, indent=2)
            if test_config.LOG_INPUT_DATA:
                common_utils.log(f"\ninput data = {data}")

    def _before_request(self, method: str, url: str, id_: int, data: Optional[Dict], params: Optional[Dict]) -> None:
        """Performs pre-processing tasks before making an HTTP request.

        Parameters
        ----------
        method : str, required
            The HTTP method for the request (e.g., 'get', 'post', 'put', 'patch').
        url : str, required
            The base URL for the request.
        id_ : int, required
            The ID to be appended to the URL.
        data : Optional[Dict], optional
            The data to be included in the request body. Defaults to None.
        params : Optional[Dict], optional
                The params to be included in the request body. Defaults to None.
        Returns
        -------
        None

        Notes
        -----
        This method performs pre-processing tasks before making an HTTP request, including constructing the request URL,
        preparing the request body data, and logging details about the request before it is sent.
        """
        self._construct_url_for_request(url, method, id_)
        self._prepare_body_for_request(data)
        self._log_before_request(method, params)

    def _after_request(self, response: Response, log_results: bool, verify: bool, expected_status_code: int, expected_response: str, schema: str, count_above: int, count_exactly: int) -> None:
        """Performs post-processing tasks after receiving an HTTP response.

        Parameters
        ----------
        response : Response, required
            The HTTP response object received after making the request.
        log_results : bool, required
            Indicates whether to log the results of the request.
        verify : bool, required
            Indicates whether to perform verification on the response.
        expected_status_code : int, required
            The expected status code for the response.
        expected_response : str, required
            The expected response data.
        schema : str, required
            The schema to verify against the response object's schema.
        count_above : int, required
            The expected count of records in the response, which should be above this value.
        count_exactly : int, required
            The expected count of records in the response, which should match this value exactly.

        Returns
        -------
        None

        Notes
        -----
        This method performs post-processing tasks after receiving an HTTP response,
        including verification of the response if required and logging the results if specified.
        """
        if verify:
            self._verify(
                raw_response=response,
                expected_status_code=expected_status_code,
                expected_response=expected_response,
                schema=schema,
                count_above=count_above,
                count_exactly=count_exactly,
                log_results=log_results,
                force_json_response=False,
            )
        if log_results:
            self._log_after_request(response)

    def _get_actual(self, expected_data, response_json):
        """gets the actual response to compare against the expected data"""
        if isinstance(expected_data, (dict, list)):
            return response_json
        if expected_data:
            if isinstance(response_json, dict):
                if "message" in response_json:
                    return response_json["message"]
            elif isinstance(response_json, list):
                if "message" in response_json[0]:
                    return response_json[0]["message"]
        return ""

    def _verify(self, raw_response: Response, expected_status_code=200, expected_response="", schema="", count_above=-1, count_exactly=-1, force_json_response=False, log_results=False) -> None:
        """Verifies the response received for the session. This is the common method that is used for verifying
        response status code, schemas, and counts.

        Parameters
        ----------
        raw_response : Response, required
            The raw response object returned by the HTTP request.
        expected_status_code: int, optional
            The expected status code of the response. Defaults to 200 if not specified.
        expected_response: dict, list, str, optional
            The expected data the tests expect in the response object. Defaults to an empty string if not specified.
        schema: JSON, optional
            The schema to verify against the response object's schema to ensure the response conforms to the expected format.
        count_above: int, optional
            Used to compare if the number of records in the response is above an expected number. Defaults to -1 if not specified.
        count_exactly: int, optional
            Used to compare if the number of records in the response is exactly equal to an expected number. Defaults to -1 if not specified.
        force_json_response: bool, optional
            If True, forces the response to be parsed as JSON. Defaults to False.
        log_results: bool, optional
            If True, logs the results of the verification. Defaults to False.

        Raises
        ------
        Exception
            Any exceptions raised, including assertion errors, are logged, and an assertion error is raised.

        Returns
        ------
        None
        """

        # Extract JSON from the response
        response_json = self._construct_response_json(raw_response, force_json_response=force_json_response)

        # Extract actual response based on expected response structure
        actual_response = self._get_actual(expected_response, response_json)

        # Log results if enabled
        if test_config.LOG_DETAIL and log_results is True:
            log_message = self._construct_log_message(
                response_json,
                raw_response.status_code,
                expected_status_code,
                count_above,
                count_exactly,
            )
            common_utils.log(log_message)

        # Perform assertions
        self.assert_data(expected_response, actual_response)
        self.assert_status_code(expected_status_code, raw_response)
        self.assert_response_count(
            response_json,
            count_above,
            count_exactly,
        )
        self.assert_schema(response_json, schema)

    def _construct_response_json(self, response, force_json_response):
        if force_json_response:
            return response.json()
        if response.status_code > 204:
            return ""
        try:
            response_json = response.json()
        except Exception:
            return []
        if "results" in response_json:
            response_json = response_json["results"]
        elif "data" in response_json:
            response_json = response_json["data"]
        return response_json

    def _construct_log_message(self, response_json, status_code, expected_status_code, expected_count_above, expected_count_exactly):
        log_message = ""
        log_message += f"expected status = {expected_status_code} actual status = {status_code}\n"
        log_message += self._construct_count_log(response_json, expected_count_above, expected_count_exactly)
        return log_message

    def _construct_count_log(self, response_json, expected_count_above, expected_count_exactly):
        log_message = ""
        if test_config.LOG_COUNTS:
            if expected_count_above > -1:
                log_message += f"expected count above = {expected_count_above} actual count = {len(response_json)} \n"
            if expected_count_exactly > -1:
                log_message += f"expected count exactly = {expected_count_exactly} actual count = {len(response_json)} \n"
        return log_message

    def _log_before_request(self, method: str, params: Optional[Dict]) -> None:
        """Logs details before making an HTTP request.

        Parameters
        ----------
        method : str, required
            The HTTP method for the request (e.g., 'get', 'post', 'put', 'patch').

        params : Optional[Dict], optional
            The params to be included in the request body. Defaults to None.

        Returns
        -------
        None
        """
        if test_config.LOG_REQUEST_URL:
            if params:
                common_utils.log(f"{method}: {self.url_for_request} {params}")
            else:
                common_utils.log(f"{method}: {self.url_for_request}")

    def _log_after_request(self, response: Response) -> None:
        """Logs details after receiving an HTTP response.

        Parameters
        ----------
        response : Response, required
            The HTTP response object received after making the request.

        Returns
        -------
        None
        """
        if test_config.LOG_RESPONSE:
            try:
                log_message = f"\nresponse = {json.dumps(response.json(), indent=2)}\n"
            except Exception:
                log_message = f"\nresponse = {response}\n"
            common_utils.log(log_message)

    # endregion
