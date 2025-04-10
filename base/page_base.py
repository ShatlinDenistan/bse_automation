import contextlib
import logging as logger
import os
import random
import time
from typing import Union

from faker import Faker
from playwright.sync_api import Locator, Page, Request, Response, expect

from config.config import TestConfig
from utils.common import CommonUtils as common_utils


class PageBase:
    def __init__(self, page: Page):
        self.page = page
        self.iframe_id = "iframe[id='wfx-frame-popup']"
        self.cookie_btn = "//p[.='Got it!']"
        self.config = TestConfig()
        self.faker = Faker()
        self.logger = logger
        self.utils = common_utils
        self.page_size_dropdown = page.locator("//div[.='Show 15 Items']")
        self.show_50_items_span = page.locator("//span[.='50']")
        self.show_15_items_span = page.locator("//span[.='15']")
        self.show_30_items_span = page.locator("//span[.='30']")
        self.show_10_items_span = page.locator("//span[.='10']")

    def action_cookie_popup(self):
        try:
            frame = self.page.frame_locator(self.iframe_id)
            element = frame.locator(self.cookie_btn)
            expect(element).to_be_visible(timeout=5000)
            element.click()
            return True
        except Exception:
            return False

    def set_page_size(self, page_size=50):
        self.page_size_dropdown.scroll_into_view_if_needed()
        self.page_size_dropdown.click()
        match page_size:
            case 50:
                expect(self.show_50_items_span).to_be_visible(timeout=5000)
                self.show_50_items_span.click()
            case 15:
                expect(self.show_15_items_span).to_be_visible(timeout=5000)
                self.show_15_items_span.click()
            case 30:
                expect(self.show_30_items_span).to_be_visible(timeout=5000)
                self.show_30_items_span.click()
            case 10:
                expect(self.show_10_items_span).to_be_visible(timeout=5000)
                self.show_10_items_span.click()
            case _:
                raise ValueError("Page size not supported")

    def go_to_page(self, page_url):
        self.wait_till_page_is_loaded()
        url_to_go_to = f"{self.config.HOME_PAGE}/{page_url}"
        # current_url = self.page.url
        # if url_to_go_to != current_url:
        self.page.goto(url_to_go_to, timeout=120000)
        self.wait_till_page_is_loaded()

    def locator(self, selector, name=None):
        if isinstance(selector, str):
            element = self.page.locator(selector)
        elif isinstance(selector, tuple):
            element = self.page.locator(selector[0])
            if len(selector) > 1:
                name = selector[1]
        else:
            element = selector
        if name is not None:
            element.name = name
        return element

    def by_name(self, name, exact=True, element_name=""):
        if exact:
            selector = f"//*[@name='{name}']"
        else:
            selector = f"//*[contains(@name,'{name}')]"
        return self.locator(selector, element_name)

    def select_value_from_multi_select(self, text_box_locator: Locator, options_locator: Locator, value=None):
        self.step(f"Select value {value} from the multiselect input")
        text_box_locator.click()
        # self.wait_till_page_is_loaded()
        if value is None:
            values = options_locator.all_inner_texts()
            value = random.choice(values)
        value_locator = options_locator.filter(has_text=value).first
        value_locator.click()
        if value_locator.is_visible():
            value_locator.click()

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

    def print_requests(self, request: Request):
        excludables = ["favicon.ico", "svg", "js", "ts", "css", "jpg", "png", "sentry", "font", "launchdarkly", "bower", "translations", "zendesk", "gif", "ping_only"]
        exclude = False
        for excludable in excludables:
            if excludable in request.url:
                exclude = True
                break
        if not exclude:
            if "https://stage.provetcloud.com/1/auth/login" in request.url:
                logger.info(f"request: {request.method}, {request.url}")

    def print_responses(self, response: Response):
        excludables = ["favicon.ico", "svg", "js", "ts", "css", "jpg", "png", "sentry", "font", "launchdarkly", "bower", "translations", "zendesk", "gif", "ping_only"]
        exclude = False
        for excludable in excludables:
            if excludable in response.url:
                exclude = True
                break
        if not exclude:
            logger.info(f"response: {response.status} {response.url}")

    def get_edit_locator_for_table_with_data(self, data_to_search: str = None, table_id: str = None):
        """Get edit locator for table with data, if no data_to_search for provided will return the first edit button"""
        if data_to_search:
            selector = f"//td[.='{data_to_search}']//parent::tr//td//a[@title='Edit']"
        else:
            selector = "(//tr//td//a[@title='Edit'])[1]"
        if table_id is not None:
            selector = f"//table[@id='{table_id}']//td[.='{data_to_search}']//parent::tr//td//a[@title='Edit']"
        return self.page.locator(selector)

    def get_delete_locator_for_table_with_data(self, delete_data_to_search, delete_title="Delete"):
        """get delete locator for table with data"""
        delete_selector = f"//td[.='{delete_data_to_search}']//parent::tr//a[@title='{delete_title}']"
        return self.locator(delete_selector, "Delete button")

    def log_element_interaction(self, message: str):
        hide_steps = os.getenv("HIDE_PAGE_ACTION_STEPS")
        if hide_steps is not None and hide_steps.lower() == "true":
            return

        # self.show_step_on_front_end(message)
        message = message.capitalize()
        if self.config.SHOW_STEP_MSG:
            logger.info(f"\t{message}")

    def step(self, message: str):
        hide_steps = os.getenv("HIDE_PAGE_ACTION_STEPS")
        if hide_steps is not None and hide_steps.lower() == "true":
            return

        # self.show_step_on_front_end(message)

        if self.config.SHOW_STEP_MSG:
            logger.info(message)

    def show_step_on_front_end(self, message: str):
        message = f"{message.capitalize()}"
        with contextlib.suppress(Exception):
            message = message.replace("\n", "<br>")
            # message = message.capitalize()
            if self.config.SHOW_STEP_MSG:

                self.page.evaluate(
                    f"""
                    const mainMessage = localStorage.getItem('step_message');
                    if (mainMessage && !document.querySelector(".main_step")) {{
                        // Create the main step message only if it doesn't exist
                        var mainElement = document.createElement('div');
                        mainElement.classList.add("main_step");
                        mainElement.style.cssText = 'position: fixed; top: 0; right: 10%; font-size: 13px; color: #FFFFFF; font-weight: bold; z-index: 2147483647; text-align: right; pointer-events: none;';
                        mainElement.innerHTML = "<span>" + mainMessage + "</span>";
                        document.body.appendChild(mainElement);
                    }}

                    // Check if sub_step already exists
                    var subElement = document.querySelector(".sub_step");
                    if (subElement) {{
                        // If it exists, update the message
                        subElement.innerHTML = "<span>{message}</span>";
                    }} else {{
                        // If it does not exist, create it
                        subElement = document.createElement('div');
                        subElement.classList.add("sub_step");
                        subElement.style.cssText = 'position: fixed; top: 15px; right: 10%; font-size: 13px; color: #FFFFFF; font-weight: normal; z-index: 2147483647; text-align: right; pointer-events: none;';
                        subElement.innerHTML = "<span>{message}</span>";
                        document.body.appendChild(subElement);
                    }}
                """
                )

            test_proof_record_mode = os.getenv("TEST_PROOF_RECORDING_MODE")
            if test_proof_record_mode is not None and test_proof_record_mode.lower() == "true":
                self.wait_for_seconds(2)

    def get_locator_and_name(self, locator: Union[Locator, str], element_name=""):
        if hasattr(locator, "name"):
            element_name = locator.name
        if isinstance(locator, str):
            if element_name == "" or element_name is None:
                if "'" in locator:
                    element_name = locator.split("'")
                    if len(element_name) > 1:
                        element_name = element_name[1]
                    else:
                        element_name = locator
                else:
                    element_name = locator.replace("#", "")
            locator = self.page.locator(locator).first

        elif isinstance(locator, Locator) and element_name is not None and len(element_name) == 0:
            with contextlib.suppress(Exception):
                temp_name = str(locator.first)
                sub_index = temp_name.find("selector")
                temp_name = temp_name[sub_index:]
                temp_name = temp_name.replace("selector=", "")
                temp_name = temp_name.replace(" >> nth=0", "")
                sub_index = temp_name.find("'") + 1
                temp_name = temp_name[sub_index:]
                sub_index = temp_name.find("'")
                temp_name = temp_name[:sub_index]
                element_name = temp_name
                element_name = element_name.replace("id_", "")
                element_name = element_name.replace("id ", "")
                element_name = element_name.replace("id", "")
                element_name = element_name.replace("#", "")
                element_name = element_name.replace("@", "")

        return locator, element_name

    def expect_to_be_visible(self, locator: Union[Locator, str], element_name="", timeout=3000):
        """assert element is visible"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        expect(locator).to_be_visible(timeout=timeout)

    def expect_to_be_hidden(self, locator: Union[Locator, str], element_name="", timeout=3000):
        """assert element is visible"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        expect(locator).to_be_hidden(timeout=timeout)

    def expect_to_be_attached(self, locator: Union[Locator, str], element_name="", timeout=3000):
        """assert element is attached"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        expect(locator).to_be_attached(timeout=timeout)

    def text_content(self, locator: Union[Locator, str], element_name=""):
        """get data"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        return locator.text_content()

    def input_value(self, locator: Union[Locator, str], element_name=""):
        """get data"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        return locator.input_value()

    def is_visible(self, locator: Union[Locator, str], element_name: str = "", timeout: int = 5000):
        """
        Wait if an locator becomes visible on the page.

        Same as .is_visible() but waits for the locator instead of immediately returning.

        Parameters:
        locator : Locator, str
            The locator to wait for.
        element_name : str
            The name of the element to log.
        timeout : int
            The maximum time to wait for the element to become visible. Default is 5s.

        """
        locator, element_name = self.get_locator_and_name(locator, element_name)
        self.step(f"check if element {element_name} is visible")
        try:
            self.wait_till_page_is_loaded()
            expect(locator).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def is_hidden(self, locator: Union[Locator, str], element_name: str = "", timeout: int = 5000):
        """
        Wait if an locator becomes hidden on the page.
        """
        locator, element_name = self.get_locator_and_name(locator, element_name)
        self.step(f"check if element {element_name} is hidden")
        try:
            self.wait_till_page_is_loaded()
            expect(locator).to_be_hidden(timeout=timeout)
            return True
        except AssertionError:
            return False

    def get_attribute(self, locator: Union[Locator, str], attribute_name, element_name=""):
        """get attribute"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        attrib = locator.get_attribute(attribute_name)
        # self.step(f"got {attribute_name} attribute for element {element_name}")

        return attrib

    def get_attribute_values(self, locator: Union[Locator, str], attribute_name, element_name=""):
        """given attribute name retrieves attribute values"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        attrib = locator.get_attribute(attribute_name)
        # self.step(f"got {attribute_name} attribute for element {element_name}")

        return attrib

    def javascript_click(self, locator: Union[Locator, str], element_name=""):
        """click element using javascript"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        with contextlib.suppress(Exception):
            locator.scroll_into_view_if_needed()
        locator.evaluate("element => element.click()")
        with contextlib.suppress(Exception):
            self.log_element_interaction(f"click '{element_name}'")

    def click(self, locator: Union[Locator, str], element_name="", force=True):
        """click element"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        with contextlib.suppress(Exception):
            locator.scroll_into_view_if_needed()
            # self.highlight_element(locator)
        locator.click(force=force)
        with contextlib.suppress(Exception):
            if len(element_name) > 0:
                self.log_element_interaction(f"click '{element_name}'")

    def focus(self, locator: Union[Locator, str], element_name=""):
        """focus element"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        locator.focus()

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    def set_checkbox_to(self, locator: Union[Locator, str], desired_setting, element_name=""):
        """set checkbox to checked or unchecked based on input"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        locator.scroll_into_view_if_needed()
        if desired_setting is True:
            self.check(locator, element_name)
        else:
            self.uncheck(locator, element_name)
        self.log_element_interaction(f"set checkbox to '{desired_setting}'")

    def check(self, locator: Union[Locator, str], element_name=""):
        """check checkbox"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        locator.focus()
        locator.scroll_into_view_if_needed()
        locator.check()
        self.log_element_interaction(f"check '{element_name}'")

    def uncheck(self, locator: Union[Locator, str], element_name=""):
        """uncheck checkbox"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        locator.focus()
        locator.scroll_into_view_if_needed()

        locator.uncheck()
        self.log_element_interaction(f"uncheck '{element_name}'")

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

    def wait_till_page_is_loaded(self, timeout: int = 30, check_interval: float = 0.5, stable_checks: int = 3):
        """wait till page is loaded. When the tests fail due to page not properly loaded, use this method.
        This is quite slow but ensures stability"""
        # self.log_element_interaction("waiting till page is loaded")

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
            # self.log_element_interaction(f"page load didnt complete in {timeout} seconds. returing...")
            return False

    def click_checkbox(self, locator: Union[Locator, str], should_select: Union[str, bool] = True, element_name=""):
        """click checkbox"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        if should_select is not None and (should_select is True or should_select.strip().upper() == "TRUE"):
            locator.scroll_into_view_if_needed()
            locator.click()
            self.log_element_interaction(f"check '{element_name}'")

    def fill(self, locator: Union[Locator, str], text, element_name=""):
        """fill text"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        if text is not None and str(text) != "":
            locator.scroll_into_view_if_needed()
            locator.focus()
            locator.clear()
            locator.fill(str(text))
            self.log_element_interaction(f"fill {element_name} textbox with text '{text}'")

    def type(self, locator: Union[Locator, str], text, element_name="", delay=10):
        """type text"""
        locator, element_name = self.get_locator_and_name(locator, element_name)

        if text is not None:
            locator.scroll_into_view_if_needed()
            locator.focus()
            locator.clear()
            locator.type(str(text), delay=delay)
            self.log_element_interaction(f"type text '{text}' in '{element_name}' textbox")

    def clear(self, locator: Locator, element_name=""):
        """type text"""
        locator, element_name = self.get_locator_and_name(locator, element_name)
        self.log_element_interaction(f"clear text from '{element_name}'")
        locator.scroll_into_view_if_needed()
        locator.focus()
        locator.clear()

    def select_option(self, locator: Union[Locator, str], option, element_name=""):
        """select option"""
        if option is None:
            return
        option = str(option)
        locator, element_name = self.get_locator_and_name(locator, element_name)
        locator.select_option(option)
        self.log_element_interaction(f"select '{element_name}' with option '{option}'")

    def select_value(self, locator: Union[Locator, str], option, element_name="", exact=False):
        """select value"""
        locator, element_name = self.get_locator_and_name(locator, element_name)

        if exact is False:
            element = locator.locator(f"//option[contains(.,'{option}')]").first.text_content()
            locator.select_option(value=element)
        else:
            self.select_option(locator, option=option)
        self.log_element_interaction(f"select '{element_name}' with value '{option}'")

    def select_option_by_value(self, locator: Union[Locator, str], value, element_name=""):
        """select value"""
        locator, element_name = self.get_locator_and_name(locator, element_name)

        element = locator.locator(f"//option[@value='{value}']").first.text_content()
        locator.select_option(value=element)
        self.log_element_interaction(f"select '{element_name}' with value '{value}'")

    def get_dropdown_selected_text(self, locator: Locator):
        """get dropdown selected text"""
        return locator.evaluate("e => e.options[e.selectedIndex].text", timeout=1000)

    def get_all_dropdown_options(self, locator: Locator):
        """get all dropdown options text"""
        return locator.evaluate("e => Array.from(e.options).map(option => option.text)", timeout=1000)

    def clear_token_input(self, locator: Union[Locator, str], element_name=""):
        locator, _ = self.get_locator_and_name(locator, element_name)

        clear_tokeninput_icons = locator.locator("//..//..//span[@class='token-input-delete-token']").element_handles()
        for clear_tokeninput_icon in clear_tokeninput_icons:
            if clear_tokeninput_icon.is_visible():
                clear_tokeninput_icon.click()

    def _handle_close_button(self, close_button):
        self.click(close_button)
        self.wait_for_seconds(1)

    def _click_on_token_input_to_activate(self, locator: Locator):
        expect(locator).to_be_visible(timeout=10000)
        self.click(locator)

    def _type_search_text(self, locator: Locator, search_text):
        self.type(locator, search_text, delay=30)
        self.wait_for_seconds(1)

    def _trigger_dropdown_with_space(self, locator: Locator):
        locator.type(" ")
        self.wait_for_seconds(1)

    def _get_dropdown_elements(self, li_class_name, dropdown_locators):
        li_selectors = f"//li[contains(@class, '{li_class_name}')]"
        for i in range(1, 4):
            all_list_items = self.page.locator(li_selectors) if dropdown_locators is None else dropdown_locators
            if all_list_items.count() > 0 and all_list_items.first.is_visible():
                return all_list_items
            self.wait_for_seconds(i)
        return None

    def _choose_element_to_select(self, all_list_items, search_text, item_to_select_text):
        if item_to_select_text:
            return self._find_item_by_text(all_list_items, item_to_select_text)
        elif search_text:
            return self._find_item_by_text(all_list_items, search_text)
        else:
            return self._select_random_item(all_list_items)

    def _find_item_by_text(self, all_list_items, text):
        text = str(text)
        words = text.split(" ")
        # Chain `has_text` with each word to filter items containing all words
        for word in words:
            all_list_items = all_list_items.filter(has_text=word)
        return all_list_items.first if all_list_items.count() > 0 else None

    def _select_random_item(self, all_list_items):
        random_index = random.randint(0, all_list_items.count() - 1)
        return all_list_items.nth(random_index)

    def select_table_rows(self, table_id):
        """select table rows"""
        total_rows = 0
        table = f"//table[@id='{table_id}']"
        row_xpath = f"{table}/tbody/tr"
        expect(self.page.locator(table)).to_be_visible()
        for i in range(5):
            rows = self.page.locator(row_xpath)
            total_rows = rows.count()
            if total_rows > 0:
                break
            self.page.wait_for_timeout(i * 100)

        for row_num in range(0, total_rows):
            row = rows.nth(row_num)
            row.click()

    def get_table_row_count(self, table_id_or_selector_or_locator: Union[str, Locator]):
        """get table row count"""
        self.wait_till_page_is_loaded()  # wait till the table is fully loaded
        if isinstance(table_id_or_selector_or_locator, Locator):
            return table_id_or_selector_or_locator.locator("//tbody//tr").count()
        if "//" in table_id_or_selector_or_locator:
            table_xpath = {table_id_or_selector_or_locator}
            row_xpath = f"{table_xpath}/tbody/tr"
        else:
            table_xpath = f"//table[@id='{table_id_or_selector_or_locator}']"
            row_xpath = f"{table_xpath}/tbody/tr"
        table_locator: Union[Locator, str] = self.page.locator(table_xpath)
        if table_locator.first.is_visible():
            rows = self.page.locator(row_xpath)
            total_rows = rows.count()
            return total_rows
        return None

    def get_table_data(self, table_id: str = None, table_xpath: str = None, max_rows=100):
        """get table data"""
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
                # while "  " in cell_content:
                #     cell_content = cell_content.replace("  ", " ")
                row_data.append(cell_content)
            table_data.append(row_data)
            if row_num >= max_rows:
                break
        return table_data

    def check_if_data_in_table(
        self, table_id: str = None, data_to_search: str = None, paging_control_id: str = None, next_button_id: str = None, table_xpath: str = None, max_pages: int = 5, match_case=True
    ) -> bool:
        """check if data in table"""
        if paging_control_id is not None:
            paging_control_div = f"//*[@id='{paging_control_id}']"
            expect(self.page.locator(paging_control_div)).to_be_visible()

        for _ in range(max_pages):
            if table_id is None:
                page_data = self.get_table_data(table_xpath=table_xpath)
            else:
                page_data = self.get_table_data(table_id)
            for row in page_data:
                for cell in row:
                    if match_case:
                        if str(data_to_search) in cell:
                            return True
                    else:
                        if str(data_to_search).lower() in str(cell).lower():
                            return True
            if next_button_id is not None:
                next_button = self.page.locator(f"#{next_button_id}:not(.disabled)")
                if next_button.is_visible():
                    next_button.focus()
                    next_button.click()
                else:
                    break
        return False

    def _select_randomly(self, locator: Union[Locator, str], select_items_locator):
        """select a random item from the given list"""
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

    def reload(self):
        self.page.reload()
        self.wait_till_page_is_loaded()

    def _select_using_value(self, locator: Union[Locator, str], select_items_locator, value):
        """select a random item from the given list"""
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(100)
        locator.click()
        item_to_select = f"({select_items_locator})[1]"
        expect(self.page.locator(item_to_select)).to_be_visible(timeout=20000)
        locator.type(value)
        total_list_items = self.page.locator(select_items_locator).count()
        index = 1
        if total_list_items > 0:
            elements = self.page.query_selector_all(select_items_locator)
            for elm in elements:

                if value == elm.inner_text():
                    break
                else:
                    index = index + 1
        item_to_select = f"({select_items_locator})[{index}]"
        select_locator = self.page.locator(item_to_select)
        expect(self.page.locator(item_to_select)).to_be_visible(timeout=10000)
        select_locator.click()

    def pick_random_element(self, locator: Union[Locator, str], include_first_option=False):
        """pick an element randomly from a group of elements"""
        index = int(include_first_option is False)
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        self.page.wait_for_timeout(2000)  # wait for the elements to load
        total_items = locator.count()
        if total_items == 0:
            random_number = 0
        else:
            random_number = random.randint(index, total_items - 1)
        random_element = locator.nth(random_number)
        return random_element

    def pick_random_option_from_dropdown(self, locator: Locator, include_first_option: bool = False) -> Union[str, None]:
        """pick an element randomly from a dropdown"""
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

    def get_locator_count(self, locator: Union[Locator, str]):
        """get number of locators"""
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        total_items = locator.count()
        return total_items

    def assert_elements_present(self, locators: list[Locator]):
        """assert elements present"""
        total_elements = len(locators)
        logger.info(f"{total_elements=}")
        errors = 0
        for locator in locators:
            try:
                assert locator.is_visible()
                logger.error(f"locator is fine: {locator}")
            except Exception:
                errors += 1
                logger.error(f"{locator} is not visible")
        assert errors == 0, f"{errors} elements of out {total_elements} need to be fixed"

    def is_element_active(self, locator):
        return "active" in self.get_attribute(locator, "class")

    def set_links_to_open_in_same_tab(self):
        # Assume `page` is your Playwright page object
        self.page.evaluate(
            """(function() {
            document.querySelectorAll('a').forEach(link => {
                link.setAttribute('target', '_self');
            });
        })()"""
        )
