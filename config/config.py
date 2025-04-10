import os


class TestConfig:
    """All the configurations for the tests"""

    API_TOKEN = f"Token {os.getenv('API_TOKEN')}"
    HOME_PAGE = os.getenv("HOME_PAGE")

    JIRA = "https://takealot.atlassian.net/"
    UPDATE_JIRA = os.getenv("UPDATE_JIRA", "False").upper() == "TRUE"

    _IS_DEV_ENV = os.getenv("ENVIRONMENT", "False").upper() == "DEV"
    LOG_RESPONSE = os.getenv("LOG_RESPONSE", "False").upper() == "TRUE"
    LOG_COUNTS = os.getenv("LOG_COUNTS", "False").upper() == "TRUE"
    LOG_INPUT = os.getenv("LOG_INPUT", "False").upper() == "TRUE"
    LOG_DETAIL = _IS_DEV_ENV
    LOG_REQUEST_URL = os.getenv("LOG_REQUEST_URL", "False").upper() == "TRUE"
    LOG_INPUT_DATA = os.getenv("LOG_INPUT_DATA", "False").upper() == "TRUE"
    SHOW_STEP_MSG = _IS_DEV_ENV
    HIGHLIGHT_ELEMENTS = _IS_DEV_ENV
    CONTEXT_FILE = "./contexts/context.json"

    TRACE_ENABLED = os.getenv("TRACE_ENABLED", "False").upper() == "TRUE"
    TRACE_PATH = "./results/trace/"
    VIDEOS_PATH = "./results/videos/"
    BROWSER = os.getenv("BROWSER", "chromium")

    class PAGES:
        """All the page urls"""

        invoices = "accounting/invoices"
        login = "login"
        home = ""
