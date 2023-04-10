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
#открываем меню пользователя
button_menu_user=browser.find_element(by=By.CLASS_NAME, value='tm-header-user-menu__user_desktop')
button_menu_user.click()
#ждем появляния тэга с именем пользователя, если такой есть, записываем в переменную name True
name = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "tm-user-item__username"), '@AndreyVavanov')
    )

try:
# Проверка что пользователь находится на главной странице сайта
    assert 'Все статьи подряд / Хабр' in browser.title
# Проверка что на странице присутствует полное имя пользователя
    assert name == True
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()