*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Processing A Refund | Credit Card | PayU
    [Tags]    qaba-458
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${paygate_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    PayU
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Cannot Process Refund When Customer Is Blacklisted
    [Tags]    qaba-457
    [Setup]    Open Web Browser
    Verify Title
    Get Customers From Database    ${blacklisted_sql}
    Create New TAL Orders    ${customer_ids[0]}    Credit Card
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Order Is NOT Eligible For Manual Refund
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Masterpass
    [Tags]    qaba-459
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${masterpass_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Enter Banking Details
    Click The EFT Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | sBux/NSFAS Wallet
    [Tags]    qaba-464
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${sbux_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    sBux
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Refund Excludes Coupon Amount
    [Tags]    qaba-464
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${order_with_coupon_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Refund Amount Excludes Coupon Amount
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Credit Card and eBucks Part Payment
    [Tags]    qaba-467
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${cc_ebucks_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Part-Payment Details    eBucks    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Instant EFT Ozow
    [Tags]    qaba-460
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${ozow_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Enter Banking Details
    Click The EFT Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    iPay
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Donation Amount Not Refunded
    [Tags]    qaba-454
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${donation_amount_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Refund Amount Excludes Donation Amount
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Mobicred
    [Tags]    qaba-463
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${mobicred_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Refund Not Available
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    Click The View Refund Log Button And Verify Details    Mobicred
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Staggered Mobicred Refunds
    [Tags]    qaba-480
    [Setup]    Open Web Browser
    Verify Title
    Create New TAL Orders    ${2420369}    Mobicred
    Cancel Order Item    ${id_order_item1[0]}
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Refund Not Available
    Cancel Order Item    ${id_order_item2[0]}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    Click The View Refund Log Button And Verify Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Cannot Process Refund When Order Is Marked As Risky
    [Tags]    qaba-466
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${risky_orders_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Order Is NOT Eligible For Manual Refund
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Deposit
    [Tags]    qaba-481
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${deposit_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Order Is NOT Eligible For Manual Refund
    [Teardown]    Tear Down
