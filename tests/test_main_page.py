# 37 тестов
# python -m pytest -v --driver Chrome --driver-path C:\Users\Irina\PycharmProjects\ControlProject\chromedriver.exe tests\test_main_page.py

from pages.main_page import MainPage
from pages.elements import ManyWebElements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from tests.data import correct_email,correct_pass,incorrect_email,incorrect_pass,correct_product,incorrect_product_title,other_value_for_search
import pytest
import random
driver=webdriver.Chrome()


def test_how_to_pay_link(web_browser):
    """при клике на ссылку "Как купить" происходит переход на соответствующую страницу"""
    page = MainPage(web_browser)
    page.how_to_pay.click()
    assert page.get_relative_link()=='/info/delivery.html','Ссылка "Как купить" не ведет на соответствующую страницу'

def test_club_bonus_link(web_browser):
    """при клике на ссылку "Клуб ON бонус" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.club_bonus.click()
    assert page.get_relative_link()=='/club/','Ссылка "Клуб ON бонус" не ведет на соответствующую страницу'

def test_help_link(web_browser):
    """при клике на ссылку "Помощь" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.help.click()
    assert page.get_relative_link()=='/feedback/','Ссылка "Помощь" не ведет на соответствующую страницу'

def test_warranty_link(web_browser):
    """при клике на ссылку "Гарантии" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.warranty.click()
    assert page.get_relative_link()=='/info/garantii.html','Ссылка "Гарантии" не ведет на соответствующую страницу'

def test_points_of_issue_link(web_browser):
    """Пункты выдачи"""
    page = MainPage(web_browser)
    page.points_of_issue.click()
    assert '/shops/' in page.get_current_url(),'Ссылка "Пункты выдачи" не ведет на соответствующую страницу'

def test_for_business_link(web_browser):
    """при клике на ссылку "Для бизнеса" происходит переход на соответствущую страницу"""
    page = MainPage(web_browser)
    page.for_business.click()
    assert page.get_relative_link()=='/info/beznal.html','Ссылка "Для бизнеса" не ведет на соответствующую страницу'

def test_logo_link(web_browser):
    """при клике на логотип "ОнлайнТрейд" происходит переход на главную страницу сайта"""
    page = MainPage(web_browser)
    page.main_logo.click()
    assert page.get_current_url() == 'https://www.onlinetrade.ru/','При нажатии на логотип "ОнлайнТрейд" не происходит перехода на главную страницу сайта'

def test_drop_menu_catalog_link(web_browser):
    """при клике на кнопку "Каталог" открывается выпадающее меню с видами товаров"""
    page = MainPage(web_browser)
    page.catalog.click()
    res=page.categoty_menu.find().is_displayed()
    assert res,'Кнопка "Каталог" не вызывает выпадающее меню'

def test_actions_link(web_browser):
    """при нажатии на кнопку "Скидки" происходит переход на страницу со скидками"""
    page = MainPage(web_browser)
    page.discounts.click()
    assert page.get_relative_link() == '/actions/','Нажатие на кнопку "Скидки" не ведет на страницу со скидками'

def test_auth_form_link(web_browser):
    """при клике на кнопку входа происходит переход к форме для ввода логина и пароля"""
    page = MainPage(web_browser)
    page.auth_button.click()
    res=page.auth_form.find().is_displayed()
    assert res,'При нажатии на кнопку авторизации не происходит переход к форме авторизации'

def test_bookmarks(web_browser):
    """при клике на логотип "Закладки" происходит переход на страницу с закладками"""
    page = MainPage(web_browser)
    page.bookmarks.click()
    assert page.get_relative_link() == '/bookmarks.html', 'Нажатие на кнопку "Закладки" не ведет на страницу с закладками'

def test_basket(web_browser):
    """при клике на логотип "Корзина" происходит переход на страницу корзины"""
    page = MainPage(web_browser)
    page.basket.click()
    assert page.get_relative_link() == '/basket.html', 'Нажатие на кнопку "Корзина" не ведет на страницу корзины'

def test_all_promotions(web_browser):
    """при клике на ссылку "Все акции" происходит переход на страницу акций"""
    page = MainPage(web_browser)
    page.all_promotions.click()
    assert page.get_relative_link() == '/actions/', 'Клик на ссылку "Все акции" не ведет на страницу акций'

def test_all_brands(web_browser):
    """при клике на ссылку "Все бренды" происходит переход на страницу брендов"""
    page = MainPage(web_browser)
    page.all_brands.click()
    assert page.get_relative_link() == '/brands/', 'Клик на ссылку "Все бренды" не ведет на страницу брендов'

def test_all_news(web_browser):
    """при клике на ссылку "Все новости" происходит переход на страницу новостей"""
    page = MainPage(web_browser)
    page.all_news.click()
    assert page.get_relative_link() == '/news/', 'Клик на ссылку "Все новости" не ведет на страницу новостей'

def test_delivery_link(web_browser):
    """при клике на ссылку "Доставка" в футере главной страницы сайта происходит переход на страницу с условиями доставки"""
    page = MainPage(web_browser)
    page.delivery.click()
    assert page.get_relative_link()=='/info/delivery.html','Ссылка "Доставка" не ведет на соответствующую страницу'

def test_selftake_link(web_browser):
    """при клике на ссылку "Самовывоз" в футере главной страницы сайта происходит переход на страницу с условиями доставки"""
    page = MainPage(web_browser)
    page.selftake.click()
    assert page.get_relative_link()=='/info/selftake.html','Ссылка "Самовывоз" не ведет на страницу с условиями самовывоза'

def test_service_link(web_browser):
    """при клике на ссылку "Сервис-центр" в футере главной страницы сайта происходит переход на страницу с условиями сервисного обслуживания"""
    page = MainPage(web_browser)
    page.service.click()
    assert page.get_relative_link()=='/info/service_centre.html','Ссылка "Сервис-центр" не ведет на страницу с условиями сервисного обслуживания'

def test_vkontakte_link(web_browser):
    """при клике на логотип "Вконтакте" в футере главной страницы сайта происходит переход на страницу магазина в соцсети "Вконтакте" """
    page = MainPage(web_browser)
    time.sleep(3)
    web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page.vkontakte.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert web_browser.current_url=='https://vk.com/onlinetrade','Клик по логотипу "Вконтакте" не ведет на страницу магазина в соцсети "Вконтакте"'

def test_telegram_link(web_browser):
    """при клике на логотип "Telegram" в футере главной страницы сайта происходит переход к чат-боту магазина в мессенджере Telegram"""
    page = MainPage(web_browser)
    time.sleep(3)
    web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page.telegram.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert web_browser.current_url=='https://t.me/onlinetradeshopru','Клик по логотипу "Telegram" не ведет к чат-боту магазина в мессенджере Telegram'

def test_youtube_link(web_browser):
    """при клике на логотип "YouTube" в футере главной страницы сайта происходит переход на страницу магазина в YouTube """
    page = MainPage(web_browser)
    time.sleep(3)
    web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page.youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert web_browser.current_url=='https://www.youtube.com/c/onlinetraderu','Клик по логотипу "YouTube" не ведет на страницу магазина в YouTube'

def test_ok_link(web_browser):
    """при клике на логотип "Одноклассники" в футере главной страницы сайта происходит переход на страницу магазина в соцсети "Одноклассники" """
    page = MainPage(web_browser)
    time.sleep(3)
    web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page.ok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert web_browser.current_url=='https://ok.ru/group/68866316828710','Клик по логотипу "Вконтакте" не ведет на страницу магазина в соцсети "Вконтакте"'
#
def test_auth_with_correct_data(web_browser):
    """при вводе в поля формы авторизации корректных данных действующего пользователя происходит вход в аккаунт"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert page.get_current_url()=='https://www.onlinetrade.ru/','При вводе в поля формы авторизации корректных данных действующего пользователя не происходит вход в аккаунт'

