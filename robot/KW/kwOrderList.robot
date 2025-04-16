*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orOrderList.robot


*** Keywords ***
Navigate to Order List Page
    Click Element   ${btnMenu}
    Click Element    ${OrderListMenuOption}

Clear Today Filter
    Click Element    ${ClearDateRangeToday}
    Click Element    ${OrderListApplyFilterButton}

Authorise Single Order
    Click Element    ${Past10days}
    Click Element    ${ApplyFilter}

    Wait Until Page Contains Element  ${FirstRowWithOrderStatusNewOrderCheckbox}
    Wait Until Element Is Enabled    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    ${order_id}     Get Text    ${OrderIdColumn}

    Scroll Element Into View    ${OrderListAuthoriseOrderButton}
    Click Element    ${OrderListAuthoriseOrderButton}
    Sleep    5s

    Wait Until Element Is Visible    ${AuthoriseOrdersModal}
    ${AuthoriseOrdersModalText}     Get Text    ${AuthoriseOrdersModal}
    Should Contain    ${AuthoriseOrdersModalText}    Authorizing Orders
    Sleep    3s
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed 1 item(s)
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed item: ${order_id}
    Click Element   ${AuthoriseOrdersModalCloseIcon}

    Input Text    ${FinPortalGlobalSearchField}    ${order_id}
    Click Element    ${FinPortalGlobalSearchIcon}
    Scroll Element Into View    ${AuthedByOrderPageBadge}
    ${AuthBy}       Get Text    ${AuthedByOrderPageBadge}
    Should Contain    ${AuthBy}    Auth by Test en-gcs

