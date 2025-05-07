*** Variables ***

${OPTION1_XPATH}    //span[contains(text(),'Identification required: Credit card')]
${OPTION2_XPATH}    //span[contains(text(),'Identification and card details required')]
${OPTION3_XPATH}    //span[contains(text(),'Identification required: Payfast & Ozow')]
${OPTION4_XPATH}    //span[contains(text(),'Identification not accepted')]
${OPTION5_XPATH}    //span[contains(text(),'Identification not received: Payfast & Ozow')]
${OPTION6_XPATH}    //span[contains(text(),'Identification not received: Credit card')]
${OPTION7_XPATH}    //span[contains(text(),'Credit card refund failed')]
${OPTION8_XPATH}    //span[contains(text(),'EFT refund failed')]
${OPTION9_XPATH}    //span[contains(text(),'Refund delayed')]
${OPTION10_XPATH}   //span[contains(text(),'Short paid')]
${OPTION11_XPATH}   //span[contains(text(),'Deposit Match')]
${OPTION12_XPATH}   //span[contains(text(),'Duplicate Payment')]
${OPTION13_XPATH}   //span[contains(text(),'Voucher Payment')]
${OPTION14_XPATH}   //span[contains(text(),'Generic')]
${random_number}    Evaluate    random.randint(1, 14)

${btnMenu}      xpath=//body/div[@id='root']/div[2]/a[1]/i[1]
${btnEftRefundMenu}     xpath=//body/div[@id='root']/div[1]/a[6]
${EFTRefundsTable}  xpath=//table
${btnSendEmailTable}    xpath=//table/tfoot/tr/th/div/div[3]/button
${ddlEmailTemplates}   xpath=//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]
${btnSendEmail}     xpath=//button[contains(text(),'Send Emails')]
${EmailSentModal}    xpath=/html/body/div[2]/div


${EmailSentModal_Close_icon}     xpath=//body/div[2]/div[1]/i[1]

${btnManualEFT}     xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[6]/div/button
${txtOrderId}   xpath=//input[@name="orderID" and @placeholder="Enter Order ID" and @type="text"]
${txtZendeskTicket}  xpath=//input[@name="zendeskTicket" and @placeholder="Enter Zendesk Ticket Number" and @type="text"]
${txtCustomerName}  xpath=//input[@name="customerName" and @placeholder="Enter Customer Name" and @type="text"]
${txtRefundAmountManualEft}  xpath=//input[@name="refundAmount" and @placeholder="Enter Refund Amount" and @type="text"]
${txtBankAccountManualEFT}  xpath=//input[@name="bankAccount" and @placeholder="Enter Bank Account Number" and @type="text"]
${ddlBankNameManualEFT}  xpath=//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[6]/div[2]/div[1]/div[1]
${ddlBranchNameManualEFT}  xpath=//div[@name="branchCode"]
${btnSubmitManualEFT}  xpath=/html/body/div[2]/div/div[2]/div/form/div/div[8]/div/div/div[1]/button
${ddlBankNameManualEFTFNBNamibia}  xpath=/html/body/div[2]/div/div[2]/div/form/div/div[6]/div[2]/div/div/div[2]
${ddlBranchNameManualEFTAllNamibia}  xpath=/html/body/div[2]/div/div[2]/div/form/div/div[7]/div[2]/div/div/div[2]/div
${ConfirmationHeaderManualEFT}  xpath=//div[contains(text(),'Credit Deduction')]
${ConfirmationTextManualEFT}  xpath=//div[contains(text(),"Don't forget to remove credit.")]
${btnOkayManualEFT}  xpath=//button[contains(text(),'Okay')]
${SuccessManualEFT}  xpath=//div[contains(text(),'EFT Refund Created Successfully.')]

${link_text}=    Get Text    xpath=//tbody/tr[1]/td[6]/a[1]
${expected_url}=   Set Variable    https://fin-portal.master.env/order/${link_text}

${ddlStatusFilter}  xpath=//div[contains(text(),'Select refund status')]
${ddlClearStatusFilter}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[1]/div/div/i
${ddlStatusFilterPending}   xpath=//span[contains(text(),'Pending')]
${ddlStatusFilterExported}  xpath=//span[contains(text(),'Exported')]
${ddlStatusFilterDeclined}  xpath=//span[contains(text(),'Declined')]

${btnApplyFilter}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[1]/button
${btnClearFilter}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[2]/button

