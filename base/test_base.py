"""Test base functionality."""

import os
import json
import time
import logging as logger
import contextlib
import pytest
from faker import Faker
from playwright.sync_api import Page
from base.endpoint_initlializer import EndpointInitializer
from config.config import TestConfig
from base.page_initializer import PageInitializer
from data.db.customer_data import CustomerData
from data.db.order_data import OrderData
from data.queries.customer_queries import CustomerQueries
from data.queries.donation_queries import DonationQueries
from data.queries.order_item_queries import OrderItemQueries
from data.queries.order_queries import OrderQueries
from data.test_data_files import TestDataFiles
from utils.common import CommonUtils
from utils.csv_utils import CSVUtils


class TestBase(PageInitializer, EndpointInitializer):
    """TestBase - The base class for all the test classes"""

    @pytest.fixture(scope="function", autouse=True)
    def _pw_page(self, _init_test: Page, get_api_session):
        self.page = _init_test
        self.session = get_api_session
        self.step_count = 0
        self.config = TestConfig()
        self.logger = logger
        self.json = json
        self.faker = Faker()
        self.utils = CommonUtils()
        self.csv_library = CSVUtils()
        self.initialize_pages(self.page)
        self.initialise_endpoints(self.session)
        self.customer_data = CustomerData()
        self.order_data = OrderData()
        self.customer_queries = CustomerQueries()
        self.donation_queries = DonationQueries()
        self.order_item_queries = OrderItemQueries()
        self.order_queries = OrderQueries()
        self.test_data_files = TestDataFiles()

    def assert_expected_vs_actual(self, expected, actual):
        """Generic method to compare expected and actual"""
        assert expected == actual, f"{expected =} != {actual =}"

    def assert_keys(self, response_json, *keys):
        for key in keys:
            assert key in response_json

    def step(self, message: str):
        self.step_count += 1
        message = f"Step {self.step_count} : {message.capitalize()}"
        # self.show_step_on_front_end(message)
        if self.config.SHOW_STEP_MSG:
            logger.info(message)
        test_proof_record_mode = os.getenv("TEST_PROOF_RECORDING_MODE")
        if test_proof_record_mode is not None and test_proof_record_mode.lower() == "true":
            self.wait_for_seconds(3)

    MAIN_STEP_CSS = "position: fixed; top: 0; right: 10%; font-size: 13px; color: #FFFFFF; " "font-weight: bold; z-index: 2147483647; text-align: right; pointer-events: none;"

    def _get_step_display_javascript(self, message: str) -> str:
        """
        Returns properly formatted JavaScript for displaying steps on the frontend
        """
        return f"""
            localStorage.setItem('step_message', `{message}`);

            // Check if the element already exists
            if (!document.querySelector(".main_step")) {{
                // Create and display the message
                var element = document.createElement('div');
                element.classList.add("main_step");
                element.style.cssText = '{self.MAIN_STEP_CSS}';
                element.innerHTML = "<span>{message}</span>";
                document.body.appendChild(element);
            }}
        """

    def show_step_on_front_end(self, message: str):
        with contextlib.suppress(Exception):
            message = message.replace("\n", "<br>")

            if self.config.SHOW_STEP_MSG:
                js_code = self._get_step_display_javascript(message)
                self.page.evaluate(js_code)

    def wait_till_page_is_loaded(self, timeout: int = 30, check_interval: float = 0.5, stable_checks: int = 3):
        """wait till page is loaded. When the tests fail due to page not properly loaded, use this method.
        This is quite slow but ensures stability"""
        with contextlib.suppress(Exception):
            self.page.wait_for_load_state("domcontentloaded")
            previous_content = ""
            stable_count = 0
            start_time = time.time()
            while time.time() - start_time < timeout:
                current_content = self.page.content()
                if current_content == previous_content:
                    stable_count += 1
                    if stable_count >= stable_checks:
                        # self.log_element_interaction("page load completed")
                        return True
                else:
                    stable_count = 0
                previous_content = current_content
                self.wait_for_milliseconds(check_interval * 100)
            return False

    def wait_for_milliseconds(self, milliseconds):
        """wait for milliseconds"""
        self.page.wait_for_timeout(milliseconds)

    def wait_for_seconds(self, seconds):
        """wait for seconds"""
        self.page.wait_for_timeout(seconds * 1000)

    def wait_till_dom_is_loaded(self):
        """wait till dom is loaded. This is quick check.
        If we are sure that the test does not need to wait for the page to load fully
        and ensure html loading doesnt need to be checked, use this method"""
        self.page.wait_for_load_state("domcontentloaded")

    def reload_page(self):
        self.page.reload()
        self.wait_till_page_is_loaded()
