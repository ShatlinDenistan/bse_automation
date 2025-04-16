*** Settings ***
Resource    ../Config/defaultConfig.robot



*** Keywords ***
Search For Customer
    [Arguments]    ${search}
    Click Element    ${searchBar}
    Click Element    ${txtSearch}
    Input Text    ${txtSearch}    ${search}
    Click Element    ${ddlSearch}
    Click Element    ${ddlCustomer}
    Click Element    ${btnSearchButton}
    Wait Until Page Contains    Customer Info    ${MIN_TIMEOUT}

Search For Order
    [Arguments]    ${search}
    Click Element    ${searchBar}
    Click Element    ${txtSearch}
    Input Text    ${txtSearch}    ${search}
    Click Element    ${ddlSearch}
    Click Element    ${ddlOrder}
    Click Element    ${btnSearchButton}
    Wait Until Page Contains    Customer Info    ${MAX_TIMEOUT}

Search For RRN
    [Arguments]    ${search}
    Click Element    ${csCloseIcon}
    Click Element    ${csSearchTxt} 
    Input Text    ${csSearchTxt}    ${search}
    Click Element    ${csSearchBtn}