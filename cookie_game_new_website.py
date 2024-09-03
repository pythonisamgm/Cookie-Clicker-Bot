
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#Create selenium object
#driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

#pass the consent prompt. Search for the button via By.CLASS_NAME and click_button afterwards.
consent = driver.find_element(By.CLASS_NAME, "fc-button-label")
consent.click()

#pass the language prompt (names of var differ from click_button's name to check the trials already done)

#language_class_with_dot = driver.find_element(By.CLASS_NAME, "langSelectButton.title")
#language_barrier_class = driver.find_element(By.CLASS_NAME, "langSelectButton title")
language_barrier = driver.find_element(By.ID, value="langSelect-EN")
#language_barrier1_tag = driver.find_element(By.TAG_NAME, "h3")
#language_barrier1_css = driver.find_element(By.CSS_SELECTOR, "div.langSelectButton title")
#language_barrier1_css_with_dot = driver.find_element(By.CSS_SELECTOR, "div.langSelectButton.title")
#language_barrier1_css = driver.find_element(By.CSS_SELECTOR, "div.langSelectButton-title")
#language_barrier1_full_xpath = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
#language_barrier1_xpath = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
#language_barrier1 = driver.find_element(By.CSS_SELECTOR, '#languageSelectHeader div')
language_barrier.click()


cookie = driver.find_element(By.ID, "bigCookie")
game_is_on = True
while game_is_on:
    cookie.click()