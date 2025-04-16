*** Settings ***
Resource    ../Config/defaultConfig.robot


*** Keywords ***
Login Fin-Portal
    Wait Until Page Contains Element    xpath=//div[contains(text(),'Log In User')]
    Input Text    xpath=//body/div[2]/div[1]/div[2]/form[1]/div[1]/input[1]    ${USERNAME}
    Input Text    xpath=//body/div[2]/div[1]/div[2]/form[1]/div[2]/input[1]    ${PASSWORD}
    Click Element    xpath=//body/div[2]/div[1]/div[3]/button[1]
    Sleep    5

Login CS-Admin
    Wait Until Page Contains Element   xpath=//input[@name="email"] 
    Input Text      xpath=//input[@name="email"]   ${USERNAME}
    Input Text    xpath=//input[@name="password"]   ${PASSWORD}
    Click Element   xpath=//*[@class="ui green basic button"]
    Sleep    5                      