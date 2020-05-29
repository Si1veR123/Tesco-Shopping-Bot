from list_creation import add_items
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import time
import csv

class Locators:
    """
    CSS Locators for buttons and widgets on the website
    """
    def __init__(self):
        self.favourite = "li.favourites-selector span.checkbox-square.checkbox-square-linked"
        self.first = "li.product-list--list-item div.inputControl-wrapper button[type='submit']"


loc = Locators()

driver = Chrome("chromedriverv80.exe")

shopping_list = add_items()

with open(f'lists/list-{time.time()}', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([shopping_list, ])

print('List has been saved in lists/list-(time)')

URL = "https://www.tesco.com/groceries/"
driver.get(URL)

input("Press 'enter' when logged in: ")

for item in shopping_list:
    # go to new item search result
    driver.get(f"https://www.tesco.com/groceries/en-GB/search?query={item}")

    # try to click on favourite filter
    while True:
        try:
            favourite_checkbox = driver.find_element_by_css_selector(loc.favourite)
            favourite_checkbox.click()
            break
        except NoSuchElementException:
            pass

    # try to select first of favs
    time.sleep(8)
    try:
        first = driver.find_element_by_css_selector(loc.first)
        first.click()

    # if there is none, select first
    except NoSuchElementException:
        driver.get(f"https://www.tesco.com/groceries/en-GB/search?query={item}")

        first = driver.find_element_by_css_selector(loc.first)
        first.click()
