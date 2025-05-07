*** Settings ***
Resource    ../Config/defaultConfig.robot

*** Keywords ***

Navigate To Deposit Match
    Click Element    xpath=//i[@aria-hidden="true" and @class="content large icon"]
    Click Element    xpath=//body/div[@id='root']/div[1]/a[3]
    Wait Until Page Contains Element    xpath=//h1[contains(text(),'Batches')]

Go To Deposit Match Page
    Click Element    xpath=//body/div[@id='root']/div[1]/a[3]
    Wait Until Page Contains Element    xpath=//h1[contains(text(),'Batches')]
  
Upload Valid Deposit Match File
    [Arguments]    ${csv_file}
    Click Element    xpath=//button[contains(text(),'Upload CSV')]
    Click Element    xpath=//div[@name="statementType" and @role="listbox"]
    Click Element    xpath=//span[contains(text(),'Generic')]
    Click Element    xpath=//div[@name="paymentMethod" and @aria-disabled="false" and @aria-expanded="false"]
    Click Element    xpath=//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]
    Choose File    xpath=//input[@type='file']    ${csv_file}
    Click Element    xpath=//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]
    Sleep    15
    ${GetBatchId}    Get Text    xpath=//a[@class="active section"]
    Set Global Variable    ${GetBatchId}

Upload Invalid Deposit Match File
    Click Element    ${BtnUploadCSV}
    Click Element    ${SelectStatementType}
    Click Element    xpath=//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[7]/span[1]
    Choose File    xpath=//input[@type='file']    ${Deposit_Match_File}
    Wait Until Element Is Visible    xpath=//span[contains(text(),'GENERIC GLOBAL 1.csv')]
    Click Element    xpath=//button[@class="ui blue compact right floated button"]

Verify CSV Error Occured
    #Element Should Contain    ${ErrorMessage}    Error: The CSV must contain the following headers: ['DATE', 'TYPE', 'M PAYMENT ID', 'GROSS', 'DESCRIPTION']
    ${error}    Get Text    ${ErrorMessage}
    Should Be Equal As Strings    ${error}    Error Occurred

Download Batch File
    [Documentation]    Download the Batch for the file you just uploaded
    Click Element    ${batchDownload}

Click The Refresh Button
    [Documentation]    Refresh Page for records to display on the page
    Sleep    15
    Click Element    ${RefreshButton}
    Wait Until Element Is Visible    ${CustomerNameLbl}    timeout=40s
    ${BatchId}    Get Text    xpath=//a[@class="active section"]
    Set Test Variable    ${BatchId}

Click Show Items Dropdown And Select 30 Items
    Click Element    ${ItemListDDL}
    Click Element    ${ListFilter30}

Navigate To Second Page
    Click Element    ${PageTwoNav}
    Wait Until Element Is Visible    ${CustomerNameLbl}

Click The Select Payment Method Dropdown And Select PayFast And Apply Filter
    Click Element    ${PaymentMethodDDL}
    Click Element    ${PayFastLst}
    Click Element    ${ApplyFilter}

Verify That Batches Are Filtered By Payment Method
    Wait Until Element Contains    ${PaymentMethodLst}    PayFast

Click The Clear Filter Button
    Click Element    ${ClearFilter}

Click The Select Date Range Field And Select Date From The Previous Week
    Input Text    ${DateFilter}    01-05-2023 - 12-05-2023
    Click Element    ${ApplyFilter}
    Wait Until Element Is Visible    ${BatchDate}    ${MIN_TIMEOUT}

Click On Existing Batch
    Click Element    xpath=//th[contains(text(),'Batch Id')]
    Press Keys    None    TAB
    Press Keys    None    ENTER
    
Click The Criteria Dropdown List And Select OrderID
    Click Element    ${CriteriaDropdown}
    Click Element    ${OdrerIdDM}

Enter Order Id On Searchbox And Apply Filer
    ${order_id_}    Get Text    ${order_no_text}
    ${customer_name_}    Get Text    ${cust_name_text}
    ${amount_}    Get Text    ${statem_amount_text}
    Set Global Variable    ${order_id_}
    Set Global Variable    ${customer_name_}
    Set Global Variable    ${amount_}
    Input Text    ${DepositMatchSearch}    ${order_id_}
    Click Element    ${ApplyFilter}
    Wait Until Element Is Visible    xpath=//a[contains(text(),'${order_id_}')]
    Click Element    ${ClearFilter}

