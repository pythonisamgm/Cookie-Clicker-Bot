from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def click_cookie():
    """automatically clicks in the cookie. Stops after five seconds"""
    click_cookie = True
    five_seconds = time.time()+10
    while click_cookie:
        #time.sleep(0.2)
        cookie.click()
        if time.time() > five_seconds:
            click_cookie = False

def what_to_buy():
    "chooses the highest item available from the right column"
    chosen_upgrade = None
    for cost,upgrade in zip(price_list,upgrades):
        if cost < money_int:
            chosen_price = cost
            chosen_upgrade = upgrade
    return chosen_upgrade


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

five_minutes = time.time()+5*60
game_is_on = True
while game_is_on:

    click_cookie()

#checks the amount of cookies generated every five seconds
    money = driver.find_element(By.ID, "money").text.replace(",", "")
    money_int = int(money)


#find the website items on the right column
    store_objects = driver.find_elements(By.CSS_SELECTOR, "#store div")


#adds items in upgrades list and items' prices in price_list. There is an extra object (number of upgrades already done), bypassed with the try/exception.
    upgrades = []
    price_list = []
    for object in store_objects:
        if object.text != "":
            try: int(object.text)
            except:
                price = int(object.text.split("\n")[0].split(" - ")[1].replace(",", ""))
                price_list.append(price)
                upgrades.append(object)


    what_to_buy().click()

#stops the game after 5 minutes
    if time.time() > five_minutes:
        print("no time left")
        game_is_on=False
