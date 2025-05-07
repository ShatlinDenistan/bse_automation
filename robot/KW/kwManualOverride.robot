*** Settings ***
Resource    ../Config/defaultConfig.robot
Library    DateTime
Library    String


*** Keywords ***

Click The Manual Override Button And Complete The Override Form
    [Arguments]    ${select_payment_method}
    # Dynamic xpath
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_method}
    Input Text    ${txtRefundAmount}    ${order_total[0]}
    Input Text    ${txtOverrideReason}    Test Override
    Click Element    ${btnRefundOverride}

Click The Manual Override Button And Complete The Override Form With Amount Exceeding Total
    [Arguments]    ${select_payment_method}
    ${refund_amount}=    Evaluate    ${order_total[0]} + 700
    Log To Console    ${refund_amount}
    # Dynamic xpath
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_method}
    Input Text    ${txtRefundAmount}    ${refund_amount}
    Input Text    ${txtOverrideReason}    Test Override
    Click Element    ${btnRefundOverride}

Click The Manual Override Button And Complete The Override Form for Credit Card and eBucks
    [Arguments]    ${select_payment_method}    ${select_payment_methods}  
    Capture Page Screenshot
    #eBucks
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_methods}
    Input Text    ${txtRefundAmount}    ${ebucks_refund_amount_text}
    Input Text    ${txtOverrideReason}    Test eBucks Override
    Click Element    ${btnRefundOverride}
    Click Button    ${btnConfirmOverride}
    Wait Until Element Is Enabled    xpath=//a[contains(text(),'Okay')]
    Click Element    xpath=//a[contains(text(),'Okay')]
    # credit Card
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_method}
    Input Text    ${txtRefundAmount}    ${refund_amount_text}
    Input Text    ${txtOverrideReason}    Test Credit card Override
    Click Element    ${btnRefundOverride}

Click The Manual Override Button And Complete The Override Form EFT
    [Arguments]    ${select_payment_method}
    # Dynamic xpath
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_method}
    Click Element    ${originalPaymentMethod}
    Click Element    ${selectEFTOriginatPayMeth}
    Input Text    ${txtEFTRefundAmount}    ${order_total[0]}

Capture EFT Banking Details
    ${AccountNumber}=     Generate Random String        8     0123456789
    Input Text    ${txtBankAccount}    ${AccountNumber}
    Click Element    ${ddlBankName}
    Click Element    ${selectBankName}
    Click Element    ${ddlBranch}
    Click Element    ${selectBranch}
    Input Text    ${txtEFTOverrideReason}    Test Override
    Click Element    ${btnEFTRefundOverride}

Confirm Manual Override And View Logs
    Click Button    ${btnConfirmOverride}
    Wait Until Element Is Enabled    xpath=//a[contains(text(),'Okay')]
    Click Element    xpath=//a[contains(text(),'Okay')]
    Go To    http://fin-portal.master.env/order/${order_ids[0]}/refunds_logs
    Sleep    2

Verify Manual Override Details
    [Arguments]    ${payment_method}
    Wait Until Page Contains    ${payment_method}
    Wait Until Page Contains    Refund
    Wait Until Page Contains    Test en-gcs

Verify That Refund Amount Excludes Donation Amount
    ${order_amount}    Get Text    xpath=/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
    ${order_amount}=    Remove String        ${order_amount}   R${SPACE}
    # ${total_converted}=    Convert To Number    ${order_amount}
    ${donation_converted}=    Convert To Number  ${donation_amount[0]}
    ${shipping_converted}=    Convert To Number  ${order_shipping[0]}
    ${refund_amount}=    Evaluate    ${order_amount} - ${donation_amount[0]}
    Log To Console    ${refund_amount}
    ${refund_amount}=      Format String     {:,}    ${refund_amount}
    ${refund_amount_text}=    Convert To String    ${refund_amount}
    Log To Console    ${refund_amount_text}
    Wait Until Element Is Visible  xpath=/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/table/tbody/tr/td[2][contains(text(),'${refund_amount_text}')]

Get Refund Amount For Payment Methods
    ${cc_order_amount}    Get Text    xpath=//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]
    ${ebucks_order_amount}    Get Text    xpath=//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
    ${cc_order_amount}=    Remove String        ${cc_order_amount}   R${SPACE}
    # ${cc_refund_amount}=      Format String     {:,}    ${cc_order_amount}
    Log To Console    ${cc_order_amount}
    ${refund_amount_text}=    Convert To String    ${cc_order_amount}

    ${ebucks_order_amount}=    Remove String        ${ebucks_order_amount}   R${SPACE}
    # ${ebucks_refund_amount}=      Format String     {:,}    ${ebucks_order_amount}
    Log To Console    ${ebucks_order_amount}
    ${ebucks_refund_amount_text}=    Convert To String    ${ebucks_order_amount}
    Log To Console    ${ebucks_refund_amount_text}
    Log To Console    ${refund_amount_text}
    Set Global Variable    ${refund_amount_text}
    Set Global Variable    ${ebucks_refund_amount_text}
    
Enter Donation And Enter A Comment
   Input Text    ${txtCreditAmount}    5
   Input Text    ${txtCreditComments}    Donation credit

Verify That There Are 2 Admin Notes For Both Manual Overrides Was Created
    Input Text    ${txtSearch}    ${order_ids[0]}
    Click Element    ${btnSearchButton}
    Wait Until Element Is Visible    xpath=//li[contains(text(),'Refund by eBucks, Amount: ')]
    Wait Until Element Is Visible    xpath=//li[contains(text(),'Refund by CreditCard, Amount: ')]

Verify That An Admin Note For The Failed Manual Override Was Created
    Input Text    ${txtSearch}    ${order_ids[0]}
    Click Element    ${btnSearchButton}
    Wait Until Element Is Visible    xpath=//div[contains(text(),'by Test en-gcs: Refund request submission failed (')]
