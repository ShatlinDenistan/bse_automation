*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Deposit Match | Incorrect Upload File Format | Do Not Process
    [Documentation]    Verify that the file does not meeting the Deposit Match file format requirements
    [Tags]    QABA-522
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Upload Invalid Deposit Match File
    Verify CSV Error Occured
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match Download Batch File
    [Documentation]    Verify that the file does not meeting the Deposit Match file format requirements
    [Tags]    QABA-522
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Upload Valid Deposit Match File    ${Deposit_Match_File}
    Click The Refresh Button
    Go To Deposit Match Page
    Download Batch File
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | All Batches | Filters
    [Documentation]    Only view filtered data on the All Batched screen
    [Tags]    QABA-523
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Click The Select Payment Method Dropdown And Select PayFast And Apply Filter
    Verify That Batches Are Filtered By Payment Method
    Click The Clear Filter Button
    Click The Select Date Range Field And Select Date From The Previous Week
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch Search
    [Documentation]    Search for orders based on specific search criteria on the Batch screen
    [Tags]    QABA-516
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Click On Existing Batch
    Click The Criteria Dropdown List And Select OrderID
    Enter Order Id On Searchbox And Apply Filer
    Click The Criteria Dropdown List And Select Statement Amount
    Enter Statement Amount On Searchbox And Apply Filer
    Click The Criteria Dropdown List And Select Customer Id
    Enter Customer ID On Searchbox And Apply Filer
    Click The Criteria Dropdown List And Select Customer Name
    Enter Customer Name On Searchbox And Apply Filer
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Filtering
    [Documentation]    Only view filtered data on the Batch screen
    [Tags]    QABA-515
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With Authorised Orders
    Click Match Status Drop-down And Select Auto Match
    Click Match Status Drop-down And Select Amount Differ
    Click Match Status Drop-down And Select Order Not Found
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Unclaimed Payments | Filters
    [Documentation]    Search for orders based on specific search criteria on the Batch screen
    [Tags]    QABA-524
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Click The Unclaimed Payment Tab
    Click Criteria Drop-down List And Select Customer Name
    Enter Customer Name And Apply Filter
    Click Criteria Drop-down List And Select Order Id
    Enter Order Id And Apply Filter
    Click Criteria Drop-down List And Select Statement Amount
    Enter Statement Amount And Apply Filter
    Click Criteria Drop-down List And Select Batch Id
    Enter Batch Id And Apply Filter
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Unclaimed Payment
    [Documentation]    Move deposits to the Unclaimed Payments page from the Batch screen for further investigation.
    [Tags]    QABA-510
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With Authorised Orders
    Click Checkbox Next To First Order In The Batch
    Click The Unclaimed Payment Button
    Navigate To Unclaimed Payment Page
    Click Criteria Drop-down List And Select Order Id
    Enter Unclaimed Payment Order Id And Apply Filter
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Remove Order
    [Documentation]    As a user, I want to remove an order from the batch.
    [Tags]    QABA-507
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Upload Valid Deposit Match File    ${Deposit_Match_File}
    Click The Refresh Button
    Click Match Status Drop-down And Select Order Not Found
    Click Checkbox Next To First Order In The Batch
    Click The Remove Order Button
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Upload File | Staggered Uploads
    [Documentation]    Upload multiple files one after the other and ensure that they are processed without any issues.
    [Tags]    QABA-529
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Upload Valid Deposit Match File    ${Deposit_Match_File}
    Click The Refresh Button
    Navigate To All Batches
    Upload Valid Deposit Match File    ${Deposit_Match_File}
    Click The Refresh Button
    Navigate To All Batches
    
Fin-Portal | Fin Portal | Deposit Match | Batch | Send Email
    [Documentation]    Send a “Deposit Update” email to multiple customers from the Batch screen.
    [Tags]    QABA-507
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With Authorised Orders
    Click Checkbox Next To First Order In The Batch
    Click Send Email Button And Send Email
    [Teardown]    Tear Down
