*** Variables ***

#${OrderListTable}   //table[@class='ui small celled compact table']
${OrderListTable}   //table[@class='ui small celled compact table']//tbody//tr
${btnMenu}  //i[@class='content large icon' and @aria-hidden='true']
${OrderListTable}   //table[@class='ui small celled compact table']//tr
${OrderListMenuOption}  //*[contains(text(),'Order List')]
${ClearAuthStatusIcon}  //i[@class='dropdown icon clear' and @aria-hidden='true']

${ClearDateRangeToday}  //div[@class='ui checked checkbox']//label[text()='Today']
${OrderListApplyFilterButton}   //button[contains(text(), 'Apply Filter')]

${Past10days}    //label[text()='Past 10 Days']

${FirstRowWithOrderStatusNewOrderCheckbox}  //tr[td[9]/div[contains(text(), 'New Order')]][1]
...  //td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]

${SecondRowWithOrderStatusNewOrderCheckbox}     //tr[td[9]/div[contains(text(), 'New Order')]][2]
...   //td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]

${ThirdRowWithOrderStatusNewOrderCheckbox}  //tr[td[9]/div[contains(text(), 'New Order')]][3]
...   //td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]


${OrderIdColumn}   //tr[td[9]/div[contains(text(), 'New Order')]][1]//a[contains(@href, '/order/')]
${OrderIdColumn2}   //tr[td[9]/div[contains(text(), 'New Order')]][2]//a[contains(@href, '/order/')]
${OrderIdColumn3}   //tr[td[9]/div[contains(text(), 'New Order')]][3]//a[contains(@href, '/order/')]
${OrderListAuthoriseOrderButton}    //button[contains(text(), 'Authorise Order(s)')]
${AuthoriseOrdersModal}     //div[contains(@class, 'ui large modal transition visible active')]
${AuthoriseOrdersModalCloseIcon}    //*[@class= 'close icon']
${FinPortalGlobalSearchField}   //*[@name='searchText' and @type='text']
${FinPortalGlobalSearchIcon}    //*[@class='search icon']
${AuthedByOrderPageBadge}   //div[contains(text(), 'Auth by')]

${OrderListCancelOrderButton}   //button[contains(text(), 'Cancel Order(s)')]
${CancelOrdersModalHeader}    //div[contains(text(),'Please confirm')]
${CancellationReasonDropdown}   //div[@name='cancelReason']
${CancellationReasonCustomerRequest}   //span[contains(text(), 'Customer request')]
${CancellationReasonSupplierOutOfStock}   //span[contains(text(), 'Supplier out of stock')]
${CancellationReasonFraud}   //span[contains(text(), 'Fraud')]
${CancellationReasonDamaged}   //span[contains(text(), 'Damaged')]
${CancellationReasonIncorrectPackaging}   //span[contains(text(), 'Incorrect Packaging')]
${CancelOrdersModalCancelButton}    //button[contains(text(), 'Cancel Orders')]
${CancelOrdersModal}     //div[contains(@class, 'ui large modal transition visible active')]
${CancelOrdersModalCloseIcon}    //*[@class= 'close icon']
${CanceledByOrderPageBadge}     //div[contains(text(), 'Canceled by')]
${OrderItemCancellationReason}  //div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]

${FirstRowWithOrderStatusCancelledCheckbox}     //tr[td[9]/div[contains(text(), 'Canceled')]][1]
...  //td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]
${OrderIdColumnCanceled}     //tr[td[9]/div[contains(text(), 'Canceled')]][1]//a[contains(@href, '/order/')]
${OrderListClearFilterButton}   //button[contains(text(), 'Clear Filter')]
${DailyDealsCheckbox}   //label[text()='Daily Deals']
${AllOrderIDColumns}    //td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]

${AuthStatusDropdown}   //div[@name='authStatus']
${AuthStatusNew}    //span[contains(text(), 'New')]
${AuthStatusAuth}    //span[text()='Auth']
${AllAuthStatusColumns}     //td[position() = (count(//th[text()='Auth Status']/preceding-sibling::th) + 1)]

${PaymentMethodDropdown}   //div[@name='paymentMethod']
${PaymentMethodCreditCard}  //span[text()='Credit Card']
${PaymentMethodCredit}  //span[text()='Credit']
${PaymentMethodPayfast}  //span[text()='PayFast']
${PaymentMethodDeposit}  //span[text()='Deposit']
${AllPaymentMethodColumns}     //td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 1)]

${ShippingMethodDropdown}   //div[@name='shippingMethod']
${ShippingMethodCollect}  //span[text()='Collect']
${ShippingMethodCourier}  //span[text()='Courier']

${MinimumOrderTotalDropdown}     //div[@name='minimumTotal']
${MinimumOrderTotalR500}    //div[@name='minimumTotal']//span[text()='R 500']
${MinimumOrderTotalR0}      //div[@name='minimumTotal']//span[text()='R 0']
${MaximumOrderTotalDropdown}     //div[@name='maximumTotal']
${MaximumOrderTotalR500}    //div[@name='maximumTotal']//span[text()='R 500']
${AllOrderTotalColumns}     //td[position() = (count(//th[text()='Order Total']/preceding-sibling::th) + 1)]

