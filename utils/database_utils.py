import os
import json
from utils.api_library import ApiLibrary


class DatabaseUtils:
    """
    Database utility class converted from kwDatabases.robot
    Contains SQL queries and database interaction methods
    """

    # SQL Queries converted from Robot Framework variables
    PAYGATE_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                  where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' 
                  and o.PaymentMethod = 'Credit Card' and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    PAYFAST_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                  where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'PayFast' 
                  and o.PaymentMethod = 'PayFast' and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    DEPOSIT_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                  where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Deposit' 
                  and o.AuthUser = 'ManualAuth' and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    OZOW_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'iPay' 
                and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    MASTERPASS_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                     where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Masterpass' 
                     order by o.OrderDate desc limit 1;"""

    CASH_ON_DEL_SQL = """select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                      where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'COD' 
                      and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    RISKY_ORDERS_SQL = """select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                       where i.Status = 'New Order' and o.Risk = 1 and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' 
                       and o.PaymentMethod = 'Credit Card' order by o.OrderDate desc limit 1;"""

    DISCOVERY_MILES_SQL = """select o.idOrder, o.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                          where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Discovery' 
                          and o.PaymentMethod = 'Discovery Miles' and o.Qty = 1 order by o.OrderDate Desc limit 1;"""

    EBUCKS_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                 where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'eBucks' 
                 and o.PaymentMethod = 'eBucks' order by o.OrderDate desc limit 1;"""

    CC_EBUCKS_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                    where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit Card' 
                    and o.PaymentMethods = 'eBucks' order by o.OrderDate desc limit 1;"""

    SBUX_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
               where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'sBux' 
               order by o.OrderDate desc limit 1;"""

    ORDER_WITH_COUPON_SQL = """select o.idOrder, o.Discount, o.Total, o.Shipping from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                            where i.Status IN ('New Order','On Hold') and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' 
                            and o.Discount > 1 and o.idCredit IS NULL order by o.OrderDate desc limit 1;"""

    PAYFLEX_SQL = """select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                  where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Payflex' 
                  and o.PaymentMethod = 'Payflex' order by o.OrderDate limit 1;"""

    DONATION_AMOUNT_SQL = """SELECT o.idOrder, o.Total, o.Shipping, i.Total, d.donation FROM take2.orders o 
                          INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder 
                          INNER JOIN take2.donations d ON i.idOrder = d.idOrder 
                          WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' 
                          ORDER BY o.OrderDate desc LIMIT 1;"""

    TAL_CREDIT_SQL = """select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                     where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit' 
                     order by o.OrderDate limit 1;"""

    MOBICRED_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                   where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Mobicred' 
                   and o.PaymentMethod = 'Mobicred' order by o.OrderDate desc limit 1;"""

    BLACKLISTED_SQL = """select idCustomer from take2.BlackListedCustomers order by timestamp desc;"""

    CREDIT_CARD_DONATION_ORDER_SQL = """select o.idOrder , i.Total from take2.orders o 
                                     INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder 
                                     INNER JOIN take2.donations d ON i.idOrder = d.idOrder 
                                     WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' 
                                     AND o.Qty = 1 ORDER BY o.OrderDate desc LIMIT 1"""

    NEW_ORDER_EBUCKS_CC_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                             where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Credit Card' 
                             and o.PaymentMethods = 'eBucks' and o.Qty = 1 and o.idCredit IS NULL 
                             order by o.OrderDate desc limit 1;"""

    NEW_ORDER_MOBICRED_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                            where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Mobicred' 
                            and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;"""

    NEW_ORDER_SBUX_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                         where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'sBux' 
                         and o.idCredit IS NULL order by o.OrderDate desc limit 1;"""

    AUTO_CANCELED_ORDERS_SQL = """select o.idOrder,o.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
                               from take2.orderitems_cancellation_reason cr join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
                               where orderitems_cancellation_reason_type_id = 12 and cancelled_by = 'auto_cancel' 
                               order by cr.date_cancelled desc limit 1;"""

    AUTO_CANCELED_ORDERS_WITH_STAFF_DISCOUNT_SQL = """select oi.idOrder,oi.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
                                                    from take2.orderitems_cancellation_reason cr join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem 
                                                    join take2.orders o on oi.idOrder = o.idOrder where cr.orderitems_cancellation_reason_type_id = 12 
                                                    and cr.cancelled_by = 'auto_cancel'and o.AdminNotes like '%Staff discount applied%'
                                                    order by cr.date_cancelled desc limit 1;"""

    AUTO_CANCELED_ORDER_WITH_CHARGES_SQL = """select oi.idOrder,o.Shipping,o.Discount from take2.orderitems_cancellation_reason cr 
                                           join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem join take2.orders o on oi.idOrder = o.idOrder 
                                           where cr.cancelled_by IN ('auto_cancel','auto_cancel_promotions') 
                                           and orderitems_cancellation_reason_type_id = 12 and o.Shipping > 1 and o.Discount > 1 
                                           and o.Auth = 'New' and oi.Status = 'Canceled' order by cr.date_cancelled desc limit 1;"""

    CANCELED_ORDER_EXCEPT_AUTO_CANCELED_SQL = """select o.idOrder,cancelled_by from take2.orderitems_cancellation_reason cr 
                                             join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
                                             where orderitems_cancellation_reason_type_id != 12 
                                             order by cr.date_cancelled desc limit 1;"""

    NEW_ORDER_WITH_NO_DISCOUNT_AMOUNT_SQL = """select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder 
                                           where o.Auth = 'New' and o.Discount = 0 
                                           and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;"""

    NEW_ORDER_WITH_NO_DISCOUNT_AND_SHIPPING_AMOUNT_SQL = """select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder 
                                                         where o.Auth = 'New' and o.Discount = 0 
                                                         and o.Shipping = 0 and oi.Status <> 'Canceled' 
                                                         order by o.OrderDate desc limit 1;"""

    ORDER_WITH_RETURNED_CANCELED_ORDER_ITEM_SQL = """select oi.idOrder, oi.status from orderitems oi join orders o on oi.idOrder = o.idOrder 
                                                  where oi.status = 'Return Canceled' 
                                                  and o.qty = 1 order by 1 desc limit 1;"""

    NEW_ORDER_WITH_DISCOUNT_AND_SHIPPING_AMOUNTS_SQL = """select o.idOrder, o.Total, o.Shipping, o.Discount from orders o 
                                                       join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount > 1 
                                                       and o.Shipping > 1 and oi.Status <> 'Canceled' 
                                                       order by o.OrderDate desc limit 1;"""

    NON_RISKY_ORDER_SQL = """select o.idOrder from take2.orders o where o.Risk = 0 order by o.OrderDate desc limit 1;"""

    PART_PAYMENT_ORDER_SQL = """select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                              where i.Status <> 'Canceled' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' 
                              order by o.OrderDate desc limit 1;"""

    ORDER_WITH_MORE_ORDER_ITEMS_SQL = """select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder 
                                      where i.Status = 'New Order' and o.Auth = 'Auth' and o.Qty > 1 
                                      order by o.OrderDate desc limit 1;"""

    def __init__(self):
        """Initialize the database utilities"""
        self.api_library = ApiLibrary()
        # Global variables to store query results
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
        Get orders from database using ApiLibrary.py

        Args:
            query: SQL query to execute

        Returns:
            Dictionary with order details
        """
        # Set the query as an environment variable
        os.environ["QUERY"] = query

        # Get orders from Take2 database
        json_content = self.api_library.get_orders_from_take2()

        # Extract values from JSON
        self.order_ids = json_content[0].get("idOrder") if json_content else None
        self.order_discount = json_content[0].get("Discount") if json_content else None
        self.order_shipping = json_content[0].get("Shipping") if json_content else None
        self.order_total = json_content[0].get("Total") if json_content else None
        self.donation_amount = json_content[0].get("donation") if json_content else None

        print(self.order_ids)

        # Return the entire result for additional processing if needed
        return {"order_ids": self.order_ids, "order_discount": self.order_discount, "order_shipping": self.order_shipping, "order_total": self.order_total, "donation_amount": self.donation_amount}

    def get_customers_from_database(self, query):
        """
        Get customers from database using ApiLibrary.py

        Args:
            query: SQL query to execute

        Returns:
            Dictionary with customer details
        """
        # Set the query as an environment variable
        os.environ["QUERY"] = query

        # Get customers from Take2 database
        json_content = self.api_library.get_customers_from_take2()

        # Extract values from JSON
        self.customer_ids = json_content[0].get("idCustomer") if json_content else None

        # Return the entire result for additional processing if needed
        return {"customer_ids": self.customer_ids}

    def create_new_tal_orders(self, customer, payment_method):
        """
        Create new TAL orders

        Args:
            customer: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary with order details
        """
        # Set environment variables
        os.environ["CUSTOMER"] = str(customer)
        os.environ["PAYMENTMENTHOD"] = payment_method

        # Create new order
        orders_content = self.api_library.create_new_order_tal()

        # Extract values from JSON
        self.order_ids = orders_content.get("order_id")
        self.id_order_item1 = orders_content.get("items")[0].get("order_item_id") if orders_content.get("items") else None
        self.id_order_item2 = orders_content.get("items")[1].get("order_item_id") if len(orders_content.get("items", [])) > 1 else None
        self.order_total = orders_content.get("total_amount")

        print(self.order_ids)

        # Return the entire result for additional processing if needed
        return {"order_ids": self.order_ids, "id_order_item1": self.id_order_item1, "id_order_item2": self.id_order_item2, "order_total": self.order_total}

    def create_new_tal_orders_not_paid(self, customer, payment_method):
        """
        Create new TAL orders that are not paid

        Args:
            customer: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary with order details
        """
        # Set environment variables
        os.environ["CUSTOMER"] = str(customer)
        os.environ["PAYMENTMENTHOD"] = payment_method

        # Create new order not paid
        orders_content = self.api_library.create_new_order_tal_not_paid()

        # Extract values from JSON
        self.order_ids = orders_content.get("order_id")
        self.order_total = orders_content.get("total_amount")

        # Return the entire result for additional processing if needed
        return {"order_ids": self.order_ids, "order_total": self.order_total}

    def create_new_tal_orders_cancelled(self, customer, payment_method):
        """
        Create new TAL orders that are cancelled

        Args:
            customer: Customer ID
            payment_method: Payment method to use

        Returns:
            Dictionary with order details
        """
        # Set environment variables
        os.environ["CUSTOMER"] = str(customer)
        os.environ["PAYMENTMENTHOD"] = payment_method

        # Create new cancelled order
        orders_content = self.api_library.create_new_order_tal_cancelled()

        # Extract values from JSON
        self.order_ids = orders_content.get("order_id")
        self.order_total = orders_content.get("total_amount")

        # Return the entire result for additional processing if needed
        return {"order_ids": self.order_ids, "order_total": self.order_total}
