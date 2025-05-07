*** Settings ***
Resource    ../Config/defaultConfig.robot

*** Keywords ***

Navigate To EFT Refunds page
    Click Element    ${btnMenu}
    Click Element    ${btnEftRefundMenu}
    Wait Until Page Contains Element   ${EFTRefundsTable}

Select multiple EFT Refund Requests
    Click Element    ${ddlTypeFilter}

    ${random_number} =    Evaluate    random.randint(1, 3)
    Run Keyword If    ${random_number} == 1    Click Element    ${ddlTypeFilterSelfService}
    Run Keyword If    ${random_number} == 2    Click Element    ${ddlTypeFilterRefund}
    Run Keyword If    ${random_number} == 3    Click Element    ${ddlTypeFilterManualOverride}

    Click Element    ${btnApplyFilter}

    Click Element    ${EftRefundsTableFirstCheckbox}
    Click Element    ${EftRefundsTableSecondCheckbox}

Select Random Template and Send Email
    Click Element    ${btnSendEmailTable}
    Click Element    ${ddlEmailTemplates}

    ${random_number}    Evaluate    random.randint(1, 14)
    Run Keyword If    ${random_number} == 1    Click Element    ${OPTION1_XPATH}
    Run Keyword If    ${random_number} == 2    Click Element    ${OPTION2_XPATH}
    Run Keyword If    ${random_number} == 3    Click Element    ${OPTION3_XPATH}
    Run Keyword If    ${random_number} == 4    Click Element    ${OPTION4_XPATH}
    Run Keyword If    ${random_number} == 5    Click Element    ${OPTION5_XPATH}
    Run Keyword If    ${random_number} == 6    Click Element    ${OPTION6_XPATH}
    Run Keyword If    ${random_number} == 7    Click Element    ${OPTION7_XPATH}
    Run Keyword If    ${random_number} == 8    Click Element    ${OPTION8_XPATH}
    Run Keyword If    ${random_number} == 9    Click Element    ${OPTION9_XPATH}
    Run Keyword If    ${random_number} == 10    Click Element    ${OPTION10_XPATH}
    Run Keyword If    ${random_number} == 11    Click Element    ${OPTION11_XPATH}
    Run Keyword If    ${random_number} == 12    Click Element    ${OPTION12_XPATH}
    Run Keyword If    ${random_number} == 13    Click Element    ${OPTION13_XPATH}
    Run Keyword If    ${random_number} == 14    Click Element    ${OPTION14_XPATH}

    Click Element    ${btnSendEmail}

Verify Email Success Message
    ${EmailSentText}    Get Text    ${EmailSentModal}

    Sleep    2s
    Should Contain    ${EmailSentText}    Sending 2 Emails
    Sleep    5s
    Page Should Contain Element     xpath=//div[contains(text(),'Successfully processed 2 item(s)')]

    Click Element    ${EmailSentModal_Close_icon}

Verify Checkboxes Are Unchecked
    Element Should Be Enabled    ${EftRefundsTableFirstCheckbox}
    Element Should Be Enabled    ${EftRefundsTableSecondCheckbox}
    Element Should Be Enabled    ${EftRefundsTableThirdCheckbox}

Select A Manual EFT Refund Request
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterManualEFT}
    Click Element    ${btnApplyFilter}
    Click Element    ${EftRefundsTableFirstCheckbox}

Verify Email Error Message
    ${EmailSentText}    Get Text    ${EmailSentModal}

    Sleep    2s
    Should Contain    ${EmailSentText}    Sending 1 Email
    Should Contain    ${EmailSentText}   Failed to process 1 item(s)
    Should Contain    ${EmailSentText}   Cannot send email to a ManualEFT request

    Click Element    ${EmailSentModal_Close_icon}

Click On An Order ID And Verify New Tab Opened
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterSelfService}
    Click Element    ${btnApplyFilter}

    ${order_id}    Get Text     xpath=//tbody/tr[7]/td[6]/a[1]
    Click Element   xpath=//tbody/tr[7]/td[6]/a[1]
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${order_id_new_tab}    Get Text     xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]
    Should Contain  ${order_id_new_tab}  ${order_id}

