*** Settings ***
Resource    ../Config/defaultConfig.robot
Library    DateTime
Library    String


*** Keywords ***
Click Payments Ledger Accordion
    # Dynamic xpath
    Click Element    xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[7]
    Sleep    ${SLEEP}

Click Authorize Now Button And Close Notification
    # credit Card
    Click Element    ${AuthorizeNow}
    Sleep    ${SLEEP}
    Wait Until Element Is Visible    ${AuthSuccessfulMessage}
    Click Element    ${CloseSuccessMessage}
    Wait Until Element Is Visible    ${VerifyManualAuthLogs}

Get Refund Amount For eBucks
    ${ebucks_order_amount}    Get Text    xpath=//tbody/tr[2]/td[9]
    ${ebucks_order_amount}=    Remove String        ${ebucks_order_amount}   R${SPACE}
    Log To Console    ${ebucks_order_amount}
    ${ebucks_refund_amount_text}=    Convert To String    ${ebucks_order_amount}
    Set Global Variable    ${ebucks_refund_amount_text}

Click The Manual Auth Override Button And Complete The Override Form
    [Arguments]    ${select_payment_method}
    # Dynamic xpath
    Click Element    ${btnManualOverride}
    Sleep    ${SLEEP}
    Click Element    ${ddlRefundMethod}
    Click Element    ${select_payment_method}
    Input Text    ${txtRefundAmount}    ${ebucks_refund_amount_text}
    Input Text    ${txtOverrideReason}    Test Override
    Click Element    ${btnRefundOverride}

Click The Credit Button And Add Credit Amount
    Click Element    css=#root > div.pusher.VerticalScrollDiv > div > div > div > div > div > div > div.ui.centered.stackable.vertically.divided.grid > div.two.column.row > div.six.wide.column > div > div.content.active > div > div > div.accordion.ui.fluid.styled > div:nth-child(6) > div > div > div > div > div > div:nth-child(3) > button
    Input Text    xpath=//input[@aria-invalid="true" and @name="amount"]    ${order_total[0]}
    Input Text    xpath=//textarea[@aria-invalid="true" and @name="comment"]    Added credit amount test
    Click Element    xpath=//button[contains(text(),'Add Credit')]
    Click Element    xpath=//button[contains(text(),'OK')]