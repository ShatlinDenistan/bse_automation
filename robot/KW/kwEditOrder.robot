*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orEditOrder.robot


*** Keywords ***
Navigate to Edit Order Screen
    Wait Until Element Is Visible    ${BlackEllipsis}
    Mouse Over    ${BlackEllipsis}
    Click Element    ${EditOrderMenuOption}

Update Payment Method

    Wait Until Element Is Visible    ${PaymentMethodDropdown}
    Click Element    ${PaymentMethodDropdown}
    ${random_number}    Evaluate    random.randint(3, 8)
    FOR    ${counter}    IN RANGE    0    ${random_number}
        Press Keys    ${None}    ARROW_DOWN
    END
    Press Keys    ${PaymentMethodDropdown}    ENTER
    Click Element    ${UpdateButton}


Verify That An Admin Note For Payment Method Update
    Wait Until Element Is Visible    ${PaymeMethodUpdateAdminNote}
    Log    ${PaymeMethodUpdateAdminNote}

Verify That Payment Method Difference Warning Banner Displays
    Sleep    ${SLEEP}   
    Wait Until Element Is Visible    ${PaymeMethodWarningBanner}
    Log    ${PaymeMethodWarningBanner}

Calculate Discount Amount Input Value
    #Get Current Order Total Amount
    ${orderTotalAmount}=   Convert To Number  ${order_total[0]}
    Log     Order Total Amount : ${orderTotalAmount}
     #Add 500 to Current Order Total to create Discount Amount
    ${addDiscountAmount}=    Evaluate    ${orderTotalAmount}+500
    Log     Discount Amount : ${addDiscountAmount}

    #Type calculated Discount Amount into Discount field and submit
    Wait Until Element Is Visible    ${DiscountAmount}
    ${convertedAddDiscountAmount}=    Convert To String    ${addDiscountAmount}
    Input Text    ${DiscountAmount}    ${convertedAddDiscountAmount}
    Click Element    ${UpdateButton}


Verify That Invalid Discount Amount Message
        Wait Until Element Is Visible    ${InvalidDiscountAmount}
        ${InvalidDiscountAmountText}=    Get Text    ${InvalidDiscountAmount}
        Should Contain    ${InvalidDiscountAmountText}    Discount amount cannot exceed the order item total of
        Log    Invalid Discount Amount Message : ${InvalidDiscountAmountText}

Add Shipping Fee And Discount Amounts
    #Random discount amount between 5 and 10
    ${random_discount_amount}    Evaluate    random.randint(5, 10)
    Set Global Variable    ${random_discount_amount}

    #Choose a shipping fee between the 3 shipping fee amounts
    ${shipping_fees}    Create List    65    200    30
    ${random_shipping_fee}=  Evaluate  random.choice(${shipping_fees})  random
    Set Global Variable    ${random_shipping_fee}

    #Send the random values to the input fields
    Wait Until Element Is Visible    ${DiscountAmount}
    Input Text    ${DiscountAmount}    ${random_discount_amount}
        
    Wait Until Element Is Visible    ${ShippingAmount}
    Input Text    ${ShippingAmount}    ${random_shipping_fee} 

    Click Element    ${UpdateButton}

Verify Discount and Shipping Fee Update Admin Notes
    Sleep    ${SLEEP}
    Should Contain    ${DiscountAppliedAdminNote}    ${DiscountAppliedAdminNote}
    Log     ${DiscountAppliedAdminNote}
    Should Contain    ${ShippingFeeAppliedAdminNote}     ${ShippingFeeAppliedAdminNote}
    Log     ${ShippingFeeAppliedAdminNote}

Verify Discount and Shipping Fee Update Audit Logs
    Sleep    ${5}
    Wait Until Element Is Visible    ${BlackEllipsis}
    Mouse Over    ${BlackEllipsis}
    Wait Until Element Is Visible    ${AuditLogMenuOption}
    Click Element    ${AuditLogMenuOption}
    Sleep    ${SLEEP}

    #Get Audit Log entry action type
    Wait Until Element Is Visible    ${AuditLogEditOrderActionType}
    ${action_type}=   Get Text    ${AuditLogEditOrderActionType}

    #Verify Action Type Equals to Edit Order
    Should Contain    ${action_type}    edit_order
    Log    ${action_type}
    
    #Get Audit Log entry data
    ${data}=   Get Text    ${AuditLogEditOrderData}

    #Verify Edit Order Data
    Should Contain    ${data}    updated_values
    Should Contain    ${data}    discount_update
    Should Contain    ${data}    shipping_update
    
    Log    ${data}
