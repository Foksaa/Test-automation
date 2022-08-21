import time

def open_page(web_browser, url):
    """ Это расширенная функция, которая также проверяет, что все изображения полностью загружены """


web_browser.get(url)

page_loaded = False
images_loaded = False

script = ("return arguments[0].complete && typeof arguments[0].natural"
          "Width != \"undefined\" && arguments[0].naturalWidth > 0")

# Дождитесь загрузки страницы (и прокрутите ее, чтобы убедиться, что все объекты будут загружены):
while not page_loaded and not images_loaded:
    time.sleep(1)

    # Прокрутите страницу вниз и дождитесь загрузки страницы:
    web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # ждать, пока загрузится последний элемент
    page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

    # Убедитесь, что каждое изображение загружено полностью
    #  # (иногда нам приходится прокручивать изображение, чтобы нажать кнопку загрузки браузера):
    # ищем изображения множественным поиском и составляем их список
    pictures = web_browser.find_elements_by_xpath('//img')
    res = []
    # далее проверяем, что каждый элемент из списка изображений имеет атрибут src, если имеет,
    for image in pictures:
        src = image.get_attribute('src')
        if src:
            # Этот метод должен вызывать прокрутку изображения в поле зрения.
            image.location_once_scrolled_into_view
            web_browser.execute_script("window.scrollTo(0, 155)")
            # проверяем что изображение готово
            image_ready = web_browser.execute_script(script, image)

            if not image_ready:
                # если изображение не готово, проверяем его и пробуем загрузить еще раз
                time.sleep(5)
                image_ready = web_browser.execute_script(script, image)
            # добавляем в итоговый список готовое изображение
            res.append(image_ready)

    # Убедитесь, что каждое изображение загружено и имеет некоторую ширину > 0:
    images_loaded = False not in res

# идем вверх
web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')