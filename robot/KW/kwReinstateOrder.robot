*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orReinstateOrder.robot


*** Keywords ***
Reinstate Order
    Wait Until Element Is Visible    ${BtnReinstate}
    Click Button    ${BtnReinstate}
    Sleep    ${SLEEP}
    Wait Until Element Is Visible    ${BtnReinstate}


    ${reinstate_staff_discount_amount}    Get Text    ${ReinstateStaffDiscountAmount}
    ${reinstate_staff_discount_amount}=    Remove String        ${reinstate_staff_discount_amount}   R${SPACE}    
    Set Global Variable    ${reinstate_staff_discount_amount}
    Log    Reinstate Staff Discount : ${reinstate_staff_discount_amount}

     ${reinstate_order_items_amount}    Get Text    ${ReinstateOrderItemsAmount}
    ${reinstate_order_items_amount}=    Remove String        ${reinstate_order_items_amount}   R${SPACE}    
    Set Global Variable    ${reinstate_order_items_amount}
    Log    Reinstate Order Items : ${reinstate_order_items_amount}

    ${reinstate_delivery_amount}    Get Text    ${ReinstateDeliveryAmount}
    ${reinstate_delivery_amount}=    Remove String        ${reinstate_delivery_amount}   R${SPACE}    
    Set Global Variable    ${reinstate_delivery_amount}
    Log    Reinstate Delivery : ${reinstate_delivery_amount}

    ${reinstate_coupon_discount_amount}    Get Text    ${ReinstateCouponDiscountAmount}
    ${reinstate_coupon_discount_amount}=    Remove String        ${reinstate_coupon_discount_amount}   R${SPACE}    
    Set Global Variable    ${reinstate_coupon_discount_amount}
    Log    Reinstate Coupon Discount : ${reinstate_coupon_discount_amount}

    ${reinstate_order_total_amount}    Get Text    ${ReinstateOrderTotalAmount}
    ${reinstate_order_total_amount}=    Remove String        ${reinstate_order_total_amount}   R${SPACE}    
    Set Global Variable    ${reinstate_order_total_amount}
    Log    Reinstate Order Total : ${reinstate_order_total_amount}

    Click Button    ${ReinstateBtn}

Verify That An Admin Note For Order Reinstatement Was Created
    Wait Until Element Is Visible    ${AdminNote}
    Log    ${AdminNote}

Get Order Financials Amounts
    Wait Until Page Contains Element    ${OrderFinancialsAccordion}
    Click Element    ${OrderFinancialsAccordion}
    ${order_financials_staff_discount_amount}    Get Text    ${OrderFinancialsStaffDiscountAmount}
    ${order_financials_staff_discount_amount}=    Remove String    ${order_financials_staff_discount_amount}    R${SPACE}-    
    Set Global Variable    ${order_financials_staff_discount_amount}
    Log    Order Financials Staff Discount : ${order_financials_staff_discount_amount}

Verify That Staff Discount on Reinstate Matches Staff Discount on Order Financials
   Should Be Equal    ${reinstate_staff_discount_amount}    ${order_financials_staff_discount_amount}

Verify That Reinstate Order Amounts Are Correct

    ${reinstate_order_total__calculation}=    Evaluate    ${reinstate_order_items_amount} + ${reinstate_delivery_amount} - ${reinstate_coupon_discount_amount}
    Log    ${reinstate_order_total__calculation}

    Should Be Equal As Numbers    ${reinstate_delivery_amount}    ${order_shipping[0]}
    Should Be Equal As Numbers    ${reinstate_coupon_discount_amount}    ${order_discount[0]}
    Should Be Equal As Numbers    ${reinstate_order_total_amount}    ${reinstate_order_total__calculation}

Verify That Reinstate Button Is Not Available
   Element Should Not Be Visible    ${BtnReinstate} 
   ${order_page_canceled_by_tag}    Get Text    ${OrderPageCanceledByBadge}
   Log    ${order_ids[0]} ${order_page_canceled_by_tag}