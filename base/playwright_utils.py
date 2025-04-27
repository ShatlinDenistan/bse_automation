import contextlib
import logging as logger
import os
import random
import time
from typing import Union

from faker import Faker
from playwright.sync_api import Locator, Page, expect

from config.config import TestConfig
from utils.common import CommonUtils as common_utils
from utils.csv_utils import CSVUtils


class PlaywrightUtils:

    def __init__(self, page: Page):
        self.page = page

        self.config = TestConfig()
        self.faker = Faker()
        self.logger = logger
        self.utils = common_utils
        self.csv_library = CSVUtils()

    def go_to_page(self, page_url):
        self.wait_till_page_is_loaded()
        url_to_go_to = f"{self.config.HOME_PAGE}/{page_url}"
        self.page.goto(url_to_go_to, timeout=120000)
        self.wait_till_page_is_loaded()

    def locator(self, selector, name=None):
        element = selector
        if isinstance(selector, str):
            element = self.page.locator(selector)
        if name is not None:
            element.name = name
        return element

    def get_table_header_column_index(self, header_name: str, table_id=None, table_xpath=None) -> int:
        if table_xpath is not None:
            header_xpath = self.page.locator(f"{table_xpath}//th")
        else:
            header_xpath = self.page.locator(f"//table[@id='{table_id}']//th")
        headers = header_xpath.all_text_contents()
        headers = [item.upper() for item in headers]
        header_name = header_name.upper()

        for i, header in enumerate(headers):
            if header_name in header:
                return i
        raise ValueError(f"Header '{header_name}' not found in table headers: {headers}")

    def get_table_headers(self, table_class=None, table_id=None):
        table_header_list = []
        if table_class:
            table_header_list = self.page.locator(f".{table_class} tr:visible:first-child").evaluate("""el => [...el.querySelectorAll('th')].map(e => e.textContent.trim())""")
        elif table_id:
            table_header_list = self.page.locator(f"#{table_id} thead tr").evaluate("""el => [...el.querySelectorAll('th')].map(e => e.textContent.trim())""")

        return table_header_list

    def log_element_interaction(self, message: str):
        hide_steps = os.getenv("HIDE_PAGE_ACTION_STEPS")
        if hide_steps is not None and hide_steps.lower() == "true":
            return

        self.show_step_on_front_end(message)
        message = message.capitalize()
        if self.config.SHOW_STEP_MSG:
            logger.info(f"\t{message}")

    def step(self, message: str):
        hide_steps = os.getenv("HIDE_PAGE_ACTION_STEPS")
        if hide_steps is not None and hide_steps.lower() == "true":
            return

        if self.config.SHOW_STEP_MSG:
            logger.info(message)

    MAIN_STEP_CSS = """position: fixed; top: 0; right: 10%; font-size: 13px; color: #FFFFFF; font-weight: bold; z-index: 2147483647; text-align: right; pointer-events: none;"""

    SUB_STEP_CSS = "position: fixed; top: 15px; right: 10%; font-size: 13px; color: #FFFFFF; " "font-weight: normal; z-index: 2147483647; text-align: right; pointer-events: none;"

    def _get_step_display_javascript(self, message: str) -> str:
        return f"""
            // Check for and display main message from localStorage
            const mainMessage = localStorage.getItem('step_message');
            if (mainMessage && !document.querySelector(".main_step")) {{
                var mainElement = document.createElement('div');
                mainElement.classList.add("main_step");
                mainElement.style.cssText = '{self.MAIN_STEP_CSS}';
                mainElement.innerHTML = "<span>" + mainMessage + "</span>";
                document.body.appendChild(mainElement);
            }}

            // Display or update sub-step message
            var subElement = document.querySelector(".sub_step");
            if (subElement) {{
                subElement.innerHTML = "<span>{message}</span>";
            }} else {{
                subElement = document.createElement('div');
                subElement.classList.add("sub_step");
                subElement.style.cssText = '{self.SUB_STEP_CSS}';
                subElement.innerHTML = "<span>{message}</span>";
                document.body.appendChild(subElement);
            }}
        """

    def show_step_on_front_end(self, message: str):
        message = f"{message.capitalize()}"
        with contextlib.suppress(Exception):
            message = message.replace("\n", "<br>")
            if self.config.SHOW_STEP_MSG:
                js_code = self._get_step_display_javascript(message)
                self.page.evaluate(js_code)

            test_proof_record_mode = os.getenv("TEST_PROOF_RECORDING_MODE")
            if test_proof_record_mode is not None and test_proof_record_mode.lower() == "true":
                self.wait_for_seconds(2)

    def is_visible(self, locator: Locator, timeout: int = 5000):
        self.step(f"check if element {locator.name} is visible")
        try:
            self.wait_till_page_is_loaded()
            expect(locator).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def is_hidden(self, locator: Locator, timeout: int = 5000):
        self.step(f"check if element {locator.name} is hidden")
        try:
            self.wait_till_page_is_loaded()
            expect(locator).to_be_hidden(timeout=timeout)
            return True
        except AssertionError:
            return False

    def javascript_click(self, locator: Locator):
        with contextlib.suppress(Exception):
            locator.scroll_into_view_if_needed()
        locator.evaluate("element => element.click()")
        with contextlib.suppress(Exception):
            self.log_element_interaction(f"click '{locator.name}'")

    def click(self, locator: Locator, force=True):
        with contextlib.suppress(Exception):
            locator.scroll_into_view_if_needed()
        locator.click(force=force)
        with contextlib.suppress(Exception):
            self.log_element_interaction(f"click '{locator.name}'")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    def check(self, locator: Locator):
        locator.focus()
        locator.scroll_into_view_if_needed()
        locator.check()
        self.log_element_interaction(f"check '{locator.name}'")

    def uncheck(self, locator: Locator):
        locator.focus()
        locator.scroll_into_view_if_needed()

        locator.uncheck()
        self.log_element_interaction(f"uncheck '{locator.name}'")

    def fill(self, locator: Locator, text):
        if text is not None and str(text) != "":
            locator.scroll_into_view_if_needed()
            locator.focus()
            locator.clear()
            locator.fill(str(text))
            self.log_element_interaction(f"fill {locator.name} textbox with text '{text}'")

    def type(self, locator: Locator, text, delay=10):
        if text is not None:
            locator.scroll_into_view_if_needed()
            locator.focus()
            locator.clear()
            locator.type(str(text), delay=delay)
            self.log_element_interaction(f"type text '{text}' in '{locator.name}' textbox")

    def clear(self, locator: Locator):
        self.log_element_interaction(f"clear text from '{locator.name}'")
        locator.scroll_into_view_if_needed()
        locator.focus()
        locator.clear()

    def select_option(self, locator: Locator, option):
        if option is None:
            return
        option = str(option)

        locator.select_option(option)
        self.log_element_interaction(f"select '{locator.name}' with option '{option}'")

    def select_value(self, locator: Locator, option, exact=False):
        if exact is False:
            element = locator.locator(f"//option[contains(.,'{option}')]").first.text_content()
            locator.select_option(value=element)
        else:
            self.select_option(locator, option=option)
        self.log_element_interaction(f"select '{locator.name}' with value '{option}'")

    def get_dropdown_selected_text(self, locator: Locator):
        return locator.evaluate("e => e.options[e.selectedIndex].text", timeout=1000)

    def get_all_dropdown_options(self, locator: Locator):
        return locator.evaluate("e => Array.from(e.options).map(option => option.text)", timeout=1000)

    def _find_element_by_text(self, all_list_items, text):
        text = str(text)
        words = text.split(" ")
        for word in words:
            all_list_items = all_list_items.filter(has_text=word)
        return all_list_items.first if all_list_items.count() > 0 else None

    def _select_random_item(self, all_list_items):
        random_index = random.randint(0, all_list_items.count() - 1)
        return all_list_items.nth(random_index)

    def get_table_row_count(self, table_id_or_selector_or_locator: Union[str, Locator]):
        self.wait_till_page_is_loaded()
        if isinstance(table_id_or_selector_or_locator, Locator):
            return table_id_or_selector_or_locator.locator("//tbody//tr").count()
        if "//" in table_id_or_selector_or_locator:
            table_xpath = {table_id_or_selector_or_locator}
            row_xpath = f"{table_xpath}/tbody/tr"
        else:
            table_xpath = f"//table[@id='{table_id_or_selector_or_locator}']"
            row_xpath = f"{table_xpath}/tbody/tr"
        table_locator: Locator = self.page.locator(table_xpath)
        if table_locator.first.is_visible():
            rows = self.page.locator(row_xpath)
            total_rows = rows.count()
            return total_rows
        return None

    def get_table_data(self, table_id: str = None, table_xpath: str = None, max_rows=100):
        self.wait_till_page_is_loaded()

        if table_id:
            table = f"//table[@id='{table_id}']"
            expect(self.page.locator(table).first).to_be_visible()
            row_xpath = f"{table}/tbody/tr"
        else:
            expect(self.page.locator(table_xpath).first).to_be_visible()
            row_xpath = f"{table_xpath}/tbody/tr"

        rows = self.page.locator(row_xpath)
        total_rows = rows.count()
        table_data = []

        for row_num in range(1, total_rows + 1):
            cells = self.page.locator(f"{row_xpath}[{row_num}]//td")
            total_cells = cells.count()
            row_data = []
            for cell_num in range(total_cells):
                cell = cells.nth(cell_num)
                cell_content = cell.text_content().strip()
                row_data.append(cell_content)
            table_data.append(row_data)
            if row_num >= max_rows:
                break
        return table_data

    def _select_randomly(self, locator: Locator, select_items_locator):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(100)
        locator.click()
        item_to_select = f"({select_items_locator})[1]"
        expect(self.page.locator(item_to_select)).to_be_visible(timeout=20000)
        for i in range(1, 5):
            total_list_items = self.page.locator(select_items_locator).count()
            if total_list_items > 0:
                break
            self.page.wait_for_timeout(i * 100)
        random_item = random.randint(1, total_list_items)
        item_to_select = f"({select_items_locator})[{random_item}]"
        select_locator = self.page.locator(item_to_select)
        expect(self.page.locator(item_to_select)).to_be_visible(timeout=10000)
        select_locator.click()

    def reload_page(self):
        self.page.reload()
        self.wait_till_page_is_loaded()

    def pick_random_locator(self, locator: Locator, include_first_option=False):
        index = int(include_first_option is False)
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        self.page.wait_for_timeout(2000)
        total_items = locator.count()
        if total_items == 0:
            random_number = 0
        else:
            random_number = random.randint(index, total_items - 1)
        random_element = locator.nth(random_number)
        return random_element

    def select_random_option_from_dropdown(self, locator: Locator, include_first_option: bool = False) -> Union[str, None]:
        index = int(include_first_option is False)
        options = locator.get_by_role("option")
        option_count = options.count()
        if option_count == 0 or (option_count == 1 and not include_first_option):
            return
        expect(options.first).to_be_attached(timeout=3000)
        random_number = random.randint(index, option_count - 1)
        expect(options.nth(random_number)).to_be_attached()
        option_text = options.nth(random_number).text_content()
        self.wait_for_milliseconds(300)
        locator.select_option(value=option_text)
        return option_text

    def set_links_to_open_in_same_tab(self):
        self.page.evaluate(
            """(function() {
            document.querySelectorAll('a').forEach(link => {
                link.setAttribute('target', '_self');
            });
        })()"""
        )

    def wait_for_milliseconds(self, milliseconds):
        if hasattr(self, "page") and self.page:
            self.page.wait_for_timeout(milliseconds)
        else:
            time.sleep(milliseconds / 1000)

    def wait_for_seconds(self, seconds):
        if hasattr(self, "page") and self.page:
            self.page.wait_for_timeout(seconds * 1000)
        else:
            time.sleep(seconds)

    def wait_for_text(self, text, timeout=5000):
        self.wait_till_page_is_loaded()
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            if text in self.page.content():
                return
            self.wait_for_seconds(1)
        raise AssertionError(f"Text '{text}' not found in page content within {timeout} milliseconds")

    def get_text(self, locator: Locator):
        self.wait_till_page_is_loaded()
        if hasattr(locator, "text_content"):
            return locator.text_content()
        elif hasattr(locator, "inner_text"):
            return locator.inner_text()
        else:
            raise AttributeError(f"can not get text from Locator '{locator}' ")

    def is_enabled(self, locator: Locator):
        self.wait_till_page_is_loaded()
        if hasattr(locator, "is_enabled"):
            return locator.is_enabled()
        else:
            raise AttributeError(f"can not get enabled status from Locator '{locator}' ")

    def press_key(
        self,
        key,
        locator: Locator = None,
    ):
        self.wait_till_page_is_loaded()
        if locator is not None:
            locator.press(key)
        else:
            self.page.keyboard.press(key)

    def accept_alert(self):
        self.wait_till_page_is_loaded()
        with contextlib.suppress(Exception):
            self.page.on("dialog", lambda dialog: dialog.accept())
            self.page.evaluate("window.alert = function() {};")

    def scroll_to_element(self, locator: Locator):
        self.wait_till_page_is_loaded()
        locator.scroll_into_view_if_needed()

    def wait_for_element_enabled(self, locator: Locator, timeout=5000):
        self.wait_till_page_is_loaded()
        try:
            expect(locator).to_be_enabled(timeout=timeout)
        except AssertionError as exc:
            raise AssertionError(f"Element '{locator.name}' not enabled within {timeout} milliseconds") from exc

    def is_disabled(self, locator: Locator):
        self.wait_till_page_is_loaded()
        if hasattr(locator, "is_disabled"):
            return locator.is_disabled()
        else:
            raise AttributeError(f"can not get disabled status from Locator '{locator}' ")

    def hover(self, locator: Locator):
        self.wait_till_page_is_loaded()
        if hasattr(locator, "hover"):
            locator.hover()
        else:
            raise AttributeError(f"can not hover on Locator '{locator}' ")

    def wait_for_element_to_be_visible(self, locator: Locator, timeout=5000):
        expect(locator).to_be_visible(timeout=timeout)

    def wait_till_dom_is_loaded(self):
        if hasattr(self, "page") and self.page:
            self.page.wait_for_load_state("domcontentloaded")

    def wait_till_page_is_loaded(self, timeout: int = 30, check_interval: float = 0.5, stable_checks: int = 3):
        if not hasattr(self, "page") or not self.page:
            return False

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
                        self.wait_for_seconds(2)
                        return True
                else:
                    stable_count = 0
                previous_content = current_content
                self.wait_for_milliseconds(check_interval * 100)
            return False

    def evaluate(self, js_code):
        return self.page.evaluate(js_code)

    def wait_till_element_visible(self, locator: Locator, timeout=5000):
        self.wait_till_page_is_loaded()
        try:
            expect(locator).to_be_visible(timeout=timeout)
        except AssertionError as exc:
            raise AssertionError(f"Element '{locator.name}' not visible within {timeout} milliseconds") from exc

    def expect_to_be_visible(self, locator: Locator, timeout=5000):
        self.wait_till_page_is_loaded()
        try:
            expect(locator).to_be_visible(timeout=timeout)
        except AssertionError as exc:
            raise AssertionError(f"Element '{locator.name}' not visible within {timeout} milliseconds") from exc
