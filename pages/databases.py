import os
import requests
import json

# API endpoint constants
EXECUTE_DB_QUERY = "http://tal-test-data-service.master.env/execute_query_anydb"
EXECUTE_TAL_DATA = "http://tal-test-data-service.master.env/create_new_order"


class Database:
    # SQL query definitions
    paygate_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' and o.Qty = 1 order by o.OrderDate desc limit 1;"
    payfast_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'PayFast' and o.PaymentMethod = 'PayFast' and o.Qty = 1 order by o.OrderDate desc limit 1;"
    deposit_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Deposit' and o.AuthUser = 'ManualAuth' and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;"
    ozow_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'iPay' and o.Qty = 1 order by o.OrderDate desc limit 1;"
    masterpass_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Masterpass' order by o.OrderDate desc limit 1;"
    cash_on_del_sql = "select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'COD' and o.Qty = 1 order by o.OrderDate desc limit 1;"
    risky_orders_sql = "select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Risk = 1 and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' order by o.OrderDate desc limit 1;"
    discovery_miles_sql = "select o.idOrder, o.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Discovery' and o.PaymentMethod = 'Discovery Miles' and o.Qty = 1 order by o.OrderDate Desc limit 1;"
    ebucks_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'eBucks' and o.PaymentMethod = 'eBucks' order by o.OrderDate desc limit 1;"
    cc_ebucks_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' order by o.OrderDate desc limit 1;"
    sbux_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'sBux' order by o.OrderDate desc limit 1;"
    order_with_coupon_sql = "select o.idOrder, o.Discount, o.Total, o.Shipping from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status IN ('New Order','On Hold') and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' and o.Discount > 1 and o.idCredit IS NULL order by o.OrderDate desc limit 1;"
    payflex_sql = "select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Payflex' and o.PaymentMethod = 'Payflex' order by o.OrderDate limit 1;"
    donation_amount_sql = "SELECT o.idOrder, o.Total, o.Shipping, i.Total, d.donation FROM take2.orders o INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder INNER JOIN take2.donations d ON i.idOrder = d.idOrder WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' ORDER BY o.OrderDate desc LIMIT 1;"
    tal_credit_sql = "select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit' order by o.OrderDate limit 1;"
    mobicred_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Mobicred' and o.PaymentMethod = 'Mobicred' order by o.OrderDate desc limit 1;"
    blacklisted_sql = "select idCustomer from take2.BlackListedCustomers order by timestamp desc;"
    credit_card_donation_order_sql = "select o.idOrder , i.Total from take2.orders o INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder INNER JOIN take2.donations d ON i.idOrder = d.idOrder WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' AND o.Qty = 1 ORDER BY o.OrderDate desc LIMIT 1"
    new_order_ebucks_cc_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' and o.Qty = 1 and o.idCredit IS NULL order by o.OrderDate desc limit 1;"
    new_order_mobicred_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Mobicred' and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;"
    new_order_sbux_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'sBux' and o.idCredit IS NULL order by o.OrderDate desc limit 1;"
    auto_canceled_orders_sql = """select o.idOrder,o.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
    from take2.orderitems_cancellation_reason cr join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
    where orderitems_cancellation_reason_type_id = 12 and cancelled_by = 'auto_cancel' order by cr.date_cancelled desc limit 1;"""
    auto_canceled_orders_with_staff_discount_sql = """select oi.idOrder,oi.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
    from take2.orderitems_cancellation_reason cr join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem 
    join take2.orders o on oi.idOrder = o.idOrder where cr.orderitems_cancellation_reason_type_id = 12 
    and cr.cancelled_by = 'auto_cancel'and o.AdminNotes like '%Staff discount applied%'order by cr.date_cancelled desc limit 1;"""
    auto_canceled_order_with_charges_sql = """select oi.idOrder,o.Shipping,o.Discount from take2.orderitems_cancellation_reason cr 
    join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem join take2.orders o on oi.idOrder = o.idOrder where cr.cancelled_by IN ('auto_cancel','auto_cancel_promotions') 
    and orderitems_cancellation_reason_type_id = 12 and o.Shipping > 1 and o.Discount > 1 and o.Auth = 'New' and oi.Status = 'Canceled' order by cr.date_cancelled desc limit 1;"""
    canceled_order_except_auto_canceled_sql = """select o.idOrder,cancelled_by from take2.orderitems_cancellation_reason cr join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
    where orderitems_cancellation_reason_type_id != 12 order by cr.date_cancelled desc limit 1;"""
    new_order_with_no_discount_amount_sql = """select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount = 0 
    and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;"""
    new_order_with_no_discount_and_shipping_amount_sql = """select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount = 0 
    and o.Shipping = 0 and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;"""
    order_with_returned_canceled_order_item_sql = """select oi.idOrder, oi.status from orderitems oi join orders o on oi.idOrder = o.idOrder where oi.status = 'Return Canceled' 
    and o.qty = 1 order by 1 desc limit 1;"""
    new_order_with_discount_and_shipping_amounts_sql = """select o.idOrder, o.Total, o.Shipping, o.Discount from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount > 1 
    and o.Shipping > 1 and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;"""
    non_risky_order_sql = "select o.idOrder from take2.orders o where o.Risk = 0 order by o.OrderDate desc limit 1;"
    part_payment_order_sql = "select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status <> 'Canceled' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' order by o.OrderDate desc limit 1;"
    order_with_more_order_items_sql = "select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.Qty > 1 order by o.OrderDate desc limit 1;"

    def __init__(self):
        # Instance variables to store order/customer details
        self.order_ids = None
        self.order_discount = None
        self.order_shipping = None
        self.order_total = None
        self.donation_amount = None
        self.customer_ids = None
        self.id_order_item1 = None
        self.id_order_item2 = None

    def get_orders_from_database(self, query):
        """
        This function gets orders from database

        Args:
            query: SQL query to execute

        Returns:
            Dictionary containing order details
        """
        json_content = self.get_orders_from_take2(query)
        if json_content and len(json_content) > 0:
            self.order_ids = json_content[0].get("idOrder")
            self.order_discount = json_content[0].get("Discount")
            self.order_shipping = json_content[0].get("Shipping")
            self.order_total = json_content[0].get("Total")
            self.donation_amount = json_content[0].get("donation")

            print(self.order_ids)
            return {"order_ids": self.order_ids, "order_discount": self.order_discount, "order_shipping": self.order_shipping, "order_total": self.order_total, "donation_amount": self.donation_amount}
        return None

    def get_customers_from_database(self, query):
        """
        This function gets customers from database

        Args:
            query: SQL query to execute

        Returns:
            Dictionary containing customer details
        """
        json_content = self.get_customers_from_take2(query)
        if json_content and len(json_content) > 0:
            self.customer_ids = json_content[0].get("idCustomer")
            return {"customer_ids": self.customer_ids}
        return None

    def create_new_tal_orders(self, customer_id, payment_method):
        """
        This function creates new orders in TAL

        Args:
            customer_id: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary containing order details
        """
        orders_content = self.create_new_order_tal(customer_id, payment_method)
        if orders_content:
            self.order_ids = orders_content.get("order_id")

            if "items" in orders_content and len(orders_content["items"]) >= 2:
                self.id_order_item1 = orders_content["items"][0].get("order_item_id")
                self.id_order_item2 = orders_content["items"][1].get("order_item_id")

            self.order_total = orders_content.get("total_amount")

            print(self.order_ids)
            return {"order_ids": self.order_ids, "id_order_item1": self.id_order_item1, "id_order_item2": self.id_order_item2, "order_total": self.order_total}
        return None

    def create_new_tal_orders_not_paid(self, customer_id, payment_method):
        """
        This function creates orders that are not paid

        Args:
            customer_id: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary containing order details
        """
        orders_content = self.create_new_order_tal_not_paid(customer_id, payment_method)
        if orders_content:
            self.order_ids = orders_content.get("order_id")
            self.order_total = orders_content.get("total_amount")
            return {"order_ids": self.order_ids, "order_total": self.order_total}
        return None

    def create_new_tal_orders_cancelled(self, customer_id, payment_method):
        """
        This function creates orders that are cancelled

        Args:
            customer_id: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary containing order details
        """
        orders_content = self.create_new_order_tal_cancelled(customer_id, payment_method)
        if orders_content:
            self.order_ids = orders_content.get("order_id")
            self.order_total = orders_content.get("total_amount")
            return {"order_ids": self.order_ids, "order_total": self.order_total}
        return None

    # API methods
    def get_orders_from_take2(self, query):
        """Get orders from the database"""
        dbname = os.getenv("DBNAME")
        dbuser = os.getenv("DBUSER")
        dbkey = os.getenv("DBKEY")
        dbhost = os.getenv("DBHOST")

        response = requests.post(
            EXECUTE_DB_QUERY,
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
            timeout=10,
        )
        return response.json()

    def get_customers_from_take2(self, query):
        """Get customers from the database"""
        dbname = os.getenv("DBNAME")
        dbuser = os.getenv("DBUSER")
        dbkey = os.getenv("DBKEY")
        dbhost = os.getenv("DBHOST")

        response = requests.post(
            EXECUTE_DB_QUERY,
            json={
                "db_lookup": "",
                "db_host": dbhost,
                "db_port": 3306,
                "db_name": dbname,
                "username": dbuser,
                "password": dbkey,
                "db_type": "mysql+pymysql",
                "query": query,
            },
            timeout=10,
        )
        return response.json()

    def create_new_order_tal(self, customer_id, payment_method):
        """Creates new orders"""
        response = requests.post(
            EXECUTE_TAL_DATA,
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
            timeout=10,
        )
        return response.json()

    def create_new_order_tal_not_paid(self, customer_id, payment_method):
        """Creates new orders that are not paid"""
        response = requests.post(
            EXECUTE_TAL_DATA,
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
            timeout=10,
        )
        return response.json()

    def create_new_order_tal_cancelled(self, customer_id, payment_method):
        """Creates new orders that are cancelled"""
        response = requests.post(
            EXECUTE_TAL_DATA,
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
            timeout=10,
        )
        return response.json()
