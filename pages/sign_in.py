from selenium.webdriver.common.by import By
from testdata import test_data as data
from lib.test_logger import *
from lib.helpers import *


sign_in = (By.XPATH, "//a[@class='login']")
email = (By.XPATH, "//input[@id='email']")
password = (By.XPATH, "//input[@id='passwd']")
signin_btn = (By.XPATH, "//*[@id='SubmitLogin']/span")
sign_out_btn = (By.XPATH, "//a[@class='logout']")


def sign_in_user():
    try:
        find_and_click(sign_in)
        find_and_send_keys(email, data.email)
        find_and_send_keys(password, data.password)
        find_and_click(signin_btn)
        logger(f"{data.first_name} user is successfully signed in")
    except Exception as e:
        logger(e, True)
