from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser=webdriver.Chrome()
#загружаем страницу
browser.get('https://habr.com/ru/all/')
#ищем кнопку открытия меню пользователя
button_menu_vxod=browser.find_element(by=By.CLASS_NAME, value='tm-header-user-menu__user_desktop')
button_menu_vxod.click()
time.sleep(2)
#ищем кнопку входа в аккаунт
button_vxod=browser.find_element(by=By.CLASS_NAME, value='tm-user-menu__auth-button')
button_vxod.click()
#ждем загрузку страницы входа
loading = WebDriverWait(browser, 10).until(
        EC.title_is('Вход — Habr Account')
    )
# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.NAME, value='email')
username.send_keys('kuzechka731@gmail.com')
# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.NAME, value='password')
password.send_keys('eXY-y4a-Nbn-d85')
#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button_auth=browser.find_element(by=By.NAME, value='go')
button_auth.click()
# ждем загрузку главной страницы
loading = WebDriverWait(browser, 10).until(
        EC.title_is('Все статьи подряд / Хабр')
    )


#открываем страницу со статьей
browser.get('https://habr.com/ru/post/726428/')
#ждем загрузку страницы
loading = WebDriverWait(browser, 10).until(
        EC.title_is('Простая Enterprise Architecture. Архитектура компании садоводов / Хабр')
    )

#ищем кнопку добавления в избранное
favourites = browser.find_element(by=By.CLASS_NAME, value='bookmarks-button')
favourites.click()

#ищем кнопку меню пользователя
button_menu_user=browser.find_element(by=By.CLASS_NAME, value='tm-header-user-menu__user_desktop')
button_menu_user.click()
#ждем открытие меню
favourites_menu_item = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "tm-user-item__username"), '@AndreyVavanov')
    )
#ищем кнопку закладки с помощью XPath
favourites_menu_item = browser.find_element(by=By.XPATH, value="/html/body/div[@id='app']/div[@class='tm-layout__wrapper']/div[@class='tm-layout']/div[@class='tm-base-layout__header tm-base-layout__header_is-sticky']/div[@class='tm-page-width']/div[@class='tm-base-layout__header-wrapper']/div[@class='tm-header-user-menu tm-base-layout__user-menu']/div[@class='tm-header-user-menu__item tm-header-user-menu__user_desktop']/div[@class='tm-dropdown tm-dropdown_active']/div[@class='tm-dropdown__body tm-dropdown__body_right']/div[@class='tm-user-menu tm-user-menu_padded']/div[@class='tm-user-menu__menu_top']/a[@class='tm-user-menu__menu-link'][4]")
favourites_menu_item.click()

#ждем загрузку страницы закладки
loading = WebDriverWait(browser, 10).until(
        EC.title_is('Публикации / Закладки / Профиль AndreyVavanov / Хабр')
    )
#ищем контейнер статьи по id 
article = browser.find_element(by=By.ID, value='726428')

try:
# Проверка что пользователь находится на главной странице сайта
    assert 'Публикации / Закладки / Профиль AndreyVavanov / Хабр' in browser.title
# Проверка что на странице присутствует избранная статья
    assert article.get_attribute('id') == '726428'
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()