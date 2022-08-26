from pyautogui_opencv import logger
import pyautogui
import time
from os import path
import os
import json
import datetime
from config import config


class Nike:
    scroll = -1
    scroll_url_size = -2
    scroll_url_cvv = -2
    _dir = 'pictures'
    _dir_config = 'config'
    sleep_url = 1
    sleep_buy = 15
    sleep_nex_buy = 10
    sleep_select_url = 10
    _dir_screenshot = 'screenshot'
    sleep_restart_url = 5


    def __init__(self, email: str, password: str, cvv:str, mmyy:str, card_number:str, name_on_card:str) -> None:
        self.email = email
        self.password = password
        self.cvv = cvv
        self.mmyy = mmyy
        self.card_number = card_number
        self.name_on_card = name_on_card
    
    def login(self, login_url:str) -> None:
        '''Login in nike.com'''
        self._open_url(url=login_url, open_tab=True)
        self._enter_write_edittext('password', self._dir, self.password)
        self._enter_write_edittext('email', self._dir, self.email)
        self._enter_button('sign_in', self._dir)
    
    def _open_json(self, _dir_json:str) -> json.JSONDecoder | None:
        try:
            with open(_dir_json, 'r') as file:
                load = json.load(file)
            return load
        except Exception:
            return None
    
    def _write_json(self, _dir_json:str, upload_json:dict) -> None:
        try:
            with open(_dir_json, 'w') as file:
                json.dump(upload_json, file, ensure_ascii=True, indent=4)
        except Exception:
            return None
    
    def _square_date(self, date_no_parse:str) -> bool:
        date_now = datetime.datetime.now()
        date_update = datetime.datetime.strptime(date_no_parse, '%Y-%m-%d')
        if date_now >= date_update:
            return True
        else:
            return False

    def _cart(self, url_cart:str) -> None:
        '''Go cart and confirm buy'''
        self._open_url(url=url_cart, select_url=True, backspace=True)
        self._enter_button(name='member_checkout', _dir=self._dir, upload_url=True)
        self._enter_button(name='continue', _dir=self._dir, upload_url=True)
        self._enter_button(name='arrives', _dir=self._dir)
        self._enter_button(name='continue', _dir=self._dir, upload_url=True)
        self._enter_button(name='continue1', _dir=self._dir, upload_url=True)
        self._enter_write_edittext(name='cvv', _dir=self._dir, text=self.cvv)
        if not config.Credit_card_in_site:
            self._enter_write_edittext(name='mmyy', _dir=self._dir, text=self.mmyy)
            self._enter_write_edittext(name='card_number', _dir=self._dir, text=self.card_number)
            self._enter_write_edittext(name='name_on_card', _dir=self._dir, text=self.name_on_card)
        self._enter_button(name='place_order', _dir=self._dir)

    def buy(self, data_json:str, shoe_size:str, url_cart:str, screenshot:bool=False) -> bool:
        download_json = self._open_json(_dir_json=path.join(self._dir_config, data_json))
        logger.info(download_json)
        upload_json = download_json.copy()
        
        while upload_json:
            download_json = upload_json.copy()
            for item, value in download_json.items():
                if self._square_date(value[1]):
                    self._open_url(value[2], select_url=True, backspace=True)
                    position = pyautogui.position()
                    newposition = (position.x + 200, position.y - 200)
                    pyautogui.moveTo(newposition)
                    if not self._enter_button(shoe_size, self._dir) == 'Coming Soon':
                        self._enter_button('buy', self._dir)

                        self._cart(url_cart=url_cart)
                        time.sleep(self.sleep_nex_buy)
                        if screenshot:
                            if not path.isdir(self._dir_screenshot):
                                os.mkdir(self._dir_screenshot)
                            pyautogui.screenshot(f'{path.join(self._dir_screenshot, item)}.png')
                        upload_json.pop(item, None)
                else:
                    logger.info(f'Date not it {value[1]}')
            time.sleep(self.sleep_buy)
            self._write_json(_dir_json=path.join(self._dir_config, data_json), upload_json=upload_json)


    def _opencv_element(self, name_element: str) -> tuple | str:
        while True:
            self._restart_url()
            if coord:=pyautogui.locateOnScreen(f'{name_element}.png'):
                return coord
            elif any(['us_' in name_element, 'buy' in name_element]):
                if pyautogui.locateOnScreen(path.join(self._dir, 'coming_soon.png')):
                    return 'Coming Soon'
                pyautogui.scroll(self.scroll_url_size)
            elif any(['continue' in name_element, 'place_' in name_element]):
                pyautogui.scroll(self.scroll)
            elif 'cvv' in name_element:
                pyautogui.scroll(self.scroll_url_cvv)
            time.sleep(1)
    

    def _enter_button(self, name: str, _dir: str, upload_url:bool=False) -> bool | str:
        '''Enter button'''
        try:
            logger.info(f'Enter {path.join(_dir, name)}')
            coord = self._opencv_element(name_element=path.join(_dir, name))
            if coord == 'Coming Soon':
                return 'Coming Soon'
            logger.info(f'Upload coord {name} = {coord}')
            pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, 1)
            pyautogui.click()
            if upload_url:
                #time.sleep(self.sleep_select_url)
                self._stay_loade_page()
            return True
        except Exception:
            return False


    def _enter_write_edittext(self, name:str, _dir:str, text:str) -> bool:
        '''Enter edittext and write text'''
        try:
            self._enter_button(name=name, _dir=_dir)
            logger.info(f'Write text = {text}')
            pyautogui.write(text)
            return True
        except Exception:
            return False
    
    def _stay_loade_page(self) -> bool:
        while True:
            if pyautogui.locateOnScreen(path.join(self._dir, 'page_load.png')):
                return True
    
    def _restart_url(self) -> bool:
            if pyautogui.locateOnScreen(path.join(self._dir, 'restart_url.png')):
                pyautogui.press('f5')
                time.sleep(self.sleep_restart_url)
                return True
            else:
                return False

    def _open_url(self, url: str, select_url:bool=False, backspace:bool=False, open_tab: bool=False) -> bool:
        '''Open new url'''
        try:
            if open_tab:
                self._stay_loade_page()
                logger.info('Open new Tab')
                with pyautogui.hold('ctrl'):
                    pyautogui.press(['t'])
            if select_url:
                self._stay_loade_page()
                with pyautogui.hold('alt'):
                    pyautogui.press('d')
            time.sleep(self.sleep_url)
            if backspace:
                pyautogui.press('backspace')
            logger.info(f'Enter url login = {url}')
            pyautogui.write(url, interval=0.1)
            pyautogui.press('enter')
        except Exception:
            return False