Authorise Multiple Orders
    Click Element    ${Past10days}
    Click Element    ${ApplyFilter}

    Wait Until Page Contains Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Wait Until Element Is Enabled    ${FirstRowWithOrderStatusNewOrderCheckbox}

    Click Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${SecondRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${ThirdRowWithOrderStatusNewOrderCheckbox}

    ${order_id_1}    Get Text    ${OrderIdColumn}
    ${order_id_2}    Get Text    ${OrderIdColumn2}
    ${order_id_3}    Get Text    ${OrderIdColumn3}

    Scroll Element Into View    ${OrderListAuthoriseOrderButton}
    Click Element    ${OrderListAuthoriseOrderButton}
    Sleep    5s

    Wait Until Element Is Visible    ${AuthoriseOrdersModal}
    ${AuthoriseOrdersModalText}    Get Text    ${AuthoriseOrdersModal}
    Should Contain    ${AuthoriseOrdersModalText}    Authorizing Orders
    Sleep    12s
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed 3 item(s)
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed item: ${order_id_1}
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed item: ${order_id_2}
    Should Contain    ${AuthoriseOrdersModalText}    Successfully processed item: ${order_id_3}

    Click Element    ${AuthoriseOrdersModalCloseIcon}

    Input Text    ${FinPortalGlobalSearchField}    ${order_id_1}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${AuthedByOrderPageBadge}
    ${AuthBy}    Get Text    ${AuthedByOrderPageBadge}
    Should Contain    ${AuthBy}    Auth by Test en-gcs

    Reload Page
    Sleep    5s
    Input Text    ${FinPortalGlobalSearchField}    ${order_id_2}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${AuthedByOrderPageBadge}
    ${AuthBy}    Get Text    ${AuthedByOrderPageBadge}
    Should Contain    ${AuthBy}    Auth by Test en-gcs

    Reload Page
    Sleep    5s
    Clear Element Text    ${FinPortalGlobalSearchField}
    Input Text    ${FinPortalGlobalSearchField}    ${order_id_3}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${AuthedByOrderPageBadge}
    ${AuthBy}    Get Text    ${AuthedByOrderPageBadge}
    Should Contain    ${AuthBy}    Auth by Test en-gcs

Cancel Single Order
    Wait Until Page Contains Element  ${FirstRowWithOrderStatusNewOrderCheckbox}
    Wait Until Element Is Enabled    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    ${order_id}     Get Text    ${OrderIdColumn}

    Scroll Element Into View    ${OrderListCancelOrderButton}
    Click Element    ${OrderListCancelOrderButton}
    Sleep    2s

    Wait Until Element Is Visible    ${CancelOrdersModalHeader}
    ${CancelOrdersHeaderText}     Get Text    ${CancelOrdersModalHeader}
    Should Contain    ${CancelOrdersHeaderText}    Please confirm if you would like to cancel selected orders.
    Click Element   ${CancellationReasonDropdown}

    ${random_number} =    Evaluate    random.randint(1, 5)
    Run Keyword If    ${random_number} == 1    Click Element    ${CancellationReasonCustomerRequest}
    Run Keyword If    ${random_number} == 2    Click Element    ${CancellationReasonSupplierOutOfStock}
    Run Keyword If    ${random_number} == 3    Click Element    ${CancellationReasonFraud}
    Run Keyword If    ${random_number} == 4    Click Element    ${CancellationReasonDamaged}
    Run Keyword If    ${random_number} == 5    Click Element    ${CancellationReasonIncorrectPackaging}

    ${SelectedReason}   Get Text   ${CancellationReasonDropdown}

    Click Element    ${CancelOrdersModalCancelButton}

    Wait Until Element Is Visible    ${CancelOrdersModal}
    ${CancelOrdersModalText}     Get Text    ${CancelOrdersModal}
    Should Contain    ${CancelOrdersModalText}    Cancelling Orders
    Should Contain    ${CancelOrdersModalText}    Successfully processed 1 item(s)
    Should Contain    ${CancelOrdersModalText}    Successfully processed item: ${order_id}
    Click Element    ${CancelOrdersModalCloseIcon}

    Input Text    ${FinPortalGlobalSearchField}    ${order_id}
    Click Element    ${FinPortalGlobalSearchIcon}
    Scroll Element Into View    ${CanceledByOrderPageBadge}
    ${CanceledBy}       Get Text    ${CanceledByOrderPageBadge}
    Should Contain    ${CanceledBy}    Canceled by Test en-gcs

    ${OrderitemReason}      Get Text    ${OrderItemCancellationReason}
    Should Contain    ${OrderitemReason}     ${SelectedReason}
    Should Contain    ${OrderitemReason}     Test en-gcs

Cancel Multiple Orders
    Click Element    ${Past10days}
    Click Element    ${ApplyFilter} 

    Wait Until Page Contains Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Wait Until Element Is Enabled    ${FirstRowWithOrderStatusNewOrderCheckbox}


    Click Element    ${FirstRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${SecondRowWithOrderStatusNewOrderCheckbox}
    Click Element    ${ThirdRowWithOrderStatusNewOrderCheckbox}

    ${order_id_1}    Get Text    ${OrderIdColumn}
    ${order_id_2}    Get Text    ${OrderIdColumn2}
    ${order_id_3}    Get Text    ${OrderIdColumn3}

    Scroll Element Into View    ${OrderListCancelOrderButton}
    Click Element    ${OrderListCancelOrderButton}
    Sleep    5s
    Click Element   ${CancellationReasonDropdown}
    Click Element    ${CancellationReasonCustomerRequest}
    Click Element    ${CancelOrdersModalCancelButton}
    Sleep    5s

    Wait Until Element Is Visible    ${CancelOrdersModal}
    ${CancelOrdersModalText}    Get Text    ${CancelOrdersModal}
    Should Contain    ${CancelOrdersModalText}    Cancelling Orders
    Sleep    12s
    Should Contain    ${CancelOrdersModalText}    Successfully processed 3 item(s)
    Should Contain    ${CancelOrdersModalText}    Successfully processed item: ${order_id_1}
    Should Contain    ${CancelOrdersModalText}    Successfully processed item: ${order_id_2}
    Should Contain    ${CancelOrdersModalText}   Successfully processed item: ${order_id_3}

    Sleep    5s

    Click Element    ${CancelOrdersModalCloseIcon}


    Input Text    ${FinPortalGlobalSearchField}    ${order_id_1}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${CanceledByOrderPageBadge}
    ${CanceledBy}     Get Text    ${CanceledByOrderPageBadge}
    Should Contain    ${CanceledBy}     Canceled by Test en-gcs

    Reload Page
    Sleep    5s
    Input Text    ${FinPortalGlobalSearchField}    ${order_id_2}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${CanceledByOrderPageBadge}
    ${CanceledBy}     Get Text    ${CanceledByOrderPageBadge}
    Should Contain    ${CanceledBy}     Canceled by Test en-gcs

    Reload Page
    Sleep    5s
    Input Text    ${FinPortalGlobalSearchField}    ${order_id_3}
    Click Element    ${FinPortalGlobalSearchIcon}
    Sleep    5s
    Scroll Element Into View    ${CanceledByOrderPageBadge}
    ${CanceledBy}     Get Text    ${CanceledByOrderPageBadge}
    Should Contain    ${CanceledBy}    Canceled by Test en-gcs

    ${OrderitemReason}      Get Text    ${OrderItemCancellationReason}
    Should Contain    ${OrderitemReason}     Customer request
    Should Contain    ${OrderitemReason}     Test en-gcs

Cancel Already Cancelled order
    Wait Until Page Contains Element  ${FirstRowWithOrderStatusCancelledCheckbox}
    Wait Until Element Is Enabled    ${FirstRowWithOrderStatusCancelledCheckbox}
    Click Element    ${FirstRowWithOrderStatusCancelledCheckbox}
    ${order_id}     Get Text    ${OrderIdColumnCanceled}

    Scroll Element Into View    ${OrderListCancelOrderButton}
    Click Element    ${OrderListCancelOrderButton}
    Sleep    2s
    Click Element   ${CancellationReasonDropdown}
    Click Element    ${CancellationReasonCustomerRequest}
    Click Element    ${CancelOrdersModalCancelButton}

    Sleep    5s
    Wait Until Element Is Visible    ${CancelOrdersModal}
    ${CancelOrdersModalText}     Get Text    ${CancelOrdersModal}
    Should Contain    ${CancelOrdersModalText}    Cancelling Orders
    Should Contain    ${CancelOrdersModalText}    Failed to process 1 item(s)
    Should Contain    ${CancelOrdersModalText}    Failed to process item: ${order_id} , Unable to process service request

Filter By Daily Deal
    Click Element    ${OrderListClearFilterButton}
    Sleep    2s
    Wait Until Element Is Visible    ${DailyDealsCheckbox}
    Click Element    ${DailyDealsCheckbox}
    Click Element    ${OrderListApplyFilterButton}

    ${order_id_elements}    Get WebElements    ${AllOrderIDColumns}
        FOR    ${element}    IN    @{order_id_elements}
            Element Should Contain    ${element}    Daily Deal
        END

Filter By Auth Status
    Click Element    ${OrderListClearFilterButton}
    Sleep    2s
    Wait Until Element Is Visible    ${OrderListTable}
    Click Element    ${AuthStatusDropdown}

    ${random_number} =    Evaluate    random.randint(1, 2)
    Run Keyword If    ${random_number} == 1    Click Element    ${AuthStatusNew}
    Run Keyword If    ${random_number} == 2    Click Element    ${AuthStatusAuth}

    ${SelectedStatus}   Get Text   ${AuthStatusDropdown}

    Click Element    ${OrderListApplyFilterButton}

    ${authstatus_elements}    Get WebElements    ${AllAuthStatusColumns}
        FOR    ${element}    IN    ${authstatus_elements}
            Element Should Contain    ${element}    ${SelectedStatus}
        END

Filter By Payment Method
    Click Element    ${OrderListClearFilterButton}
    Wait Until Element Is Visible    ${OrderListTable}
    Click Element    ${PaymentMethodDropdown}

    ${random_number} =    Evaluate    random.randint(1, 2)
    Run Keyword If    ${random_number} == 1    Click Element    ${PaymentMethodCreditCard}
    Run Keyword If    ${random_number} == 2    Click Element    ${PaymentMethodPayfast}

    ${SelectedPaymentMethod}   Get Text   ${PaymentMethodDropdown}

    Click Element    ${OrderListApplyFilterButton}

    ${paymentmethod_elements}    Get WebElements    ${AllPaymentMethodColumns}
        FOR    ${element}    IN    ${paymentmethod_elements}
            Element Should Contain    ${element}    ${SelectedPaymentMethod}
        END

Filter By Shipping Method
    Click Element    ${OrderListClearFilterButton}
    Wait Until Element Is Visible    ${OrderListTable}
    Click Element    ${ShippingMethodDropdown}

    Click Element    ${ShippingMethodCollect}

    Click Element    ${OrderListApplyFilterButton}

    ${shippingmethod_elements}    Get WebElements    ${AllOrderIDColumns}
        FOR    ${element}    IN    ${shippingmethod_elements}
            Element Should Contain    ${element}    Collection
        END

Filter By Minimum Order Total
    Click Element    ${OrderListClearFilterButton}
    Wait Until Element Is Visible    ${OrderListTable}

    Click Element    ${MinimumOrderTotalDropdown}
    Click Element    ${MinimumOrderTotalR500}

    Click Element    ${OrderListApplyFilterButton}

    ${row_count}    WebAutomationFramework.Get Element Count   ${OrderListTable}
        FOR    ${row_index}    IN RANGE    1    ${row_count + 1}
            ${order_total}    Get Text    //table[@class='ui small celled compact table']//tbody//tr[${row_index}]//td[7]
            Log    ${order_total}
            ${numeric_value}    Evaluate    ${order_total.replace('R', '').replace(',', '')}
            Log    ${numeric_value}
            Should Be True    ${numeric_value} > 500
            Log    ${numeric_value} is greater than R 500
        END

Filter By Maximum Order Total
    Click Element    ${OrderListClearFilterButton}
    Wait Until Element Is Visible    ${OrderListTable}

    Click Element    ${MinimumOrderTotalDropdown}
    Click Element    ${MinimumOrderTotalR0}

    Click Element    ${MaximumOrderTotalDropdown}
    Click Element    ${MaximumOrderTotalR500}

    Click Element    ${OrderListApplyFilterButton}

    ${row_count}    WebAutomationFramework.Get Element Count   ${OrderListTable}
        FOR    ${row_index}    IN RANGE    1    ${row_count + 1}
            ${order_total}    Get Text    //table[@class='ui small celled compact table']//tbody//tr[${row_index}]//td[7]
            Log    ${order_total}
            ${numeric_value}    Evaluate    ${order_total.replace('R', '').replace(',', '')}
            Log    ${numeric_value}
            Should Be True    ${numeric_value} < 500
            Log    ${numeric_value} is less than R 500
        END

Filter By Multiple Filters
    Click Element    ${OrderListClearFilterButton}
    Wait Until Element Is Visible    ${OrderListTable}

    Click Element    ${AuthStatusDropdown}
    Click Element    ${AuthStatusNew}

    Click Element    ${PaymentMethodDropdown}
    Click Element    ${PaymentMethodCreditCard}

    Click Element    ${ShippingMethodDropdown}
    Click Element    ${ShippingMethodCollect}

    Click Element    ${OrderListApplyFilterButton}

        ${authstatus_elements}    Get WebElements    ${AllAuthStatusColumns}
        FOR    ${element}    IN    ${authstatus_elements}
            Element Should Contain    ${element}    New
            Log    All Auth status rows are New
        END

        ${paymentmethod_elements}    Get WebElements    ${AllPaymentMethodColumns}
        FOR    ${element}    IN    ${paymentmethod_elements}
            Element Should Contain    ${element}    Credit Card
            Log    All Payment method rows are Credit Card
        END

        ${shippingmethod_elements}    Get WebElements    ${AllOrderIDColumns}
        FOR    ${element}    IN    ${shippingmethod_elements}
            Element Should Contain    ${element}    Collection
            Log    All Shipping method rows are Collect
        END