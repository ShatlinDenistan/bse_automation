*** Settings ***
Resource    ../../Config/defaultConfig.robot


*** Test Cases ***
Fin-Portal | Manual Credit Reason | Add Credit Breach Credit To Customer
    [Documentation]    Verify that a user can successfully allocate Credit breach credit to a customer
    [Tags]    QABSE-1339
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    100
    Expand The Customer Credit Section And Click The Credit Button
    Select A Credit Reason    ${reasonCreditBreach} 
    Enter Jira Number for Credit Breach Reason
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Credit Breach Min and Max Amount Rules
    [Documentation]    Verify Credit breach credit reason min and max amount rules
    [Tags]    QABSE-1339
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    100
    Expand The Customer Credit Section And Click The Credit Button
    Select A Credit Reason    ${reasonCreditBreach} 
    Enter Jira Number for Credit Breach Reason
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    10000001
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add Goowdill Credit To Order
    [Documentation]    Verify that a user can successfully add Goodwill credit to an order
    [Tags]    QABSE-1354
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonGoodwill}
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Goodwill Min and Max Amount Rules
    [Documentation]    Verify Goodwill credit reason min and max amount rules
    [Tags]    QABSE-1354
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonGoodwill}
    Enter Invalid Min Amount    -1
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    800
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down


Fin-Portal | Manual Credit Reason | Add Late Delivery Fee Credit To Order
    [Documentation]    Verify that a user can successfully add Late Delivery Fee credit to an order
    [Tags]    QABSE-1344
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonLateDeliveryFee}
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Late Delivery Fee Min and Max Amount Rules
    [Documentation]    Verify Late Delivery Fee credit reason min and max amount rules
    [Tags]    QABSE-1344
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonLateDeliveryFee}
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    300
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add Subscription late delivery fee Credit To Order
    [Documentation]    Verify that a user can successfully add Subscription late delivery fee credit to an order
    [Tags]    QABSE-1405
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonSubLateDelivery}
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Subscription late delivery fee Min and Max Amount Rules
    [Documentation]    Verify Goodwill credit reason min and max amount rules
    [Tags]    QABSE-1354
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonSubLateDelivery}
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    51
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add B2B Bulk Orders Credit To Customer
    [Documentation]    Verify that a user can successfully allocate B2B bulk orders credit to a customer
    [Tags]    QABSE-1335
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    100
    Expand The Customer Credit Section And Click The Credit Button
    Select A Credit Reason    ${reasonB2bBulkOrder} 
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate B2B Bulk Orders Min and Max Amount Rules
    [Documentation]    Verify B2B bulk orders credit reason min and max amount rules
    [Tags]    QABSE-1335
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Customer    100
    Expand The Customer Credit Section And Click The Credit Button
    Select A Credit Reason    ${reasonB2bBulkOrder} 
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    10000001
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add Failed EFT refunds Credit To Order
    [Documentation]    Verify that a user can successfully add Failed EFT refunds credit to an order
    [Tags]    QABSE-1404
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonFailedEFTRefunds}
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify That Order Credit Is Applied
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Failed EFT refunds Min and Max Amount Rules
    [Documentation]    Verify Goodwill credit reason min and max amount rules
    [Tags]    QABSE-1404
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonFailedEFTRefunds}
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    2000000
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add System Error Credit To Order Item
    [Documentation]    Verify that a user can successfully add Sytem Error credit to an order item
    [Tags]    QABSE-1353
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand Order Items Section And Click The Credit Item Option
    Select A Credit Reason    ${reasonSystemError}
    Enter RFN for System Error Reason
    Enter a Negative Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate System Error Min and Max Amount Rules
    [Documentation]    Verify System Error credit reason min and max amount rules
    [Tags]    QABSE-1353
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    74269681
    Expand Order Items Section And Click The Credit Item Option
    Select A Credit Reason    ${reasonSystemError}
    Enter RFN for System Error Reason
    Enter Invalid Min Amount    -2000000
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    1
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add Duplicate Payment Credit To Order
    [Documentation]    Verify that a user can successfully add Duplicate payment credit to an order
    [Tags]    QABSE-1349
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonDuplicatePayment}
    Enter Calculated Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Duplicate Payment Min and Max Amount Rules
    [Documentation]    Verify Duplicate payment credit reason min and max amount rules
    [Tags]    QABSE-1349
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonDuplicatePayment}
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    5000000
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add COD retrun Credit To Order
    [Documentation]    Verify that a user can successfully add COD return credit to an order
    [Tags]    QABSE-1403
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${order_with_returned_canceled_order_item.sql}
    Search For Order    ${order_ids[0]}
    Get Return Cancelled Amount From Order Financials
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonCODReturn}
    Enter Return Canceled Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate COD Return Min and Max Amount Rules
    [Documentation]    Verify COD return credit reason min and max amount rules
    [Tags]    QABSE-1403
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${order_with_returned_canceled_order_item.sql}
    Search For Order    ${order_ids[0]}
    Get Return Cancelled Amount From Order Financials
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonCODReturn}
    Enter Invalid Min Amount    0
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    Enter Invalid Max Amount    ${calculatedReturnedCancelledAmount}
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Add Credit Error retrun Credit To Order
    [Documentation]    Verify that a user can successfully add Credit Error credit to an order
    [Tags]    QABSE-1340
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${canceled_order_except_auto_canceled.sql}
    Search For Order    ${order_ids[0]}
    Get Cancelled Amount From Order Financials
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonCreditError} 
    Enter Canceled Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    [Teardown]    Tear Down

Fin-Portal | Manual Credit Reason | Validate Credit Error Cancelled Items Check
    [Documentation]    Verify Credit error credit reason checks for cancelled items on oter
    [Tags]    QABSE-1340
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Expand The Customer Credit Section And Click The Allocate Credit Button
    Select A Credit Reason    ${reasonCreditError} 
    Enter An Amount And Enter An Admin Note For Order Credit
    Select The Add Credit Button
    Select OK On The Dialog
    Verify Validation Error
    [Teardown]    Tear Down
