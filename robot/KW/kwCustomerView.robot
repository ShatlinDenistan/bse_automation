*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orCustomerView.robot

*** Keywords ***

Verify Customer Details
    Wait Until Page Contains    Brian Delta  
    Click Element     ${nameGoogleIcon}
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    Wait Until Page Contains    dev+1@take2.co.za 
    Click Element     ${emailGoogleIcon}
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    Element Should Be Visible   ${verifiedCellphoneIcon} 

Verify Notes Section with Edit Option
    Wait Until Page Contains Element    ${notesDropdown}
    Click Element   ${notesDropdown}
    Element Should Be Visible    ${notesEditBtn}
    Click Element    ${notesEditBtn}

Verify Fin Notes Section with Edit Option
    Wait Until Page Contains Element   ${finNotesDropdown}
    Click Element   ${finNotesDropdown}
    Element Should Be Visible    ${finNotesEditBtn}
    Click Element    ${finNotesEditBtn}

Verify Customer Credit 
    Wait Until Element Is Visible    ${customerCreditAccordion}
    Element Should Be Visible        ${availableCredit}     
    Element Should Be Visible        ${allocateCreditBtn}
    Element Should Be Visible        ${allocateCreditBtn}
    Element Should Be Visible        ${creditHistoryTable}

Verify Customer Address 
    Wait Until Element Is Visible   ${addressesAccordion}
    Click Element      ${addressesAccordion}
    ${addresses}    Get WebElements  ${addressCards} 
        FOR    ${element}    IN     ${addresses}  
            Element Should Be Visible    ${addressGoogleIcon}
            Click Element     ${addressGoogleIcon}
            Sleep    2s
            @{WindowHandles}=   Get Window Handles
            Sleep    2s
            WebAutomationFramework.Switch Window    ${WindowHandles}[0]
        END

Verify Email Logs
    Wait Until Element Is Visible    ${emailLogsAccordion} 
    Click Element     ${emailLogsAccordion} 
    Element Should Be Visible     ${emailCards} 

Verify Customer Returns History
    Wait Until Element Is Visible    ${customerCreditAccordion}
    Click Element                    ${customerCreditAccordion} 
    Wait Until Element Is Visible    ${returnsHistoryAccordion} 
    Click Element                    ${returnsHistoryAccordion} 
    Element Should Be Visible        ${returnsTable} 

Verify Zendesk Tickets 
    Wait Until Element Is Visible    ${zendeskTicketAccordion} 
    Click Element      ${zendeskTicketAccordion} 

Verify Registered And Last Modified Dates 
    Element Should Be Visible     ${registeredDate} 
    Element Should Be Visible   ${modifiedDate} 

Blacklist A Customer
   Wait Until Element Is Visible    ${blacklistBtn}  
   Click Element     ${blacklistBtn} 
   Click Element     ${fraudReasonDDL} 
   Click Element     ${fraudReasonID} 
   Input Text    ${finNotes}      Automation Testing
   Click Element  ${submitBlacklistCustomer} 
   Handle Alert   Accept
   Wait until element is visible  ${pop-up} 
   ${message}=  Get text  ${pop-up} 
   Should be equal  ${message}  Successfully blacklisted the customer\n×

Add Credit
    Click Element                    ${allocateCreditBtn} 
    Sleep    ${SLEEP}
    Click Element                    ${creditReasonDDL}
    Click Element                    ${creditReason}
    ${CreditAmount}=     Generate Random String        3     123456789
    Set Global Variable    ${CreditAmount}
    Input Text    ${creditAmountTxt}    ${CreditAmount}
    Input Text    ${adminNotes}     Good will
    Click Element    ${addCreditBtn}                
    Click Element    ${okBtn}                        
    Wait until element is visible  ${pop-up} 
    ${message}=  Get text  ${pop-up} 
    Should be equal  ${message}  Successfully credited user\n×

Edit Customer
    Click Element    ${editCustomerBtn}            
    Input Text       ${CustName}   Mike
    Input Text       ${CustSurname}  Jackson
    Input Text       ${businessName}   Automation Test PTY LTD
    Input Text       ${VATNumber}     9876543211
    Click Element    ${accStatusDDL}
    Click Element    ${accStatus}             
    Click Element    ${fraudReasonList}   
    Click Element    ${fraudReason}   
    Click Element    ${staffAccountCheck}     
    Click Element    ${blockVouCheck}  
    Click Element    ${confirmBtn}                                
    Wait until element is visible  ${pop-up} 
    ${message}=  Get text  ${pop-up} 
    Should be equal  ${message}  Customer status data updated successfully\n×


