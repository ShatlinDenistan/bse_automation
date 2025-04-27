import os


class TestConfig:
    """All the configurations for the tests"""

    # Environment settings
    _IS_DEV_ENV = os.getenv("ENVIRONMENT", "False").upper() == "DEV"

    # URLs and Endpoints
    BFF_URL = os.getenv("BFF_ENV_URL")
    TEST_DATA_SERVICE = os.getenv("TEST_DATA_SERVICE")
    HOME_PAGE = os.getenv("HOME_PAGE")
    JIRA = "https://takealot.atlassian.net/"
    UPDATE_JIRA = os.getenv("UPDATE_JIRA", "False").upper() == "TRUE"

    # File paths
    CONTEXT_FILE = "./contexts/context.json"
    TRACE_PATH = "./output/trace/"
    VIDEOS_PATH = "./output/videos/"

    # Logging settings
    LOG_RESPONSE = os.getenv("LOG_RESPONSE", "False").upper() == "TRUE"
    LOG_COUNTS = os.getenv("LOG_COUNTS", "False").upper() == "TRUE"
    LOG_INPUT = os.getenv("LOG_INPUT", "False").upper() == "TRUE"
    LOG_DETAIL = _IS_DEV_ENV
    LOG_REQUEST_URL = os.getenv("LOG_REQUEST_URL", "False").upper() == "TRUE"
    LOG_INPUT_DATA = os.getenv("LOG_INPUT_DATA", "False").upper() == "TRUE"
    SHOW_STEP_MSG = _IS_DEV_ENV
    HIGHLIGHT_ELEMENTS = _IS_DEV_ENV

    # Browser settings
    BROWSER = os.getenv("BROWSER", "chromium")
    TRACE_ENABLED = os.getenv("TRACE_ENABLED", "False").upper() == "TRUE"

    # Timeouts
    MAX_TIMEOUT = 60  # seconds
    MIN_TIMEOUT = 15  # seconds
    SLEEP = 5  # seconds
