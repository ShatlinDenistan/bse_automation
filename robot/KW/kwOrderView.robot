*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orOrderView.robot
Resource    ../OR/orOrderList.robot

*** Keywords ***
Add Admin Notes
    Wait Until Element Is Visible    ${noteDD}   
    Click Element      ${noteDD}  
    Click Element    ${addNotesBtn}   
    Input Text       ${notesTxtField}  Automation Admin Note
    Click Element   ${confirmAddBtn}   
    Wait until element is visible  ${noteConfirmMessage} 
    ${addNoteMessageText}=  Get text  ${noteConfirmMessage} 
    ${result}    Replace String   ${addNoteMessageText}   Request failed with status code 403\n×\n    ${EMPTY}  
    Should Contain   ${result}  Note successfully added to Customer: 8441423\n

Update To Blacklist 
   Wait Until Element Is Visible    ${blacklistCustBtn}  
   Click Element     ${blacklistCustBtn} 
   Click Element     ${fraudReasonList} 
   Click Element     ${fraudReasonSelection}  
   Input Text    ${finNote}      Automation Testing
   Click Element  ${confirmBlacklist} 
   Handle Alert   Accept
   Sleep    3s
   Wait until element is visible  ${noteConfirmMessage}
   ${message}=  Get text  ${noteConfirmMessage}
   ${result}    Replace String   ${message}  Request failed with status code 403\n×\n    ${EMPTY}  
   Should Contain   ${result}  Successfully blacklisted the customer\n×

Update To Whitelist
   Wait Until Element Is Visible    ${whitelistCustBtn}  
   Click Element     ${whitelistCustBtn}  
   Click Element  ${confirmWhitelist} 
   Handle Alert   Accept
   Sleep    6s
   Wait until element is visible  ${noteConfirmMessage}
   ${message}=  Get text  ${noteConfirmMessage}
   ${result}    Replace String   ${message}  Request failed with status code 403\n×\n    ${EMPTY}  
   Should Contain   ${result}  Successfully Whitelisted Customer: 8441423

Cancel All Order Items
   Wait Until Element Is Visible    ${cancelAllItemBtn}
   Click Element     ${cancelAllItemBtn} 
   Click Element    ${cancellationReason}
   Scroll To Element    ${customerRequestCancelReason} 
   Click Element    ${customerRequestCancelReason} 
   Click Element    ${confirmCancellingBtn}
   Click Element    ${closeCancelModal}

   ${orderStatusText}=    Get Text    ${orderStatus}
   Should Contain    ${orderStatusText}    Canceled by

Send an Email
   ${custID}    Get Text    ${customerID}
   Click Element    ${emailCustomer}
   Click Element     ${emailTemplateDDL} 
   Click Element     ${emailTemplateSelection} 
   Scroll Element Into View    ${sendEmailBtn}
   Click Element    ${sendEmailBtn}
   Wait until element is visible  ${noteConfirmMessage}
   ${message}=  Get text  ${noteConfirmMessage}
   ${result}    Replace String   ${message}  \n×\nRequest failed with status code 404\n×    ${EMPTY}
   Should Contain   ${result}  (Identification Not Accepted) email sent to customer ${custID}

Mark Order As Risky
    Wait Until Element Is Visible    ${markAsRiskyBtn}
    Click Element    ${markAsRiskyBtn}
    Input Text    ${markAsRiskyReason}    Automation Test Risky Reason
    Click Element    ${addReasonBtn} 
    ${flaggedAsRiskText}=  Get text  ${flaggedAsRisk}
    Should Contain   ${flaggedAsRiskText}  Flagged as risky

Verify Audit Log Entry
    [Arguments]    ${actionType}
    Wait Until Element Is Visible    ${orderEllipsisMenu}
    Click Element    ${orderEllipsisMenu}
    Click Element    ${auditLogMenuOption}
    Wait Until Element Is Visible    ${auditLogActionType}
    ${actionTypeText}=   Get Text    ${auditLogActionType}
    Should Contain    ${actionTypeText}    ${actionType}

