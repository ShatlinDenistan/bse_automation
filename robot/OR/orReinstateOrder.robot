*** Variables ***

${BtnReinstate}    xpath=//button[contains(text(),'Reinstate')]
${ReinstateBtn}    xpath=//*[@class='ui small modal transition visible active']//button[contains(text(),'Reinstate')]
${AdminNote}     xpath=//div[contains(text(),'Order reinstated')]
${ReinstateStaffDiscountAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td
${ReinstateOrderItemsAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td
${ReinstateDeliveryAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Delivery')]//following-sibling::td
${ReinstateCouponDiscountAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Coupon Discount')]//following-sibling::td
${ReinstateOrderTotalAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Total')]//following::td
${ReinstateStaffDiscountAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td
${ReinstateOrderItemsAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td
${ReinstateDeliveryAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Delivery')]//following-sibling::td
${ReinstateCouponDiscountAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Coupon Discount')]//following-sibling::td
${ReinstateOrderTotalAmount}     xpath=//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Total')]//following::td
${OrderFinancialsAccordion}    xpath=//div[contains(text(),'Order Financials')]//i
${OrderFinancialsStaffDiscountAmount}    xpath=//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Staff Discount')]//following-sibling::td
${OrderPageCanceledByBadge}    xpath=//*[@class='ten wide column label-container']/span/div[1]


