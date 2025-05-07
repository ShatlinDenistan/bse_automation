*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Fin Portal | Deposit Match | Batch | Show Items and Pagination
    [Documentation]    View all the records in a large deposit csv file via Show Items and Pagination
    [Tags]    QABA-514
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Upload Valid Deposit Match File    ${Deposit_Match_File_30}
    Click The Refresh Button
    Click Show Items Dropdown And Select 30 Items
    Navigate To Second Page
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Authorise Order
    [Documentation]    Manually Auth a new order from the Batch screen
    [Tags]    QABA-511
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With New Status Orders
    Click The Refresh Button
    Select New Order And Authorise
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Cancel Order
    [Documentation]    Cancel a new order from the Batch screen
    [Tags]    QABA-509
    [Setup]    Open Web Browser
    Login Fin-Portal   
    Navigate To Deposit Match
    Select Batch With New Status Orders
    Click The Refresh Button
    Select Authorised Order And Cancel
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Manually Match and Credit Order
    [Documentation]    Manually Match a deposit/payment to a canceled order and credit the order in the Batch screen.
    [Tags]    QABA-513
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With Authorised Orders
    Select Authorised Order And Cancel
    Click The Match Button And Type In The Order ID
    Click The Match Button And Close Modal
    [Teardown]    Tear Down

Fin-Portal | Fin Portal | Deposit Match | Batch | Manually Match and Auth Order
    [Documentation]    Manually Match a deposit/payment to a new order and Authorise it in the Batch screen.
    [Tags]    QABA-512
    [Setup]    Open Web Browser
    Login Fin-Portal
    Navigate To Deposit Match
    Select Batch With Authorised Orders
    Click The Match Button And Type In The Order ID
    Click The Match Button And Close Modal
    Select Authorised Order And Authorise
    [Teardown]    Tear Down
