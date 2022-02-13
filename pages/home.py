from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.test_logger import *
from lib.helpers import *


dresses_button = (
    By.XPATH, "//li[@id='category-thumbnail']//following::a[@title='Dresses']")
dresses_names = (
    By.XPATH, "//a[@class='product_img_link']/img[contains(@title, 'Dress' )]")
dresses_prices = (
    By.XPATH, "//div[@class='right-block']//span[@class='price product-price']")


def get_dresses_names():
    find_and_click(dresses_button)
    dressesnames = find_all(dresses_names)
    prices = find_all(dresses_prices)
    try:
        str = ""
        for index, title in enumerate(dressesnames):
            str += (title.get_attribute("title") +
                    " : " + prices[index].text + "\n")
        create_file_and_write(data.data_file, str)
        logger("The results are got")
        return str
    except Exception as e:
        logger(e, True)
