from pages.base import WebPage
from pages.elements import WebElement
import pickle

class AccountPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.onlinetrade.ru/member/'
        super().__init__(web_driver, url)

        with open('cookies.tmp', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            web_driver.add_cookie(cookie)
        web_driver.refresh()

    email=WebElement(xpath='//span[@class="userInfo__itemData"]')
    member_edit=WebElement(xpath='//a[@title="Личные данные"]')
    member_status=WebElement(xpath='//a[@title="Статус клиента "]')
    edit_passw=WebElement(xpath='//a[@title="Смена пароля"]')
    adresses=WebElement(xpath='//a[@title="Адреса доставки"]')
    orders=WebElement(xpath='//a[@title="Заказы"]')
    exit=WebElement(xpath='//a[@title="Выйти из профиля"]')