Click On A Customer Name And Verify New Tab Opened
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterSelfService}
    Click Element    ${btnApplyFilter}

    ${Customer_Name}    Get Text   xpath=//tbody/tr[7]/td[8]/a[1]
    Click Element    xpath=//tbody/tr[7]/td[8]/a[1]
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${Customer_Name_New_Tab}   Get Text    xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]
    Should Contain     ${Customer_Name_New_Tab}    ${Customer_Name}

Click The Manual EFT Button And Verify The Fields
     Click Element    ${btnManualEFT}
     Page Should Contain Element     ${txtOrderId}
     Page Should Contain Element     ${txtZendeskTicket}
     Page Should Contain Element     ${txtCustomerName}
     Page Should Contain Element     ${txtRefundAmountManualEFT}
     Page Should Contain Element     ${txtBankAccountManualEFT}
     Page Should Contain Element     ${ddlBankNameManualEFT}
     Page Should Contain Element     ${ddlBranchNameManualEFT}
     ${ManualEFT_Modal_buttons}     Get Text    xpath=/html/body/div[2]/div/div[2]/div/form/div/div[8]/div
     Should Contain    ${ManualEFT_Modal_buttons}    Submit
     Should Contain    ${ManualEFT_Modal_buttons}    Cancel

Populate Manual EFT Refund Request Mandatory Fields
     Input Text    ${txtCustomerName}    BseUIAutomator
     Element Should Be Disabled   ${btnSubmitManualEFT}
     Input Text    ${txtRefundAmountManualEFT}    1
     Element Should Be Disabled   ${btnSubmitManualEFT}
     Input Text    ${txtBankAccountManualEFT}    480121212
     Element Should Be Disabled   ${btnSubmitManualEFT}

     # Click the dropdown to open the options
     Click Element    ${ddlBankNameManualEFT}
     Click Element    ${ddlBankNameManualEFTFNBNamibia}
     Click Element    ${ddlBranchNameManualEFT}
     Click Element    ${ddlBranchNameManualEFTAllNamibia}
     Element Should Be Enabled    ${btnSubmitManualEFT}

Verify Credit Deduction Popup
     Click Element   ${btnSubmitManualEFT}

     Page Should Contain Element    ${ConfirmationHeaderManualEFT}
     Page Should Contain Element    ${ConfirmationTextManualEFT}

Verify Manual EFT Success
    Click Element    ${btnOkayManualEFT}
    Page Should Contain Element    ${SuccessManualEFT}
    ${Manual_EFT_Created}   Get Text    xpath=//table/tbody/tr[1]
    Should Contain    ${Manual_EFT_Created}     BseUIAutomator
    Should Contain    ${Manual_EFT_Created}     R 1.00
    Should Contain    ${Manual_EFT_Created}     480121212
    Should Contain    ${Manual_EFT_Created}     FNB/RMB
    Should Contain    ${Manual_EFT_Created}     Test en-gcs
    
Apply Status Filter
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterExported}
    Click Element    ${btnApplyFilter}
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[3]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Exported
        END
    Click Element    ${ddlClearStatusFilter}
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterDeclined}
    Click Element    ${btnApplyFilter}
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[3]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Declined
        END
    Click Element    ${btnClearFilter}

Apply Type Filter
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterSelfService}
    Click Element    ${btnApplyFilter}
    
    Sleep    2s
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[2]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Self Service
        END
    Click Element    ${ddlClearTypeFilter}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterRefund}
    Click Element    ${btnApplyFilter}
    
    Sleep    2s
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[2]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Refund
        END
    Click Element    ${ddlClearTypeFilter}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterManualOverride}
    Click Element    ${btnApplyFilter}
    
    Sleep    2s
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[2]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Manual Override
        END
        
    Click Element    ${ddlClearTypeFilter}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterManualEFT}
    Click Element    ${btnApplyFilter}
    
    Sleep    2s
        FOR    ${row}    IN RANGE    1    16
            ${locator} =    Set Variable    //tbody/tr[${row}]/td[2]
            ${element_text} =    Get Text    ${locator}
            Should Contain    ${element_text}    Manual EFT
        END
    Click Element    ${btnClearFilter}

