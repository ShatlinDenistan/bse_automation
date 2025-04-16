*** Settings ***
Resource    ../../Config/defaultConfig.robot

*** Test Cases ***


Fin-Portal | Vouchers | Cancel A Voucher
    [Documentation]    Verify that a user can cancel a voucher on the vouchers page
    [Tags]    QABA-178
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Redeemed And Paid Status
    Select And Cancel A Voucher
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Activate A Voucher
    [Documentation]    Verify that a user can activate a canceled voucher
    [Tags]    QABA-176
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Canceled Redeem Status
    Select And Activate A Voucher
    Verify Voucher Status
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Update A Voucher To Not Paid
    [Documentation]    Verify that a user can Update a Voucher from Paid to Not Paid
    [Tags]    QABA-192
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Paid Status
    Select And Update To Not Paid
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Update A Voucher To Paid
    [Documentation]    Verify that a user can Update a Voucher from Not Paid to Paid
    [Tags]    QABA-192
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Not Paid Status
    Select And Update To Paid
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Custom Date Range
    [Documentation]    Verify that a user can filter using a custom date ranger on the voucher page
    [Tags]    QABSE-1384
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Date Range
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Voucher Category
    [Documentation]    Verify that a user can filter by a voucher category on the voucher page
    [Tags]    QABSE-1384
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Voucher Category
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Redeemed Status
    [Documentation]    Verify that a user can filter by Redeemed Status on the voucher page
    [Tags]    QABSE-1384
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Redeemed Status
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Combination Of Multiple Filter Options
    [Documentation]   Verify that a user can apply multiple filters at once on the voucher page
    [Tags]    QABSE-1384
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Multiple Filter Options
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Order ID
    [Documentation]   Verify that a user can filter by Order ID on the voucher page
    [Tags]    QABSE-1384
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter Using Order ID
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Voucher Code
    [Documentation]   Verify that a user can filter by voucher code on the voucher page
    [Tags]    QABSE-195
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Voucher Code
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Customer ID
    [Documentation]   Verify that a user can search for customer who purchased a voucher on the voucher page
    [Tags]    QABSE-193
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter Using Customer ID
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Filter By Used By Customer ID
    [Documentation]   Verify that a user can filter by customer ID on the voucher page
    [Tags]    QABSE-195
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Filter By Redeemed Status
    Filter By Used By Customer ID
    [Teardown]    Tear Down

Fin-Portal | Vouchers | Send Email
    [Documentation]   Verify that a user can send an email from the Vouchers page
    [Tags]    QABSE-175
    [Setup]   Open Web Browser
    Login Fin-Portal
    Navigate To Vouchers
    Select and Send Email
    Verify Email Was Sent Successfully
    [Teardown]    Tear Down