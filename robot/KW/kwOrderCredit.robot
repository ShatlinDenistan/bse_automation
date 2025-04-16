*** Settings ***
Resource    ../Config/defaultConfig.robot


*** Keywords ***
Expand The Customer Credit Section And Click The Allocate Credit Button
    # Dynamic xpath
    Click Element    ${btnCustomerCudion}
    Sleep    ${SLEEP}
    Click Element    ${btnCredit}

Select A Credit Reason
    [Arguments]    ${reason}
    Click Element    ${dropdownCreditReason}
    Scroll To Element    ${reason}
    Wait Until Element Is Visible    ${reason}
    Click Element    ${reason}

Enter An Amount And Enter An Admin Note For Order Credit
    ${OrderCreditAmount}=     Generate Random String        1     35
    Set Global Variable    ${OrderCreditAmount}
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${OrderCreditAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note


Enter Invalid Min Amount
    [Arguments]    ${minAmount}
    Set Global Variable    ${minAmount}
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${minAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note

Enter Invalid Max Amount
    [Arguments]    ${maxAmount}
    Set Global Variable    ${maxAmount}
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${maxAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note

Verify Validation Error
    ${error}    Get Text    ${validationError}
    Should Be Equal As Strings    ${error}    Validation Error

Enter Jira Number for Credit Breach Reason
    Input Text    ${txtJiraNumber}    Automation-Jira-Number-123

Expand Order Items Section And Click The Credit Item Option
    Click Element    ${btnOrderItemMenu} 
    Click Element    ${creditItemOption}

Enter a Negative Amount And Enter An Admin Note For Order Credit
    ${OrderCreditAmount}=    Convert To Integer    -3
    Set Global Variable    ${OrderCreditAmount}
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${OrderCreditAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note

Enter RFN for System Error Reason
    Input Text    ${txtRFNNumber}    Automation-RFN-Number-1
    
Enter Calculated Amount And Enter An Admin Note For Order Credit
    #Get amounts in DB
    ${orderTotalAmount}=   Convert To Number    ${order_total[0]}
    ${orderShipping}=   Convert To Number    ${order_shipping[0]}
    ${orderDiscount}=   Convert To Number    ${order_discount[0]}

    #Calculate Auth Total
    ${calculatedAuthTotal}=    Evaluate    ${orderTotalAmount} + ${orderShipping} - ${orderDiscount} + 10000
    ${calculatedAuthTotal}=      Format String     {:,}    ${calculatedAuthTotal}
    ${calculatedAuthTotal}=    Convert To String    ${calculatedAuthTotal}

    Set Global Variable    ${calculatedAuthTotal}

    #Enter Credit Amount and Admin Note
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${calculatedAuthTotal}
    Input Text    ${txtCreditComments}    Automation Test Admin Note


Get Return Cancelled Amount From Order Financials
    #Get Returned Canceled Total Amount from Order Financials
    Wait Until Element Is Visible    ${accordionOrderFinancials}
    Click Element    ${accordionOrderFinancials}

    ${returnCancelledAmount}    Get Text    ${orderFinancialsReturnCancelled}
    ${globalReturnCancelledAmount}=    Remove String    ${returnCancelledAmount}    R${SPACE}     
    
    Set Global Variable    ${globalReturnCancelledAmount}

    #Convert
    ${globalReturnCancelledAmount_convertedToNumber}=    Convert To Number    ${globalReturnCancelledAmount}
    ${calculatedReturnedCancelledAmount}=    Evaluate    ${globalReturnCancelledAmount_convertedToNumber} + 10000
    Set Global Variable    ${calculatedReturnedCancelledAmount}


Enter Return Canceled Amount And Enter An Admin Note For Order Credit
    #Enter Credit Amount and Admin Note
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${globalReturnCancelledAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note


Get Cancelled Amount From Order Financials
    #Get Returned Canceled Total Amount from Order Financials
    Wait Until Element Is Visible    ${accordionOrderFinancials}
    Click Element    ${accordionOrderFinancials}

    ${cancelledAmount}    Get Text    ${orderFinancialsnCancelled}
    ${globalCancelledAmount}=    Remove String    ${cancelledAmount}    R${SPACE}     
    
    Set Global Variable    ${globalCancelledAmount}

    #Convert
    ${globalCancelledAmount_convertedToNumber}=    Convert To Number    ${globalCancelledAmount}
    ${calculatedCancelledAmount}=    Evaluate    ${globalCancelledAmount_convertedToNumber} + 10000
    Set Global Variable    ${calculatedCancelledAmount}

Enter Canceled Amount And Enter An Admin Note For Order Credit
    #Enter Credit Amount and Admin Note
    Clear Element Text    ${txtCreditAmount}
    Input Text    ${txtCreditAmount}    ${globalCancelledAmount}
    Input Text    ${txtCreditComments}    Automation Test Admin Note


    

