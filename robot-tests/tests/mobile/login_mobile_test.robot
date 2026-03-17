*** Settings ***
Documentation    Mobile login test for KalyNow using Appium.
...
...              This is a placeholder showing how to structure a mobile test.
...              Configure APPIUM_URL, PLATFORM_NAME, DEVICE_NAME, and APP_PATH
...              in your .env file before running.
Library          AppiumLibrary

Suite Teardown   Close Application


*** Variables ***
${APPIUM_URL}       http://localhost:4723/wd/hub
${PLATFORM_NAME}    Android
${DEVICE_NAME}      emulator-5554
${APP_PATH}         /path/to/kalyNow.apk
${VALID_EMAIL}      test@example.com
${VALID_PASSWORD}   TestPassword123!


*** Test Cases ***
Mobile Login With Valid Credentials
    [Documentation]    A registered user should be able to log in via the mobile app.
    [Tags]    smoke    login    mobile
    Open Application
    ...    ${APPIUM_URL}
    ...    platformName=${PLATFORM_NAME}
    ...    deviceName=${DEVICE_NAME}
    ...    app=${APP_PATH}
    ...    automationName=UiAutomator2
    Wait Until Page Contains Element    id=email_input
    Input Text    id=email_input       ${VALID_EMAIL}
    Input Text    id=password_input    ${VALID_PASSWORD}
    Click Element    id=login_button
    Wait Until Page Contains Element    id=home_screen
    Page Should Contain Element    id=home_screen