Manually Authorize An Order
    Wait Until Element Is Visible    ${authoriseNowBtn}
    Click Element    ${authoriseNowBtn}
    Wait Until Element Is Visible    ${authoriseNowModalMessage}
    ${successMessage}=    Get Text    ${authoriseNowModalMessage}
    Should Contain     ${successMessage}    Successfully processed 1 item(s)
    Click Element    ${authoriseNowModalCloseIcon}

Verify Tracking Information For Cancelled Order
    [Arguments]    ${heading}
    Wait Until Element Is Visible    ${orderFullfilmentAccordion}
    Click Element    ${orderFullfilmentAccordion}

    ${orderTrackingHeadingText}=    Get Text    ${orderTrackingHeading}
    Log To Console     ${orderTrackingHeadingText}
    Should Contain     ${orderTrackingHeadingText}    ${heading}

Verify Order Tracking Heading
    [Arguments]    ${heading}
    Wait Until Element Is Visible    ${orderFullfilmentAccordion}
    Click Element    ${orderFullfilmentAccordion}
    ${orderTrackingHeadingText}=    Get Text    ${orderTrackingHeading}
    Should Contain     ${orderTrackingHeadingText}    ${heading}   

Verify Order Tracking For Digital Products Only Order
    Wait Until Element Is Visible    ${orderFullfilmentAccordion}
    Click Element    ${orderFullfilmentAccordion}
    ${orderTrackingUserInfoText}=    Get Text    ${orderTrackingUserInfo}
    Should Contain     ${orderTrackingUserInfoText}   Digital Product(s)   

Edit Customer Details
    Click Element    ${editCustomerBtn}            
    Input Text       ${CustName}   Mike
    Input Text       ${CustSurname}  Jackson
    Input Text       ${businessName}   Automation Test PTY LTD
    Input Text       ${VATNumber}     9876543211
    Click Element    ${accStatusDDL}
    Click Element    ${accStatus}            
    Click Element    ${fraudReasonList}   
    Click Element    ${fraudReason}   
    Click Element    ${staffAccountCheck}     
    Click Element    ${blockVouCheck}  
    Click Element    ${confirmBtn}   
    Wait until element is visible  ${pop-up} 
    ${message}=  Get text  ${pop-up} 
    Should Contain   ${message}  Customer status data updated successfully\n×

View Order Events
  Click Element   ${orderEllipsisMenu}
  Click Element  ${orderEventsMenu}
  Wait Until Element Is Visible  ${eventLogResults} 

Verify Part Payment Methods Badges
    Wait Until Element Is Visible    ${firstPaymentMethodBadge} 
    ${firstPaymentMethodText}=    Get Text    ${firstPaymentMethodBadge}
    ${secondPaymentMethodText}=    Get Text    ${secondPaymentMethodBadge}

    Should Contain    ${firstPaymentMethodText}    Credit Card
    Should Contain    ${secondPaymentMethodText}   eBucks

Add Order Notes 
    Wait Until Element Is Visible    ${orderNotesAccordion}
    Click Element    ${orderNotesBtn}
    Input Text       ${orderNotesTextField}     Automation Test: Order Note 
    Click Element    ${addNoteBtn}
    Wait until element is visible  ${noteAddedMessage}
    ${addNoteMessageText}=  Get text  ${noteAddedMessage}
    Should Contain  ${addNoteMessageText}  Note successfully added to Order

Add Fin Notes
    Sleep    10
    Wait Until Element Is Visible    ${finNotesAccordion}  
    Click Element   ${addFinNotesBtn}  
    Input Text      ${finNotesTextField}     Automation Test: Fin Note 
    Click Element   ${addFinNotesConfirmBtn}
    Wait until element is visible  ${noteAddedMessage}
    ${addNoteMessageText}=  Get text  ${noteAddedMessage}
    Should Contain  ${addNoteMessageText}  Note successfully added to Customer

