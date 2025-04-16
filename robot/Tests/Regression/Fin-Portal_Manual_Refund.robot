*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Refunds | Processing A Refund | Credit Card | PayGate
    [Tags]    qaba-478
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
    Click The View Refund Log Button And Verify Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Instant EFT PayFast
    [Tags]    qaba-477
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${payfast_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    PayFast
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Cash On Delivery
    [Tags]    qaba-466
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${cash_on_del_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Order Is NOT Eligible For Manual Refund
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Discovery Miles
    [Tags]    qaba-462
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${discovery_miles_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    Discovery Miles
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | eBucks
    [Tags]    qaba-461
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${ebucks_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Search For Order    ${order_ids[0]}
    Click The View Refund Log Button And Verify Details    eBucks
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Staggered Credit Card Refunds
    [Tags]    qaba-456
    [Setup]    Open Web Browser
    Verify Title
    Create New TAL Orders    ${2420369}    Credit Card
    Cancel Order Item    ${id_order_item1[0]}
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Refund Button And Submit Refund Request
    Cancel Order Item    ${id_order_item2[0]}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    Click The View Refund Log Button And Verify Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Payflex
    [Tags]    qaba-455
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${payflex_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Refund Not Available
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    Click The View Refund Log Button And Verify Details    Payflex
    [Teardown]    Tear Down

Fin-Portal | Manual Refunds | Processing A Refund | Takealot Credit
    [Tags]    qaba-465
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${tal_credit_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Verify That Order Is NOT Eligible For Manual Refund
    [Teardown]    Tear Down