Click The Criteria Dropdown List And Select Statement Amount
    Click Element    ${CriteriaDropdown}
    Click Element    ${StatementAmountDM}

Enter Statement Amount On Searchbox And Apply Filer
    Input Text    ${DepositMatchSearch}    ${amount_}
    Click Element    ${ApplyFilter}
    Click Element    ${ClearFilter}

Click The Criteria Dropdown List And Select Customer Id
    Click Element    ${CriteriaDropdown}
    Click Element    ${CustomerIdDM}

Enter Customer ID On Searchbox And Apply Filer
    Input Text    ${DepositMatchSearch}    2571878
    Click Element    ${ApplyFilter}
    Click Element    ${ClearFilter}

Click The Criteria Dropdown List And Select Customer Name
    Click Element    ${CriteriaDropdown}
    Click Element    ${CustomerNameDM}

Enter Customer Name On Searchbox And Apply Filer
    Input Text    ${DepositMatchSearch}    ${customer_name_}
    Click Element    ${ApplyFilter}
    Click Element    ${customer_name_link}

Select Authorised Order And Cancel
    Wait Until Element Is Enabled    ${chkNewOrder}    ${MIN_TIMEOUT}
    Click Element    ${chkNewOrder}
    Click Element    ${btnCancelOrder}
    Click Element    ${cancelReasonDropdown} 
    Click Element    ${cancelReason}
    Click Element    ${btnConfirmCancelOrder}

Select Batch With Authorised Orders
    Go To    http://fin-portal.master.env/all_batches/2007


Select Batch With New Status Orders
    Get Orders From Database    ${new_order_ebucks_cc_sql}
    ${orderid_string} =    Convert To String    ${order_ids[0]}
    Clear File    testData/NewOrderUploadFile.csv
    Append To File    testData/NewOrderUploadFile.csv     "Description,Amount",
    Append To File    testData/NewOrderUploadFile.csv    ${\n}
    Append To File    testData/NewOrderUploadFile.csv     ${orderid_string}
    Append To File    testData/NewOrderUploadFile.csv     ,100
    Click Element    xpath=//button[contains(text(),'Upload CSV')]
    Click Element    xpath=//div[@name="statementType" and @role="listbox"]
    Click Element    xpath=//span[contains(text(),'Generic')]
    Click Element    xpath=//div[@name="paymentMethod" and @aria-disabled="false" and @aria-expanded="false"]
    Click Element    xpath=//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]
    Choose File    xpath=//input[@type='file']    ${Deposit_Match_New_Order_File} 
    Click Element    xpath=//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]
    ${GetBatchId}    Get Text    xpath=//a[@class="active section"]
    Set Global Variable    ${GetBatchId}

Select New Order And Authorise
    Wait Until Element Is Enabled    ${chkNewOrder}   ${MIN_TIMEOUT}
    Click Element   ${chkNewOrder}
    Click Element    ${btnAuthoriseOrder}
    Wait Until Element Is Visible    ${VerifyAuthoriseOrder}

Select Authorised Order And Authorise
    Wait Until Element Is Enabled    ${chkOrder}    ${MIN_TIMEOUT}
    Click Element   ${chkOrder}
    Click Element    ${btnAuthoriseOrder}
    Wait Until Element Is Visible    ${VerifyAuthoriseOrder}

Click Match Status Drop-down And Select Auto Match
    Click Element    ${MatchStatus}
    Click Element    ${AutoMatch}
    Click Element    ${ApplyFilter}
    Wait Until Page Contains    AUTO MATCH    
    Click Element    ${ClearFilter}

Click Match Status Drop-down And Select Amount Differ
    Click Element    ${MatchStatus}
    Click Element    ${AmountDiffer}
    Click Element    ${ApplyFilter}
    Wait Until Page Contains    Amount Differ
    Click Element    ${CloseFilterButton}