Add Customer Notes
    Sleep    10
    Wait Until Element Is Visible    ${customerNotesAccordion}
    Click Element    ${customerNotesAccordion}
    Click Element    ${addCustomerNotesBtn}  
    Input Text       ${customerNotesTextField}    Automation Test: Customer Note 
    Click Element    ${addCustomerNotesConfirmBtn}
    Wait until element is visible  ${noteAddedMessage}
    ${addNoteMessageText}=  Get text  ${noteAddedMessage}
    Should Contain  ${addNoteMessageText}  Note successfully added to Customer

Cancel An Order Item
   Click Element     ${selectItemCheckbox} 
   Click Element     ${cancelSelectedItemBtn} 
   Click Element    ${cancellationReason}
   Scroll To Element    ${customerRequestCancelReason} 
   Click Element    ${customerRequestCancelReason} 
   Click Element    ${confirmCancellingBtn}
   Wait Until Element Is Visible   ${cancellationResults} 
   ${message}=    Get Text    ${cancellationResults} 
   Should Contain    ${message}    Orderitem has successfully been cancelled
View Payment Ledger
    Wait Until Element Is Visible    ${paymentLedgerAccordion}
    Click Element    ${paymentLedgerAccordion}
    ${firstPaymentProviderText}=    Get Text    ${paymentLedgerfirstProvder}
    ${secondPaymentProviderText}=    Get Text    ${paymentLedgersecondProvder}
    Should Contain    ${firstPaymentProviderText}    eBucks
    Should Contain    ${secondPaymentProviderText}   PayU
    ${amountPaidText}=    Get Text    ${paymentLedgerPaidTotalAmount}
    Should Be Equal As Strings    ${amountPaidText}    1,699.00

Bookmark an Order
    Wait Until Element Is Visible    ${bookmarkIcon}  
    Click Element    ${bookmarkIcon}  
    Input Text  ${bookmarkNotes}  Testing
    Click Element  ${doneButton}
    Sleep  3 
    ${counter}  Get Text  ${bookmarkCounter} 
    Should Be Equal  ${counter}  1

 Remove Bookmarks   
    Click Element    ${bookmarksPage} 
    Click Element    ${removeBookmarksCheckbox}
    Click Element    ${removeBtn} 
    Wait Until Element Is Visible    ${progressBar} 
    Click Element   ${closeModal}  
    ${msg}  Get Text  ${confirmationMsg}  
    Should Be Equal  ${msg}  No bookmarks to show here  

Verify Order Financials
    Wait Until Element Is Visible    ${orderFinancialsAccordion}
    Click Element    ${orderFinancialsAccordion}
    #Verify Order Items Amount
    ${orderItemAmountConverted}=    Get Text    ${totalOrderItemsAmount}
    ${orderItemAmountConverted}=    Remove String    ${orderItemAmountConverted}    R${SPACE}
    ${orderItemAmountConverted}=    Convert To Number    ${orderItemAmountConverted}
    Should Be Equal     ${orderItemAmountConverted}   ${order_total[0]}
    Set Global Variable    ${orderItemAmountConverted}
     #Verify Shipping Amount
    ${shippingAmountConverted}=    Get Text    ${shippingAmount}
    ${shippingAmountConverted}=    Remove String    ${shippingAmountConverted}    R${SPACE}
    ${shippingAmountConverted}=    Convert To Number    ${shippingAmountConverted}
    Should Be Equal     ${shippingAmountConverted}    ${order_shipping[0]}
    Set Global Variable    ${shippingAmountConverted}
    #Verify Sub-Total Amount
    ${subTotalAmountConverted}=    Get Text    ${subTotalAmount}
    ${subTotalAmountConverted}=    Remove String    ${subTotalAmountConverted}    R${SPACE}
    ${subTotalAmountConverted}=    Convert To Number    ${subTotalAmountConverted}
    ${subTotalCalculation}=    Evaluate    ${order_total[0]} + ${order_shipping[0]}
    Should Be Equal     ${subTotalAmountConverted}    ${subTotalCalculation}
    Set Global Variable    ${subTotalCalculation}
     #Verify Discount Amount
    ${discountAmountConverted}=    Get Text    ${discountAmount}
    ${discountAmountConverted}=    Remove String    ${discountAmountConverted}    ? 
    ${discountAmountConverted}=    Remove String    ${discountAmountConverted}    R${SPACE}-
    ${discountAmountConverted}=    Convert To Number    ${discountAmountConverted}
    Should Be Equal     ${discountAmountConverted}    ${order_discount[0]}
    Set Global Variable    ${discountAmountConverted}

