from typing import List
from data.db.test_data_service import TestDataService
from models.customer_model import CustomerModel


class CustomerData(TestDataService):

    def get_customers(self, query):
        json_content = self._execute_query(query)
        return List(CustomerModel().from_json(json_content))
