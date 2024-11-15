*** Settings ***
Library  SeleniumLibrary
Resource  resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${HOME_URL}  http://localhost:5001

*** Test Cases ***

When counter is set to a specific value it shows on the page
    Go To  ${HOME_URL}
    Click Button  Nollaa
    Page Should Contain  nappia painettu 0 kertaa
    Input Text  name=new_value  10
    Click Button  aseta
    Page Should Contain  nappia painettu 10 kertaa