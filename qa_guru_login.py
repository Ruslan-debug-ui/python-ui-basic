import time

from selene import browser, have


def test_valid_login():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('somepasshere').press_enter()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))

    browser.quit()


def test_wrong_password():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com')
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))

    browser.quit()


def test_empty_password():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=email]').type('qagurubot@gmail.com').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))

    browser.quit()


def test_empty_login():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('[name=password]').type('assdaff').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))

    browser.quit()

def test_google():
    browser.open('https://google.com')
    browser.element('textarea#APjFqb').type('yashaka/selene').press_enter()


def test_tvi_wrong_login_and_passwd():
    browser.open('https://tvindex-release-1-1.stage-ingress.mediascope.net')
    browser.element('[name=username]').type('yashaka/selene')
    browser.element('[name=password]').type('yashaka/selene').press_enter()
    browser.element('.fcUAKQ.jqmkso.sc-brqgnP.sc-fMiknA').should(have.text('Invalid user credential'))
    #time.sleep(5)

def test_tvi_login():
    browser.open('https://tvindex-release-1-1.stage-ingress.mediascope.net')
    browser.element('[name=username]').type('front_test')
    browser.element('[name=password]').type('Vlas2!@on').press_enter()
    browser.element('.kkXdPA.sc-pIjat').should(have.text('TV Index UI 1.1.0'))
    #time.sleep(5)

def test_initial_page():
    browser.open('https://tvindex-release-1-1.stage-ingress.mediascope.net')
    browser.element('div#root > .hIGHoI.sc-pLyGp').should(have.text('Version: 295545'))
    #time.sleep(1000)

def test_initial_page_1():
    browser.open('https://tvindex-release-1-1.stage-ingress.mediascope.net')
    browser.element(".sc-caSCKo").should(have.text('Авторизация'))