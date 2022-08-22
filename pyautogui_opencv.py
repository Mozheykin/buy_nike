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
        pyautogui.moveTo(318, 748, duration=1)
        pyautogui.doubleClick()
        time.sleep(1)
    else:
    # My Linux settings
        logger.info('Swap tab')
        with pyautogui.hold('win'):
            pyautogui.press(['2'])


    nike_buy = nike.Nike(email=config.email, password=config.password, cvv=config.CVV, mmyy=config.MMYY, card_number=config.Card_number, name_on_card=config.Name_on_card)
    nike_buy.login(login_url=config.url_login)
    nike_buy.buy(data_json='data.json', shoe_size=config.Shoe_size, url_cart=config.url_cart)

    

if __name__ == '__main__':
    main()