Filter By Customer ID
    Click Element    ${ddlFilterBy}
    Click Element    ${ddlFilterByCustomerID}
    Mouse Over   xpath=//table/tbody/tr[15]/td[8]/a
    ${customer_id}  Get Text    xpath=/html/body/div[2]/div
    ${numeric_part}  Get Substring  ${customer_id}  12
    Input Text    ${FilterBySearch}    ${numeric_part}
    Click Element    ${btnApplyFilter}
    Click Element    ${CustomerName}
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${customerinfoID}  Get Text    ${customerinfo}
    Should Be Equal As Integers  ${customerinfoID}  ${numeric_part}
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    Click Element    ${btnClearFilter}

Filter By Order ID
    Click Element    ${ddlFilterBy}
    Click Element    ${ddlFilterByOrderID}
    ${order_id}     Get Text    ${orderIDEFTRefundstable1}
    Input Text    ${FilterBySearch}    ${order_id}
    Click Element    ${btnApplyFilter}
    ${order_id2}     Get Text    ${orderIDEFTRefundstable2}
    Should Be Equal As Integers    ${order_id}    ${order_id2}
    Click Element    ${btnClearFilter}

Filter By Bank Account Number
    Click Element    ${ddlFilterBy}
    Click Element    ${ddlFilterByBankAccountNumber}
    ${bankaccountnumber}     Get Text    ${bankaccEFTRefundstable}
    Input Text    ${FilterBySearch}    ${bankaccountnumber}
    Click Element    ${btnApplyFilter}
    ${bankaccountnumber2}     Get Text    ${bankaccEFTRefundstable}
    Should Be Equal As Integers    ${bankaccountnumber}    ${bankaccountnumber2}
    Click Element    ${btnClearFilter}

Filter By Zendesk Ticket Number
    Click Element    ${ddlShowItems}
    Click Element    ${ddlShow250Items}
    Sleep    2s
        FOR    ${row_index}    IN RANGE    1    250
            ${zendeskticketurl}    Set Variable    //table/tbody/tr[${row_index}]/td[7]
            ${text}    Get Text    ${zendeskticketurl}
            Run Keyword If    "${text}" != ""    Exit For Loop
        END
    ${zendesknumber}  Get Substring  ${text}  43
    Reload Page  # This is done because at some screen resolutions the ${ddlFilterBy} is hidden by the top menu
    Click Element    ${ddlFilterBy}
    Click Element    ${ddlFilterByZendeskTicketNumber}
    Input Text    ${FilterBySearch}    ${zendesknumber}
    Click Element    ${btnApplyFilter}
    ${zendeskticketurl2}  Get Text    ${zendeskticketEFTRefundstable}
    Should Contain    ${zendeskticketurl2}    ${zendesknumber}

Apply Date Range Filter And Show Items Filter And Pagination
    Click Element    ${ddlDateRange}
    Input Text    ${ddlDateRange}    01-07-2023 - 31-07-2023
    Click Element    ${btnApplyFilter}
    Click Element    ${ddlShowItems}
    Click Element    ${ddlShow30Items}
    Sleep    2s
        FOR    ${row}    IN RANGE    1    31
                ${locator} =    Set Variable    //tbody/tr[${row}]/td[4]
                ${element_text} =    Get Text    ${locator}
                Should Contain    ${element_text}    Jul-2023
        END

    Click Element    ${LastPage}
        FOR    ${row}    IN RANGE    1    5
                ${locator} =    Set Variable    //table[1]/tbody[1]/tr[${row}]/td[4]
                ${element_text} =    Get Text    ${locator}
                Should Contain    ${element_text}    Jul-2023
        END

