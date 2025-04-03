from playwright.sync_api import Page, expect


class PageBase:
    def __init__(self, page: Page):
        self.page = page
        self.page_size_dropdown = page.locator("//div[.='Show 15 Items']")
        self.show_50_items_span = page.locator("//span[.='50']")
        self.show_15_items_span = page.locator("//span[.='15']")
        self.show_30_items_span = page.locator("//span[.='30']")
        self.show_10_items_span = page.locator("//span[.='10']")

    def get_table_data(self, table_id: str = None, table_xpath: str = None, max_rows=100):
        """get table data"""

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
