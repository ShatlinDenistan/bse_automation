*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Override | Blacklisted Customer
    [Tags]    qaba-488
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${blacklisted_sql}
    Create New TAL Orders    ${customer_ids[0]}    Credit Card
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

Fin-Portal | Manual Override | eBucks, Credit Card And Tal Credit Part Payment
    [Tags]    qaba-500
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${cc_ebucks_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Get Refund Amount For Payment Methods
    Click The Manual Override Button And Complete The Override Form for Credit Card and eBucks    ${lstCreditCard}    ${lsteBucks}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Paygate
    [Teardown]    Tear Down

Fin-Portal | Manual Override | eBucks And Credit Card Part Payment
    [Tags]    qaba-489
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${cc_ebucks_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Get Refund Amount For Payment Methods
    Click The Manual Override Button And Complete The Override Form for Credit Card and eBucks    ${lstCreditCard}    ${lsteBucks}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Paygate
    Verify That There Are 2 Admin Notes For Both Manual Overrides Was Created
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Deposit
    [Tags]    qaba-502
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${deposit_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Deposit
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Instant EFT | Ozow
    [Tags]    qaba-487
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${ozow_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    iPay
    [Teardown]    Tear Down

Fin-Portal | Manual Override | eBucks
    [Tags]    qaba-485
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${ebucks_sql}
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form    ${lsteBucks}
    Confirm Manual Override And View Logs
    Verify Manual Override Details    eBucks
    [Teardown]    Tear Down

Fin-Portal | Manual Override | sBux/NSFAS Wallet
    [Tags]    qaba-501
    [Setup]    Open Web Browser
    Verify Title
    Create New TAL Orders    ${13866233}    sBux
    Cancel Paid Order
    Login Fin-Portal
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Accordion Under Customer Info
    On Order View Page Expand The Order Items Accordion And Click Refund
    Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
    Capture EFT Banking Details
    Confirm Manual Override And View Logs
    Verify Manual Override Details    Deposit
    [Teardown]    Tear Down

Fin-Portal | Manual Override | Refund Additional Donation Charge
  [Tags]   qaba-504
  [Setup]   Open Web Browser
  Verify Title
  Get Orders From Database    ${credit_card_donation_order_sql}
  Cancel Paid Order
  Login Fin-Portal
  Search For Order    ${order_ids[0]}
  Expand The Customer Credit Section And Click The Credit Button For Order
  Enter Donation And Enter A Comment
  Select The Add Credit Button
  Select OK On The Dialog
  On Order View Page Expand The Order Items Accordion And Click Refund 
  Click The Manual Override Button And Complete The Override Form EFT    ${lstEFT}
  Capture EFT Banking Details
  Confirm Manual Override And View Logs
  Verify Manual Override Details    EFT
  [Teardown]    Tear Down

 Fin-Portal | Manual Override | EFT | Original Payment Method Is Credit Card And eBucks
    [Tags]    qaba-491
    [Setup]    Open Web Browser
    Verify Title
    Get Orders From Database    ${cc_ebucks_sql}
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