${ddlTypeFilter}  xpath=//div[contains(text(),'Select refund type')]
${ddlClearTypeFilter}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[2]/div/div/i
${ddlTypeFilterSelfService}  xpath=//span[contains(text(),'Self Service')]
${ddlTypeFilterRefund}  xpath=//span[contains(text(),'Refund')]
${ddlTypeFilterManualOverride}  xpath=//span[contains(text(),'Manual Override')]
${ddlTypeFilterManualEFT}  xpath=//span[contains(text(),'Manual EFT')]

${ddlFilterBy}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/div
${ddlFilterByCustomerID}  xpath=//span[contains(text(),'Customer ID')]
${CustomerName}  xpath=//table/tbody/tr/td[8]/a
${FilterBySearch}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/input
${customerinfo}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span
${ddlFilterByOrderID}  xpath=//span[contains(text(),'Order ID')]
${orderIDEFTRefundstable2}  xpath=//table/tbody/tr/td[6]
${orderIDEFTRefundstable1}  //table/tbody/tr[15]/td[6]
${ddlFilterByBankAccountNumber}  xpath=//span[contains(text(),'Bank Account Number')]
${bankaccEFTRefundstable}  xpath=//table/tbody/tr/td[10]
${ddlFilterByZendeskTicketNumber}  xpath=//span[contains(text(),'Zendesk Ticket Number')]
${zendeskticketEFTRefundstable}  xpath=//table/tbody/tr/td[7]
${ddlShow250Items}  xpath=//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[6]

${chkDateRangeToday}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[1]/div[1]/div/label
${ddlDateRange}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[2]/div/div/input
${fldDateCreated}  Xpath=//table/tbody/tr[1]/td[4]
${ddlShowItems}  xpath=//div[contains(text(),'Show 15 Items')]
${ddlShow30Items}  xpath=//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[3]
${LastPage}  xpath=//table/tfoot/tr/th/div/div[5]/div[2]/a[7]

${orderid_link_text}   xpath=//tbody/tr[1]/td[6]/a[1]

${EftRefundsTableFirstCheckbox}   xpath=//table/tbody/tr[1]/td[1]/div
${EftRefundsTableSecondCheckbox}    xpath=//table/tbody/tr[2]/td[1]/div
${EftRefundsTableThirdCheckbox}     xpath=//table/tbody/tr[3]/td[1]/div
${EftRefundsTableFirstOrder}    xpath=//table/tbody/tr[1]/td[6]/a
${EftRefundsTableSecondOrder}   xpath=//table/tbody/tr[2]/td[6]/a
${EftRefundsTableThirdOrder}    xpath=//table/tbody/tr[3]/td[6]/a

${btnExportRequest}     xpath=//table/tfoot/tr/th/div/div[1]/button
${ExportModal}  xpath=/html/body/div[2]/div/div[1]
${ErrorModal}   xpath=/html/body/div[2]/div/div[2]/div/div/div
${ddlExportBank}   xpath=/html/body/div[2]/div/div[2]/div/form/div[1]/div
${ddlNedbank}   xpath=/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[1]/span
${ddlAbsa}      xpath=/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[2]/span
${btnExport}   xpath=/html/body/div[2]/div/div[2]/div/form/div[2]/button[2]
${ExportStatus}     xpath=/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]
${btnExportCloseIcon}   xpath=/html/body/div[2]/div/i

${btnDeclineEFTRequests}    xpath=//table/tfoot/tr/th/div/div[2]/button
${DeclineModal}    xpath=/html/body/div[2]/div
${btnConfirmDecline}    xpath=/html/body/div[2]/div/div[2]/div/form/div[2]/button[1]
${fldDeclineCancellationReason}     xpath=/html/body/div[2]/div/div[2]/div/form/div[1]/div/input
${DeclineConfirmModal}      xpath=/html/body/div[2]/div/div[1]
${DeclineConfirmModalSuccess}   xpath=/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div
${CloseDeclineConfirm}  xpath=/html/body/div[2]/div/i
${DeclineText}  xpath=/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/p/span[1]/text()[3]
${rowitem}        xpath=//table/tbody/tr[rownum]/td[3]

${ExportedFileDownloadIcon}    xpath=//table/tbody/tr/td[12]/a/i
${EFTRefundsTableFirstFileText}    xpath=//table/tbody/tr/td[12]/a