*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Override | Credit Card
    [Tags]    qaba-482
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${paygate_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form    ${lstCreditCard}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Instant EFT | PayFast
    [Tags]    qaba-488
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${payfast_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form    ${lstPayfast}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    PayFast
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Masterpass
    [Tags]    qaba-484
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${masterpass_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    EFT
    [Teardown]    Tear Down

Fin-Portal | Manual Override | EFT | Original Payment Method Is Credit Card
    [Tags]    qaba-484
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${paygate_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    EFT
    [Teardown]    Tear Down

Fin-Portal | Manual Override | EFT | Discovery Miles
    [Tags]    qaba-486
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${discovery_miles_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form    ${lstDiscoveryMiles}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Discovery Miles
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Refund Amount Exceeds Settlement Amount
    [Tags]    qaba-483
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${paygate_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form With Amount Exceeding Total    ${lstCreditCard}
    Confirm Manual Override And View Logs
    Verify That An Admin Note For The Failed Manual Override Was Created
    [Teardown]    Tear Down
