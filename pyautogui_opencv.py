import time
import pyautogui
from config import config
from loguru import logger
import nike



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
    
    nike.Nike.scroll = config.scroll
    nike.Nike.scroll_url_size = config.scroll_url_size
    nike.Nike.scroll_url_cvv = config.scroll_url_cvv
    nike.Nike._dir = config._dir
    nike.Nike._dir_config = config._dir_config
    nike.Nike.sleep_url = config.sleep_url
    nike.Nike.sleep_buy = config.sleep_buy
    nike.Nike.sleep_nex_buy = config.sleep_nex_buy
    nike.Nike.sleep_select_url = config.sleep_select_url
    nike.Nike._dir_screenshot = config._dir_screenshot
    nike.Nike.sleep_restart_url = config.sleep_restart_url


    nike_buy = nike.Nike(email=config.email, password=config.password, cvv=config.CVV, mmyy=config.MMYY, card_number=config.Card_number, name_on_card=config.Name_on_card)
    if config.Authentication_site:
        nike_buy.login(login_url=config.url_login)
    nike_buy.buy(data_json='data.json', shoe_size=config.Shoe_size, url_cart=config.url_cart)

    

if __name__ == '__main__':
    main()