Tests
*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwEditOrder.robot

Test Setup    Open Web Browser
Test Teardown    Tear Down

Force Tags    EditOrder    Sanity


*** Test Cases ***
Fin-Portal | Edit Order | Cannot Update Shipping and Discount on Auth'd Orders
    [Documentation]    Verify that a user cannot update Shipping and Discount on Auth'd orders
    [Tags]    QABA-531
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${paygate_sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Verify That Both Shipping and Discount Disabled Fields Are On Edit Order Screen

Fin-Portal | Edit Order | Update Discount Amount
    [Documentation]    Verify that user can update the discount amount
    [Tags]    QABA-534
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Navigate to Edit Order Screen
    Update Discount Amount
    Verify that the Discount Amount is Updated on Order Financials  

    
    
     