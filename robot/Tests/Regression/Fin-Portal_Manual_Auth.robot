*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Auth | Mobicred
    [Tags]    qaba-495
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${new_order_mobicred_sql}
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Click Payments Ledger Accordion
    Click Authorize Now Button And Close Notification
    Expand The Customer Credit Accordion Under Customer Info
    Click The Credit Button And Add Credit Amount
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    EFT
    [Teardown]    Tear Down

Fin-Portal | Manual Auth | sBux | Order Not Canceled Or Return Canceled
    [Tags]    qaba-494
    [Setup]    Open Web Browser
    Create New TAL Orders Not Paid    ${13866233}    sBux
    Verify Title
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Click Payments Ledger Accordion
    Click Authorize Now Button And Close Notification
    Expand The Customer Credit Accordion Under Customer Info
    Click The Credit Button And Add Credit Amount
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    EFT
    [Teardown]    Tear Down
