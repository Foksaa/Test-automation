# python -m pytest -v --driver Chrome --driver-path C:\Users\Irina\PycharmProjects\SmartPageObject\chromedriver.exe

import pytest
from pages.yandex import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

    # получаем список названий найденных товаров, формируем текст ошибки (если в поиске выпал неправильный товар) и проверяем,
    # только ли айфоны в найденном
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg

# тестируем, переводится ли латиница в кириллицу в случае ошибки в раскладке
def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # вводим слово "смартфон" в английской раскладке и нажимаем на кнопку поиска
    page.search = 'cvfhnajy'
    page.search_run_button.click()

    # проверяем, что в найденном есть товары
    assert page.products_titles.count() > 0

    # проверяем, что найдены именно смартфоны
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg

# проверяем, что работает фильтр по цене
@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.
        Note: this test case will fail because there is a bug in
              sorting products by price.
    """

    page = MainPage(web_browser)
    # вводим в поиск название "чайник"
    page.search = 'чайник'
    page.search_run_button.click()

    # прокрутить до элемента - кнопка сортировать по цене и нажать на нее, подождать пока страница загрузится
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # получить список цен продуктов, отсортированных поцене
    all_prices = page.products_prices.get_text()

    # сконвертировать все цены в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # отсортировать список цен

    print(all_prices)
    print(sorted(all_prices))

    # сравнить отсортированный список с неотсортированным - они должны быть равны
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"