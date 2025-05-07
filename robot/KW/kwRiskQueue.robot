*** Settings ***
Resource    ../Config/defaultConfig.robot 
Resource    ../OR/orRiskQueue.robot

*** Keywords ***

Navigate To Risk Queue
    Click Element    ${MenuBtn}
    Click Element    ${RiskQueueMenuOption}
    Wait Until Page Contains Element    ${ResultsTable} 

Click Show Items Dropdown And Select 10 Items
    Click Element    ${ItemListDDL}
    Click Element    ${ListFilter10}

Navigate To Next Page
    Click Element    ${NxtPage} 
    Wait Until Element Is Visible   ${ResultsTable} 

Select an order to clear risk
   Click Element     ${OrderCheckbox}
   Click Element     ${ClearRiskBtn} 

Handle Alerts
    Handle Alert   Accept

Filter Using Payment Method
    Click Element    ${ClearFilterBtn}  
    Wait Until Element Is Visible    ${ResultsTable}  
    Click Element    ${PaymentMethodDropdown}
    ${random_number} =    Evaluate    random.randint(1, 2)
    Run Keyword If    ${random_number} == 1    Click Element    ${PaymentMethodCredit}
    Run Keyword If    ${random_number} == 2    Click Element    ${PaymentMethodPayfast}
    ${SelectedPaymentMethod}   Get Text   ${PaymentMethodDropdown}
    Click Element    ${ApplyFilterBtn} 
    ${paymentmethod_elements}    Get WebElements    ${AllPaymentMethodColumns}
        FOR    ${element}    IN    ${paymentmethod_elements}
            Element Should Contain    ${element}    ${SelectedPaymentMethod}
        END

Filter Using Shipping Method
    Click Element     ${ClearFilterBtn} 
    Wait Until Element Is Visible    ${ResultsTable}  
    Click Element    ${ShippingMethodDropdown}
    Click Element    ${ShippingMethodDelivery}
    Click Element     ${ApplyFilterBtn}
    ${shippingmethod_elements}    Get WebElements    ${AllOrderIDColumns}
        FOR    ${element}    IN    ${shippingmethod_elements}
            Element Should Contain    ${element}    Express Delivery
        END

Filter Using Minimum Amount 
    Click Element     ${ClearFilterBtn} 
    Wait Until Element Is Visible    ${ResultsTable}  
    Click Element    ${MinimumOrderTotalDropdown}
    Click Element    ${MinimumOrderTotalR500}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row_index}    IN RANGE    1    ${row_count + 1}
            ${order_total}    Get Text    //table[@class='ui small celled compact table']//tbody//tr[${row_index}]//td[10]
            Log    ${order_total}
            ${numeric_value}    Evaluate    ${order_total.replace('R', '').replace(',', '')}
            Log    ${numeric_value}
            Should Be True    ${numeric_value} > 500
            Log    ${numeric_value} is greater than R 500
        END

Filter Using Maximum Amount
    Click Element    ${ClearFilterBtn} 
    Wait Until Element Is Visible    ${ResultsTable}  
    Click Element    ${MinimumOrderTotalDropdown}
    Click Element    ${MinimumOrderTotalR0}
    Click Element    ${MaximumOrderTotalDropdown}
    Click Element    ${MaximumOrderTotalR5000}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row_index}    IN RANGE    1    ${row_count + 1}
            ${order_total}    Get Text    //table[@class='ui small celled compact table']//tbody//tr[${row_index}]//td[10]
            Log    ${order_total}
            ${numeric_value}    Evaluate    ${order_total.replace('R', '').replace(',', '')}
            Log    ${numeric_value}
            Should Be True    ${numeric_value} < 5000
            Log    ${numeric_value} is less than R 5000
        END

Filter Using Multiple Filters
    Click Element    ${ClearFilterBtn} 
    Wait Until Element Is Visible    ${ResultsTable}
    Click Element    ${VirtualItemsCheckbox}
    Click Element    ${DateRangeCheckbox}
    Click Element    ${PaymentMethodDropdown}
    Click Element    ${PaymentMethodCredit}
    Click Element    ${MaximumOrderTotalDropdown}
    Click Element    ${MaximumOrderTotalR5000}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row_index}    IN RANGE    1    ${row_count + 1}
            ${order_total}    Get Text    //table[@class='ui small celled compact table']//tbody//tr[${row_index}]//td[10]
            Log    ${order_total}
            ${numeric_value}    Evaluate    ${order_total.replace('R', '').replace(',', '')}
            Log    ${numeric_value}
            Should Be True    ${numeric_value} < 5000
            Log    ${numeric_value} is less than R 5000
        END

    Click Element    ${ApplyFilterBtn}

        ${paymentmethod_elements}    Get WebElements    ${AllPaymentMethodColumns}
        FOR    ${element}    IN    ${paymentmethod_elements}
            Element Should Contain    ${element}    Credit
            Log    All Payment method rows are Credit
        END