@pytest.mark.parametrize("email",list(incorrect_email.keys())[0:2],
                         ids=list(incorrect_email.values())[0:2])
def test_auth_with_empty_email(web_browser,email):
    """при вводе в поле для email пустого значения или пробела происходит переход на страницу с сообщением об ошибке"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert 'Вы не указали информацию для входа' in page.get_page_source()

@pytest.mark.xfail
@pytest.mark.parametrize("email",list(incorrect_email.keys())[2:],
                         ids=list(incorrect_email.values())[2:])
def test_auth_with_uncorrect_email(web_browser,email):
    """при вводе в поле для ввода email некорректного значения пробела происходит переход на страницу с сообщением об ошибке
    тест помечен как падающий, т.к. при вводе букв русского алфавита появляется сообщение о том, что не указана информация для входа"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(email)
    page.pass_field.send_keys(correct_pass)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()

@pytest.mark.parametrize("passw",list(incorrect_pass.keys())[0:2],
                         ids=list(incorrect_pass.values())[0:2])
def test_auth_with_empty_pass(web_browser,passw):
    """при вводе в поле для пароля пустого значения или пробела появляется сообщение об ошибке"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(passw)
    page.login_button.click()
    assert 'Вы не указали информацию для входа' in page.get_page_source()

@pytest.mark.parametrize("passw",list(incorrect_pass.keys())[2:],
                         ids=list(incorrect_pass.values())[2:])
def test_auth_with_incorrect_pass(web_browser,passw):
    """при вводе в поле для ввода пароля некорректного значения пробела происходит переход на страницу с сообщением об ошибке"""
    page = MainPage(web_browser)
    page.auth_button.click()
    page.email_field.send_keys(correct_email)
    page.pass_field.send_keys(passw)
    page.login_button.click()
    assert 'Указан неверный e-mail или пароль' in page.get_page_source()

@pytest.mark.xfail
def test_search_field(web_browser):
    """в результате поиска через поисковую строку главной страницы отображаются товары с названием, соответствующим введенному в строку тексту
    тест помечен как падающий, т.к. в результате поиска по слову "пылесос" в результатах поиска отображаются стеклоочистители"""
    page = MainPage(web_browser)
    page.search_field.click()
    product=random.choice(correct_product)
    page.search_field.send_keys(product)
    page.search_button.click()
    if page.products_titles.count()>0:
        for title in page.products_titles.get_text():
            assert product in title.lower(),f'Поиск через поисковую строку выдал товар с названием, не соответствующим введенному тексту - {title}'
    if page.product_kategory.count()>0:
        for kategory in page.product_kategory.get_text():
            assert product in kategory.lower(),f'Поиск через поисковую строку выдал категории товар с названиями, не соответствующим введенному тексту - {kategory}'

@pytest.mark.xfail
@pytest.mark.parametrize("product",list(incorrect_product_title.keys()),
                         ids=list(incorrect_product_title.values()))
def test_search_field_eng_text(web_browser,product):
    """при вводе в поисковую строку главной страницы названия товара с орфографическими ошибками, пробелами, в различном регистре, латиницей,
    в английской раскладке в результате поиска отображаются товары с названием, соответствующим введенному в строку тексту
    тест помечен как падающий, т.к. в некоторых случаях отображаются товары с соответствующим названием, в некоторых - нет """
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys(product)
    page.search_button.click()
    assert page.products_titles.count()>0,'Товары не найдены'
    for title in page.products_titles.get_text():
        assert 'телевизор' in title.lower(),'При вводе в поисковую строку главной страницы видоизмененного текста' \
                                            'поиск осуществляется не в соответствии с ввееденным значением'

@pytest.mark.xfail
def test_search_field_backspace(web_browser):
    """при вводе в поисковую строку главной страницы пробела
    в результате поиска отображается сообщение о том, что задан пустой поисковый запрос
    тест помечен как падающий, поскольку появляется сообщение о том, что товары не найдены из-за допущенной ошибки в поисковом запросе
    или отсутствии товара"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys(' ')
    page.search_button.click()
    assert 'Ничего не найдено' in page.get_page_source(),'При вводе в поисковую строку главной страницы пробела \
                                                            в результате поиска не отображается сообщение о том, что задан пустой поисковый запрос'

