*** Variables ***

${addressesAccordion}            xpath=//span[contains(text(),'Addresses')]   //input[@name="customerId"]
${addressGoogleIcon}             xpath=//*[@class="map small icon"]
${allocateCreditBtn}             xpath=//button[contains(text(),'Allocate credit')]
${creditHistoryTable}            xpath=//*[@class="ui small celled compact table"]
${availableCredit}               xpath=//*[@class="ui green small circular horizontal label"]   
${customerCreditAccordion}       xpath=//span[contains(text(),'Customer Credit')]
${customerFullname}              xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/text()[2]
${emailGoogleIcon}               xpath=//*[@class="google icon"]
${emailLogsAccordion}            xpath=//span[contains(text(),'Email Logs')]
${emailCards}                    xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[12]/div/div[1]
${finNotesDropdown}              xpath=//span[contains(text(),'Fin Notes')]
${finNotesEditBtn}               xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/button
${notesDropdown}                 xpath=//span[contains(text(),'Notes')]
${notesEditBtn}                  xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/button
${nameGoogleIcon}                xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/i
${modifiedDate}                  xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]
${refundHistoryAccordion}        xpath=//span[contains(text(),'Refund History')]
${refundHistoryTable}            xpath=//*[@class="ui small celled structured compact table"]
${returnsHistoryAccordion}       xpath=//span[contains(text(),'Returns History')]
${returnsTable}                  xpath=//*[@class="ui small celled table"]   
${registeredDate}                xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]
${verifiedCellphoneIcon}         xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div
${zendeskTicketAccordion}        xpath=//span[contains(text(),'Zendesk Tickets')]
${fraudReasonDDL}                xpath=//div[contains(text(),'Fraud Reason')]
${fraudReasonID}                 xpath=//span[contains(text(),'Returns abuse')]
${finNotes}                      xpath=//input[@name="finNote"]
${submitBlacklistCustomer}       xpath=//button[@class="ui negative right floated button"][contains(text(),'Blacklist')]
${pop-up}                        xpath=//*[@id="noty_layout__topRight"]
${blacklistBtn}                  xpath=//button[contains(text(),'Blacklist Customer')]
${creditAmountTxt}               xpath=//input[@name="amount"]
${creditReasonDDL}               xpath=//div[@name="reason"]
${creditReason}                  xpath=//*[contains(text(),'B2B bulk orders')]   
${adminNotes}                    xpath=//textarea[@name="adminNote"]
${addCreditBtn}                  xpath=//button[@class="ui blue button"]
${okBtn}                         xpath=//button[@class="ui primary button"]
${editCustomerBtn}               xpath=//button[contains(text(),'Customer Info')]
${CustName}                      xpath=//input[@name="customerFirstName"]
${CustSurname}                   xpath=//input[@name="customerSurname"]  
${businessName}                  xpath=//input[@name="businessName"] 
${VATNumber}                     xpath=//input[@name="vatNumber"]
${accStatusDDL}                  xpath=//div[@name="accountStatus"]
${accStatus}                     xpath=//span[text()='suspended']  
${fraudReasonList}               xpath=//div[@name="fraudReasonID"]
${fraudReason}                   xpath=//span[text()='Coupon abuse']  
${staffAccountCheck}             xpath=//label[text()='Staff Account'] 
${blockVouCheck}                 xpath=//label[text()='Block Vouchers'] 
${confirmBtn}                    xpath=//button[contains(text(),'Confirm')]
${emailCustomerBtn}              xpath=//button[contains(text(),'Email Customer')]
${ddlEmailTemplatesDropDown}     xpath=//div[@name="emailTemplate"]
${emailModalCustomerId}          xpath=//input[@name="customerId"]
${emailModalOrderId}             xpath=//input[@name="orderId"]
${emailModalSubject}             xpath=//input[@name="emailSubject"] 
${emailModalBody}                xpath=//textarea[@name="emailBody"] 
${sendEmailBtn}                  xpath=//button[contains(text(),'Send Email')]
${emailLogsAccordion}            xpath=//span[contains(text(),'Email Logs')]
${lastestEmailSent}              xpath=//*[@class="ui fluid card email-card"]/div/div/span/a/span[1]
${addressCards}                  xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/div
${notesAccordion}                xpath=//span[contains(text(),'Notes')]
${noteBtn}                       xpath=//button[contains(text(),'Note')]
${addNotesTextField}             xpath=//textarea[@name="customerNote"] 
${addNoteBtn}                    xpath=//button[contains(text(),'Add Note')]
${noteAddedMessage}              xpath=//*[@class="noty_body"]
${auditLogsIcon}                 xpath=//*[@class="list alternate outline icon link"]
${auditLogResults}               xpath=//*[@class="ui striped basic very compact table"]   
${salesHistoryAccordion}         xpath=//span[contains(text(),'Sales History')]
${salesHistoryTable}             xpath=//*[@class="ui small celled striped compact table"]
${OrderID}                       xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[1]/a 
${OrderIDPg2}                    xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]
${productTitlePg1}               xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a
${productTitlePg2}               xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[6]
${show10ItemsDDL}                xpath=//div[contains(text(),'Show 10 Items')]
${show30ItemsDDL}                xpath=//div[contains(text(),'Show 30 Items')]
${show30OrderItems}              xpath=//span[contains(text(),'30')]
${show10OrderItems}              xpath=//span[contains(text(),'10')]
${orderItemsAccordion}           xpath=//span[contains(text(),'Order Items')]
${orderLink}                     xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[5]/a
${nextPage}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[12]/div/div[2]/a[4]
${prevPage}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[6]/div/div[2]/a[1]
${refundTypeColumn}              xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[9] 
${uploadID}                      xpath=//button[contains(text(),'Upload')]
${uploadField}                   xpath=//input[@type='file'] 
${documentsAccordion}            xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[13]
${removeID}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[14]/div/div/div/div[2]/ol/a[2]
${confirmUpload}                 xpath=//*[@class="ui primary button"]
