import os


class TestConfig:
    """All the configurations for the tests"""

    BFF_URL = os.getenv("BFF_ENV_URL")
    TEST_DATA_SERVICE = os.getenv("TEST_DATA_SERVICE")
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
    TRACE_PATH = "./ouput/trace/"
    VIDEOS_PATH = "./output/videos/"
    BROWSER = os.getenv("BROWSER", "chromium")

    # Timeouts
    MAX_TIMEOUT = 60  # seconds
    MIN_TIMEOUT = 20  # seconds
    SLEEP = 2  # seconds

    # Test Data

    Deposit_Match_File = "testData/GENERIC GLOBAL 1.csv"
    Deposit_Match_File_30 = "testData/GENERIC MORE THAN 15 RECORDS.csv"
    Deposit_Match_File_Auth = "testData/GENERIC GLOBAL AuthNew.csv"
    Deposit_Match_New_Order_File = "testData/NewOrderUploadFile.csv"
    CustomerID_Doc = "testData/Customer_ID.jpeg"

    class PAGES:
        """All the page urls"""

        invoices = "accounting/invoices"
        login = "login"
        home = ""
