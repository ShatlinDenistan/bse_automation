*** Variables ***

# Search
${searchBar}    xpath=//div[@id='root']
${txtSearch}    xpath=//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/input[1]
${ddlSearch}    xpath=//div[contains(text(),'-- all --')]
${ddlCustomer}    xpath=//span[contains(text(),'Customer')]
${ddlOrder}    xpath=//span[contains(text(),'Order Number')]
${btnSearchButton}    xpath=//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/button[1]
