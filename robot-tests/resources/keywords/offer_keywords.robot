*** Settings ***
Documentation    Reusable keywords for offer management flows.
...              Import this resource in any test that involves creating or viewing offers.
Library          SeleniumLibrary
Resource         ../pages/home_page.robot


*** Keywords ***
Navigate To Create Offer Page
    [Documentation]    Click the "Create Offer" button on the home page.
    Click Element    ${HOME_CREATE_OFFER_BUTTON}
    Wait Until Page Contains Element    ${OFFER_TITLE_INPUT}

Fill Offer Form
    [Documentation]    Fill in the offer creation form.
    [Arguments]    ${title}    ${description}    ${discount}
    Input Text    ${OFFER_TITLE_INPUT}          ${title}
    Input Text    ${OFFER_DESCRIPTION_INPUT}    ${description}
    Input Text    ${OFFER_DISCOUNT_INPUT}       ${discount}

Submit Offer Form
    [Documentation]    Submit the offer creation form.
    Click Element    ${OFFER_SUBMIT_BUTTON}

Verify Offer Created
    [Documentation]    Assert that the offer was created successfully.
    Wait Until Page Contains    Offer created successfully