View Order Audit Logs
    Wait Until Element Is Visible    ${orderEllipsisMenu}
    Click Element    ${orderEllipsisMenu}
    Click Element    ${auditLogMenuOption}
    Wait Until Element Is Visible    ${logsTable} 

View Address
    Wait Until Element Is Visible     ${custAccNumber}
    Mouse Over   ${custAccNumber} 
    Wait Until Element Is Visible   ${addressGoogleIcon} 
    Click Element   ${addressGoogleIcon} 
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]   

Verify Order Details
    [Arguments]    ${searchOrderId}
    #Verify Order ID
    ${orderIdConverted}=    Get Text    ${order-id} 
    Should Be Equal      ${orderIdConverted}  ${searchOrderId}
    #Verify auth status
    ${statusCheck}=    Get Text    ${authStatus} 
    Should Contain    ${statusCheck}    Auth
    #Payment method
    ${paymentMethodTag}=    Get Text    ${firstPaymentMethodBadge} 
    Should Contain    ${paymentMethodTag}    Credit Card Token
    #Auth date
    ${authDateTag}=    Get Text    ${authDate} 
    Should Contain        ${authDateTag}   25-Jan-2024 @ 9:31  
    Click Element    ${orderFullfilmentAccordion}
    #Order Fulfillment
    ${orderTrackingUserInfoText}=    Get Text    ${orderTrackingUserInfo}
    Should Contain     ${orderTrackingUserInfoText}   Digital Product(s)
    Click Element    ${orderFullfilmentAccordion}
    #Order Notes
    Scroll Element Into View   ${orderNotesAccordion}
    Wait Until Element Is Visible   ${orderComments}  
    #Cust Info
    Mouse Over   ${custAccNumber} 
    Wait Until Element Is Visible   ${custInfoPop-up}
    ${custStatusCheck}=    Get Text    ${custStatus} 
    Should Contain     ${custStatusCheck}    active
    #Order Financials
    Click Element    ${orderFinancialsAccordion}
    #Verify Total Paid Amount
    ${orderTotalPaidConverted}=    Get Text    ${totalPaidAmount} 
    Should Contain     ${orderTotalPaidConverted}   R 100.00

Get RRN Details
    Wait Until Element Is Visible    ${RRN}
    Click Element     ${RRN}
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s 
    WebAutomationFramework.Switch Window    ${WindowHandles}[1] 

 Verify RRN Details 
   [Arguments]    ${RRNTxt}  
   Search For RRN   ${RRNTxt}   

Update Order Item to Shipped
    Wait Until Element Is Visible    ${editOrderItemMenu}  
    ${itemStatus}=   Get Text    ${returnCanceledTag}
    Should Contain   ${itemStatus}    Return Canceled
    Click Element    ${editOrderItemMenu}  
    Click Element    ${updateStatusMenuOption} 
    Click Element    ${updateToShippedButton} 
    Sleep    4s
    ${itemStatus}=    Get Text    ${shippedTag}
    Should Contain    ${itemStatus}    Shipped

Verify Payment Ledger Logs
    Wait Until Element Is Visible    ${paymentLedgerAccordion}
    Click Element    ${paymentLedgerAccordion} 
    #verify Payment Provider
    ${paymentProviderText}=    Get Text     ${paymentLedgerPaymentProvider}
    Should Contain     ${paymentProviderText}    Payflex

View Email Logs
    Scroll Element Into View    ${emailLogsAccordion}  
    Click Element   ${emailLogsAccordion}   
    Click Element   ${viewEmailBtn} 
    Wait Until Element Is Visible    ${emailView} 

