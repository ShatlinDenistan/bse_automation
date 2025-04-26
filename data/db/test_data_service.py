import os
import requests

from config.config import TestConfig


class TestDataService:
    def __init__(self):
        """Initialize common variables used across methods"""
        # Get database connection parameters once
        self.dbname = os.getenv("DBNAME")
        self.dbuser = os.getenv("DBUSER")
        self.dbkey = os.getenv("DBKEY")
        self.dbhost = os.getenv("DBHOST")
        self.query = os.getenv("QUERY")
        self.customer_id = os.getenv("CUSTOMER")
        self.payment_method = os.getenv("PAYMENTMENTHOD")
        self.db_port = 9002
        # Get API endpoints from environment variables
        self.config = TestConfig()
        self.execute_db_query_endpoint = f"{self.config.TEST_DATA_SERVICE}/execute_query_anydb"

    def _execute_query(self, query):
        """Common method for executing database queries"""
        response = requests.post(
            self.execute_db_query_endpoint,
            json={
                "db_lookup": "",
                "db_host": self.dbhost,
                "db_port": self.db_port,
                "db_name": self.dbname,
                "username": self.dbuser,
                "password": self.dbkey,
                "db_type": "mysql+pymysql",
                "query": query,
            },
            timeout=100,
        )
        return response.json()
