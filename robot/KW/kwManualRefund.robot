*** Settings ***
Resource    ../Config/defaultConfig.robot
Library    DateTime
Library    String
Library    XML


*** Keywords ***
Expand The Customer Credit Accordion Under Customer Info
    Sleep    ${MIN_TIMEOUT}
    Click Element    xpath=//div[contains(text(),' available credit')]
    Sleep    ${SLEEP}

On Order View Page Expand The Order Items Accordion And Click Refund
    Go To    http://fin-portal.master.env/refund/${order_ids[0]}
    Wait Until Page Contains    Amount to be refunded
 
Click The Refund Button And Submit Refund Request
    Wait Until Element Is Visible     ${btnRefund}
    Click Element    ${btnRefund}
    Wait Until Element Is Visible    ${btnSubmittingRefundReq}
    Click Element    ${btnOkay}
    ${date}=      Get Current Date      exclude_millis=yes
    ${get_date_time}=      Convert Date      ${date}      result_format=%d-%b-%Y @ %H:%M
    Set Global Variable    ${get_date_time}

Click The View Refund Log Button And Verify Details
    [Arguments]    ${payment_method}
    Click Element    xpath=//a[contains(text(),'View Refund Log')]
    Wait Until Page Contains    ${payment_method}
    Wait Until Page Contains    Refund
    Wait Until Page Contains    Test en-gcs
    # Wait Until Page Contains    ${get_date_time}

Click The View Refund Log Button And Verify Part-Payment Details
    [Arguments]    ${payment_method}    ${payment_methods}
    Click Element    xpath=//a[contains(text(),'View Refund Log')]
    Wait Until Page Contains    ${payment_method}
    Wait Until Page Contains    ${payment_methods}
    Wait Until Page Contains    fin_portal
    Wait Until Page Contains    Refund
    Wait Until Page Contains    Test en-gcs
    Wait Until Page Contains    ${get_date_time}

Verify That Order Is NOT Eligible For Manual Refund
    Wait Until Element Is Visible    xpath=//li[contains(text(),'Order ${order_ids[0]} is not eligible for refund.')]

Click The Refund Button And Enter Banking Details
    Wait Until Page Contains    Amount to be refunded
    Input Text    xpath=//input[@autocomplete="off" and @name="bankAccount" and @type="text"]    96696696
    Click Element    xpath=//div[@name="bank" and @role="listbox" and @class="ui fluid selection dropdown"]
    Click Element    xpath=//span[contains(text(),'Capitec Bank')]
    Click Element    xpath=//div[contains(text(),'- - Select branch - -')]
    Click Element    xpath=//span[contains(text(),'Capitec Bank CPC')]

Click The EFT Refund Button And Submit Refund Request
    Click Element    ${btnRefund}
    Wait Until Page Contains    Bank account number 96696696 is associated with
    Click Element    xpath=//button[contains(text(),'Proceed')]
    Click Element    ${btnOkay}
    ${date}=      Get Current Date      exclude_millis=yes
    ${get_date_time}=      Convert Date      ${date}      result_format=%d-%b-%Y @ %H:%M
    Set Global Variable    ${get_date_time}

Verify that Refund Amount Excludes Coupon Amount
    ${total_converted}=    Convert To Number    ${order_total[0]}
    ${discount_converted}=    Convert To Number  ${order_discount[0]}
    ${shipping_converted}=    Convert To Number  ${order_shipping[0]}
    ${refund_amount}=    Evaluate    ${total_converted} + ${shipping_converted} - ${discount_converted}
    ${refund_amount}=      Format String     {:,}    ${refund_amount}
    ${refund_amount_text}=    Convert To String    ${refund_amount}
    Log To Console    ${refund_amount_text}
    Wait Until Element Is Visible  xpath=/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/table/tbody/tr/td[2][contains(text(),'${refund_amount_text}')]

Verify That Refund Not Available
    Wait Until Element Is Visible    xpath=//li[contains(text(),'Order ${order_ids[0]} is not eligible for refund.')]
