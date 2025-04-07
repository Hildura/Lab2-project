*** Settings ***
Library    DatabaseLibrary
Library    OperatingSystem

Suite Setup    Yhdista Tietokantaan
Suite Teardown    Sulje Yhteys

*** Variables ***
${DB_HOST}       localhost
${DB_NAME}       verkkokauppa
${DB_USER}       admin
${DB_PASSWORD}   salasana123
${DB_PORT}       5432
${DB_TYPE}       PostgreSQL

*** Keywords ***
Yhdista Tietokantaan
    Log    Yhdistetään tietokantaan: ${DB_NAME} käyttäjällä ${DB_USER}
    Connect To Database Using Custom Params    ${DB_TYPE}    ${DB_NAME}    ${DB_USER}    ${DB_PASSWORD}    ${DB_HOST}    ${DB_PORT}
    Log    Tietokantayhteys onnistui!

Sulje Yhteys
    Log    Suljetaan tietokantayhteys...
    Disconnect From Database
    Log    Yhteys suljettu.

*** Test Cases ***
Testaa Tietokantayhteys
    Log    Testataan tietokantayhteyttä...
    ${tulos}=    Query    SELECT * FROM tuotteet WHERE tuoteryhma = 'Suojakuoret';
    Log    Tuotteita löydetty: ${tulos}
