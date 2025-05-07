*** Variables ***


# PLP
${btnCustomerCudion}                xpath=//span[contains(text(),'Customer Credit')]
${btnCredit}                        xpath=//*[contains(text(),'Allocate credit')]
${txtCreditAmount}                  xpath=//input[@name="amount"]
${txtCreditComments}                xpath=//textarea[@name="adminNote"]
${dropdownCreditReason}             xpath=//*[@name="reason"]
${reasonGoodwill}                   xpath=//*[@role='option']/span[contains(text(),'Goodwill')]
${reasonLateDeliveryFee}            xpath=//*[@role='option']/span[contains(text(),'Late delivery fee')]
${validationError}                  xpath=//*[@class='ui negative message']/div/div
${reasonSubLateDelivery}            xpath=//*[@role='option']/span[contains(text(),'Subscription late delivery fee')]
${reasonCreditBreach}               xpath=//*[@role='option']/span[contains(text(),'Credit breach')]
${txtJiraNumber}                    xpath=//input[@name="extra"]
${reasonB2bBulkOrder}               xpath=//*[@role='option']/span[contains(text(),'B2B bulk orders')]
${reasonFailedEFTRefunds}           xpath=//*[@role='option']/span[contains(text(),'Failed EFT refunds')]
${accordionOrderItems}              xpath=//span[contains(text(),'Order Items')]
${btnOrderItemMenu}                 xpath=//div[@class='accordion ui']//*[@class='ui simple dropdown']/i
${creditItemOption}                 xpath=//*[contains(text(),'Credit Item')]
${reasonSystemError}                xpath=//*[@role='option']/span[contains(text(),'System error: Credit removal failed')]
${txtRFNNumber}                     xpath=//*[@placeholder="Please enter a RFN number"]
${reasonDuplicatePayment}           xpath=//*[@role='option']/span[contains(text(),'Duplicate payment')]
${reasonCODReturn}                  xpath=//*[@role='option']/span[contains(text(),'COD return')]
${accordionOrderFinancials}         xpath=//*[contains(text(),'Order Financials')]
${orderFinancialsReturnCancelled}   xpath=//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Return Cancelled')]//following-sibling::td
${orderFinancialsnCancelled}        xpath=//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Cancelled')]//following-sibling::td
${reasonCreditError}                xpath=//*[@role='option']/span[contains(text(),'Credit error')]