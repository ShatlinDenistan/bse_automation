*** Settings ***
Resource    ../Config/defaultConfig.robot
Library    OperatingSystem


*** Variables ***
${master_env}=    https://cs-admin-bff.master.env
${test_data_baseurl}=    http://tal-test-data-service.master.env


*** Keywords ***
Cancel Paid Order
    [Documentation]    Cancel Paid Order
    Create Auth Token
    Create Session    CancelPaidOrderSession    ${master_env}
    ${body}=    Get File    ${EXECDIR}/testData/cancel_order.json
    ${header}=    Create Dictionary    Content-Type=application/json    Authorization=${token[0]}
    ${response}=    Post On Session   CancelPaidOrderSession    /orders/${order_ids[0]}/cancel    data=${body}   headers=${header}
    ${status_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    ${resp_body}=    Convert To String    ${response.content}
    Should Contain    ${resp_body}    true
    Log To Console    ${order_ids}

Create Auth Token
    [Documentation]    Create Authetication For Cancel Order
    Create Session    CreateAuthSession    ${master_env}
    ${body}=    Get File    ${EXECDIR}/testData/create_auth_token.json
    ${header}=    Create Dictionary    Content-Type=application/json
    ${response}=    Post On Session   CreateAuthSession    /authenticate    data=${body}   headers=${header}
    ${json_content}=    To Json    ${response.content}
    ${token}    Get Value From Json    ${json_content}    $.token
    Set Global Variable    ${token}
