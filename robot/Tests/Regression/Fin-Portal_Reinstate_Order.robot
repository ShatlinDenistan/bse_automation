Tests
*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwReinstateOrder.robot

Test Setup    Open Web Browser
Test Teardown    Tear Down

Force Tags    ReinstateOrder    Regression


*** Test Cases ***
Fin-Portal | Reinstate Order | Fully Auto-Canceled Order
    [Documentation]    Verify that a user can reinstate a fully auto canceled order
    [Tags]    QABA-546
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${auto_canceled_orders_sql}
    Search For Order    ${order_ids[0]}
    Reinstate Order 
    Verify That An Admin Note For Order Reinstatement Was Created


Fin-Portal | Reinstate Order | Auto-Canceled Order with Staff Discount
    [Documentation]    Verify that a user can reinstate an auto cancelled order that has Staff discount
    [Tags]    QABA-549
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${auto_canceled_orders_with_staff_discount.sql}
    Search For Order    ${order_ids[0]}
    Reinstate Order 
    Verify That An Admin Note For Order Reinstatement Was Created
    Get Order Financials Amounts
    Verify That Staff Discount on Reinstate Matches Staff Discount on Order Financials

Fin-Portal | Reinstate Order | Auto-Canceled Order with Shipping and Coupon Discount
    [Documentation]    Verify that a user can reinstate an auto cancelled order that has Shipping and Coupon Discount 
    [Tags]    QABA-547
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${auto_canceled_order_with_charges.sql}
    Search For Order    ${order_ids[0]}
    Reinstate Order 
    Verify That Reinstate Order Amounts Are Correct
    Verify That An Admin Note For Order Reinstatement Was Created

Fin-Portal | Reinstate Order | Reinstate Button Not Available for Orders Not Auto Canceled
    [Documentation]    Verify that when an order is NOT auto canceled the reinstate order button is not available
    [Tags]    QABA-548
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${canceled_order_except_auto_canceled.sql}
    Search For Order    ${order_ids[0]}
    Verify That Reinstate Button Is Not Available