*** Settings ***
Resource    ../../Config/defaultConfig.robot

Test Setup    Open Web Browser
Test Teardown    Tear Down

Force Tags    EFTRefunds    Regression

*** Test Cases ***
Fin-Portal | EFT Refunds | Order ID Redirects
    [Documentation]    Verify that a user can click on an OrderID and be redirected to the appropriate page
    [Tags]    QABA-564
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Click On An Order ID And Verify New Tab Opened

Fin-Portal | EFT Refunds | Customer ID Redirects
    [Documentation]    Verify that a user can click on a customer Name and be redirected to the appropriate page
    [Tags]    QABA-564
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Click On A Customer Name And Verify New Tab Opened

Fin-Portal | EFT Refunds | Filter and Search | Filter By Status And Type
    [Documentation]    Verify that a user can filter by status and type on the EFT Refunds page
    [Tags]    QABA-554
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Apply Status Filter
    Apply Type Filter

Fin-Portal | EFT Refunds | Filter and Search | Filter By Customer ID Order ID And Bank Account Number
    [Documentation]    Verify that a user can filter by Customer ID, Order ID,  and Bank Account Number
    [Tags]    QABA-554
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Filter By Customer ID
    Filter By Order ID
    Filter By Bank Account Number

Fin-Portal | EFT Refunds | Filter and Search | Filter By Zendesk Ticket Number
    [Documentation]    Verify that a user can filter by Zendesk Ticket Number
    [Tags]    QABA-554
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Filter By Zendesk Ticket Number

Fin-Portal | EFT Refunds | Filter and Search | Date Range Filter Show Items and Pagination
    [Documentation]    Verify that a user can filter by date range and then show items per page and navigate between EFT Refunds pages
    [Tags]    QABA-554
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Apply Date Range Filter And Show Items Filter And Pagination

Fin-Portal | EFT Refunds | Export Requests | Single Request
    [Documentation]    Verify that a user can successfully export a single EFT Refund Request
    [Tags]    QABA-555
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Export One Request On Pending Status
    Verify Exported Row

Fin-Portal | EFT Refunds | Export Requests | Multiple Requests
    [Documentation]    Verify that a user can successfully export multiple EFT Refund Requests at once
    [Tags]    QABA-555
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Export Three Requests On Pending Status

Fin-Portal | EFT Refunds | Export Requests | Incorrect Status
    [Documentation]    Verify that a user cannot successfully export an EFT Refund Requests that is already exported
    [Tags]    QABA-555
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Export Request On Exported Status

Fin-Portal | EFT Refunds | Manual EFT Refund Request
    [Documentation]    Verify that a user can perform a manual eft and that the modal has all the neccesary fields
    [Tags]    QABA-562
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Click The Manual EFT Button And Verify The Fields
    Populate Manual EFT Refund Request Mandatory Fields
    Verify Credit Deduction Popup
    Verify Manual EFT Success

Fin-Portal | EFT Refunds | Decline Requests
    [Documentation]    Verify that a user can successfully decline EFT Refund Requests on Pending Status
    [Tags]    QABA-557
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Decline Requests On Pending Status

Fin-Portal | EFT Refunds | Decline Requests Already Cancelled/Declined
    [Documentation]    Verify that a user cannot successfully decline an EFT Refund Requests that is exported or declined
    [Tags]    QABA-557
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Decline Requests On Exported or Declined Status

Fin-Portal | EFT Refunds | Export Requests | Verify EFT Refund Exported csv file
    [Documentation]    Verify that the Bank csv files that has exported EFT Refund requests, have the correct format
    [Tags]    QABA-556
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Export Request And Download Nedbank File
    Export Request And Download Absa File

Fin-Portal | EFT Refunds | Send Email
    [Documentation]    Verify that a user can send “scripted” emails to multiple customers from the EFT Refunds page
    [Tags]    QABA-558
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Select Multiple EFT Refund Requests
    Select Random Template And Send Email
    Verify Email Success Message
    Verify Checkboxes Are Unchecked

Fin-Portal | EFT Refunds | Send Email to Manual EFT Request
    [Documentation]    Verify that a user cannot send “scripted” emails to Manual EFT Refund Requests
    [Tags]    QABA-558
    Login Fin-Portal
    Navigate To EFT Refunds Page
    Select A Manual EFT Refund Request
    Select Random Template And Send Email
    Verify Email Error Message