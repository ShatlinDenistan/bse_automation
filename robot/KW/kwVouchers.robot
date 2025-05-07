*** Settings ***
Resource    ../Config/defaultConfig.robot
Resource    ../OR/orVouchers.robot

*** Keywords ***

Navigate To Vouchers
    Click Element    ${menuBtn}
    Click Element    ${vouchersMenuOption} 
    Wait Until Page Contains Element    ${resultsTable} 

Filter By Redeemed And Paid Status
    Wait Until Element Is Visible    ${resultsTable} 
    Click Element    ${redeemedStatusDropdown}  
    Click Element    ${redeemedStatusAvailable}  
    Click Element    ${paidStatusDropdown}  
    Click Element    ${paidStatusOption}  
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${redeemedStatus_elements}    Get WebElements    ${AllOrderStatusColumns} 
        FOR    ${element}    IN    ${redeemedStatus_elements}
            Element Should Contain    ${element}    Available
        END
    ${paidStatus_elements}    Get WebElements    ${AllOrderPaidColumns}
        FOR    ${element}    IN    ${paidStatus_elements}
            Element Should Contain    ${element}    True
        END

Select And Cancel A Voucher
    Click Element     ${orderIDCheckBox}
    Click Element     ${expireBtn}
    Wait Until Element Is Visible    ${verificationMessage}
    Click Element    ${closeIcon}

Filter By Canceled Redeem Status
    Wait Until Element Is Visible    ${resultsTable} 
    Click Element    ${redeemedStatusDropdown}  
    Click Element    ${redeemedStatusCancelled}  
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${redeemedStatus_elements}    Get WebElements    ${AllOrderStatusColumns} 
        FOR    ${element}    IN    ${redeemedStatus_elements}
            Element Should Contain    ${element}    Cancelled
        END

Select And Activate A Voucher
    ${voucherCodeText}    Get Text    ${voucherCode}
    Set Global Variable    ${voucherCodeText} 

    Click Element     ${orderIDCheckBox}
    Click Element     ${activeBtn}
    Click Element     ${activeVoucherBtn}
    Wait Until Element Is Visible    ${verifyActivatedVoucher}
    Click Element    ${closeIcon}


Verify Voucher Status
    Wait Until Element Is Visible    ${clearFilter}    ${MAX_TIMEOUT} 
    Scroll Element Into View    ${clearFilter}
    Click Element    ${clearFilter}

    Wait Until Element Is Visible    ${filterByField}
    Click Element    ${filterByField}
    Click Element    ${filterByVoucherCode}
    Log To Console    ${voucherCodeText}

    Input Text       ${searchTermField}   ${voucherCodeText}
    Click Element    ${applySearchFilter}
    Element Should Contain    ${voucherStatus}    Available

Filter By Not Paid Status
    Wait Until Element Is Visible    ${resultsTable} 
    Click Element    ${paidStatusDropdown}  
    Click Element    ${notPaidStatusOption}    
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${paidStatus_elements}    Get WebElements    ${AllOrderPaidColumns}
        FOR    ${element}    IN    ${paidStatus_elements}
            Element Should Contain    ${element}    False
        END

Select And Update To Paid
    ${voucherCodeText}    Get Text    ${voucherCode}
    Click Element     ${orderIDCheckBox}
    Click Element     ${paidBtn} 
    Wait Until Element Is Visible    ${verificationMessage}
    Click Element    ${closeIcon}

    Wait Until Element Is Visible    ${clearFilter}    ${MAX_TIMEOUT} 
    Scroll Element Into View    ${clearFilter}
    Click Element    ${clearFilter}

    Wait Until Element Is Visible    ${filterByField}
    Click Element    ${menuBtn}
    Click Element    ${filterByField}
    Click Element    ${filterByVoucherCode}
    Log To Console    ${voucherCodeText}

    Input Text       ${searchTermField}   ${voucherCodeText}
    Click Element    ${applySearchFilter}
    Element Should Contain    ${paidStatus}     True

Filter By Paid Status
    Wait Until Element Is Visible    ${resultsTable}  
    Click Element    ${paidStatusDropdown}  
    Click Element    ${paidStatusOption}  
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${paidStatus_elements}    Get WebElements    ${AllOrderPaidColumns}
        FOR    ${element}    IN    ${paidStatus_elements}
            Element Should Contain    ${element}  True  
        END

Select And Update To Not Paid
    ${voucherCodeText}    Get Text    ${voucherCode}
    Click Element     ${orderIDCheckBox}
    Click Element     ${notPaidBtn} 
    Wait Until Element Is Visible    ${verificationMessage}
    Click Element    ${closeIcon}

    Wait Until Element Is Visible    ${clearFilter}    ${MAX_TIMEOUT} 
    Scroll Element Into View    ${clearFilter}
    Click Element    ${clearFilter}

    Wait Until Element Is Visible    ${filterByField}
    Click Element    ${menuBtn}
    Click Element    ${filterByField}
    Click Element    ${filterByVoucherCode}
    Log To Console    ${voucherCodeText}

    Input Text       ${searchTermField}   ${voucherCodeText}
    Click Element    ${applySearchFilter}
    Element Should Contain    ${paidStatus}     False

Filter By Date Range
    Click Element    ${clearFilter}
    Click Element    ${DateFilter}
    Input Text       ${DateFilter}    01-05-2024 - 31-05-2024
    Click Element    ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row}    IN RANGE    1    ${row_count + 1}
               ${locator} =    Set Variable    //tbody/tr[${row}]/td[3]
               ${element_text} =    Get Text    ${locator}
               Should Contain    ${element_text}    May-2024
        END