Verify that Discount and Shipping Amounts Are Added To Order Financials 
    Wait Until Page Contains Element    ${OrderFinancialsAccordion}
    Click Element    ${OrderFinancialsAccordion}

    #Verify Shipping is added
    ${order_financials_shipping_amount}    Get Text    ${OrderFinancialsShippingAmount}
    ${order_financials_shipping_amount}=    Remove String    ${order_financials_shipping_amount}    R${SPACE}
    Log    Order Financials Shipping : ${order_financials_shipping_amount}

    #Verify Discount is added 
    ${order_financials_discount_amount}    Get Text    ${OrderFinancialsDiscountAmount}
    ${order_financials_discount_amount}=    Remove String    ${order_financials_discount_amount}    R${SPACE}    
    Log    Order Financials Discount : ${order_financials_discount_amount}

Navigate to Update To Shipped Screen
    Wait Until Page Contains Element    ${ReturnCanceledOrderItemMenu}
    Click Element    ${ReturnCanceledOrderItemMenu}
    Click Element    ${UpdateToShippedMenuOption}

Update Order Item Status From Returned Canceled To Shipped
    Wait Until Page Contains Element    ${UpdateToShippedMenuOption}
    
    ${message_text}=    Get Text    ${UpdateToShippedModalMessage}
    Should Contain    ${message_text}    Update status for order

    Click Element    ${UpdateToShippedButton}

Verify Update From Return Canceled To Shipped Admin Note and Audit Log Entry
    Sleep    ${SLEEP}

    #Verify Admin Note has been added
    Should Contain    ${UpdateToShippedAdminNote}    ${UpdateToShippedAdminNote}
    Log    AdminNote : ${UpdateToShippedAdminNote} 

    #Verify the update to shipped audit log
    Sleep    ${10}
    Wait Until Element Is Visible    ${BlackEllipsis}
    Mouse Over    ${BlackEllipsis}
    Wait Until Element Is Visible    ${AuditLogMenuOption}
    Click Element    ${AuditLogMenuOption}

    #Get Audit Log entry action type
    Sleep    ${10}
    Wait Until Element Is Visible    ${AuditLogEditOrderActionType}
    ${action_type}=   Get Text    ${AuditLogEditOrderActionType}

    #Verify Action Type Equals to Edit Order
    Should Contain    ${action_type}    update_order_item_to_shipped
    Log    ${action_type}
Verify That Both Shipping and Discount Disabled Fields Are On Edit Order Screen
   Element Should Not Be Visible    ${DiscountAmount}
   Element Should Not Be Visible    ${ShippingAmount}

   Element Should Be Visible    ${DiscountAmountDisabledField}
   Element Should Be Visible    ${ShippingFeeDisabledField}

Update Shipping Amount
    Wait Until Element Is Visible    ${ShippingAmount}
    Input Text    ${ShippingAmount}    75
    Click Element    ${UpdateButton}

Verify that the Shipping Amount is Updated on Order Financials 
    Wait Until Page Contains Element    ${OrderFinancialsAccordion}
    Click Element    ${OrderFinancialsAccordion}

    ${order_financials_shipping_amount}    Get Text    ${OrderFinancialsShippingAmount}
    ${order_financials_shipping_amount}=    Remove String    ${order_financials_shipping_amount}    R${SPACE}
    Log To Console    ${order_financials_shipping_amount}

    Should Be Equal    ${order_financials_shipping_amount}    75.00

Update Discount Amount
    Wait Until Element Is Visible    ${DiscountAmount}
    Input Text    ${DiscountAmount}    10
    Click Element    ${UpdateButton}

Verify that the Discount Amount is Updated on Order Financials 
    Wait Until Page Contains Element    ${OrderFinancialsAccordion}
    Click Element    ${OrderFinancialsAccordion}

    ${order_financials_discount_amount}    Get Text    ${OrderFinancialsDiscountAmount}
    ${order_financials_discount_amount}=    Remove String    ${order_financials_discount_amount}    R${SPACE}
    Log To Console    ${order_financials_discount_amount}

    Should Be Equal    ${order_financials_discount_amount}    10.00

Verify That Payment Method Options Are Displayed
    ${expected_Options}=  Create List    COD   Credit Card  Credit Card Token  MasterPass  PayFast  iPay  OneVoucher  eBucks   Discovery Miles   Mobicred   NSFAS Wallet | Celbux eVoucher   Deposit   Credit   Payflex   Nedbank Personal Loan  TakealotCredit
    Click Element  ${PaymentMethodDropdown}
    ${paymentOptions_text}=    Get Text    ${PaymentMethodDropdown}
    ${actual_Options}=    Split String    ${paymentOptions_text}    \n
    Remove Values From List    ${actual_Options}    -- none --    -- none -- 
    Lists Should Be Equal    ${actual_Options}    ${expected_Options}
    Close Browser