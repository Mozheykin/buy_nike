from datetime import datetime
import time
import pyautogui
import config
from loguru import logger
import json


def opencv_element(name_element: str) -> tuple:
    while True:
        if coord:=pyautogui.locateOnScreen(f'{name_element}.png'):
            return coord
        elif name_element.startswith('us_') or name_element.startswith('buy'):
            pyautogui.scroll(-1)
        elif name_element == 'continue' or name_element.startswith('place_'):
            pyautogui.scroll(-1)
        elif name_element == 'cvv':
            pyautogui.scroll(-1)
        time.sleep(1)

def login_site() -> None:
    '''Login nike.com'''
    # Login site
    logger.info(f'Enter url login = {config.url_login}')
    pyautogui.write(config.url_login, interval=0.1)
    pyautogui.press('enter')

    #Enter password
    logger.info(f'Enter password = {config.password}')
    coord = opencv_element(name_element='password')
    logger.info(f'Upload coord password = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.password)

    
    # Enter Email
    logger.info(f'Enter email = {config.email}')
    coord = opencv_element(name_element='email')
    logger.info(f'Upload coord email = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.email)

    #Enter sign in
    logger.info(f'Enter sign in')
    coord = opencv_element(name_element='sign_in')
    logger.info(f'Upload coord sign in = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()

    return True


def cart() -> None:
    '''Go cart and confirm buy'''
    # Login site
    with pyautogui.hold('ctrl'):
        pyautogui.press('l')
        time.sleep(2)
    logger.info(f'Enter url login = {config.url_cart}')
    pyautogui.write(config.url_cart, interval=0.1)
    pyautogui.press('enter')

    # Press member checkout
    logger.info(f'Press member checkout')
    coord = opencv_element(name_element='member_checkout')
    logger.info(f'Upload coord member checkout = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    time.sleep(2)

    # Press continue
    logger.info(f'Press continue')
    coord = opencv_element(name_element='continue')
    logger.info(f'Upload coord continue = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    time.sleep(2)

    # Press arrives
    logger.info(f'Press arrives')
    coord = opencv_element(name_element='arrives')
    logger.info(f'Upload coord arrives = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()

    # Press continue
    logger.info(f'Press continue')
    coord = opencv_element(name_element='continue')
    logger.info(f'Upload coord continue = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    time.sleep(2)

    # Press continue
    logger.info(f'Press continue')
    coord = opencv_element(name_element='continue1')
    logger.info(f'Upload coord continue = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    time.sleep(4)

    #Enter cvv
    logger.info(f'Enter password = {config.CVV}')
    coord = opencv_element(name_element='cvv')
    logger.info(f'Upload coord cvv = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.CVV, interval=0.1)

    #Enter mm/yy
    logger.info(f'Enter password = {config.MMYY}')
    coord = opencv_element(name_element='mmyy')
    logger.info(f'Upload coord mm/yy = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.MMYY, interval=0.1)

    #Enter card number
    logger.info(f'Enter password = {config.Card_number}')
    coord = opencv_element(name_element='card_number')
    logger.info(f'Upload coord card number = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.Card_number, interval=0.1)

    #Enter name on card
    logger.info(f'Enter password = {config.Name_on_card}')
    coord = opencv_element(name_element='name_on_card')
    logger.info(f'Upload coord name on card = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    pyautogui.write(config.Name_on_card, interval=0.1)

    # Press Place Order
    logger.info(f'Press Place Order')
    coord = opencv_element(name_element='place_order')
    logger.info(f'Upload coord place order = {coord}')
    pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
    pyautogui.click()
    time.sleep(2)

    


def buy_sneakers() -> None:
    '''Buy sneakers'''
    logger.info('Buy sneakers')
    with open('data.json', 'r') as file:
        snkrs = json.load(file)
    date_now = datetime.now()
    upload_json = snkrs.copy()
    for item, value in snkrs.items():
        logger.info(f'Check {item}')
        date_update = datetime.strptime(value[1], '%Y-%m-%d')
        if date_now >= date_update:
            # Go to url sneakers
            logger.info(f'Enter url sneakers = {value[2]}')
            with pyautogui.hold('ctrl'):
                pyautogui.press('l')
            time.sleep(2)
            pyautogui.write(value[2], interval=0.1)
            pyautogui.press('enter')
            # Search size
            logger.info(f'Search size')
            coord = opencv_element(name_element=config.Shoe_size)
            logger.info(f'Upload coord sign in = {coord}')
            pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
            pyautogui.click()
            # Click buy
            logger.info(f'Click buy')
            coord = opencv_element(name_element='buy')
            logger.info(f'Upload coord sign in = {coord}')
            pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
            pyautogui.click()

            cart()
            #Screenshot
            time.sleep(10)
            pyautogui.screenshot(f'{item}.png')
            upload_json.pop(item, None)
        else: 
            logger.info(f'Date not it {value[1]}')

    
    with open('data.json', 'w') as file:
        json.dump(upload_json, file, ensure_ascii=True, indent=4)


def main() -> None:
    logger.add('info.log', format="{time} {level} {message}", level="INFO")
    # Open Google Chrom
    logger.info('Open Google Chrom')
    # pyautogui.moveTo(318, 748, duration=1)
    # pyautogui.doubleClick()
    time.sleep(1)
    # My Linux settings
    logger.info('Swap tab')
    with pyautogui.hold('win'):
        pyautogui.press(['2'])
    # Open new Tab
    logger.info('Open new Tab')
    with pyautogui.hold('ctrl'):
        pyautogui.press(['t'])
    

    login_site()
    time.sleep(10)
    buy_sneakers()

    

if __name__ == '__main__':
    main()