Filter Using Daily Deal
    Click Element    ${ClearFilterBtn} 
    Wait Until Element Is Visible    ${CheckboxDailyDeals}
    Click Element    ${CheckboxDailyDeals}
    Click Element    ${ApplyFilterBtn}
    Wait Until Element Is Visible    ${ResultsTable} 

Filter Using Date Range
    Click Element    ${ClearFilterBtn} 
    Click Element    ${DateFilter}
    Input Text       ${DateFilter}    01-05-2024 - 31-05-2024
    Click Element    ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row}    IN RANGE    1    ${row_count + 1}
               ${locator} =    Set Variable    //tbody/tr[${row}]/td[4]
               ${element_text} =    Get Text    ${locator}
               Should Contain    ${element_text}    May-2024
        END

Select First Order on Grid
    ${OrderIDText}    Get Text    ${OrderIDHyperlink}
    Set Global Variable    ${OrderIDText}
    Click Element    ${OrderCheckbox}

Select Email Template and Send Email
    Click Element    ${btnSendEmailTable}
    Click Element    ${ddlEmailTemplates}

    ${random_number}    Evaluate    random.randint(1, 14)
    Run Keyword If    ${random_number} == 1    Click Element    ${OPTION1_XPATH}
    Run Keyword If    ${random_number} == 2    Click Element    ${OPTION2_XPATH}
    Run Keyword If    ${random_number} == 3    Click Element    ${OPTION3_XPATH}
    Run Keyword If    ${random_number} == 4    Click Element    ${OPTION4_XPATH}
    Run Keyword If    ${random_number} == 5    Click Element    ${OPTION5_XPATH}
    Run Keyword If    ${random_number} == 6    Click Element    ${OPTION6_XPATH}
    Run Keyword If    ${random_number} == 7    Click Element    ${OPTION7_XPATH}
    Run Keyword If    ${random_number} == 8    Click Element    ${OPTION8_XPATH}
    Run Keyword If    ${random_number} == 9    Click Element    ${OPTION9_XPATH}
    Run Keyword If    ${random_number} == 10    Click Element    ${OPTION10_XPATH}
    Run Keyword If    ${random_number} == 11    Click Element    ${OPTION11_XPATH}
    Run Keyword If    ${random_number} == 12    Click Element    ${OPTION12_XPATH}
    Run Keyword If    ${random_number} == 13    Click Element    ${OPTION13_XPATH}
    Run Keyword If    ${random_number} == 14    Click Element    ${OPTION14_XPATH}

    Click Element    ${btnSendEmail}

Verify Email Sent Success Message
    ${EmailSentText}    Get Text    ${EmailSentModal}

    Sleep    2s
    Page Should Contain Element     xpath=//div[contains(text(),'Successfully processed')]

    Click Element    ${EmailSentModal_Close_icon}

Cancel Single Order
    Scroll Element Into View    ${RiskQueueCancelOrderButton}
    Click Element    ${RiskQueueCancelOrderButton}
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
    Set Global Variable    ${SelectedReason}

    Click Element    ${CancelOrdersModalCancelButton}

    Wait Until Element Is Visible    ${CancelOrdersModal}
    ${CancelOrdersModalText}     Get Text    ${CancelOrdersModal}
    Should Contain    ${CancelOrdersModalText}    Cancelling Orders
    Sleep    3s
    ${CancelOrdersSuccessMessageModalText}     Get Text    ${CancelOrderModalSuccessMessage} 
    Should Contain    ${CancelOrdersSuccessMessageModalText}    Successfully processed 1 item(s)
    Click Element    ${CancelOrdersModalCloseIcon}

Verify Canceled Order Status
    Input Text    ${FinPortalGlobalSearchField}    ${OrderIDText}
    Click Element    ${FinPortalGlobalSearchIcon}
    Scroll Element Into View    ${CanceledByOrderPageBadge}
    ${CanceledBy}       Get Text    ${CanceledByOrderPageBadge}
    Should Contain    ${CanceledBy}    Canceled by Test en-gcs

    ${OrderitemReason}      Get Text    ${OrderItemCancellationReason}
    Should Contain    ${OrderitemReason}     ${SelectedReason}
    Should Contain    ${OrderitemReason}     Test en-gcs