Export One Request On Pending Status
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}

    ${random_number} =    Evaluate    random.randint(1, 3)
    Run Keyword If    ${random_number} == 1    Click Element    ${ddlTypeFilterSelfService}
    Run Keyword If    ${random_number} == 2    Click Element    ${ddlTypeFilterRefund}
    Run Keyword If    ${random_number} == 3    Click Element    ${ddlTypeFilterManualOverride}

    Click Element    ${btnApplyFilter}
    Click Element    ${EftRefundsTableFirstCheckbox}

    ${ExportedOrderID}  Get Text   ${EftRefundsTableFirstOrder}

    Click Element   ${btnExportRequest}
    ${HeaderText}   Get Text    ${ExportModal}
    Should Contain  ${HeaderText}    Export 1 EFT Refund Request
    Click Element   ${ddlExportBank}
    Click Element   ${ddlNedbank}
    Click Element   ${btnExport}
    Sleep    3s
    ${ExportOutcome}    Get Text    ${ExportStatus}
    Should Contain  ${ExportOutcome}    SUCCESSFUL
    Click Element   ${btnExportCloseIcon}

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID}
    Click Element    ${btnApplyFilter}

    Sleep    2s

Verify Exported Row
    ${ExportedRowFile}     Get Text  xpath=//table/tbody/tr[1]/td[12]/a
    ${current_date}    Get Current Date    result_format=%Y-%m-%d
    Should Contain    ${ExportedRowFile}    ${current_date}
    Should Contain    ${ExportedRowFile}    Test_en-gcs.csv

    ${ExportedRowStatus}     Get Text  xpath=//table/tbody/tr[1]/td[3]
    Should Contain    ${ExportedRowStatus}     Exported

    ${ExportedRowOperator}     Get Text  xpath=//table/tbody/tr[1]/td[13]
    Should Contain    ${ExportedRowOperator}     Test en-gcs

    ${ExportedRowDate}      Get Text       xpath=//table/tbody/tr[1]/td[14]
    ${current_date2}        Get Current Date     result_format=%d-%b-%Y
    ${exported_date}        Set Variable    ${ExportedRowDate.split(' ')[0]}
    Should Contain  ${ExportedRowDate}   ${exported_date}

Export Three Requests On Pending Status
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${btnApplyFilter}

    Click Element    ${EftRefundsTableFirstCheckbox}
    Click Element    ${EftRefundsTableSecondCheckbox}
    Click Element    ${EftRefundsTableThirdCheckbox}

    Click Element    ${btnExportRequest}
    ${HeaderText}   Get Text    ${ExportModal}
    Should Contain    ${HeaderText}    Export 3 EFT Refund Requests
    Click Element    ${ddlExportBank}
    Click Element   ${ddlNedbank}
    Click Element    ${btnExport}
    ${ExportOutcome}    Get Text    ${ExportStatus}
    Should Contain    ${ExportOutcome}    SUCCESSFUL
    Click Element   ${btnExportCloseIcon}

Export Request On Exported Status
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterExported}
    Click Element    ${btnApplyFilter}
    Click Element    ${EftRefundsTableFirstCheckbox}
    Click Element    ${btnExportRequest}
    ${ErrorText}   Get Text    ${ErrorModal}
    Log    ${ErrorText}
    Should Contain    ${ErrorText}    1 selected EFT refund request already exported
    Should Contain    ${ErrorText}    Please deselect all records which have an "Exported" status