View Order Items Information
    Wait Until Element Is Visible    ${orderItemsAccordion}
    ${orderItemStatusText}=    Get Text     ${orderItemStatus}
    Should Be Equal As Strings    ${orderItemStatusText}    Canceled
    ${orderItemCanceledByText}=    Get Text    ${orderItemCanceledBy}
    Should Be Equal As Strings    ${orderItemCanceledByText}    auto_cancel

Verify Show Items and Pagination
    Wait Until Element Is Visible    ${orderItemsShowItems}
    Click Element    ${orderItemsShowItems}
    Press Keys    ${None}    ARROW_UP
    Press Keys    ${None}    ARROW_UP
    Press Keys    ${None}    ENTER
    Sleep    1s
    Click Element    ${orderItemsPaginationPageTwo}

View Coupon History
    Wait Until Element Is Visible    ${couponHistoryAccordion}
    Scroll Element Into View    ${couponHistoryAccordion}
    Click Element    ${couponHistoryAccordion}
    Element Should Be Visible    ${couponCode}

Verify Delivery Tracking Information
    [Arguments]    ${heading}
    ${itemStatus}=   Get Text    ${deliveredTag} 
    Should Contain   ${itemStatus}    Delivered
    Click Element    ${orderFullfilmentAccordion}
    Scroll Element Into View  ${instructionDroppedDatetime}  
    Wait Until Element Is Visible    ${orderTrackingHeading}
    ${orderTrackingHeadingText}=    Get Text    ${orderTrackingHeading}
    Should Contain     ${orderTrackingHeadingText}    ${heading}
    ${signedByText}=    Get Text    ${signedBy}
    Should Contain   ${signedByText}  Signed by: Nqobani (Customer)
    ${instructionDatetimeText}=    Get Text    ${instructionDroppedDatetime}   
    Should Contain   ${instructionDatetimeText}  25 Aug 2024 @ 22:01
    ${shippedDatetimeText}=    Get Text   ${shippedFromWarehouseDatetime}
    Should Contain   ${shippedDatetimeText}  26 Aug 2024 @ 11:27
    ${deliveredToDatetimeText}=    Get Text    ${deliveredToCustomerDatetime}
    Should Contain   ${deliveredToDatetimeText}   30 Aug 2024 @ 9:34
    ${itemStatus}=   Get Text    ${deliveredTag} 
    Should Contain   ${itemStatus}    Delivered
    Click Element    ${orderFullfilmentAccordion}

Verify Waybill Tracking
   ${orderItemText}=    Get Text    ${orderItem} 
   Click Element    ${TrackBtn}
   Wait Until Element Is Visible    ${waybillNo}
   ${WayBillNoText}=    Get Text    ${waybillNo}
   Should Contain   ${WayBillNoText}   Waybill No: MDX133806010
   ${courierText}=    Get Text   ${courier}
   Should Contain   ${courierText}   Courier: Takealot Delivery Team
   Click Element    ${parcelBlock}  
   ${parcelOrderItemText}=    Get Text   ${parcel}
   Should Be Equal     ${orderItemText}   ${parcelOrderItemText}
   Should Contain   ${parcelOrderItemText}   Menggao - Baby Play Mat - Activity Gym & Ball Pit - Toys for Babies

Not Ready For Collection
   Click Element    ${orderFullfilmentAccordion}
   Wait Until Element Is Visible    ${orderTrackingHeading}
   ${isReadyText}=    Get Text    ${signedBy}
   Should Contain   ${isReadyText}  Note: We'll send you an SMS or email once your order is ready for collection
   ${estimateCollectionDateText}=    Get Text    ${estimatedCollectionDate}
   Should Contain   ${estimateCollectionDateText}   Estimated Collection from Wed, 4 Dec 2024
   Click Element    ${TrackBtn}
   ${waybillCollectionText}=    Get Text    ${waybillEstimateCollectionDate}
   Should Contain    ${waybillCollectionText}  NOT YET READY

Verify Refund History Information
    Wait Until Element Is Visible    ${refundHistoryAccordion}
    Click Element    ${refundHistoryAccordion}
    Scroll Element Into View   ${refundHistoryAccordion}
    ${refundedAmounText}=    Get Text    ${refundedAmount}
    Should Contain    ${refundedAmounText}    R 649.00
    ${refundedPaymentMethodText}=    Get Text    ${refundedPaymentMethod}
    Should Contain    ${refundedPaymentMethodText}    Credit card

