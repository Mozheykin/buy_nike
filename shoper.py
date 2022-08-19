from http import cookies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver.v2 as uc
import config
import time
from random import random
from loguru import logger
from datetime import datetime
from fake_useragent import UserAgent
import os
from selenium_stealth import stealth

def wait_until_clickable(driver :webdriver, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    elif css_selector:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    elif _id:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.ID, _id)))


def wait_until_present(driver :webdriver, xpath :str=None, css_selector=None, class_name :str=None, _id :str=None, duration :int=10000, frequency :float=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    elif css_selector:
        WebDriverWait(driver, duration, frequency).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    elif _id:
        WebDriverWait(driver, duration, frequency).until(EC.presence_of_element_located((By.ID, _id)))


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
            logger.info(f'SEARCH XPATH={xpath}')
            return driver.find_element(By.XPATH, xpath)
        except NoSuchElementException as ex:
            logger.error(ex.with_traceback)


class Nike:
    def __init__(self, path: str, user_agent :str, headless :bool) -> None:
        '''Create driver'''
        username = os.getenv("USERNAME")
        userProfile = "/home/legal/.config/google-chrome/Default"
        ua = UserAgent()
        userAgent = ua.random
        options = uc.ChromeOptions()
        # options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        # Antidetect
        # options.add_argument("--disable-blink-features")
        options.add_argument('--disable-blink-features=AutomationControlled')
        # Maximaze window
        options.add_argument("--start-maximized")
        # options.add_argument("--disable-popup-blocking")
        # options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # Add user-agent
        options.add_argument(f'user-agent={userAgent}')
        #create driver
        # self.driver = webdriver.Chrome(executable_path=path, options=options)
        self.driver = uc.Chrome()
    #     self.driver.add_cookie({
	# 	"_abck": "3F2E9DA270B440BDDEAF9D3D820475FB~-1~YAAQT7GvwxOEpWOCAQAA62L+sAjTXI3lmQH1CFy1sfMSsw5SEgk+XhlQFnE/hzMEht8kt+gLOfaghi9N9adJESundTlhxYUrklyKwcvcBYb398ZqDEuns4bSE9FAOeT69cJ/0VikjdEKoRUMkhUB56/SWOXrPsVDo9xrqj4taVsWx2n593udyF3hTNNXopPYdpXYgAzezpYSDK/dJTg5bOXpCO5dJLqatQ6zxnfbsqWQFwSsjc8k43f/1t3Ajt7SqG/qM0/6JLbMy9PDPaTplLdIl81IxZmdTsk1czMi+8fdvgxfpW0ZunrtIoIYSLkZlw3QABz4cnW7OIjvTg60k7Ecg5Z2kIQ1cRoqY+z+znQ14SKG6C1A5M9f1sPTDDiyHxZMxh4LF0dyBeX6WPCDPtJottxUW4+X0X6eKzUd6y9SP8w9QIbsU1fC8jueEIR+PMYHadi0ZzoM+JyBeS2ZsWzwWAw=~-1~-1~-1",
	# 	"bm_sz": "7A8DFF6D80486C5F2FFE820F27473DFB~YAAQ7LCvw6J2HmOCAQAA5zzZsBARTJ8Q4YyzUBpauKgmMCySaZbnkTPDChUnmY9iXNNgMaIHlKhaDdQIbx3LqktQpJYWpTuS4drsNsvSzNjFry5aaMhunRB0UEc5EvUpy9FxNs0+NECo3E2vbTGjRQm+EY+pWcP3bZupfWPf2t7KU/8yd0IoAC4ujkyoomGNP5OFX5VzFFB4gtwjuzEazFCVwAr2hFDcsrWdAa/nBd2dE1RRFVr9KKi+vSlF4Q0FRV14uJNcOxINN4dMVXovK0LvKK6zeHccEcNTa+/9TJ8k+8Icx60XjkwTWcScVQTk4WPDqf0Y1cD8ykFvY2WeAoL43okmhNonOZg5DoOSphNVOrMVimbdlqRlpXdhDDuUZDrkWF4xtVsC4I/Q2suju+DTwdTf3v3G/b25FHu84nuiHRnbzg==~3159876~4539969",
	# })

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                                "source":
                                    "const newProto = navigator.__proto__;"
                                    "delete newProto.webdriver;"
                                    "navigator.__proto__ = newProto;"
                                })
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
            )
        
        # self.driver.add_cookie(config.cookies)
        self.action = ActionChains(self.driver)
        logger.info('Create driver')

    def login(self, url_login: str, email :str, password:str) -> None:
        '''Login in nike.com'''
        # self.driver.execute_script(f"window.open('{url_login}');")
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url=url_login)
        
        wait_until_visible(driver=self.driver, xpath="//input[@name='emailAddress']")

        email_input = self.driver.find_element(By.XPATH, '//input[@name="emailAddress"]')
        self.action.move_to_element(email_input).perform()
        time.sleep(random() * 3)
        self.action.click()
        email_input.clear()
        for item in email:
            email_input.send_keys(item)
            time.sleep(random())

        
        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        self.action.move_to_element(password_input).perform()
        time.sleep(random() * 3)
        self.action.click()
        password_input.clear()
        for item in password:
            password_input.send_keys(item)
            time.sleep(random())

        sign_in = self.driver.find_element(By.XPATH, '//input[@value="SIGN IN"]')
        self.action.move_to_element(sign_in).perform()
        time.sleep(random() * 3)
        self.action.click()
        sign_in.click()

        logger.debug(self.driver.get_cookies)
        
        wait_until_visible(driver=self.driver, xpath="//a[@data-path='myAccount:greeting']", duration=5)
        logger.info('Login in Nike')

        wait_until_visible(driver=self.driver, xpath="//span[text()='My Account']")
        time.sleep(15)
    
    def snkrs(self, snkrs: dict, shoe_size: str) -> None:
        for value in snkrs.values():
            date_now = datetime.now()
            date_buy = datetime.strptime(value[1], '%Y-%m-%d')
            if date_now > date_buy:
                logger.info(f'in element {value[2]}')
                self.driver.get(url=value[2])
                time.sleep(random() * 3)
                wait_until_visible(driver=self.driver, xpath=f"//button[text()='{shoe_size}' and not(@disabled)]")
                if element:=check_exists_by_xpath(self.driver, xpath=f"//button[text()='{shoe_size}']"):
                    self.action.move_to_element(element).perform()
                    self.action.click()
                    # element.click()
                    logger.info('Select size')
                time.sleep(random() * 3)
                wait_until_clickable(driver=self.driver, xpath=f"//button[text()='Buy  {value[0]}' and not(@disabled)]")
                if element:=check_exists_by_xpath(self.driver, xpath=f"//button[text()='Buy  {value[0]}']"):
                    self.action.move_to_element(element).perform()
                    time.sleep(random() * 3)
                    self.action.click()
                    # element.click() 
                    logger.info('Click Buy')
                
        logger.info('Add snkrs to card')
    
    def card(self, url_card: str) -> None:
        # cookies = self.driver.get_cookies
        # if element:=check_exists_by_xpath(self.driver, xpath=f"//a[@class='shopping-cart-button']"):
        #     self.action.move_to_element(element).perform()
        #     element.click() 
        #     logger.info('Click Card')
        # self.driver.get(url=url_card)
        time.sleep(150)
    

    def google(self):
        self.driver.get(url='https://www.youtube.com/watch?v=wzb9zNB0-1s')
        wait_until_visible(driver=self.driver, xpath='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-text-inline-expander/yt-formatted-string/a')
        # time.sleep(10)
        
        url = self.driver.find_element(By.LINK_TEXT, 'https://www.nike.com/ca/launch/t/air-...')
        self.action.move_to_element(url).perform()
        time.sleep(random() * 3)
        url.click()
        time.sleep(150)

    def close(self) -> None:
        self.driver.close()
        self.driver.quit()


def main() -> None:
    logger.add('nike.log', format="{time} {level} {message}", level="INFO", rotation='5 MB')
    logger.info('Start programm')
    nike = Nike(path=config.path_driver, user_agent=config.user_agent, headless=config.headless)
    # nike.google()
    # First look login!  ERROR
    nike.login(url_login=config.url_login, email=config.email, password=config.password)
    # Second look add snekers in card! Dont press keys in card!
    # nike.snkrs(snkrs=config.Snkrs, shoe_size=config.Shoe_size)
    # nike.card(url_card=config.url_card)

    nike.close()


if __name__ == '__main__':
    main()