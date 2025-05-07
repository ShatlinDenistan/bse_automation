*** Settings ***
Resource    ../Config/defaultConfig.robot


*** Keywords ***
Verify Title
    Title Should Be  Login
    Capture Page Screenshot    EMBED
