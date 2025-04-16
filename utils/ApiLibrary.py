import requests
from robot.libraries.BuiltIn import BuiltIn

execute_db_query = 'http://tal-test-data-service.master.env/execute_query_anydb'
execute_tal_data = 'http://tal-test-data-service.master.env/create_new_order'

class ApiLibrary(object):
    
    def get_orders_from_take2(self):
        """Get orders from the database"""
        dbname = BuiltIn().get_variable_value('${DBNAME}')
        query = BuiltIn().get_variable_value('${QUERY}')
        dbuser = BuiltIn().get_variable_value('${DBUSER}')
        dbkey = BuiltIn().get_variable_value('${DBKEY}')
        dbhost = BuiltIn().get_variable_value('${DBHOST}')
        response = requests.post(
            execute_db_query,
            json={
                'db_lookup': '',
                'db_host': dbhost,
                'db_port': 9002,
                'db_name': dbname,
                'username': dbuser,
                'password': dbkey,
                'db_type': 'mysql+pymysql',
                'query': query,
            },
        )
        return response.json()
    
    def get_customers_from_take2(self):
        """Get customers from the database"""
        dbname_t2 = BuiltIn().get_variable_value('${DBNAME}')
        query_t2 = BuiltIn().get_variable_value('${QUERY}')
        dbuser_t2 = BuiltIn().get_variable_value('${DBUSER}')
        dbkey_t2 = BuiltIn().get_variable_value('${DBKEY}')
        dbhost_t2 = BuiltIn().get_variable_value('${DBHOST}')
        response = requests.post(
            execute_db_query,
            json={
                'db_lookup': '',
                'db_host': dbhost_t2,
                'db_port': 3306,
                'db_name': dbname_t2,
                'username': dbuser_t2,
                'password': dbkey_t2,
                'db_type': 'mysql+pymysql',
                'query': query_t2,
            },
        )
        return response.json()

    def create_new_order_tal(self):
        """Creates new orders"""
        customer_id = BuiltIn().get_variable_value('${CUSTOMER}')
        payment_method = BuiltIn().get_variable_value('${PAYMENTMENTHOD}')
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [
                    {
                        "product_id": 27408192,
                        "quantity": 1,
                        "unit_price": 400.0
                    },
                    {
                        "product_id": 27408193,
                        "quantity": 1,
                        "unit_price": 600.0
                    }
                ],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": True,
                "percentage_of_amount_due_to_pay": 100,
                "complete_payment": True,
                "add_donation": False,
                "cancel_order": False
            },
        )
        return response.json()
    
    def create_new_order_tal_not_paid(self):
        """Creates new orders"""
        customer_id = BuiltIn().get_variable_value('${CUSTOMER}')
        payment_method = BuiltIn().get_variable_value('${PAYMENTMENTHOD}')
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [
                    {
                        "product_id": 27408192,
                        "quantity": 1,
                        "unit_price": 400.0
                    },
                    {
                        "product_id": 27408193,
                        "quantity": 1,
                        "unit_price": 600.0
                    }
                ],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": False,
                "percentage_of_amount_due_to_pay": 0,
                "complete_payment": False,
                "add_donation": False,
                "cancel_order": False
            },
        )
        return response.json()
    
    def create_new_order_tal_cancelled(self):
        """Creates new orders"""
        customer_id = BuiltIn().get_variable_value('${CUSTOMER}')
        payment_method = BuiltIn().get_variable_value('${PAYMENTMENTHOD}')
        response = requests.post(
            execute_tal_data,
            json={
                "customer_id": int(customer_id),
                "products": [
                    {
                        "product_id": 27408192,
                        "quantity": 1,
                        "unit_price": 400.0
                    },
                    {
                        "product_id": 27408193,
                        "quantity": 1,
                        "unit_price": 600.0
                    }
                ],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": payment_method,
                "pay_full_amount_due": True,
                "percentage_of_amount_due_to_pay": 100,
                "complete_payment": True,
                "add_donation": False,
                "cancel_order": True
            },
        )
        return response.json()