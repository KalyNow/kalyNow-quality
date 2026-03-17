*** Settings ***
Documentation    Reusable keywords for authentication flows.
...              Import this resource in any test that needs login/logout.
Library          SeleniumLibrary
Resource         ../pages/login_page.robot
Resource         ../pages/home_page.robot


*** Keywords ***
Open Browser And Go To Login Page
    [Documentation]    Open the browser and navigate to the login page.
    Open Browser    ${WEB_URL}/login    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    ${LOGIN_EMAIL_INPUT}

Login With Credentials
    [Documentation]    Fill in and submit the login form.
    [Arguments]    ${email}    ${password}
    Input Text          ${LOGIN_EMAIL_INPUT}       ${email}
    Input Text          ${LOGIN_PASSWORD_INPUT}    ${password}
    Click Element       ${LOGIN_SUBMIT_BUTTON}

Verify Login Success
    [Documentation]    Assert that the user has been redirected to the home page.
    Wait Until Page Contains Element    ${HOME_WELCOME_MESSAGE}
    Page Should Contain Element         ${HOME_WELCOME_MESSAGE}

Close Browser Session
    [Documentation]    Close the browser at the end of a test.
    Close Browser
