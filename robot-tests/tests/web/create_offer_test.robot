*** Settings ***
Documentation    Web test: create an offer after logging in.
...
...              Verifies that an authenticated user can navigate to the
...              offer creation form and successfully publish a new offer.
Library          SeleniumLibrary
Resource         ../../resources/keywords/auth_keywords.robot
Resource         ../../resources/keywords/offer_keywords.robot

Suite Setup      Open Browser And Go To Login Page
Suite Teardown   Close Browser Session


*** Variables ***
${WEB_URL}          http://localhost:3000
${BROWSER}          chrome
${VALID_EMAIL}      test@example.com
${VALID_PASSWORD}   TestPassword123!


*** Test Cases ***
Create Offer As Authenticated User
    [Documentation]    After login, the user should be able to create a new offer.
    [Tags]    smoke    offer    web
    Login With Credentials    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Login Success
    Navigate To Create Offer Page
    Fill Offer Form
    ...    title=Happy Hour Deal
    ...    description=50% off all drinks from 5pm to 7pm
    ...    discount=50
    Submit Offer Form
    Verify Offer Created
