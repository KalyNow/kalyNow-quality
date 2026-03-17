*** Settings ***
Documentation    Login page locators and low-level actions.
...              This file defines all selectors for the login page UI.
Library          SeleniumLibrary


*** Variables ***
${LOGIN_EMAIL_INPUT}        id=email
${LOGIN_PASSWORD_INPUT}     id=password
${LOGIN_SUBMIT_BUTTON}      id=login-submit
${LOGIN_ERROR_MESSAGE}      id=login-error
