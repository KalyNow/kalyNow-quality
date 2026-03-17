*** Settings ***
Documentation    Home page locators and low-level actions.
...              This file defines all selectors for the main home page UI.
Library          SeleniumLibrary


*** Variables ***
${HOME_WELCOME_MESSAGE}       id=welcome-message
${HOME_CREATE_OFFER_BUTTON}   id=create-offer-btn
${OFFER_TITLE_INPUT}          id=offer-title
${OFFER_DESCRIPTION_INPUT}    id=offer-description
${OFFER_DISCOUNT_INPUT}       id=offer-discount
${OFFER_SUBMIT_BUTTON}        id=offer-submit
