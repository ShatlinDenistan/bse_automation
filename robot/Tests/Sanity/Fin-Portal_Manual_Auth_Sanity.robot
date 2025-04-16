*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Auth | eBucks And Credit Card
    [Tags]    qaba-499
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${new_order_ebucks_cc_sql}
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Click Payments Ledger Accordion
    Get Refund Amount For eBucks
    Click Authorize Now Button And Close Notification
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Auth Override Button And Complete The Override Form    ${lsteBucks}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    eBucks
    [Teardown]    Tear Down

Fin-Portal | Manual Auth | Credit Card And eBucks Part Pay | UnAuthd Order
    [Tags]    qaba-496
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${new_order_ebucks_cc_sql}
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Click Payments Ledger Accordion
    Click Authorize Now Button And Close Notification
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    EFT
    [Teardown]    Tear Down
