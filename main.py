import time
import pyautogui
from config import config
from loguru import logger
import sender_command
from typing import NamedTuple
import nike

class Options_nike(NamedTuple):
    scroll = float
    scroll_url_size = float
    scroll_url_cvv = float
    _dir = str
    _dir_config = str 
    _dir_screenshot = str 
    sleep_select_url = int
    sleep_url = int
    sleep_buy = int
    sleep_nex_buy = int 
    sleep_restart_url = int 
    email = str
    password = str 
    cvv = str
    mmyy = str
    card_number = str
    name_on_card = str




def main() -> None:
    logger.add('info.log', format="{time} {level} {message}", level="INFO")
    # Open Google Chrom
    if not config.Debug:
        logger.info('Open Google Chrom')
        pyautogui.moveTo(config.x, config.y, duration=1)
        pyautogui.doubleClick()
        time.sleep(1)
    else:
    # My Linux settings
        logger.info('Swap tab')
        with pyautogui.hold('win'):
            pyautogui.press(['2'])
    
    options_nike = Options_nike(
        scroll = config.scroll,
        scroll_url_size = config.scroll_url_size,
        scroll_url_cvv = config.scroll_url_cvv,
        _dir = config._dir,
        _dir_config = config._dir_config,
        sleep_url = config.sleep_url,
        sleep_buy = config.sleep_buy,
        sleep_nex_buy = config.sleep_nex_buy,
        sleep_select_url = config.sleep_select_url,
        _dir_screenshot = config._dir_screenshot,
        sleep_restart_url = config.sleep_restart_url,
        email=config.email, 
        password=config.password, 
        cvv=config.CVV, 
        mmyy=config.MMYY, 
        card_number=config.Card_number, 
        name_on_card=config.Name_on_card
    )
    

    nike_buy = sender_command.CMD(options = options_nike)
    if config.Authentication_site:
        nike.login(login_url=config.url_login, class_=nike_buy, opt=options_nike)
    nike.buy(data_json='data.json', shoe_size=config.Shoe_size, url_cart=config.url_cart, class_=nike_buy, opt=options_nike)

    

if __name__ == '__main__':
    main()