Filter By Voucher Category
    Wait Until Element Is Visible    ${resultsTable}  
    Click Element    ${voucherCategoryDropdown}
    Click Element    ${voucherCategoryCV}
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${voucherCategory_elements}    Get WebElements     ${voucherCategoryList} 
        FOR    ${element}    IN    ${voucherCategory_elements} 
            Element Should Contain    ${element}  Corporate Voucher  
        END

Filter By Redeemed Status
    Wait Until Element Is Visible    ${resultsTable}  
    Click Element    ${redeemedStatusDropdown}
    Click Element    ${redeemedStatusRedeemed}
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${redeemedStatus_elements}    Get WebElements     ${redeemedStatusList} 
        FOR    ${element}    IN    ${redeemedStatus_elements} 
            Element Should Contain    ${element}  Redeemed 
        END

Filter By Multiple Filter Options
    Wait Until Element Is Visible    ${resultsTable} 
    Click Element    ${DateFilter}
    Input Text       ${DateFilter}    01-05-2024 - 31-05-2024

    Click Element    ${voucherCategoryDropdown}
    Click Element    ${voucherCategoryCV} 

    Click Element    ${redeemedStatusDropdown}
    Click Element    ${redeemedStatusCancelled}


    Click Element    ${paidStatusDropdown}  
    Click Element    ${paidStatusOption}  
  
    Click Element    ${applySearchFilter}
    Wait Until Element Is Visible    ${resultsTable}   ${MAX_TIMEOUT} 
    ${redeemedStatus_elements}    Get WebElements     ${redeemedStatusList} 
        FOR    ${element}    IN    ${redeemedStatus_elements} 
            Element Should Contain    ${element}  Cancelled  
        END  

    ${voucherCategory_elements}    Get WebElements     ${voucherCategoryList} 
        FOR    ${element}    IN    ${voucherCategory_elements} 
            Element Should Contain    ${element}  Corporate Voucher  
        END 

    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row}    IN RANGE    1    ${row_count + 1}
               ${locator} =    Set Variable    //tbody/tr[${row}]/td[3]
               ${element_text} =    Get Text    ${locator}
               Should Contain    ${element_text}    May-2024
        END

    ${paidStatus_elements}    Get WebElements    ${AllOrderPaidColumns}
        FOR    ${element}    IN    ${paidStatus_elements}
            Element Should Contain    ${element}  True  
        END


Filter Using Order ID
    ${orderID}    Get Text    ${voucherOrderID}
    Click Element     ${filterByField} 
    Click Element     ${searchCriteriaOptionOrderID}
    Input Text        ${searchTermField}   ${orderID}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row}    IN RANGE    1    ${row_count + 1}
               ${locator} =    Set Variable    //tbody/tr[${row}]/td[2]
               ${element_text} =    Get Text    ${locator}
               Should Contain    ${element_text}    ${orderID}
        END
        
Filter By Voucher Code
    ${voucherCode}    Get Text    ${voucherCodeID}
    Click Element     ${filterByField} 
    Click Element     ${filterByVoucherCode} 
    Input Text        ${searchTermField}   ${voucherCode}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    WebAutomationFramework.Get Element Count   ${ResultsTable}  
        FOR    ${row}    IN RANGE    1    ${row_count + 1}
               ${locator} =    Set Variable    //tbody/tr[${row}]/td[6]
               ${element_text} =    Get Text    ${locator}
               Should Contain    ${element_text}    ${voucherCode} 
        END

Filter Using Customer ID
    ${customerName}    Get Text    ${openCustomerInfo} 
    Click Element     ${openCustomerInfo} 
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${customerID}  Get Text    ${customerinfo} 
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    Click Element     ${filterByField} 
    Click Element     ${filterByCustomerID}
    Input Text        ${searchTermField}   ${customerID}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    Get WebElements    ${openCustomerInfo}
        FOR    ${element}    IN    ${row_count}
            Element Should Contain    ${element}  ${customerName} 
        END

 Filter By Used By Customer ID
    ${customerName}    Get Text    ${openUsedByCustomerInfo} 
    Click Element     ${openUsedByCustomerInfo}  
    Sleep    2s
    @{WindowHandles}=   Get Window Handles
    Sleep    2s
    WebAutomationFramework.Switch Window    ${WindowHandles}[1]
    ${customerID}  Get Text    ${customerinfo} 
    WebAutomationFramework.Switch Window    ${WindowHandles}[0]
    Click Element     ${filterByField} 
    Click Element     ${filterByUsedByCustomerID}
    Input Text        ${searchTermField}   ${customerID}
    Click Element     ${ApplyFilterBtn}
    ${row_count}    Get WebElements    ${openUsedByCustomerInfo}
        FOR    ${element}    IN    ${row_count}
            Element Should Contain    ${element}  ${customerName} 
        END

Select and Send Email
    Wait Until Element Is Visible    ${orderIDCheckBox}
    Click Element    ${orderIDCheckBox}
    Wait Until Element Is Visible    ${emailBtn}
    Click Element    ${emailBtn}  

Verify Email Was Sent Successfully
    ${EmailSentText}    Get Text    ${EmailSentModal}

    Sleep    2s
    Page Should Contain Element     xpath=//div[contains(text(),'Successfully processed')]

    Click Element    ${emailSentModalCloseIcon}