# 7 тестов
# для запуска тестов необходимо выполнить в терминале команду:
# python -m pytest -v --driver Chrome --driver-path C:\Users\Irina\PycharmProjects\SmartPageObject\chromedriver.exe tests\test_auth_page.py
from pages.auth_page import AuthPage
from pages.account_page import AccountPage
from tests.data import correct_email,correct_pass,incorrect_email,incorrect_pass
import pytest

def test_authorisation_with_correct_data(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert page.get_relative_link()=='/member/','При вводе в поля формы авторизации корректных данных действующего пользователя не происходит вход в аккаунт'

@pytest.mark.parametrize("email",list(incorrect_email.keys())[0:2],
                         ids=list(incorrect_email.values())[0:2])
def test_auth_with_empty_email(web_browser,email):
    """при вводе в поле для email пустого значения или пробела происходит переход на страницу с сообщением об ошибке"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert 'Вы не указали информацию для входа' in page.get_page_source()

@pytest.mark.xfail
@pytest.mark.parametrize("email",list(incorrect_email.keys())[2:],
                         ids=list(incorrect_email.values())[2:])
def test_auth_with_uncorrect_email(web_browser,email):
    """при вводе в поле для ввода email некорректного значения происходит переход на страницу с сообщением об ошибке
    тест помечен как падающий, т.к. при вводе букв русского алфавита появляется сообщение о том, что не указана информация для входа"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()

@pytest.mark.parametrize("passw",list(incorrect_pass.keys())[0:2],
                         ids=list(incorrect_pass.values())[0:2])
def test_auth_with_empty_pass(web_browser,passw):
    """при вводе в поле для пароля пустого значения или пробела появляется сообщение об ошибке"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(passw)
    page.login_button.click()
    assert 'Вы не указали информацию для входа' in page.get_page_source()

@pytest.mark.parametrize("passw",list(incorrect_pass.keys())[2:],
                         ids=list(incorrect_pass.values())[2:])
def test_auth_with_incorrect_pass(web_browser,passw):
    """при вводе в поле для ввода пароля некорректного значения пробела происходит переход на страницу с сообщением об ошибке"""
    page = AuthPage(web_browser)
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(passw)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()

def test_forget_pass(web_browser):
    """при клике на ссылку "Забыли пароль?" происходит переход на страницу восстановления пароля"""
    page = AuthPage(web_browser)
    page.forget_pass.click()
    assert page.get_relative_link()=='/member/restore.html','При клике на ссылку "Забыли пароль?" не происходит переход на страницу восстановления пароля'

def test_reg_button(web_browser):
    """при клике на ссылку "Зарегистрироваться" происходит переход на страницу регистрации"""
    page = AuthPage(web_browser)
    page.reg_button.click()
    assert page.get_relative_link()=='/member/register.html','При клике на ссылку "Зарегистрироваться" не происходит переход на страницу регистрации'