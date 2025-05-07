*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwOrderList.robot

Test Setup    Open Web Browser
Test Teardown    Tear Down

Force Tags    OrderList    Regression

*** Test Cases ***
Fin-Portal | Order List | Authorise order
    [Documentation]    Verify that a user can Authorise an order from the order list page
    [Tags]    QABA-622
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Clear Today Filter
    Authorise Single Order

Fin-Portal | Order List | Authorise Multiple Orders
    [Documentation]    Verify that a user can Authorise multiple orders from the order list page
    [Tags]    QABA-622
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Clear Today Filter
    Authorise Multiple Orders

Fin-Portal | Order List | Cancel an order
    [Documentation]    Verify that a user can cancel an order from the order list page
    [Tags]    QABA-623
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Clear Today Filter
    Cancel Single Order

Fin-Portal | Order List | Cancel Multiple orders
    [Documentation]    Verify that a user can cancel multiple orders from the order list page
    [Tags]    QABA-623
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Clear Today Filter
    Cancel Multiple Orders

Fin-Portal | Order List | Cancel Already Cancelled order
    [Documentation]    Verify that a user cant cancel an already cancelled order from the order list page
    [Tags]    QABA-623
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Clear Today Filter
    Cancel Already Cancelled order

Fin-Portal | Order List | Filter By Daily Deals
    [Documentation]    Verify that a user can filter for daily deals orders on the order list page
    [Tags]    QABA-625
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Daily Deal

Fin-Portal | Order List | Filter By Auth Status
    [Documentation]    Verify that a user can filter by Auth Status on the order list page
    [Tags]    QABA-626
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Auth Status

Fin-Portal | Order List | Filter By Payment Method
    [Documentation]    Verify that a user can filter by Payment Method on the order list page
    [Tags]    QABA-626
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Payment Method

Fin-Portal | Order List | Filter By Shipping Method
    [Documentation]    Verify that a user can filter by Shipping Method on the order list page
    [Tags]    QABA-626
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Shipping Method

Fin-Portal | Order List | Filter By Minimum/Maximum Order Total
    [Documentation]    Verify that a user can filter by Minumum and Maximum Order Total on the order list page
    [Tags]    QABA-626
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Minimum Order Total
    Filter By Maximum Order Total

Fin-Portal | Order List | Filter By Multiple Filters
    [Documentation]    Verify that a user can apply multiple filters at once on the order list page
    [Tags]    QABA-626
    Verify Title
    Login Fin-Portal
    Navigate to Order List Page
    Filter By Multiple Filters