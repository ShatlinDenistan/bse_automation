*** Variables ***

${BlackEllipsis}    //*[@class='six wide column']//*[@class='black ellipsis vertical small icon']
${EditOrderMenuOption}    //*[contains(text(),'Edit Order')]
${PaymentMethodDropdown}    //*[@name='paymentMethod']
${UpdateButton}    //button[contains(text(),'Update')]
${PaymeMethodUpdateAdminNote}     //div[contains(text(),'Payment method updated ')]
${PaymeMethodWarningBanner}    //*[@class='banner-container']
${DiscountAmount}    //*[@name='discountAmount']
${InvalidDiscountAmount}    //*[@class='ui error message']/div/p/li
${ShippingAmount}    //*[@name='shippingAmount']
${DiscountAppliedAdminNote}     //div[contains(text(),'Discount applied:')]
${ShippingFeeAppliedAdminNote}     //div[contains(text(),'Shipping fee applied:')]
${AuditLogMenuOption}    //*[contains(text(),'Audit log')]
${AuditLogEditOrderActionType}    //*[@class='ui striped basic very compact table']/tbody/tr/td[3]
${AuditLogEditOrderData}    //*[@class='ui striped basic very compact table']/tbody/tr/td[5]
${OrderFinancialsAccordion}    xpath=//div[contains(text(),'Order Financials')]//i
${OrderFinancialsShippingAmount}    //div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Shipping')]//following-sibling::td
${OrderFinancialsDiscountAmount}    //div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Discount')]//following-sibling::td
${ReturnCanceledOrderItemMenu}    //div[@class='accordion ui fluid styled']//*[@role='listbox']
${UpdateToShippedMenuOption}    //*[contains(text(),'Update to shipped')]
${UpdateToShippedModalMessage}    //div[@class='ui tiny modal transition visible active']//*[@class='ui form']/p
${UpdateToShippedButton}    //div[@class='ui tiny modal transition visible active']//button[contains(text(),'Update to shipped')]
${OrderItemStatus}    //div[@class='accordion ui']//table[@class='ui table']//td[8]/div
${UpdateToShippedAdminNote}    //div[contains(text(),'status updated from Return Canceled to Shipped')]
${DiscountAmountDisabledField}    //*[contains(text(),'Discount')]/parent::div//parent::div/div/p
${ShippingFeeDisabledField}    //*[contains(text(),'Shipping')]/parent::div//parent::div/div/p
