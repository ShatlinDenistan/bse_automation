*** Variables ***

${AllOrderIDColumns}             //td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]
${ApplyFilterBtn}                //button[contains(text(), 'Filter')]
${CheckboxDailyDeals}            //*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/div
${ClearFilterBtn}                //button[contains(text(), 'Clear Filter')]
${ClearRiskBtn}                  xpath=//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[1]
${DateRangeCheckbox}             //*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[3]/div
${DateRangeFilter}               //*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[4]/div
${MenuBtn}                       xpath=//i[@aria-hidden="true" and @class="content large icon"]
${MinimumOrderTotalDropdown}     //div[@name='minimumTotal']
${MinimumOrderTotalR500}         //div[@name='minimumTotal']//span[text()='500']
${MinimumOrderTotalR0}           //div[@name='minimumTotal']//span[text()='0']
${MaximumOrderTotalDropdown}     //div[@name='maximumTotal']
${MaximumOrderTotalR5000}        //div[@name='maximumTotal']//span[text()='5000']
${NxtPage}                       xpath=//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[2]/a[2]
${OrderCheckbox}                 xpath=//body/div[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[1]/div
${ResultsTable}                  xpath=//*[@class="ui small celled compact table"]
${RiskQueueMenuOption}           xpath=//body/div[@id="root"]/div[1]/a[4]
${PaymentMethodCredit}           //span[text()='Credit']
${PaymentMethodDeposit}          //span[text()='Deposit']
${PaymentMethodDropdown}         //div[@name='paymentMethod']
${PaymentMethodPayfast}          //span[text()='PayFast']
${AllPaymentMethodColumns}       //td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 7)]
${ShippingMethodDropdown}        //div[@name='shippingMethod']
${ShippingMethodDelivery}        //span[text()='Courier']
${VirtualItemsCheckbox}          //*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[2]/div

${btnSendEmailTable}    xpath=//table/tfoot/tr/th/div/div[3]/button
${ddlEmailTemplates}   xpath=//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]
${btnSendEmail}     xpath=//button[contains(text(),'Send Emails')]
${EmailSentModal}    xpath=/html/body/div[2]/div
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

${RiskQueueCancelOrderButton}   //button[contains(text(), 'Cancel Order(s)')]
${CancelOrdersModalHeader}    //div[contains(text(),'Please confirm')]
${CancellationReasonDropdown}   //div[@name='cancelReason']
${CancellationReasonCustomerRequest}   //span[contains(text(), 'Customer request')]
${CancellationReasonSupplierOutOfStock}   //span[contains(text(), 'Supplier out of stock')]
${CancellationReasonFraud}   //span[contains(text(), 'Fraud')]
${CancellationReasonDamaged}   //span[contains(text(), 'Damaged')]
${CancellationReasonIncorrectPackaging}   //span[contains(text(), 'Incorrect Packaging')]
${CancelOrdersModalCancelButton}    //button[contains(text(), 'Cancel Orders')]
${CancelOrdersModal}     //div[contains(@class, 'ui large modal transition visible active')]
${CancelOrderModalSuccessMessage}    //div[contains(@class, 'ui success message')]/div/div
${CancelOrdersModalCloseIcon}    //*[@class= 'close icon']
${OrderIDHyperlink}    //*[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[2]/a
${FinPortalGlobalSearchField}   //*[@name='searchText' and @type='text']
${FinPortalGlobalSearchIcon}    //*[@class='search icon']
${CanceledByOrderPageBadge}     //div[contains(text(), 'Canceled by')]
${OrderItemCancellationReason}  //div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]