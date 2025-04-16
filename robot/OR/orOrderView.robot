*** Variables ***

${addNotesBtn}                   xpath=//button[@class="ui mini primary right floated button"]  
${confirmAddBtn}                 xpath=//button[@class="ui blue right floated button"]
${noteDD}                        xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/span
${notesTxtField}                 xpath=//textarea[@name="customerNote"]
${noteConfirmMessage}            xpath=//*[@id="noty_layout__topRight"]
${blacklistCustBtn}              xpath=//button[contains(text(),'Blacklist Customer')]
${fraudReasonList}               xpath=//div[contains(text(),'Fraud Reason')]
${fraudReasonSelection}          xpath=//span[contains(text(),'Returns abuse')]
${finNote}                       xpath=//input[@name="finNote"]
${confirmBlacklist}              xpath=//button[@class="ui negative right floated button"][contains(text(),'Blacklist')]
${confirmWhitelist}              xpath=//button[@class="ui blue right floated button"][contains(text(),'Confirm')]
${whitelistCustBtn}              xpath=//button[contains(text(),'Whitelist Customer')]
${cancelAllItemBtn}              xpath=//button[contains(text(),'Cancel All Items')]
${cancellationReason}            xpath=//*[@name="reasonTypeID"]
${customerRequestCancelReason}   xpath=//span[contains(text(),'Customer request')]
${confirmCancellingBtn}          xpath=//button[contains(text(),'Confirm Cancelling')]
${closeCancelModal}              xpath=//*[@class="close icon"]
${orderStatus}                   xpath=//div[@class="ten wide column label-container"]/span/div[1]
${emailCustomer}                 xpath=//button[contains(text(),'Email Customer')]
${emailTemplateSelection}        xpath=//span[contains(text(),'Identification not accepted')]
${emailTemplateDDL}              xpath=//*[@name="emailTemplate"]
${customerID}                    xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]
${markAsRiskyBtn}                xpath=//button[contains(text(),'Mark as risky')]
${markAsRiskyReason}             xpath=//input[@name="reason"]
${addReasonBtn}                  xpath=//button[contains(text(),'Add Reason')]
${flaggedAsRisk}                 xpath=//div[@class="ui red basic label"]
${orderEllipsisMenu}             xpath=//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']
${auditLogMenuOption}            xpath=//*[contains(text(),'Audit log')]
${auditLogActionType}            xpath=//*[@class='ui striped basic very compact table']/tbody/tr/td[3]
${auditLogOrderData}             xpath//*[@class='ui striped basic very compact table']/tbody/tr/td[5]
${authoriseNowBtn}               xpath=//button[contains(text(),'Authorise Now')]
${authoriseNowModalMessage}      xpath=//div[@class="ui success message"]/div/div
${authoriseNowModalCloseIcon}    xpath=//i[@class="close icon"]
${orderFullfilmentAccordion}     xpath=//*[contains(text(),'Order Fulfillment')]
${orderTrackingHeading}          xpath=//h5[@class="ui header"]
${orderTrackingUserInfo}         xpath=//div[@class="ui info message"]/div[1]
${eventLogResults}               xpath=//*[@class="ui red celled padded table"] 
${orderEventsMenu}               xpath=//*[contains(text(),'Order events')]
${firstPaymentMethodBadge}       xpath=//div[@class="ui blue basic label"]
${secondPaymentMethodBadge}      xpath=//div[@class="ui orange basic label"]
${orderNotesAccordion}           xpath=//div[@class='ten wide column']//span[text()='Notes']
${orderNotesBtn}                 xpath=//button[@class='ui mini icon primary right floated button']
${orderNotesTextField}           xpath=//textarea[@name="orderNote"]
${addNotesConfirmBtn}            xpath=//button[@class="ui primary button"]
${customerNotesAccordion}        xpath=//div[@class='six wide column']//span[text()='Notes']
${addCustomerNotesBtn}           xpath=//button[@class='ui mini primary right floated button']
${customerNotesTextField}        xpath=//textarea[@name="customerNote"]
${addCustomerNotesConfirmBtn}    xpath=//button[@class="ui blue right floated button"]
${finNotesAccordion}             xpath=//div[@class='six wide column']//span[text()='Notes']
${addFinNotesBtn}                xpath=//button[@class='ui mini primary right floated button']
${finNotesTextField}             xpath=//textarea[@name="customerNote"]
${addFinNotesConfirmBtn}         xpath=//button[@class="ui blue right floated button"]
${cancelSelectedItemBtn}         xpath=//button[contains(text(),'Cancel Selected Items')]
${selectItemCheckbox}            xpath=//div[@class="ui fitted checkbox"]
${cancellationResults}           xpath=//*[@class='ui celled striped table']/tbody/tr/td[2]
${paymentLedgerAccordion}        xpath=//div[@class='ten wide column']//*[text()='Payment Ledger']
${paymentLedgerfirstProvder}     xpath=//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='2']
${paymentLedgersecondProvder}    xpath=//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='3']
${paymentLedgerPaidTotalAmount}  xpath=//tfoot/tr[@class='center aligned']/th[2]
${bookmarkIcon}                  xpath=//*[@class='grey bookmark outline link icon']
${bookmarkNotes}                 xpath=//textarea[@placeholder="Notes..."]
${bookmarkCounter}               xpath=//*[@class='ui teal mini circular floating label label-on-corner']
${bookmarksPage}                 xpath=//*[@class='grey bookmark outline large icon']
${closeModal}                    xpath=//*[@class='close icon']
${confirmationMsg}               xpath=//*[@class='ui message']
${doneButton}                    xpath=//button[@class='ui primary right floated button']
${removeBookmarksCheckbox}       xpath=//*[@class='ui fitted checkbox']
${removeBtn}                     xpath=//button[@class='ui mini icon negative right floated button']
${progressBar}                   xpath=//*[@class='ui green progress']
${orderFinancialsAccordion}      xpath=//div[@class='ten wide column']//*[text()='Order Financials']
${totalOrderItemsAmount}         xpath=//tbody/tr/td[text()='Total Order Items']/following-sibling::*[1]/div
${shippingAmount}                xpath=//tbody/tr/td[text()='Shipping']/following-sibling::*[1]/div
${subTotalAmount}                xpath=//tbody/tr/td[text()='Sub-Total']/following-sibling::*[1]/div
${discountAmount}                xpath=//tbody/tr/td[text()='Discount']/following-sibling::*[1]/div
${orderTotalAmount}              xpath=//tbody/tr/td[text()='Order Total']/following-sibling::*[1]/div
${logsTable}                     xpath=//*[@class='ui striped basic very compact table']
${custAccNumber}                 xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]
${order-id}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]
${orderDate}                     xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[3]/div[1]
${authStatus}                    xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[1]
${authDate}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[3]
${waybillMenuOption}             xpath=//*[contains(text(),'Waybill log')]
${orderComments}                 xpath=//*[@class="ui mini comments"]
${closeIcon}                     xpath=//*[@class="close icon]
${custInfoPop-up}                xpath=//*[@class="ui bottom center basic popup transition visible"]
${custStatus}                    xpath=//*[@class="ui green mini basic label"]
${totalPaidAmount}               xpath=//tbody/tr/td[text()='Total Paid']/following-sibling::*[1]/div
${csCloseIcon}                   xpath=/html/body/div[2]/div/i
${csSearchTxt}                   xpath=//*[@id="app"]/div/div[1]/div[1]/div/input[1]
${csSearchBtn}                   xpath=//*[@id="app"]/div/div[1]/div[1]/div/button
${RRN}                           xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[7]/div[2]/a
${editOrderItemMenu}             xpath=//*[@class="blue write square large icon"]
${updateStatusMenuOption}        xpath=//*[contains(text(),'Update to shipped')]
${updateToShippedButton}         xpath=//button[@class="ui blue button"][contains(text(),'Update to shipped')]
${shippedTag}                    xpath=//div[@class="ui green tiny label"][contains(text(),'Shipped')]
${returnCanceledTag}             xpath=//div[@class="ui red tiny label"][contains(text(),'Return Canceled')]
${paymentLedgerAccordion}        xpath=//div[@class='ten wide column']//*[text()='Payment Ledger']
${paymentLedgerPaymentProvider}  xpath=//*[@class="ui celled fixed structured table"]/tbody/tr[1]/td[1]
${emailLogsAccordion}            xpath=//div[@class='ten wide column']//*[text()='Email Logs']
${viewEmailBtn}                  xpath=//*[@class='blue mail outline icon']
${emailView}                     xpath=//*[@class='ui scrolling modal transition visible active']
${orderItemStatus}               xpath=//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[1]
${orderItemCanceledBy}           xpath=//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[3]/div/p[3]
${orderItemsShowItems}           xpath=//div[@class='ui compact item dropdown']
${orderItemsPaginationPageTwo}   xpath=//*[@aria-label='Pagination Navigation']/a[3]
${couponHistoryAccordion}        xpath=//*[text()='Coupon History']
${couponCode}                    xpath=//div[text()='UAFORHER']
${signedBy}                      xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/p
${instructionDroppedDatetime}    xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div
${shippedFromWarehouseDatetime}  xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div
${deliveredToCustomerDatetime}   xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div
${waybillNo}                     xpath=/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]
${courier}                       xpath=/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]
${parcelBlock}                   xpath=/html/body/div[2]/div/div[2]/div/div/div[1]/div/a/div
${parcel}                        xpath=/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/span/a
${orderItem}                     xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a
${deliveredTag}                  xpath=//div[@class="ui green tiny label"][contains(text(),'Delivered')]
${TrackBtn}                      xpath=//button[@class='ui blue small button']
${estimatedCollectionDate}       xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/h5
${waybillEstimateCollectionDate}  xpath=/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]
${collectionEstimate}             xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div/span
${refundHistoryAccordion}        xpath=//*[text()='Refund History']
${refundedAmount}                xpath=//td[contains(text(),'RFN-pg3x-45rz')]/following-sibling::td[1]/div[2]/div
${refundedPaymentMethod}         xpath=//td[contains(text(),'RFN-pg3x-45rz')]/following::td[3]
${streetAddress}                 xpath=//div[@class="column"][contains(text(),'6 Birkenhead Road')]
${suburbAddress}                 xpath=//div[@class="column"][contains(text(),'Umbilo')]
${cityAddress}                   xpath=//div[@class="column"][contains(text(),'Berea')]
${provinceAddress}               xpath=//div[@class="column"][contains(text(),'KwaZulu-Natal')]
${codeAddress}                   xpath=//div[@class="column"][contains(text(),'4075')]
${copyAddressBtn}                xpath=//button[@class='ui blue mini right floated button']
${addressCopiedBtn}              xpath=//button[@class='ui green mini right floated button']
${residentialTxt}                xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div[1]
${searchGoogleIcon}              xpath=//div[@class='header customer-card-header']//i[@class='google icon']
${shippingMethod}                xpath=(//table[@class='ui small unstackable basic very compact table']//td[text()='Courier'])[1]
${shippingPlan}                  xpath=(//table[@class='ui small unstackable basic very compact table']//td[text()='Standard'])[1]
${shippingCourier}               xpath=(//table[@class='ui small unstackable basic very compact table']//td[text()='MDX133806010 - Takealot Delivery Team'])[1]
${shippingPromisedDate}          xpath=(//table[@class='ui small unstackable basic very compact table']//td[text()='28 Aug 2024'])[1]
${shippingDeliveredDate}         xpath=(//table[@class='ui small unstackable basic very compact table']//td[text()='30 Aug 2024'])[1]
${instructionDroppedDate1}       xpath=(//div[text()='27 May 2024 @ 17:46'])[1]
${instructionDroppedDate2}       xpath=(//div[text()='27 May 2024 @ 0:34'])
${shippedFromWarehouseDate1}     xpath=(//div[text()='28 May 2024 @ 1:31'])
${shippedFromWarehouseDate2}     xpath=(//div[text()='27 May 2024 @ 17:46'])[2]
${deliveredDate1}                xpath=(//div[text()='30 May 2024 @ 11:40'])
${deliveredDate2}                xpath=(//div[text()='29 May 2024 @ 10:58'])
${orderTrackingHeading1}         xpath=(//*[text()='Delivered Thu, 30 May 2024'])
${orderTrackingHeading2}         xpath=(//*[text()='Delivered Wed, 29 May 2024'])
${signedBy1}                     xpath=(//*[text()='Signed by: Slindile Mncwango (Customer)'])
${signedBy2}                     xpath=(//*[text()='Signed by Slindile Mncwango'])
${waybillNumber1}                xpath=(//*[text()='MDX127668689'])
${waybillNumber2}                xpath=(//*[text()='MDX127583371'])
${waybillNumberLink}             xpath=(//*[text()='MDX133806010'])
${mrDexpressCopyright}           xpath=//*[@class="popup ui-dialog-content ui-widget-content"]
${orderTrackingFirstConsignment}    xpath=//div[@class='ui segment instruction-container'][1]
${firstConsigmentDeliveredDate}  xpath=//div[@class='ui segment instruction-container'][1]/div[1]/div/h5
${firstConsigmentSignedBy}       xpath=//div[@class='ui segment instruction-container'][1]/div[1]/div/p
${firstConsigmentWaybillNumber}  xpath=//div[@class='ui segment instruction-container'][1]/div[2]/div/div[1]/span/a
${cancelledItems}                xpath=(//*[text()='Cancelled Item(s)'])
${cancelledTag}                  xpath=//div[@class="ui red tiny label"][contains(text(),'Canceled')]
${partDeliveredDate}             xpath=(//*[text()='Delivered Mon, 19 Sep 2022'])   
${ipAddressIcon}                 xpath=//*[@class="question circle outline icon link"]   
${ipAddress}                     xpath=//input[@name="ipAddress"]
${ipAddressModel}                xpath=//*[@class="ui tiny modal transition visible active"]
${custNamePopup}                 xpath=//table[@class='ui small unstackable very basic very compact table']//td[text()='Slindile Mncwango']
${custDateRegistered}            xpath=//table[@class='ui small unstackable very basic very compact table']//td[text()='16-Oct-2018 @ 10:41']
${custBlacklistStatus}           xpath=//div[@class="ui green basic label"][contains(text(),'Not Blacklisted')]
${firstConsigmentTrackBtn}       xpath=//div[@class='ui segment instruction-container'][1]/div[1]/button
${trackingWaybillNumber}         xpath=//strong[text()='Waybill No: ']/following-sibling::*[1]
${trackingFirstParcelInfo}       xpath=//div[@class='ui fluid vertical tabular menu']/a[1]
${trackingFirstParcelNumber}     xpath=//div[@class='ui fluid vertical tabular menu']/a[1]/div/div/strong
${trackingFirstParcelItem}       xpath=//div[@class='stretched twelve wide computer sixteen wide mobile twelve wide tablet column']//*[@class='content']/span
${orderListMenuOption}           xpath=//*[contains(text(),'Order List')]
${orderListTable}                xpath=//table[@class='ui small celled compact table']//tbody//tr
${btnMenu}                       xpath=//i[@class='content large icon' and @aria-hidden='true']
${orderListClearFilterButton}    xpath=//button[contains(text(), 'Clear Filter')]
${past10DaysDateRangeCheckbox}   xpath=//label[text()='Past 10 Days']
${orderListFirstNewStatusOrder}  xpath=//tr[td[9]/div[contains(text(), 'New Order')]][1]//td[2]/a
${collectionEstimateDate}        xpath=//div[@class='ui segment instruction-container']//h5
${collectionNotYetReadyMessage}  xpath=//div[@class='ui segment instruction-container']//div/span

${deliveryEstimateDate}          xpath=//div[@class='ui segment instruction-container']//h5
${deliveryNotYetReadyMessage}    xpath=//div[@class='ui segment instruction-container']//div/span