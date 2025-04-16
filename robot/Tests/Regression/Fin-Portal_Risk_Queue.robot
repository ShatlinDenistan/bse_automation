*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Risk Queue | Show Items and Pagination
    [Documentation]    View all the records in the Risk Queue page via Show Items and Pagination
    [Tags]    QABA-639
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Click Show Items Dropdown And Select 10 Items
    Navigate To Next Page
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Clear Risk
    [Documentation]    Verify that a user can clear a risk label from the Risk Queue page
    [Tags]    QABA-631
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Select an order to clear risk
    Handle Alerts    
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Filter By Payment Method 
    [Documentation]    Verify that a user can filter by Payment Method on the Risk Queue page
    [Tags]    QABA-636
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Payment Method
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Filter By Shipping Method
    [Documentation]    Verify that a user can filter by Shipping Method on the Risk Queue page
    [Tags]    QABA-636
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Shipping Method
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Filter By Minimum/Maximum Order Total
    [Documentation]    Verify that a user can filter by Minumum and Maximum Order Total on the Risk Queue page
    [Tags]    QABA-637
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Minimum Amount 
    Filter Using Maximum Amount
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Filter By Multiple Filters
    [Documentation]    Verify that a user can apply multiple filters at once on the Risk Queue page
    [Tags]    QABA-638
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Multiple Filters
     [Teardown]    Tear Down

Fin-Portal | Risk Queue | Filter By Daily Deals
    [Documentation]    Verify that a user can filter for daily deals orders on the Risk Queue page
    [Tags]    QABA-625
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Daily Deal
    [Teardown]    Tear Down


Fin-Portal | Risk Queue | Filter By Date Range
    [Documentation]    Verify that a user can filter for a specific date range on the Risk Queue page
    [Tags]    QABA-635
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Filter Using Date Range
    [Teardown]    Tear Down

Fin-Portal | Risk Queue | Send Email
    [Documentation]    Verify that a user can send a random email from the Risk Queue Page
    [Tags]    QABA-633
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Select First Order on Grid
    Select Email Template and Send Email
    Verify Email Sent Success Message

Fin-Portal | Risk Queue | Cancel Order
    [Documentation]    Verify that a user can cancel an order from the Risk Queue Page
    [Tags]    QABA-632
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Risk Queue
    Select First Order on Grid
    Cancel Single Order
    Verify Canceled Order Status