Send Generic Email
    Click Element    ${emailCustomerBtn}
    Wait Until Element Is Enabled    ${ddlEmailTemplates}
    Press Keys    ${emailModalCustomerId}    TAB
    Press Keys    ${emailModalorderId}    TAB
    Sleep    1s
    Press Keys    ${ddlEmailTemplates}    TAB
    ${subjectText}    Set Variable    Automation Test Email Subject
    Input Text    ${emailModalSubject}    ${subjectText}
    Input Text    ${emailModalBody}    Automation Test Email Subject 123 %*$&
    Scroll Element Into View    ${sendEmailBtn}
    Click Element    ${sendEmailBtn}

View Email Logs For Latest Email Sent
    Reload Page
    Wait Until Element Is Visible    ${emailLogsAccordion}
    Click Element    ${emailLogsAccordion}
    ${lastEmailSubjectText}=    Get text  ${lastestEmailSent} 
    Should be equal  ${lastEmailSubjectText}  Automation Test Email Subject
   

Add Admin Note
    Wait Until Element Is Visible    ${notesAccordion}
    Click Element    ${notesAccordion}
    Click Element    ${noteBtn}
    Input Text       ${addNotesTextField}    Automation Admin Note
    Click Element    ${addNoteBtn}
    Wait until element is visible  ${noteAddedMessage}
    ${addMoteMessageText}=  Get text  ${noteAddedMessage}
    Should Contain  ${addMoteMessageText}  Note successfully added to Customer

View Audit Logs
    Wait Until Element Is Visible    ${auditLogsIcon}
    Click Element   ${auditLogsIcon}
    Element Should Be Visible     ${auditLogResults} 

Verify Order Link
    Wait Until Element Is Visible    ${customerCreditAccordion} 
    Click Element      ${customerCreditAccordion}
    Click Element      ${salesHistoryAccordion} 
    ${orderID1}  Get Text   ${OrderID}
    Click Element      ${OrderID}
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${orderID2}  Get Text  ${OrderIDPg2}  
    Should Be Equal As Strings    ${orderID1}   ${OrderID2}  

Verify Product Title
   ${productTitle1}  Get Text  ${productTitlePg1}
   @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    ${productTitle2}  Get Text  ${productTitlePg2} 
    Should Be Equal As Strings    ${productTitle1}   ${productTitle2}

Verify Refund History
    Click Element                    ${customerCreditAccordion} 
    Click Element                    ${refundHistoryAccordion} 
    Element Should Be Visible        ${refundHistoryTable} 
    Click Element                    ${orderLink}

Click Paging Button
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    Wait Until Element Is Visible    ${orderItemsAccordion}
    Scroll To Element                ${show10ItemsDDL}
    Click Element                    ${show10ItemsDDL}
    Click Element                    ${show30OrderItems}
    Scroll To Element                ${show30ItemsDDL}   
    Click Element                    ${show30ItemsDDL} 
    Click Element                    ${Show10OrderItems}  
    
Click Items Per Page  
    Scroll To Element               ${show10ItemsDDL}
    Click Element                   ${nextPage} 
    Click Element                   ${prevPage}

Verify SSR History
    Click Element                    ${customerCreditAccordion} 
    Click Element                    ${refundHistoryAccordion} 
    Wait Until Element Is Visible    ${refundHistoryTable}   ${MAX_TIMEOUT} 
    ${RefundType}    Get WebElements  ${refundTypeColumn}  
    ${found}    Set Variable    False
    FOR    ${element}    IN    ${RefundType}
    ${text}    Get Text    ${element}
    Run Keyword If    '${text}' == 'SelfService'    Set Test Variable    ${found}    True
    Exit For Loop If    '${found}' == 'True'
    END
    Run Keyword If    '${found}' == 'False'    Fail    'Self Service Refund not found'

Upload Valid ID Doc
    [Arguments]    ${csv_file}
    Scroll To Element        ${documentsAccordion}       
    Click Element    ${documentsAccordion} 
    Choose File    ${uploadField}    ${csv_file}
    Click Element    ${uploadID} 
    Sleep    5
    Element Should Be Visible       ${pop-up}

Remove ID Doc
    Click Element   ${removeID} 
    Click Button    ${confirmUpload}  