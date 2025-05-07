Tests
*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwEditOrder.robot

Test Setup    Open Web Browser
Test Teardown    Tear Down

Force Tags    EditOrder    Regression


*** Test Cases ***
Fin-Portal | Edit Order | Update Payment Method
    [Documentation]    Verify that a user can update payment method on an Authorized order
    [Tags]    QABA-546
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${paygate_sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Update Payment Method
    Verify That Payment Method Difference Warning Banner Displays
    Verify That An Admin Note For Payment Method Update


Fin-Portal | Edit Order | Add Discount Amount Greater Than Order Total Amount
    [Documentation]    Verify that a user cannot apply discount amount more than order total amount
    [Tags]    QABA-546
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount_amount.sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Calculate Discount Amount Input Value
    Verify That Invalid Discount Amount Message

Fin-Portal | Edit Order | Add Discount and Shipping Amounts
    [Documentation]    Verify that applying discount and shipping fee to a new order updates the Order's Auth Amount
    [Tags]    QABA-532    QABA-536
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount__and_shipping_amount.sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Add Shipping Fee And Discount Amounts
    Verify that Discount and Shipping Amounts Are Added To Order Financials 
    Verify Discount and Shipping Fee Update Admin Notes
    Verify Discount and Shipping Fee Update Audit Logs    

Fin-Portal | Edit Order | Order Item Update to Shipped
    [Documentation]    Verify that a user can update an order items stauts from Returned Canceled to Shipped
    [Tags]    QABA-544
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${order_with_returned_canceled_order_item.sql}
    Search For Order    ${order_ids[0]}
    Navigate to Update To Shipped Screen
    Update Order Item Status From Returned Canceled To Shipped
    Verify Update From Return Canceled To Shipped Admin Note and Audit Log Entry


Fin-Portal | Edit Order | Update Shipping Amount
    [Documentation]    Verify that updating the shipping amount and the order total
    [Tags]    QABA-534
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Update Shipping Amount
    Verify that the Shipping Amount is Updated on Order Financials  

Fin-Portal | Edit Order | Payment Method Options
    [Documentation]    Verify that the Payment Method drop-down list has all the available payment methods
    [Tags]    QABA-543
    Verify Title
    Login Fin-Portal
    Search For Order    98278540
    Navigate to Edit Order Screen 
    Verify That Payment Method Options Are Displayed