Click Match Status Drop-down And Select Order Not Found
    Click Element    ${MatchStatus}
    Click Element    ${OrderNotFound}
    Click Element    ${ApplyFilter}
    Wait Until Page Contains    Order Not Found

Click The Unclaimed Payment Tab
    Click Element    ${UnclaimedPaymentsTab}

Click Criteria Drop-down List And Select Customer Name
    [Documentation]    Keyword to select search term
    Click Element    ${CriteriaDropdown}
    Click Element    ${CustomerNameDM}

Enter Customer Name And Apply Filter
    [Documentation]    Keyword to search for Customer Name
    Input Text    ${txtCriteriaSearch}   Jack
    Click Element    ${ApplyFilter}
    Click Element    ${ClearFilter}

Click Criteria Drop-down List And Select Order Id
    [Documentation]    Keyword to select search term
    Click Element    ${CriteriaDropdown}
    Click Element    ${OdrerIdDM}

Enter Order Id And Apply Filter
    [Documentation]    Keyword to search for Order Id
    Input Text    ${txtCriteriaSearch}    972479
    Click Element    ${ApplyFilter}
    Click Element    ${ClearFilter}

Click Criteria Drop-down List And Select Statement Amount
    [Documentation]    Keyword to select search term
    Click Element    ${CriteriaDropdown}
    Click Element    ${StatementAmountDM}

Enter Statement Amount And Apply Filter
    [Documentation]    Keyword to search for Statement Amount
    Input Text    ${txtCriteriaSearch}    592.00
    Click Element    ${ApplyFilter}
    Wait Until Page Contains    R 592.00
    Click Element    ${ClearFilter}

Click Criteria Drop-down List And Select Batch Id
    [Documentation]    Keyword to select search term
    Click Element    ${CriteriaDropdown}
    Click Element    ${BatchId}

Enter Batch Id And Apply Filter
    [Documentation]    Keyword to search for Batch Id
    Input Text    ${txtCriteriaSearch}   1905
    Click Element    ${ApplyFilter}
    Wait Until Element Contains    ${BatchIdValue}    1905
    Click Element    ${ClearFilter}

Click Checkbox Next To First Order In The Batch
    Click Element    ${OrderNumberCheckbox}
    ${UnclaimedOrderId}    Get Text    ${OrderNumberText}
    Set Test Variable    ${UnclaimedOrderId}
 

Click The Unclaimed Payment Button
    Click Element    ${BtnUnclaimedPayment}
    Click Element    ${CloseIcon}

Navigate To Unclaimed Payment Page
    Click Element    xpath=//a[contains(text(),'Unclaimed Payments')]
    Wait Until Page Contains    All Batches

Enter Unclaimed Payment Order Id And Apply Filter
    [Documentation]    Keyword to search for Order Id
    Input Text    ${txtCriteriaSearch}    ${UnclaimedOrderId}
    Click Element    ${ApplyFilter}
    Wait Until Element Is Visible    xpath=//a[contains(text(),'${UnclaimedOrderId}')]
    Click Element    ${ClearFilter}

Click The Remove Order Button
    Click Element    ${RemoveOrder}
    Click Element    ${CloseIcon}

Click The Match Button And Type In The Order ID
    Click Element    ${BtnMatch}
    Wait Until Element Is Visible  ${txtMatchOrderId}
    Input Text    ${txtMatchOrderId}   ${OrderId} 

Click The Match Button And Close Modal
    Click Element    ${BtnMatchSubmit}
    Wait Until Page Contains    Form data posted successfully
    Click Element    ${CloseIcon}

Navigate To All Batches
    Click Element    xpath=//a[contains(text(),'All Batches')]
    Wait Until Page Contains    All Batches
    Wait Until Page Contains Element    xpath=//a[contains(text(),'${BatchId}')]

Click Send Email Button And Send Email
    Click Element    xpath=//button[contains(text(),'Send Email')]
    Click Element    xpath=//button[@class="ui blue button" and @type="submit"]
    Wait Until Element Is Visible    xpath=//div[contains(text(),'Successfully processed 1 item(s)')]
    Click Element    ${CloseIcon}
