from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import config
import time
from random import random
from loguru import logger
import datetime


def wait_until_clickable(driver :webdriver, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    elif css_selector:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    elif _id:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.ID, _id)))


def wait_until_visible(driver :webdriver, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
    elif css_selector:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    elif _id:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.ID, _id)))


def check_exists_by_xpath(driver :webdriver, xpath :str) -> WebElement | None:
        try:
            return driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            logger.error('Check_exists_by_xpath NoSuchElementException ERROR')


class Nike:
    def __init__(self, path: str, user_agent :str, headless :bool) -> None:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(executable_path=path, options=options)
        logger.info('Create driver')
    
    def login(self, url_login: str, email :str, password:str) -> None:
        self.driver.get(url=url_login)
        wait_until_visible(driver=self.driver, xpath="//input[@name='emailAddress']")

        email_input = self.driver.find_element(By.XPATH, '//input[@name="emailAddress"]')
        email_input.clear()
        for item in email:
            email_input.send_keys(item)
            time.sleep(random())

        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.clear()
        for item in password:
            password_input.send_keys(item)
            time.sleep(random())

        sign_in = self.driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
        
        wait_until_visible(driver=self.driver, xpath="//a[@data-path='myAccount:greeting']", duration=5)
        logger.info('Login in Nike')
    
    def snkrs(self, snkrs: dict) -> None:
        for value in snkrs.values():
            if datetime.now() > datetime.strptime(value[1]):
                self.driver.get(url=value[2])
                time.sleep(10)
                if element:=check_exists_by_xpath(self.driver, xpath="//button[text()='US 11']"):
                    element.click()
                if element:=check_exists_by_xpath(self.driver, xpath="//button[@data-qa='feed-buy-cta']"):
                    element.click()    

        logger.info('Add snkrs to card')
    
    def close(self) -> None:
        self.driver.close()
        self.driver.quit()


def main() -> None:
    logger.add('nike.log', format="{time} {level} {message}", level="INFO", rotation='5 MB')
    logger.info('Start programm')
    nike = Nike(path=config.path_driver, user_agent=config.user_agent, headless=config.headless)
    try:
        # nike.login(url_login=config.url_login, email=config.email, password=config.password)
        nike.snkrs(url_snkrs=config.Snkrs)
    except Exception as ex:
        logger.error(ex.with_traceback)
    finally:
        nike.close()


if __name__ == '__main__':
    main()