Decline Requests On Pending Status
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}

    ${random_number} =    Evaluate    random.randint(1, 3)
    Run Keyword If    ${random_number} == 1    Click Element    ${ddlTypeFilterSelfService}
    Run Keyword If    ${random_number} == 2    Click Element    ${ddlTypeFilterRefund}
    Run Keyword If    ${random_number} == 3    Click Element    ${ddlTypeFilterManualOverride}

    Click Element    ${btnApplyFilter}

    Click Element    ${EftRefundsTableFirstCheckbox}
    Click Element    ${EftRefundsTableSecondCheckbox}
    Click Element    ${EftRefundsTableThirdCheckbox}

    ${ExportedOrderID1}  Get Text   ${EftRefundsTableFirstOrder}
    ${ExportedOrderID2}  Get Text   ${EftRefundsTableSecondOrder}
    ${ExportedOrderID3}  Get Text   ${EftRefundsTableThirdOrder}

    Click Element    ${btnDeclineEFTRequests}
    ${DeclineModalText}     Get Text     ${DeclineModal} 
    Should Contain    ${DeclineModalText}    Decline 3 EFT Refund Requests
    Element Should Be Disabled    ${btnConfirmDecline}
    Input Text    ${fldDeclineCancellationReason}    Test Decline UI Automation
    Element Should Be Enabled    ${btnConfirmDecline}
    Click Element    ${btnConfirmDecline}

    ${DeclineConfirmModalText}  Get Text    ${DeclineModal}
    Should Contain    ${DeclineConfirmModalText}    Cancelling 3 EFT Refund Requests
    Should Contain    ${DeclineConfirmModalText}    Successfully processed 3 item(s)
    Click Element    ${CloseDeclineConfirm}

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID1}
    Click Element    ${btnApplyFilter}

    ${ExportedRowStatus}     Get Text  xpath=//table/tbody/tr[1]/td[3]
    Should Contain    ${ExportedRowStatus}     Declined

    ${ExportedRowOperator}     Get Text  xpath=//table/tbody/tr[1]/td[13]
    Should Contain    ${ExportedRowOperator}     Test en-gcs

    Click Element   ${btnClearFilter}

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID2}
    Click Element    ${btnApplyFilter}

    ${ExportedRowStatus}     Get Text  xpath=//table/tbody/tr[1]/td[3]
    Should Contain    ${ExportedRowStatus}     Declined

    ${ExportedRowOperator}     Get Text  xpath=//table/tbody/tr[1]/td[13]
    Should Contain    ${ExportedRowOperator}     Test en-gcs

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID3}
    Click Element    ${btnApplyFilter}

    ${ExportedRowStatus}     Get Text  xpath=//table/tbody/tr[1]/td[3]
    Should Contain    ${ExportedRowStatus}     Declined

    ${ExportedRowOperator}     Get Text  xpath=//table/tbody/tr[1]/td[13]
    Should Contain    ${ExportedRowOperator}     Test en-gcs

Decline Requests On Exported or Declined Status
    Click Element    ${ddlStatusFilter}

    ${random_number} =    Evaluate    random.randint(1, 2)
    Run Keyword If    ${random_number} == 1    Click Element    ${ddlStatusFilterExported}
    Run Keyword If    ${random_number} == 2    Click Element    ${ddlStatusFilterDeclined}

    Click Element    ${btnApplyFilter}
    Click Element    ${EftRefundsTableFirstCheckbox}
    Click Element    ${EftRefundsTableSecondCheckbox}
    Click Element    ${EftRefundsTableThirdCheckbox}

    Click Element    ${btnDeclineEFTRequests}
    Input Text    ${fldDeclineCancellationReason}    Test Decline UI Automation Exported or Declined status
    Click Element    ${btnConfirmDecline}
    ${DeclineConfirmModalFailedText}       Get Text    ${DeclineModal}
    Should Contain    ${DeclineConfirmModalFailedText}    Failed to process 3 item(s)
    Should Contain    ${DeclineConfirmModalFailedText}    EFT Refund request has already been cancelled/exported