Verify Delivery Address
    Click Element    ${orderFullfilmentAccordion}
    ${streetText}=    Get Text    ${streetAddress}
    Should Contain   ${streetText}  6 Birkenhead Road
    ${suburbText}=    Get Text    ${suburbAddress}   
    Should Contain   ${suburbText}  Umbilo
    ${cityText}=    Get Text   ${cityAddress}
    Should Contain   ${cityText}  Berea
    ${provinceText}=    Get Text    ${provinceAddress}
    Should Contain   ${provinceText}   KwaZulu-Natal
    ${codeText}=   Get Text    ${codeAddress} 
    Should Contain   ${codeText}    4075
    Click Element  ${copyAddressBtn} 
    ${addressCopiedText}=   Get Text    ${addressCopiedBtn}
    Should Contain  ${addressCopiedText}    Address copied!
    ${residentialText}=   Get Text    ${residentialTxt} 
    Should Contain  ${residentialText}    residential
    Click Element    ${orderFullfilmentAccordion}

Verify the Google Search 
    Wait Until Element Is Visible    ${searchGoogleIcon}    
    Click Element     ${searchGoogleIcon}   
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]

Verify Order Total on Canceled Order
    Wait Until Element Is Visible    ${orderFinancialsAccordion}
    Click Element    ${orderFinancialsAccordion}
    ${orderTotalAmountText}=    Get Text    ${orderTotalAmount}
    ${orderTotalAmountText}=    Remove String    ${orderTotalAmountText}    R${SPACE}
    Should Contain    ${orderTotalAmountText}    439.0

Verify Order Total on Return Item
    Wait Until Element Is Visible    ${orderFinancialsAccordion}
    Click Element    ${orderFinancialsAccordion}
    ${orderTotalAmountText}=    Get Text    ${orderTotalAmount}
    ${orderTotalAmountText}=    Remove String    ${orderTotalAmountText}    R${SPACE}
    Should Contain    ${orderTotalAmountText}    2,550.00

Verify Shipping Information
    Click Element    ${orderFullfilmentAccordion}
    ${methodText}=    Get Text   ${shippingMethod}  
    Should Contain   ${methodText}  Courier
    ${planText}=    Get Text    ${shippingPlan}    
    Should Contain   ${planText}  Standard
    ${courierText}=    Get Text   ${shippingCourier} 
    Should Contain   ${courierText}  MDX133806010 - Takealot Delivery Team
    ${promisedDateText}=    Get Text    ${shippingPromisedDate}
    Should Contain   ${promisedDateText}  28 Aug 2024
    ${deliveredDateText}=   Get Text    ${shippingDeliveredDate}
    Should Contain   ${deliveredDateText}   30 Aug 2024

Verify Multiple Waybill Tracking 
    Click Element    ${orderFullfilmentAccordion}
    Scroll Element Into View  ${instructionDroppedDate1}  
    Wait Until Element Is Visible    ${orderTrackingHeading1}
    ${orderTrackingHeading1Txt}=    Get Text    ${orderTrackingHeading1}
    Should Contain     ${orderTrackingHeading1Txt}    Delivered Thu, 30 May 2024
    ${signedByTxt}=    Get Text    ${signedBy1}
    Should Contain   ${signedByTxt}  Signed by: Slindile Mncwango (Customer)
    ${WayBillNoTxt}=    Get Text    ${waybillNumber1}
    Should Contain   ${WayBillNoTxt}   MDX127668689
    ${instructionDatetimeTxt}=    Get Text    ${instructionDroppedDate1}   
    Should Contain   ${instructionDatetimeTxt}  27 May 2024 @ 17:46
    ${shippedDatetimeTxt}=    Get Text   ${shippedFromWarehouseDate1}
    Should Contain   ${shippedDatetimeTxt}  28 May 2024 @ 1:31
    ${deliveredToDatetimeTxt}=    Get Text    ${deliveredDate1}
    Should Contain   ${deliveredToDatetimeTxt}   30 May 2024 @ 11:40
    Scroll Element Into View  ${instructionDroppedDate2}  
    ${signedByTxt}=    Get Text    ${signedBy2}
    Should Contain   ${signedByTxt}  Signed by Slindile Mncwango
    ${WayBillNoTxt}=    Get Text    ${waybillNumber2}
    Should Contain   ${WayBillNoTxt}   MDX127583371
    ${instructionDatetimeTxt}=    Get Text    ${instructionDroppedDate2}   
    Should Contain   ${instructionDatetimeTxt}  27 May 2024 @ 0:34
    ${shippedDatetimeTxt}=    Get Text   ${shippedFromWarehouseDate2}
    Should Contain   ${shippedDatetimeTxt}  27 May 2024 @ 17:46
    ${deliveredToDatetimeTxt}=    Get Text    ${deliveredDate2}
    Should Contain   ${deliveredToDatetimeTxt}   29 May 2024 @ 10:58 