@pytest.mark.parametrize("value",list(other_value_for_search.keys()),
                         ids=list(other_value_for_search.values()))
@pytest.mark.xfail
def test_other_value_for_search_field(web_browser,value):
    """при вводе в поисковую строку главной страницы спецсимволов, китайских символов, очень длинной строки или цифр
    появляется сообщение о том, что введенное значение некорректно
    тест помечен как падающий, поскольку при вводе произвольного набора букв появляется сообщение о том, что товары не найдены,
    при вводе спецсимволов происходит переход на недоступную страницу (сайт не может обработать этот запрос),
    при вводе китайских символов или очень длинной строки происходит переход на пустую страницу"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys(value)
    page.search_button.click()
    assert 'Ничего не найдено' in page.get_page_source(),'При вводе в поисковую строку главной страницы спецсимволов,' \
                                                         ' китайских символов, очень длинной строки или цифр\
                                                        в результате поиска не отображается сообщение о том, что введенное значение некорректно'

def test_sort_product_by_price_from_min(web_browser):
    """при нажатии кнопки сортировки товаров по критерию "сначала подешевле" товары сортируются от самых дешевых к самым дорогим"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="js__listingSort_ID"]')))
    select_object_sort = Select(select_element_sort)
    select_object_sort.select_by_value('price-asc')
    all_prices=ManyWebElements(xpath='//span[@class="price regular"]').get_text()
    all_prices=[float(pr.replace(' ','')) for pr in all_prices]
    assert all_prices==sorted(all_prices)

