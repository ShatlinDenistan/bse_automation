*** Variables ***

${applySearchFilter}              xpath=//button[contains(text(), 'Filter')]
${AllOrderPaidColumns}            xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 7)]
${AllOrderStatusColumns}          xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]
${clearFilter}                    xpath=//button[contains(text(), 'Clear Filter')]
${notPaidBtn}                     xpath=//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[5]/button
${closeIcon}                      xpath=//i[@aria-hidden="true" and @class="close icon"] 
${expireBtn}                      xpath=//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[3]/button
${menuBtn}                        xpath=//i[@aria-hidden="true" and @class="content large icon"]
${orderIDCheckBox}                xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div
${paidStatusDropdown}             xpath=//*[@id="root"]/div[3]/div/div/div/form/div/div/div[5]/div/div
${paidBtn}                        xpath=//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[4]/button
${paidStatusOption}               xpath=//span[text()='Paid']
${notPaidStatusOption}             xpath=//span[text()='Not Paid']
${resultsTable}                   xpath=//*[@class="ui small celled compact table"]
${redeemedStatusDropdown}         xpath=//*[@id="root"]/div[3]/div/div/div/form/div/div/div[4]/div/div/div[1]
${redeemedStatusAvailable}        xpath=//span[text()='Available']
${verificationMessage}            xpath=//div[contains(text(),'Successfully processed 1 item(s)')]
${vouchersMenuOption}             xpath=//body/div[@id='root']/div[1]/a[2]
${redeemedStatusCancelled}        xpath=//span[text()='Cancelled']
${activeBtn}                      xpath=//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[2]/button
${activeVoucherBtn}               xpath=//html/body/div[2]/div/div[2]/div/div[2]
${verifyActivatedVoucher}         xpath=//div[contains(text(),'Successfully processed 1 item(s)')]
${voucherCode}                    xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[6]/a
${filterByField}                  xpath=//div[@name='searchCriteria']
${filterByVoucherCode}            xpath=//span[contains(text(), 'Voucher Code')]
${searchTermField}                xpath=//*[@name='searchTerm']
${voucherStatus}                  xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[10]/div
${paidStatus}                     xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[8]/div
${voucherCategoryDropdown}        xpath=//*[@id="root"]/div[3]/div/div/div/form/div/div/div[3]/div
${voucherCategoryCV}              xpath=//span[contains(text(), 'Corporate Voucher')]
${voucherCategoryList}            xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 4)]
${redeemedStatusDropdown}         xpath=//*[@id="root"]/div[3]/div/div/div/form/div/div/div[4]/div/div
${redeemedStatusCancelled}        xpath=//span[contains(text(), 'Cancelled')]
${redeemedStatusList}             xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]
${voucherOrderID}                 xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]
${searchCriteriaOptionOrderID}    xpath=//span[contains(text(), 'Order ID')]
${voucherCodeID}                  xpath=//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 5)]
${redeemedStatusRedeemed}         xpath=//span[text()='Redeemed']
${filterByCustomerID}             xpath=//span[contains(text(), 'Customer ID')]
${openCustomerInfo}               xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[4]/a
${openUsedByCustomerInfo}         xpath=//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[12]/a
${filterByUsedByCustomerID}       xpath=//span[contains(text(), 'Used By Customer ID')]
${customerinfoID}                 xpath=//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span
${emailBtn}                       xpath=//*[@class="mail icon"]
${emailSentModal}                 xpath=/html/body/div[2]/div
${emailSentModalCloseIcon}        xpath=//body/div[2]/div[1]/i[1]