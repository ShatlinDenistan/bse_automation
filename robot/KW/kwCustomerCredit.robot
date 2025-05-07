*** Settings ***
Resource    ../Config/defaultConfig.robot
Library    DateTime
Library    String


*** Variables ***
${a}      @ 0

*** Keywords ***
Expand The Customer Credit Section And Click The Credit Button
    # Dynamic xpath
    Sleep    ${SLEEP}
    Click Element    ${btnCredit}

Enter An Amount And Enter A Comment
    ${CustomerCreditAmount}=     Generate Random String        3     123456789
    Set Global Variable    ${CustomerCreditAmount}
    Input Text    ${txtCreditAmount}    ${CustomerCreditAmount}


Select The Add Credit Button
    Click Element    ${btnAddCredit}
    Wait Until Element Is Visible    ${lblConfirmDialog}

Select OK On The Dialog
    Click Element    ${btnConfirmCredit}

Verify That Customer Credit Is Applied
    ${date}=      Get Current Date      exclude_millis=yes
    ${get_date_time}=      Convert Date      ${date}      result_format=%d-%b-%Y @ %H:%M
    ${str_date}=    Convert To String    ${get_date_time} 
    IF    '${a}' in '${str_date}'
        ${str_date}    Replace String    ${str_date}    @ 0    @${SPACE}
        Log To Console    ${str_date}
    ELSE
        Log To Console    ${str_date}
    END
    Page Should Contain    R ${CustomerCreditAmount}
    Page Should Contain    Not linked to an order
    # Element Should Be Visible    xpath=//td[contains(text(),'${str_date}')]

Verify That Order Credit Is Applied
    [Documentation]    Scroll until credit amount is visible and verify that credit was added
    Execute Javascript    window.scrollTo(0, 250)
    Page Should Contain    ${OrderCreditAmount}
