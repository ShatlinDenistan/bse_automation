"""methods for providing test data to the test methods"""

import os
from collections import namedtuple


def get_credentials():
    """Get the credentials from os environments"""
    credentials = namedtuple("credentials", "username password")
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    return credentials(username=username, password=password)
