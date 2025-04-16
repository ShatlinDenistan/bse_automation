*** Settings ***
Resource    ../../Config/defaultConfig.robot
Resource    ../../KW/kwOrderView.robot
Resource    ../../KW/kwOrderList.robot

*** Test Cases ***
  
Fin-Portal | Add Note
    [Documentation]    Verify that a user can add a note on the order view page
    [Tags]    QABSE-242
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    126388782
    Add Admin Notes    
    [Teardown]    Tear Down

Fin-Portal | Blacklist and Whitelist a Customer
    [Documentation]    Verify that a user can update the blacklist status on the order view page
    [Tags]    QABSE-235
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    126388782
    Update To Blacklist 
    Update To Whitelist 
    [Teardown]    Tear Down

Fin-Portal | Cancel an Order
    [Documentation]    Verify that a user can cancel an order 
    [Tags]    QABSE-131
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount_amount.sql}
    Search For Order    ${order_ids[0]}
    Cancel All Order Items
    [Teardown]    Tear Down

Fin-Portal | Send an Email
    [Documentation]    Verify that a user can send an email to the customer on the order view page
    [Tags]    QABSE-234
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount_amount.sql}
    Search For Order    ${order_ids[0]}
    Send an Email
    [Teardown]    Tear Down

Fin-Portal | Mark Order As Risky
    [Documentation]    Verify that a user can mark an order as risky on the order view page
    [Tags]    QABSE-231
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${non_risky_order.sql}
    Search For Order    ${order_ids[0]}
    Mark Order As Risky
    Verify Audit Log Entry    mark_order_as_risky
    [Teardown]    Tear Down

Fin-Portal | Authorize Order
    [Documentation]    Verify that a user can manually authorize an order
    [Tags]    QABSE-132
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount__and_shipping_amount.sql}
    Search For Order    ${order_ids[0]}
    Manually Authorize An Order
    Verify Audit Log Entry    authorise_order
    [Teardown]    Tear Down
Fin-Portal | No Order Tracking Information For Digital Items Only Order
    [Documentation]    Verify that there is no tracking information for a digital items only order
    [Tags]    QABSE-853
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    145423528
    Verify Order Tracking For Digital Products Only Order  
    [Teardown]    Tear Down

Fin-Portal | No Order Tracking Information For A Cancelled Order
    [Documentation]    Verify that there is no tracking information for a canceleld order
    [Tags]    QABSE-857
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount_amount.sql}
    Search For Order    ${order_ids[0]}
    Cancel All Order Items
    Verify Order Tracking Heading    Cancelled Item(s)   
    [Teardown]    Tear Down

Fin-Portal | Edit Customer Details
    [Documentation]    Verify that a user can edit customer information on the order view page
    [Tags]    QABSE-210
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    162699008
    Edit Customer Details
    [Teardown]    Tear Down

Fin-Portal | View Order Events
    [Documentation]       Verify that the order events can be viewed on the order view page
    [Tags]    QABSE-134
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${paygate_sql} 
    Search For Order    ${order_ids[0]}
    View Order Events
    [Teardown]    Tear Down

Fin-Portal | Multiple Payment Methods Badges
    [Documentation]    Verify that we display all payment method badges for a part paid order
    [Tags]    QABSE-825
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${part_payment_order.sql}
    Search For Order    ${order_ids[0]}  
    Verify Part Payment Methods Badges
    [Teardown]    Tear Down

Fin-Portal | Add Notes
    [Documentation]    Verify that a user can add order, customer and fin notes on the order view page
    [Tags]    QABSE-233
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_no_discount_amount.sql}
    Search For Order    ${order_ids[0]}
    Add Order Notes    
    Add Customer Notes
    Add Fin Notes
    [Teardown]    Tear Down

Fin-Portal | Cancel an Order Item
    [Documentation]    Verify that a user can cancel an order item
    [Tags]    QABSE-228
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${order_with_more_order_items.sql}
    Search For Order    ${order_ids[0]}
    Cancel An Order Item
    [Teardown]    Tear Down