Export Request And Download Nedbank File
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterSelfService}
    Click Element    ${btnApplyFilter}

    Click Element    ${EftRefundsTableFirstCheckbox}
    ${ExportedOrderID}  Get Text   ${EftRefundsTableFirstOrder}
    Click Element   ${btnExportRequest}

    Click Element   ${ddlExportBank}
    Click Element   ${ddlNedbank}
    Click Element   ${btnExport}
    Click Element   ${btnExportCloseIcon}

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID}
    Click Element    ${btnApplyFilter}

    Sleep    2s

    ${csvFileName}  Get Text    ${EFTRefundsTableFirstFileText}

    Log     File name =:${csvFileName}
    
    Sleep    2s
    
    Click Element    ${ExportedFileDownloadIcon}

    Sleep    15s

##When running the test locally on your machine uncomment this part, the code will then find the file in your Downloads
#    ${file_path}=    Set Variable    /Users/your_user_name/Downloads/${csvFileName}

#Else use this so that the file is found in the root of the repo when the code runs daily
    ${file_path}=    Set Variable    ${csvFileName}

    File Should Exist    ${file_path}

    ${csv_data}=    csvLibrary.Read Csv File    ${file_path}

    Log    Verifying CSV file contents...

    ${expected_headers} =    Create List
    ...    From account number
    ...    From account name
    ...    My statement description (DR)
    ...    Beneficiary account number
    ...    Beneficiary sub-account number
    ...    Branch code
    ...    Beneficiary name
    ...    Beneficiary statement description (CR)
    ...    Amount
    ...    Notification details

            FOR    ${header}    IN    @{expected_headers}
            List Should Contain Value    ${csv_data}    ${header}
            Log    Headers from Nedbank file:${header}
            END

    Should Contain    ${csv_data}    1004069537
    Should Contain    ${csv_data}    T2 HOME ENTERTAINMENT (PTY) LTD
    Should Contain    ${csv_data}    Takealot.com

Export Request And Download Absa File
    Click Element    ${ddlStatusFilter}
    Click Element    ${ddlStatusFilterPending}
    Click Element    ${ddlTypeFilter}
    Click Element    ${ddlTypeFilterSelfService}
    Click Element    ${btnApplyFilter}

    Click Element    ${EftRefundsTableFirstCheckbox}
    ${ExportedOrderID}  Get Text   ${EftRefundsTableFirstOrder}
    Click Element   ${btnExportRequest}

    Click Element   ${ddlExportBank}
    Click Element   ${ddlAbsa}
    Click Element   ${btnExport}
    Click Element   ${btnExportCloseIcon}

    Click Element   ${btnClearFilter}
    Click Element   ${ddlFilterBy}
    Click Element   ${ddlFilterByOrderID}
    Input Text    ${FilterBySearch}    ${ExportedOrderID}
    Click Element    ${btnApplyFilter}

    Sleep    2s

    ${csvFileName}  Get Text    ${EFTRefundsTableFirstFileText}

    Log     File name =:${csvFileName}

    Sleep    2s

    Click Element    ${ExportedFileDownloadIcon}

    Sleep    15s

##When running the test locally on your machine uncomment this part, the code will then find the file in your Downloads
#    ${file_path}=    Set Variable    /Users/your_user_name/Downloads/${csvFileName}

#Else use this so that the file is found in the root of the repo when the code runs daily
    ${file_path}=    Set Variable    ${csvFileName}

    File Should Exist    ${file_path}

    ${csv_data}=    csvLibrary.Read Csv File    ${file_path}

    Log    Verifying CSV file contents...

    ${expected_headers} =    Create List
    ...    From branch code
    ...    From account number
    ...    From account name
    ...    My statement description (DR)
    ...    Beneficiary account number
    ...    Beneficiary sub-account number
    ...    Branch code
    ...    Beneficiary name
    ...    Beneficiary statement description (CR)
    ...    Amount

            FOR    ${header}    IN    @{expected_headers}
                List Should Contain Value    ${csv_data}    ${header}
                Log    Headers from Absa file:${header}
            END

    Should Contain    ${csv_data}    632005
    Should Contain    ${csv_data}    4098659558
    Should Contain    ${csv_data}    TAKEALOT ONLINE RF PTY LTD
    Should Contain    ${csv_data}    Takealot.com
