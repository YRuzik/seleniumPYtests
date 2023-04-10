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

#ищем кнопку меню пользователя
button_menu_user=browser.find_element(by=By.CLASS_NAME, value='tm-header-user-menu__user_desktop')
button_menu_user.click()
#ждем открытие меню
favourites_menu_item = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "tm-user-item__username"), '@AndreyVavanov')
    )
#ищем кнопку смены языка с помощью XPath
language_menu_item = browser.find_element(by=By.XPATH, value="/html/body/div[@id='app']/div[@class='tm-layout__wrapper']/div[@class='tm-layout']/div[@class='tm-base-layout__header tm-base-layout__header_is-sticky']/div[@class='tm-page-width']/div[@class='tm-base-layout__header-wrapper']/div[@class='tm-header-user-menu tm-base-layout__user-menu']/div[@class='tm-header-user-menu__item tm-header-user-menu__user_desktop']/div[@class='tm-dropdown tm-dropdown_active']/div[@class='tm-dropdown__body tm-dropdown__body_right']/div[@class='tm-user-menu tm-user-menu_padded']/div[@class='tm-user-menu__menu_bottom'][2]/button[@class='tm-user-menu__menu-link tm-user-menu__menu-link_grey']")
language_menu_item.click()

#ищем переключатель на английский интерфейс по id 
ui = browser.find_element(by=By.ID, value='uiEnglish')
browser.execute_script("arguments[0].click();", ui)

#ищем кнопку сохранения настроек
save_pref_button=browser.find_element(by=By.CLASS_NAME, value='tm-page-settings-form__submit')
save_pref_button.click()

#ждем перезагрузку страницы
loading = WebDriverWait(browser, 10).until(
        EC.title_is('All articles in a row / Habr')
    )

#ищем текст одного из разделов статей
link = browser.find_element(by=By.XPATH, value="/html/body/div[@id='app']/div[@class='tm-layout__wrapper']/div[@class='tm-layout']/div[@class='tm-base-layout__header tm-base-layout__header_is-sticky']/div[@class='tm-page-width']/div[@class='tm-base-layout__header-wrapper']/div[@class='tm-main-menu']/div[@class='tm-main-menu__section']/nav[@class='tm-main-menu__section-content']/a[@class='tm-main-menu__item'][1]")
try:
# Проверка что пользователь находится на английской версии сайта
    assert 'All articles in a row / Habr' in browser.title
# Проверка что на странице присутствует название раздела статей на английском
    assert link.text == 'My feed'
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()