Verify Waybill Link
   Click Element    ${orderFullfilmentAccordion}
   Scroll Element Into View   ${waybillNumberLink}  
   Click Element    ${waybillNumberLink} 
   Sleep    2s
   @{WindowHandles}=   Get Window Handles
   Sleep    2s
   WebAutomationFramework.Switch Window    ${WindowHandles}[1]
   Wait Until Element Is Visible   ${mrDexpressCopyright} 

Verify Order Tracking for Delivered Physical Products 
    Click Element    ${orderFullfilmentAccordion}  
    Scroll Element Into View   ${orderTrackingFirstConsignment}
    Wait Until Element Is Visible   ${firstConsigmentDeliveredDate}
    ${deliveredDatetimeTxt}=    Get Text   ${firstConsigmentDeliveredDate}
    Should Contain Any     ${deliveredDatetimeTxt}   Delivered Wed, 15 Dec 2021
    ${signedByTxt}=    Get Text    ${firstConsigmentSignedBy}
    Should Contain   ${signedByTxt}  Signed by: Trimira Chetty (Customer)
    ${wayBillNoTxt}=    Get Text    ${firstConsigmentWaybillNumber}
    Should Contain   ${wayBillNoTxt}   MDX69461955

Verify Partial Order Delivery 
    ${itemStatus}=   Get Text    ${deliveredTag} 
    Should Contain   ${itemStatus}    Delivered
    ${itemStatus}=   Get Text    ${cancelledTag} 
    Should Contain   ${itemStatus}    Canceled
    Click Element    ${orderFullfilmentAccordion}
    Scroll Element Into View  ${signedBy1}
    ${orderTrackingHeadingTxt}=    Get Text   ${partDeliveredDate}
    Should Contain     ${orderTrackingHeadingTxt}    Delivered Mon, 19 Sep 2022
    ${signedByTxt}=    Get Text    ${signedBy1}
    Should Contain   ${signedByTxt}  Signed by: Slindile Mncwango (Customer)
    Scroll Element Into View   ${cancelledItems} 
    ${CancelledItemsTxt}=    Get Text     ${cancelledItems}
    Should Contain   ${CancelledItemsTxt}   Cancelled Item(s)

Verify IP Address
   Click Element   ${ipAddressIcon} 
   Wait Until Element Is Visible   ${ipAddressModel} 
   ${ipAddressTxt}   Get Value    ${ipAddress}    
   Should Contain    ${ipAddressTxt}    41.115.115.60

Hover Over CustomerID
    Wait Until Element Is Visible     ${custAccNumber}  
    Mouse Over   ${custAccNumber} 
    Wait Until Element Is Visible   ${custInfoPop-up}

Verify Customer Info    
    ${CustNamePopupTxt}=    Get Text   ${custNamePopup}
    Should Contain  ${CustNamePopupTxt}    Slindile Mncwango 
    ${custDateRegisteredTxt}=    Get Text   ${custDateRegistered}  
    Should Contain   ${custDateRegisteredTxt}   16-Oct-2018 @ 10:41
    ${custBlaclistStatusCheck}=    Get Text    ${custBlacklistStatus} 
    Should Contain     ${custBlaclistStatusCheck}    Not Blacklisted

