"""
Contains SQL queries related to the orders table
"""


class OrderQueries:
    """SQL queries for the orders table"""

    # Payment method specific queries
    paygate_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'CreditCard'
        and o.PaymentMethod = 'Credit Card'
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    payfast_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'PayFast'
        and o.PaymentMethod = 'PayFast'
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    deposit_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'Deposit'
        and o.AuthUser = 'ManualAuth'
        and o.idCredit IS NULL
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    ozow_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'iPay'
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    masterpass_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'Masterpass'
        order by o.OrderDate desc
        limit 1
    """

    cash_on_del_sql = """
        select o.idOrder
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'COD'
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    discovery_miles_sql = """
        select o.idOrder, o.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'Discovery'
        and o.PaymentMethod = 'Discovery Miles'
        and o.Qty = 1
        order by o.OrderDate Desc
        limit 1
    """

    ebucks_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'eBucks'
        and o.PaymentMethod = 'eBucks'
        order by o.OrderDate desc
        limit 1
    """

    cc_ebucks_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'Credit Card'
        and o.PaymentMethods = 'eBucks'
        order by o.OrderDate desc
        limit 1
    """

    sbux_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'sBux'
        order by o.OrderDate desc
        limit 1
    """

    payflex_sql = """
        select o.idOrder
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'Payflex'
        and o.PaymentMethod = 'Payflex'
        order by o.OrderDate
        limit 1
    """

    tal_credit_sql = """
        select o.idOrder
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.PaymentMethod = 'Credit'
        order by o.OrderDate
        limit 1
    """

    mobicred_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.AuthUser = 'Mobicred'
        and o.PaymentMethod = 'Mobicred'
        order by o.OrderDate desc
        limit 1
    """

    # Order status related queries
    risky_orders_sql = """
        select o.idOrder
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Risk = 1
        and o.Auth = 'Auth'
        and o.AuthUser = 'CreditCard'
        and o.PaymentMethod = 'Credit Card'
        order by o.OrderDate desc
        limit 1
    """

    non_risky_order_sql = """
        select o.idOrder
        from take2.orders o
        where o.Risk = 0
        order by o.OrderDate desc
        limit 1
    """

    # Orders with specific characteristics
    order_with_coupon_sql = """
        select o.idOrder, o.Discount, o.Total, o.Shipping
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status IN ('New Order','On Hold')
        and o.AuthUser = 'CreditCard'
        and o.PaymentMethod = 'Credit Card'
        and o.Discount > 1
        and o.idCredit IS NULL
        order by o.OrderDate desc
        limit 1
    """

    part_payment_order_sql = """
        select o.idOrder
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status <> 'Canceled'
        and o.PaymentMethod = 'Credit Card'
        and o.PaymentMethods = 'eBucks'
        order by o.OrderDate desc
        limit 1
    """

    order_with_more_order_items_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'Auth'
        and o.Qty > 1
        order by o.OrderDate desc
        limit 1
    """

    # New order queries
    new_order_ebucks_cc_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'New'
        and o.PaymentMethod = 'Credit Card'
        and o.PaymentMethods = 'eBucks'
        and o.Qty = 1
        and o.idCredit IS NULL
        order by o.OrderDate desc
        limit 1
    """

    new_order_mobicred_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'New'
        and o.PaymentMethod = 'Mobicred'
        and o.idCredit IS NULL
        and o.Qty = 1
        order by o.OrderDate desc
        limit 1
    """

    new_order_sbux_sql = """
        select o.idOrder, i.Total
        from take2.orders o
        join take2.orderitems i on o.idOrder = i.idOrder
        where i.Status = 'New Order'
        and o.Auth = 'New'
        and o.PaymentMethod = 'sBux'
        and o.idCredit IS NULL
        order by o.OrderDate desc
        limit 1
    """

    new_order_with_no_discount_amount_sql = """
        select o.idOrder, o.Total
        from orders o
        join orderitems oi on o.idOrder=oi.idOrder
        where o.Auth = 'New'
        and o.Discount = 0
        and oi.Status <> 'Canceled'
        order by o.OrderDate desc
        limit 1
    """

    new_order_with_no_discount_and_shipping_amount_sql = """
        select o.idOrder, o.Total
        from orders o
        join orderitems oi on o.idOrder=oi.idOrder
        where o.Auth = 'New'
        and o.Discount = 0
        and o.Shipping = 0
        and oi.Status <> 'Canceled'
        order by o.OrderDate desc
        limit 1
    """

    new_order_with_discount_and_shipping_amounts_sql = """
        select o.idOrder, o.Total, o.Shipping, o.Discount
        from orders o
        join orderitems oi on o.idOrder=oi.idOrder
        where o.Auth = 'New'
        and o.Discount > 1
        and o.Shipping > 1
        and oi.Status <> 'Canceled'
        order by o.OrderDate desc
        limit 1
    """
