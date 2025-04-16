import os

import requests

execute_db_query = "http://tal-test-data-service.master.env/execute_query_anydb"
execute_tal_data = "http://tal-test-data-service.master.env/create_new_order"


class ApiLibrary:

    def get_orders_from_take2(self):
        """Get orders from the database"""
        dbname = os.getenv("DBNAME")
        query = os.getenv("QUERY")
        dbuser = os.getenv("DBUSER")
        dbkey = os.getenv("DBKEY")
        dbhost = os.getenv("DBHOST")
        response = requests.post(
            execute_db_query,
            json={
                "db_lookup": "",
                "db_host": dbhost,
                "db_port": 9002,
                "db_name": dbname,
                "username": dbuser,
                "password": dbkey,
                "db_type": "mysql+pymysql",
                "query": query,
            },
            timeout=100,
        )
        return response.json()

    def get_customers_from_take2(self):
        """Get customers from the database"""
        dbname_t2 = os.getenv("DBNAME")
        query_t2 = os.getenv("QUERY")
        dbuser_t2 = os.getenv("DBUSER")
        dbkey_t2 = os.getenv("DBKEY")
        dbhost_t2 = os.getenv("DBHOST")
        response = requests.post(
            execute_db_query,
            json={
                "db_lookup": "",
                "db_host": dbhost_t2,
                "db_port": 3306,
                "db_name": dbname_t2,
                "username": dbuser_t2,
                "password": dbkey_t2,
                "db_type": "mysql+pymysql",
                "query": query_t2,
            },
            timeout=100,
        )
        return response.json()

    def create_new_order_tal(self):
        """Creates new orders"""
        customer_id = os.getenv("CUSTOMER")
        payment_method = os.getenv("PAYMENTMENTHOD")
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [{"product_id": 27408192, "quantity": 1, "unit_price": 400.0}, {"product_id": 27408193, "quantity": 1, "unit_price": 600.0}],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": True,
                "percentage_of_amount_due_to_pay": 100,
                "complete_payment": True,
                "add_donation": False,
                "cancel_order": False,
            },
            timeout=100,
        )
        return response.json()

    def create_new_order_tal_not_paid(self):
        """Creates new orders"""
        customer_id = os.getenv("CUSTOMER")
        payment_method = os.getenv("PAYMENTMENTHOD")
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [{"product_id": 27408192, "quantity": 1, "unit_price": 400.0}, {"product_id": 27408193, "quantity": 1, "unit_price": 600.0}],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": False,
                "percentage_of_amount_due_to_pay": 0,
                "complete_payment": False,
                "add_donation": False,
                "cancel_order": False,
            },
            timeout=100,
        )
        return response.json()

    def create_new_order_tal_cancelled(self):
        """Creates new orders"""
        customer_id = os.getenv("CUSTOMER")
        payment_method = os.getenv("PAYMENTMENTHOD")
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [{"product_id": 27408192, "quantity": 1, "unit_price": 400.0}, {"product_id": 27408193, "quantity": 1, "unit_price": 600.0}],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": True,
                "percentage_of_amount_due_to_pay": 100,
                "complete_payment": True,
                "add_donation": False,
                "cancel_order": True,
            },
            timeout=100,
        )
        return response.json()
