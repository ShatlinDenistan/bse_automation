"""
Contains SQL queries related to order items and order item cancellations
"""


class OrderItemQueries:
    """SQL queries for order items and their related operations"""

    # Order item cancellation queries
    auto_canceled_orders_sql = """
        select o.idOrder, o.idOrderItem, cr.orderitems_cancellation_reason_type_id, cr.cancelled_by, cr.date_cancelled
        from take2.orderitems_cancellation_reason cr
        join take2.orderitems o on cr.orderitem_id = o.idOrderItem
        where orderitems_cancellation_reason_type_id = 12
        and cancelled_by = 'auto_cancel'
        order by cr.date_cancelled desc
        limit 1
    """

    auto_canceled_orders_with_staff_discount_sql = """
        select oi.idOrder, oi.idOrderItem, cr.orderitems_cancellation_reason_type_id, cr.cancelled_by, cr.date_cancelled
        from take2.orderitems_cancellation_reason cr
        join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem
        join take2.orders o on oi.idOrder = o.idOrder
        where cr.orderitems_cancellation_reason_type_id = 12
        and cr.cancelled_by = 'auto_cancel'
        and o.AdminNotes like '%Staff discount applied%'
        order by cr.date_cancelled desc
        limit 1
    """

    auto_canceled_order_with_charges_sql = """
        select oi.idOrder, o.Shipping, o.Discount
        from take2.orderitems_cancellation_reason cr
        join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem
        join take2.orders o on oi.idOrder = o.idOrder
        where cr.cancelled_by IN ('auto_cancel','auto_cancel_promotions')
        and orderitems_cancellation_reason_type_id = 12
        and o.Shipping > 1
        and o.Discount > 1
        and o.Auth = 'New'
        and oi.Status = 'Canceled'
        order by cr.date_cancelled desc
        limit 1
    """

    canceled_order_except_auto_canceled_sql = """
        select o.idOrder, cancelled_by
        from take2.orderitems_cancellation_reason cr
        join take2.orderitems o on cr.orderitem_id = o.idOrderItem
        where orderitems_cancellation_reason_type_id != 12
        order by cr.date_cancelled desc
        limit 1
    """

    # Order item status queries
    order_with_returned_canceled_order_item_sql = """
        select oi.idOrder, oi.status
        from orderitems oi
        join orders o on oi.idOrder = o.idOrder
        where oi.status = 'Return Canceled'
        and o.qty = 1
        order by 1 desc
        limit 1
    """
