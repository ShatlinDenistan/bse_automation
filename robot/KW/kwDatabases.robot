*** Settings ***
Resource    ../Config/defaultConfig.robot

*** Variables ***
${paygate_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' and o.Qty = 1 order by o.OrderDate desc limit 1;
${payfast_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'PayFast' and o.PaymentMethod = 'PayFast' and o.Qty = 1 order by o.OrderDate desc limit 1;
${deposit_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Deposit' and o.AuthUser = 'ManualAuth' and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;
${ozow_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'iPay' and o.Qty = 1 order by o.OrderDate desc limit 1;
${masterpass_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Masterpass' order by o.OrderDate desc limit 1;
${cash_on_del_sql}    select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'COD' and o.Qty = 1 order by o.OrderDate desc limit 1;
${risky_orders_sql}    select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Risk = 1 and o.Auth = 'Auth' and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' order by o.OrderDate desc limit 1;
${discovery_miles_sql}    select o.idOrder, o.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Discovery' and o.PaymentMethod = 'Discovery Miles' and o.Qty = 1 order by o.OrderDate Desc limit 1;
${ebucks_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'eBucks' and o.PaymentMethod = 'eBucks' order by o.OrderDate desc limit 1;
${cc_ebucks_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' order by o.OrderDate desc limit 1;
${sbux_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'sBux' order by o.OrderDate desc limit 1;
${order_with_coupon_sql}    select o.idOrder, o.Discount, o.Total, o.Shipping from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status IN ('New Order','On Hold') and o.AuthUser = 'CreditCard' and o.PaymentMethod = 'Credit Card' and o.Discount > 1 and o.idCredit IS NULL order by o.OrderDate desc limit 1;
${payflex_sql}    select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Payflex' and o.PaymentMethod = 'Payflex' order by o.OrderDate limit 1;
${donation_amount_sql}    SELECT o.idOrder, o.Total, o.Shipping, i.Total, d.donation FROM take2.orders o INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder INNER JOIN take2.donations d ON i.idOrder = d.idOrder WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' ORDER BY o.OrderDate desc LIMIT 1;
${tal_credit_sql}    select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.PaymentMethod = 'Credit' order by o.OrderDate limit 1;
${mobicred_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.AuthUser = 'Mobicred' and o.PaymentMethod = 'Mobicred' order by o.OrderDate desc limit 1;
${blacklisted_sql}    select idCustomer from take2.BlackListedCustomers order by timestamp desc;
${credit_card_donation_order_sql}  select o.idOrder , i.Total from take2.orders o INNER JOIN take2.orderitems i ON o.idOrder = i.idOrder INNER JOIN take2.donations d ON i.idOrder = d.idOrder WHERE i.Status = 'New Order' AND o.Auth = 'Auth' AND o.PaymentMethod = 'Credit Card' AND o.Qty = 1 ORDER BY o.OrderDate desc LIMIT 1 
${new_order_ebucks_cc_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' and o.Qty = 1 and o.idCredit IS NULL order by o.OrderDate desc limit 1;
${new_order_mobicred_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'Mobicred' and o.idCredit IS NULL and o.Qty = 1 order by o.OrderDate desc limit 1;
${new_order_sbux_sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'New' and o.PaymentMethod = 'sBux' and o.idCredit IS NULL order by o.OrderDate desc limit 1;
${auto_canceled_orders_sql}    select o.idOrder,o.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
...  from take2.orderitems_cancellation_reason cr join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
...  where orderitems_cancellation_reason_type_id = 12 and cancelled_by = 'auto_cancel' order by cr.date_cancelled desc limit 1;
${auto_canceled_orders_with_staff_discount.sql}    select oi.idOrder,oi.idOrderItem,cr.orderitems_cancellation_reason_type_id,cr.cancelled_by,cr.date_cancelled 
...  from take2.orderitems_cancellation_reason cr join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem 
...  join take2.orders o on oi.idOrder = o.idOrder where cr.orderitems_cancellation_reason_type_id = 12 
...  and cr.cancelled_by = 'auto_cancel'and o.AdminNotes like '%Staff discount applied%'order by cr.date_cancelled desc limit 1;
${auto_canceled_order_with_charges.sql}    select oi.idOrder,o.Shipping,o.Discount from take2.orderitems_cancellation_reason cr 
...  join take2.orderitems oi on cr.orderitem_id = oi.idOrderItem join take2.orders o on oi.idOrder = o.idOrder where cr.cancelled_by IN ('auto_cancel','auto_cancel_promotions') 
...  and orderitems_cancellation_reason_type_id = 12 and o.Shipping > 1 and o.Discount > 1 and o.Auth = 'New' and oi.Status = 'Canceled' order by cr.date_cancelled desc limit 1;
${canceled_order_except_auto_canceled.sql}    select o.idOrder,cancelled_by from take2.orderitems_cancellation_reason cr join take2.orderitems o on cr.orderitem_id = o.idOrderItem 
...  where orderitems_cancellation_reason_type_id != 12 order by cr.date_cancelled desc limit 1;
${new_order_with_no_discount_amount.sql}    select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount = 0 
...  and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;
${new_order_with_no_discount__and_shipping_amount.sql}    select o.idOrder, o.Total from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount = 0 
...  and o.Shipping = 0 and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;
${order_with_returned_canceled_order_item.sql}    select oi.idOrder, oi.status from orderitems oi join orders o on oi.idOrder = o.idOrder where oi.status = 'Return Canceled' 
...  and o.qty = 1 order by 1 desc limit 1;
${new_order_with_discount_and_shipping_amounts.sql}    select o.idOrder, o.Total, o.Shipping, o.Discount from orders o join orderitems oi on o.idOrder=oi.idOrder where o.Auth = 'New' and o.Discount > 1 
...  and o.Shipping > 1 and oi.Status <> 'Canceled' order by o.OrderDate desc limit 1;
${non_risky_order.sql}    select o.idOrder from take2.orders o where o.Risk = 0 order by o.OrderDate desc limit 1;
${part_payment_order.sql}    select o.idOrder from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status <> 'Canceled' and o.PaymentMethod = 'Credit Card' and o.PaymentMethods = 'eBucks' order by o.OrderDate desc limit 1;
${order_with_more_order_items.sql}    select o.idOrder, i.Total from take2.orders o join take2.orderitems i on o.idOrder = i.idOrder where i.Status = 'New Order' and o.Auth = 'Auth' and o.Qty > 1 order by o.OrderDate desc limit 1;

*** Keywords ***
Get Orders From Database
    [Documentation]    This function gets orders from database using ApiLibrary.py
    [Arguments]    ${QUERY}
    ${json_content}    Get Orders From Take2
    ${order_ids}    Get Value From Json    ${json_content}    $[0].idOrder
    ${order_discount}    Get Value From Json    ${json_content}    $[0].Discount
    ${order_total}    Get Value From Json    ${json_content}    $[0].Total
    ${order_shipping}    Get Value From Json    ${json_content}    $[0].Shipping
    ${donation_amount}    Get Value From Json    ${json_content}    $[0].donation
    Log To Console    ${order_ids}
    Set Global Variable    ${order_ids}
    Set Global Variable    ${order_discount}
    Set Global Variable    ${order_shipping}
    Set Global Variable    ${order_total} 
    Set Global Variable    ${donation_amount}

Get Customers From Database
    [Documentation]    This function gets customers from database using ApiLibrary.py
    [Arguments]    ${QUERY}
    ${json_content}    Get Customers From Take2
    ${customer_ids}    Get Value From Json    ${json_content}    $[0].idCustomer
    Set Global Variable    ${customer_ids}

Create New TAL Orders
    [Documentation]    This function gets orders from database using ApiLibrary.py
    [Arguments]    ${CUSTOMER}    ${PAYMENTMENTHOD}
    ${orders_content}    Create New Order Tal
    ${order_ids}    Get Value From Json    ${orders_content}    $.order_id
    ${id_order_item1}    Get Value From Json    ${orders_content}    $.items[0].order_item_id
    ${id_order_item2}    Get Value From Json    ${orders_content}    $.items[1].order_item_id
    ${order_total}    Get Value From Json    ${orders_content}    $.total_amount
    Set Global Variable    ${order_ids}
    Set Global Variable    ${id_order_item1}
    Set Global Variable    ${id_order_item2}
    Set Global Variable    ${order_total}
    Log To Console    ${order_ids}

Create New TAL Orders Not Paid
    [Documentation]    This function creates orders that are not paid
    [Arguments]    ${CUSTOMER}    ${PAYMENTMENTHOD}
    ${orders_content}    Create New Order Tal Not Paid
    ${order_ids}    Get Value From Json    ${orders_content}    $.order_id
    ${order_total}    Get Value From Json    ${orders_content}    $.total_amount
    Set Global Variable    ${order_ids}
    Set Global Variable    ${order_total}

Create New TAL Orders Cancelled
    [Documentation]    This function creates orders that are not paid
    [Arguments]    ${CUSTOMER}    ${PAYMENTMENTHOD}
    ${orders_content}    Create New Order Tal Cancelled
    ${order_ids}    Get Value From Json    ${orders_content}    $.order_id
    ${order_total}    Get Value From Json    ${orders_content}    $.total_amount
    Set Global Variable    ${order_ids}
    Set Global Variable    ${order_total}