Fin-Portal | View Payment Ledger
    [Documentation]    Verify that a user can view Payment Ledger information
    [Tags]    QABSE-244
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    162110009
    View Payment Ledger
    [Teardown]    Tear Down

Fin-Portal | Bookmarks Page
    [Documentation]    Verify that a user can bookmark an order and remove bookmarks.
    [Tags]    QABSE-135
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    126388782
    Bookmark an Order
    Remove Bookmarks 
    [Teardown]    Tear Down
Fin-Portal | Order Financials Breakdown
    [Documentation]    Verify that a user can view order financials information
    [Tags]    QABSE-96
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${new_order_with_discount_and_shipping_amounts.sql}
    Search For Order    ${order_ids[0]}
    Verify Order Financials
    [Teardown]    Tear Down

Fin-Portal | View Order Audit Logs
    [Documentation]    Verify that a user can view the order audit logs on the order view page
    [Tags]    QABSE-239
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    145480196
    View Order Audit Logs
    [Teardown]    Tear Down

Fin-Portal | View Address
    [Documentation]    Verify that a user can view the address on Google maps
    [Tags]    QABSE-245
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    145480196
    View Address
    [Teardown]    Tear Down    

Fin-Portal | View Order
    [Documentation]    Verify the order information is displayed on the order view page
    [Tags]    QABSE-246
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    145423528
    Verify Order Details   145423528
    [Teardown]    Tear Down  

Fin-Portal | View RRN
    [Documentation]    Verify that the user can view the RRN details
    [Tags]    QABSE-227
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    163732899
    Get RRN Details
    Login CS-Admin
    Verify RRN Details  RRN-T6QRV-9K4W
    [Teardown]    Tear Down  

Fin-Portal | Update Order Item Status
    [Documentation]    Verify that the user can edit an order item status
    [Tags]    QABSE-230
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${order_with_returned_canceled_order_item.sql} 
    Search For Order    ${order_ids[0]}
    Update Order Item to Shipped   
    [Teardown]    Tear Down

Fin-Portal | View Payment Ledger Logs
    [Documentation]    Verify that a user can view payment ledger
    [Tags]    QABSE-97
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${payflex_sql}
    Search For Order    ${order_ids[0]}
    Verify Payment Ledger Logs
    [Teardown]    Tear Down

Fin-Portal | View Email Logs
    [Documentation]    Verify that a user can view email logs
    [Tags]    QABSE-238
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    163732899
    Send an Email
    View Email Logs
    [Teardown]    Tear Down

Fin-Portal | View Order Items Status
    [Documentation]    Verify that a user can view order item information
    [Tags]    QABSE-99
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Get Orders From Database    ${auto_canceled_orders_sql} 
    Search For Order    ${order_ids[0]}
    View Order Items Information
    [Teardown]    Tear Down

Fin-Portal | Verify Order Items Pagination
    [Documentation]    Verify order items accordion pagination
    [Tags]    QABSE-99
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    165251543
    Verify Show Items and Pagination
    [Teardown]    Tear Down

Fin-Portal | View Coupon History
    [Documentation]    Verify that a user can view coupon history on the order page
    [Tags]    QABSE-24
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    148935094
    View Coupon History
    [Teardown]    Tear Down

Fin-Portal | Verify Order Tracking Information
    [Documentation]    Verify that the delivery order is delivered and all waybill tracking information displays
    [Tags]    QABSE-874
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    159445954
    Verify Delivery Tracking Information   Delivered Fri, 30 Aug 2024
    Verify Waybill Tracking  
    [Teardown]    Tear Down

Fin-Portal | Verify Order Not Ready For Collection
    [Documentation]    Verify that the order is not ready for collection and no waybill tracking information displays
    [Tags]    QABSE-873
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    166825424
    Not Ready For Collection  
    [Teardown]    Tear Down

