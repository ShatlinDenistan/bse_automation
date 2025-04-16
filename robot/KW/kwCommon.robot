*** Settings ***
Resource    ../Config/defaultConfig.robot


*** Keywords ***
Tear Down
    # IF  '${TEST_STATUS}'== 'PASS'
    #         Execute Javascript  sauce:job-result=passed
    #     ELSE
    #         Execute Javascript  sauce:job-result=failed
        
    # END
    Capture Page Screenshot
    Close All Browsers

