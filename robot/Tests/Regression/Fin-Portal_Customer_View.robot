*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwCustomerView.robot

*** Test Cases ***

Fin-Portal | Verify Customer Details
    [Documentation]    Verify that the customer details are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Customer Details
    [Teardown]    Tear Down

Fin-Portal | Verify Notes Section
    [Documentation]    Verify that the customer notes are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Notes Section with Edit Option
    [Teardown]    Tear Down

Fin-Portal | Verify Fin-Note Section
    [Documentation]    Verify that the Fin Notes are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Fin Notes Section with Edit Option
    [Teardown]    Tear Down

Fin-Portal | Verify Customer Credit
    [Documentation]    Verify that the Customer Credit Accordion is displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Customer Credit
    [Teardown]    Tear Down

Fin-Portal | Verify Customer Address
    [Documentation]    Verify that the Customer Address is displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Customer Address
    [Teardown]    Tear Down

Fin-Portal | Verify Email Logs
    [Documentation]    Verify that the Email Logs are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Email Logs
    [Teardown]    Tear Down

Fin-Portal | Verify Returns History
    [Documentation]    Verify that the Returns History Accordion is displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Customer Returns History
    [Teardown]    Tear Down

Fin-Portal | Verify Zendesk Tickets
    [Documentation]    Verify that the Zendesk Tickets are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Zendesk Tickets
    [Teardown]    Tear Down

Fin-Portal | Verify Registered and Modified Dates
    [Documentation]    Verify that the Registered and Last Modified Dates are displayed on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Registered And Last Modified Dates
    [Teardown]    Tear Down

Fin-Portal | Blacklist a Customer
    [Documentation]    Verify that a user can Blacklist a TAL customer on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    34345
    Blacklist A Customer
    [Teardown]    Tear Down

Fin-Portal | Add Credit 
    [Documentation]    Verify that a user can add credit to a customer on the customer view page
    [Tags]    QABSE-260
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    34345
    Add Credit
    [Teardown]    Tear Down

Fin-Portal | Edit Customer 
    [Documentation]    Verify that a user can edit customer information on the customer view page
    [Tags]    QABSE-211
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    34345
    Edit Customer
    [Teardown]    Tear Down

Fin-Portal | Email Customer
    [Documentation]    Verify that a user can send a generic email on the customer view page
    [Tags]    QABSE-251    QABSE-223
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    112
    Send Generic Email
    View Email Logs For Latest Email Sent
    [Teardown]    Tear Down

Fin-Portal | Add Note
    [Documentation]    Verify that a user can add a note on the customer view page
    [Tags]    QABSE-250
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    555
    Add Admin Note
    [Teardown]    Tear Down

Fin-Portal | View Audit Logs
    [Documentation]    Verify that a user can view the audit logs on the customer view page
    [Tags]    QABSE-941
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    555
    View Audit Logs
    [Teardown]    Tear Down

Fin-Portal | View Sales History 
    [Documentation]    Verify that a user can view the sales history on the customer view page
    [Tags]    QABSE-222
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1
    Verify Order Link
    Verify Product Title
    [Teardown]    Tear Down

Fin-Portal | View Refund History 
    [Documentation]    Verify that a user can view the refunds history on the customer view page
    [Tags]    QABSE-86
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    14046903
    Verify Refund History
    Click Paging Button
    Click Items Per Page 
    [Teardown]    Tear Down

Fin-Portal | View SSR History
    [Documentation]    Verify that a user can view self service refund history on the customer view page
    [Tags]    QABA-85
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    1322249
    Verify SSR History
    [Teardown]    Tear Down

Fin-Portal | Upload And Remove ID Document
    [Documentation]    Verify that a user can Upload & Remove ID document on the customer view page
    [Tags]    QABA-247
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${paygate_sql} 
    Search For Order    ${order_ids[0]}
    Upload Valid ID Doc    ${CustomerID_Doc}
    Remove ID Doc
    [Teardown]    Tear Down