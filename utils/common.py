import random
import string
import time

import datetime
import logging as logger
import math
import os
import secrets
import timeit
from collections import UserString
from io import IOBase
from os import PathLike
from typing import Any, Iterable, Mapping

import re
from config.config import TestConfig as test_config

TRUE_STRINGS = {"TRUE", "YES", "ON", "1"}
FALSE_STRINGS = {"FALSE", "NO", "OFF", "0", "NONE", ""}


class CommonUtils:
    """Common utility functions for various operations."""

    @staticmethod
    def get_file_extension(filename: str) -> str:
        """
        Get the file extension from a filename.
        :param filename: The name of the file.
        :return: The file extension.
        """
        return filename.split(".")[-1] if "." in filename else ""

    @staticmethod
    def create_random_email(domain: str = "example.com") -> str:
        """
        Create a random email address.
        :param domain: The domain for the email address.
        :return: A random email address.
        """

        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        timestamp = int(time.time())
        return f"{random_string}{timestamp}@{domain}"

    @staticmethod
    def check_if_data_exists_in_table(data, table_data, column_number):
        """Checks if given data exists in the specified column of the table"""
        for row in table_data:
            if row[column_number] == data:
                return True
        return False

    @staticmethod
    def start_tracking_time(message=None):
        """Starts timer and logs optional message"""
        if message:
            logger.info("start tracking time: %s", message)
        return timeit.default_timer()

    @staticmethod
    def end_tracking_time(start_time):
        """Ends timer and logs total time taken"""
        total_time = timeit.default_timer() - start_time
        time_string = f"{total_time:.2f} seconds"
        if total_time > 60:
            time_string = f"{(total_time / 60):.2f} minutes"
        if total_time > 3600:
            time_string = f"{(total_time / 3600):.2f} hours"
        logger.info("Total time taken: %s", time_string)

    @staticmethod
    def random_test_string(use_spaces=True):
        """Generates a random test string to use for naming files"""
        return f"automation {CommonUtils().get_datetime_string(use_spaces=use_spaces)}"

    @staticmethod
    def pad_date_string_with_zero(date_string: str):
        """Pads the date string with leading zeros if needed"""
        date_list = date_string.split("/")
        for i, _ in enumerate(date_list):
            date_list[i] = f"0{date_list[i]}" if len(date_list[i]) < 2 else date_list[i]
        if len(date_list[2]) == 2:
            date_list[2] = f"20{date_list[2]}"
        return "/".join(date_list)

    @staticmethod
    def random_email():
        """Generates a random email"""
        return f"{secrets.token_hex(8)}@gmail.com"

    @staticmethod
    def file_is_empty(path):
        """Checks if file at path is empty"""
        return os.stat(path).st_size == 0

    @staticmethod
    def get_alpha_numeric(length, data_type="letters"):
        """Returns a random alphanumeric string of given length and type"""
        alpha_num = ""
        if data_type == "digits":
            case = string.digits
        elif data_type == "lower":
            case = string.ascii_lowercase
        elif data_type == "mix":
            case = string.ascii_letters + string.digits
        elif data_type == "upper":
            case = string.ascii_uppercase
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for _ in range(length))

    @staticmethod
    def get_random_string(char_count=10):
        """Returns a random lowercase string of specified length"""
        return CommonUtils().get_alpha_numeric(char_count, "lower")

    @staticmethod
    def get_unique_name_list(list_size=5, item_length=None):
        """Returns a list of unique random strings"""
        return CommonUtils().get_random_string(item_length[i] for i in range(list_size))

    @staticmethod
    def verify_list_match(expected, actual):
        """Checks if two lists have the same elements"""
        return set(expected) == set(actual)

    @staticmethod
    def verify_list_contains(expected, actual):
        """Checks if all elements in expected exist in actual"""
        length = len(expected)
        return all(expected[i] in actual for i in range(length))

    @staticmethod
    def verify_text_contains(actual, expected):
        """Checks if expected text is in actual text (case-insensitive)"""
        return expected.lower() in actual.lower()

    @staticmethod
    def verify_text_match(actual, expected):
        """Checks if two texts match exactly (case-insensitive)"""
        return expected.lower() == actual.lower()

    @staticmethod
    def plural_or_not(item):
        """Returns 's' if item count is plural, else empty string"""
        count = item if CommonUtils().is_integer(item) else len(item)
        return "" if count in (1, -1) else "s"

    @staticmethod
    def is_integer(item):
        """Checks if item is an integer"""
        return isinstance(item, int)

    @staticmethod
    def is_number(item):
        """Checks if item is a number (int or float)"""
        return isinstance(item, (int, float))

    @staticmethod
    def is_bytes(item):
        """Checks if item is bytes or bytearray"""
        return isinstance(item, (bytes, bytearray))

    @staticmethod
    def is_string(item):
        """Checks if item is a string"""
        return isinstance(item, str)

    @staticmethod
    def is_pathlike(item):
        """Checks if item is a path-like object"""
        return isinstance(item, PathLike)

    @staticmethod
    def is_list_like(item):
        """Checks if item behaves like a list"""
        if isinstance(item, (str, bytes, bytearray, UserString, IOBase)):
            return False
        return isinstance(item, Iterable)

    @staticmethod
    def is_dict_like(item):
        """Checks if item behaves like a dictionary"""
        return isinstance(item, Mapping)

    @staticmethod
    def type_converter(argument: Any) -> str:
        """Returns the type name of the argument in lowercase"""
        return type(argument).__name__.lower()

    @staticmethod
    def generate_random_email_and_password(domain=None, email_prefix=None):
        """Generates a random email and password with optional domain and prefix"""
        if not domain:
            domain = "takealot.com"
        if not email_prefix:
            email_prefix = "test_user"
        temp_length = 10
        random_string = "".join(random.choices(string.ascii_lowercase, k=temp_length))
        generated_email = f"{email_prefix}_{random_string}@{domain}"
        temp_length = 20
        generated_password = "".join(random.choices(string.ascii_lowercase, k=temp_length))
        return {"email": generated_email, "password": generated_password}

    @staticmethod
    def generate_random_string(length=10, prefix=None, suffix=None):
        """Generates a random string with optional prefix and suffix"""
        random_string = "".join(random.choices(string.ascii_lowercase, k=length))
        if prefix:
            random_string = prefix + random_string
        if suffix:
            random_string += suffix
        return random_string

    @staticmethod
    def generate_random_number(length=4):
        """Generates a random number with specified digit length"""
        random_number = random.randint(1 * pow(10, length), (1 * pow(10, length + 1)) - 1)
        return random_number

    @staticmethod
    def get_datetime():
        """Returns current datetime as formatted string"""
        return datetime.datetime.now().strftime("%d-%m %H:%M:%S.%f")[:-3]

    @staticmethod
    def get_datetime_string(date=datetime.datetime.now(), use_spaces=False):
        """Returns formatted date string with optional spaces"""
        if use_spaces:
            return date.strftime("%d-%m-%y %H:%M:%S")
        return date.strftime("%d%m%y%H%M%S")

    @staticmethod
    def get_date_month_year_string():
        """Returns current date as dd_mm_yy string"""
        return datetime.datetime.now().strftime("%d_%m_%y")

    @staticmethod
    def get_random_date(days: int = 365):
        """Returns a random date within the past given number of days"""
        start_date = datetime.datetime.now()
        end_date = start_date - datetime.timedelta(days)
        random_date = start_date + (end_date - start_date) * random.random()
        return str(random_date)

    @staticmethod
    def get_random_date_between(start_range: int, end_range: int):
        """Returns a random future date between two ranges in days"""
        start_date = datetime.datetime.now()
        random_number_of_days = random.randint(start_range, end_range)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return str(random_date)

    @staticmethod
    def get_date_based_on_variable(days):
        """Returns date offset from today by given number of days"""
        current_date = datetime.date.today()
        result_date = current_date + datetime.timedelta(days=days)
        return result_date

    @staticmethod
    def get_key_by_value(dictionary, search_value):
        """Returns dictionary key for a given value"""
        for key, value in dictionary.items():
            if value == search_value:
                return key
        return None

    @staticmethod
    def log(message):
        """Logs message if LOG_DETAIL is enabled"""
        if test_config.LOG_DETAIL:
            logger.info(message)

    @staticmethod
    def get_test_name():
        """Returns the current pytest test name"""
        current_test = os.environ.get("PYTEST_CURRENT_TEST")
        test_name = current_test.split(":")[-1].split(" ")[0]
        test_name = test_name.replace("[chromium]", "")
        return test_name.lower()

    @staticmethod
    def log_test_name():
        """Logs the current test name as a footer"""
        test_name = CommonUtils().get_test_name()
        footer = f"{test_name} completed "
        logger.info(CommonUtils().construct_test_info_line(footer))

    @staticmethod
    def construct_test_info_line(text):
        """Returns a formatted log line with the given text"""
        filler_full_length = 100
        filler_length = (filler_full_length - len(text)) // 2
        filler_left = filler_length
        if filler_length % 2 == 1:
            filler_left = filler_length + 1
        return f'{"=" * filler_left}{text}{"=" * filler_length}'

    @staticmethod
    def get_hour_string(hour):
        """Formats an hour into HH:00:00 string"""
        hour = f"0{hour}" if hour < 10 else hour
        hour = f"{hour}:00:00"
        return hour

    @staticmethod
    def get_timestamp(prefix: str = None, suffix: str = None) -> str:
        """Returns unique timestamp string with optional prefix and suffix"""
        pre = prefix if prefix is not None else ""
        if len(pre) > 0 and pre[-1] != "_":
            pre += "_"
        time_stamp = CommonUtils().get_datetime_string(datetime.datetime.now())
        suf = suffix if suffix is not None else ""
        return f"{pre}{time_stamp}{suf}"

    @staticmethod
    def round_time_up(date: datetime.datetime, rounding: int = 15):
        """Round time up to next x time"""
        mins = date.minute

        mins = (math.floor((mins - 1) / rounding + 1) * rounding) - mins

        return date + datetime.timedelta(minutes=mins)

    @staticmethod
    def get_random_record(collection):
        """get a random record from a collection"""
        count = len(collection) - 1
        record = collection[random.randint(0, count)]
        return record

    @staticmethod
    def get_env(key: str, default: Any = None) -> Any:
        """Get an environment variable ignoring case and return a default value if it is not set.
        Parameters
        ----------
        key : str, required
            The name of the environment variable.
        default : Any, optional
            The default value to return if the environment variable is not set. Defaults to None.

        Returns
        ------
        Any
            The value of the environment variable or the default value if it is not set.
        """
        value = next((value for key, value in os.environ.items() if key.lower() == "browser"), default)
        return value

    @staticmethod
    def is_valid_url(url):
        url_pattern = re.compile(r"^https?://")
        assert bool(url_pattern.match(url)) is True