def test_sort_product_by_price_from_max(web_browser):
    """при нажатии кнопки сортировки товаров по критерию "сначала подороже" товары сортируются от самых дорогих к самым дешевым"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="js__listingSort_ID"]')))
    select_object_sort = Select(select_element_sort)
    select_object_sort.select_by_value('price-desc')
    all_prices=ManyWebElements(xpath='//span[@class="price regular"]').get_text()
    all_prices=[float(pr.replace(' ','')) for pr in all_prices]
    assert all_prices[::-1]==sorted(all_prices)

def test_sort_product_by_price_from_title_asc(web_browser):
    """при нажатии кнопки сортировки товаров по критерию "по названию (а-я)" товары сортируются в алфавитном порядке"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="js__listingSort_ID"]')))
    select_object_sort = Select(select_element_sort)
    select_object_sort.select_by_value('title-asc')
    all_titles=ManyWebElements(xpath='//span[@class="indexGoods__item__name"]').get_text()
    all_titles=[float(pr.replace(' ','')) for pr in all_titles]
    assert all_titles==sorted(all_titles)

def test_sort_product_by_price_from_title_desc(web_browser):
    """при нажатии кнопки сортировки товаров по критерию "по названию (я-а)" товары сортируются в порядке, обратном алфавитному"""
    page = MainPage(web_browser)
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    select_element_sort = WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="js__listingSort_ID"]')))
    select_object_sort = Select(select_element_sort)
    select_object_sort.select_by_value('title-desc')
    all_titles=ManyWebElements(xpath='//span[@class="indexGoods__item__name"]').get_text()
    all_titles=[float(pr.replace(' ','')) for pr in all_titles]
    assert all_titles[::-1]==sorted(all_titles)

def test_product_in_basket(web_browser):
    """при нажатии на кнопку "Купить" на карточке товара счетчик корзины увеличивается на 1"""
    page = MainPage(web_browser)
    count=int(page.count_of_basket.get_text())
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    WebDriverWait(web_browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="button button__orange js__ajaxExchange"]')))[3].click()
    WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@title="Оформить заказ"]'))).click()
    time.sleep(5)
    count_new=int(WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="itemCount"]'))).text)
    assert count_new==(count+1),'При нажатии на кнопку "Купить" на карточке товара счетчик корзины не увеличивается на 1'

def test_product_in_bookmarks(web_browser):
    """при нажатии на кнопку "Добавить в закладки" на карточке товара счетчик закладок увеличивается на 1"""
    page = MainPage(web_browser)
    count=int(page.count_of_bookmarks.get_text())
    page.search_field.click()
    page.search_field.send_keys('телевизор')
    page.search_button.click()
    WebDriverWait(web_browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@data-handler="bookmarks"]')))[2].click()
    time.sleep(5)
    count_new=int(WebDriverWait(web_browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div  [@class="huab__cell__text js__bookmarksCount"]'))).text)
    assert count_new==(count+1),'При нажатии на кнопку "Добавить в закладки" на карточке товара счетчик закладок не увеличивается на 1'
#