Fin-Portal | Verify Refund History Information
    [Documentation]    Verify refund history information
    [Tags]    QABSE-957
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    154899984
    Verify Refund History Information
    [Teardown]    Tear Down

Fin-Portal | Verify Delivery Address
    [Documentation]    Verify the order delivery address
    [Tags]    QABSE-98
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    163732899
    Verify Delivery Address
    [Teardown]    Tear Down 

Fin-Portal | Verify Customer Google Search
    [Documentation]    Verify the google search of the customer
    [Tags]    QABSE-237
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    163732899
    Verify the Google Search 
    [Teardown]    Tear Down

Fin-Portal | Verify Canceled Order
    [Documentation]    Verify the google search of the customer
    [Tags]    QABSE-237
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    148158095
    Verify Order Total on Canceled Order
    [Teardown]    Tear Down

Fin-Portal | Verify Return Order Total Calculation 
    [Documentation]    Verify Return Order Total Calculation
    [Tags]    QABSE-782
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    160199453
    Verify Order Total on Return Item
    [Teardown]    Tear Down

Fin-Portal | Verify Delivery Information
    [Documentation]    Verify that the user is able to view the delivery information
    [Tags]    QABSE-241
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    159445954
    Verify Delivery Tracking Information   Delivered Fri, 30 Aug 2024
    Verify Delivery Address
    Verify Shipping Information
    [Teardown]    Tear Down

Fin-Portal | Verify Multiple Waybill Information
    [Documentation]    Verify that the delivery order with multiple waybills is delivered and all waybill tracking information displays
    [Tags]    QABSE-875
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    153301924
    Verify Multiple Waybill Tracking  
    [Teardown]    Tear Down

Fin-Portal | Verify Waybill link
    [Documentation]    Verify that when the user clicks the waybill number link, the user is redirected to the mrdexpress page
    [Tags]    QABSE-855
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    159445954
    Verify Waybill Link 
    [Teardown]    Tear Down

Fin-Portal | Verify Order Tracking for Physical Products Order
    [Documentation]    Verify tracking information displays for physical products that have been delivered
    [Tags]    QABSE-854
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    98278540
    Verify Order Tracking for Delivered Physical Products 
    [Teardown]    Tear Down

Fin-Portal | Verify Order Information for a Part Delivered Order
    [Documentation]    Verify that the delivery order includes delivery details for the part of the order that has already been delivered.
    [Tags]    QABSE-682
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order   112799490
    Verify Partial Order Delivery 
    [Teardown]    Tear Down

Fin-Portal | Verify IP Address
    [Documentation]    Verify that a user is able to check the IP Address
    [Tags]    QABSE-243
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order   112799490
    Verify IP Address
    [Teardown]    Tear Down

Fin-Portal | Quick Customer View
    [Documentation]    Verify that hovering over the CustomerID displays a small popup with basic customer information
    [Tags]    QABSE-221
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order   112799490
    Hover Over CustomerID
    Verify Customer Info
    [Teardown]    Tear Down

Fin-Portal | Verify Order Shipping Information
    [Documentation]    Verify order shipping information on the waybill tracking modal
    [Tags]    QABSE-852
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Search For Order    169820566
    Verify Order Shipping Info
    [Teardown]    Tear Down

Fin-Portal | Verify Order Not Yet Ready Collected
    [Documentation]    Verify order that is not yet ready for collection
    [Tags]    QABSE-871
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Navigate to OrderList Page
    Filter By Collect Shipping Method and Daily Deals
    Verify Collection Not Yet Ready
    [Teardown]    Tear Down

Fin-Portal | Verify Order Not Yet Ready For Delivery
    [Documentation]    Verify order that is not yet ready for delivery
    [Tags]    QABSE-873
    [Setup]    Open Web Browser
    Verify Title
    Login Fin-Portal
    Navigate to OrderList Page
    Filter By Courier Shipping Method and Daily Deals
    Verify Delivery Not Yet Shipped
    [Teardown]    Tear Down