*** Settings ***
Documentation    Web login tests for KalyNow.
...
...              Verifies that a valid user can log in successfully
...              and that invalid credentials show an error.
Library          SeleniumLibrary
Resource         ../../resources/keywords/auth_keywords.robot

Suite Teardown   Close Browser Session


*** Variables ***
${WEB_URL}      http://localhost:3000
${BROWSER}      chrome
${VALID_EMAIL}      test@example.com
${VALID_PASSWORD}   TestPassword123!


*** Test Cases ***
Login With Valid Credentials
    [Documentation]    A registered user should be redirected to the home page after login.
    [Tags]    smoke    login    web
    Open Browser And Go To Login Page
    Login With Credentials    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Login Success

Login With Invalid Password
    [Documentation]    An invalid password should show an error message on the login page.
    [Tags]    negative    login    web
    Open Browser And Go To Login Page
    Login With Credentials    ${VALID_EMAIL}    wrong_password
    Wait Until Page Contains Element    ${LOGIN_ERROR_MESSAGE}
    Page Should Contain Element         ${LOGIN_ERROR_MESSAGE}
