# python -m pytest -v --driver Chrome --driver-path C:\Users\Irina\PycharmProjects\ControlProject\chromedriver.exe tests\test_account_page.py
# 6 тестов

from pages.account_page import AccountPage

def test_member_edit_link(web_browser):
    """при клике на ссылку "Личные данные" происходит переход на соответствущую страницу"""
    page = AccountPage(web_browser)
    page.member_edit.click()
    assert page.get_relative_link()=='/member/edit.html','Ссылка "Личные данные" не ведет на соответствующую страницу'

def test_member_status_link(web_browser):
    """при клике на ссылку "Статус клиента" происходит переход на соответствущую страницу"""
    page = AccountPage(web_browser)
    page.member_status.click()
    assert page.get_relative_link()=='/member/vip_status.html','Ссылка "Статус клиента" не ведет на соответствующую страницу'

def test_edit_pass_link(web_browser):
    """при клике на ссылку "Смена пароля" происходит переход на соответствущую страницу"""
    page = AccountPage(web_browser)
    page.edit_passw.click()
    assert page.get_relative_link()=='/member/change_password.html','Ссылка "Смена пароля" не ведет на соответствующую страницу'

def test_adresses_link(web_browser):
    """при клике на ссылку "Адреса доставки" происходит переход на страницу с адресами доставки"""
    page = AccountPage(web_browser)
    page.adresses.click()
    assert page.get_relative_link()=='/member/addresses_list.html','Ссылка "Адреса доставки" не ведет на соответствующую страницу'

def test_orders_link(web_browser):
    """при клике на ссылку "Мои заказы" происходит переход на соответствущую страницу"""
    page = AccountPage(web_browser)
    page.orders.click()
    assert page.get_relative_link()=='/member/orders.html','Ссылка "Мои заказы" не ведет на соответствующую страницу'

def test_exit_link(web_browser):
    """при клике на ссылку "Выход" происходит переход на страницу входа в акакунт"""
    page = AccountPage(web_browser)
    page.exit.click()
    assert page.get_relative_link()=='/member/login.html','Ссылка "Выход" не ведет на страницу входа в аккаунт'