Verify Order Shipping Info 
    Click Element    ${orderFullfilmentAccordion}  
    Scroll Element Into View   ${orderTrackingFirstConsignment}
    Wait Until Element Is Visible   ${firstConsigmentTrackBtn}
    Click Element    ${firstConsigmentTrackBtn}
    Sleep    2s
    ${trackingWaybillNumberTxt}=    Get Text    ${trackingWaybillNumber}
    Should Contain    ${trackingWaybillNumberTxt}    MDX144323298
    Click Element    ${trackingFirstParcelInfo}
    ${trackingFirstParcelNumberTxt}=    Get Text    ${trackingFirstParcelNumber}
    Should Contain    ${trackingFirstParcelNumberTxt}    Parcel - S057933520
    ${trackingFirstParcelItemTxt}=    Get Text    ${trackingFirstParcelItem} 
    Should Contain    ${trackingFirstParcelItemTxt}    1 × Flaming Thai Sauces - 4 Asian Flavour Mixed Pack

Filter By Collect Shipping Method and Daily Deals
    Click Element    ${orderListClearFilterButton}
    Click Element    ${DailyDealsCheckbox}
    Click Element    ${past10DaysDateRangeCheckbox}
    Wait Until Element Is Visible    ${OrderListTable}
    Click Element    ${ShippingMethodDropdown}
    Click Element    ${ShippingMethodCollect}
    Click Element    ${AuthStatusDropdown}
    Click Element    ${AuthStatusAuth}
    ${SelectedStatus}   Get Text   ${AuthStatusDropdown}
    Click Element    ${OrderListApplyFilterButton}
    ${authstatus_elements}    Get WebElements    ${AllAuthStatusColumns}
        FOR    ${element}    IN    ${authstatus_elements}
            Element Should Contain    ${element}    ${SelectedStatus}
        END
    Click Element    ${OrderListApplyFilterButton}
    Click Element    ${orderListFirstNewStatusOrder}
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]


Verify Collection Not Yet Ready
    Wait Until Element Is Visible    ${orderFullfilmentAccordion} 
    Click Element    ${orderFullfilmentAccordion} 
    ${collectionEstimateDateText} =  Get text  ${collectionEstimateDate} 
    Should Contain    ${collectionEstimateDateText}    Estimated Collection from
    ${collectionNotYetReadyMessageText} =  Get text  ${collectionNotYetReadyMessage}
    Should Contain    ${collectionNotYetReadyMessageText}   NOT YET READY

Filter By Courier Shipping Method and Daily Deals
    Click Element    ${DailyDealsCheckbox}
    Wait Until Element Is Visible    ${OrderListTable}
    Click Element    ${ShippingMethodDropdown}
    Click Element    ${ShippingMethodCourier} 
    Click Element    ${AuthStatusDropdown}
    Click Element    ${AuthStatusAuth}
    ${SelectedStatus}   Get Text   ${AuthStatusDropdown}
    Click Element    ${OrderListApplyFilterButton}
    ${authstatus_elements}    Get WebElements    ${AllAuthStatusColumns}
        FOR    ${element}    IN    ${authstatus_elements}
            Element Should Contain    ${element}    ${SelectedStatus}
        END
    Click Element    ${orderListFirstNewStatusOrder}
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]    
    
Verify Delivery Not Yet Shipped
    Wait Until Element Is Visible    ${orderFullfilmentAccordion} 
    Click Element    ${orderFullfilmentAccordion} 
    ${deliveryEstimateDateText} =  Get text  ${deliveryEstimateDate} 
    Should Contain      ${deliveryEstimateDateText}   Delivery by ------
    ${deliveryNotYetReadyMessageText} =  Get text  ${deliveryNotYetReadyMessage}
    Should Contain    ${deliveryNotYetReadyMessageText}   NOT YET SHIPPED
