from email.policy import strict
from main import logger
import pyautogui
import time
from os import path
import os
import json
import datetime
from config import config
from typing import NamedTuple

class CMD:
    def __init__(self, options: NamedTuple, email: str, password: str, cvv:str, mmyy:str, card_number:str, name_on_card:str) -> None:
        self.email = email
        self.password = password
        self.cvv = cvv
        self.mmyy = mmyy
        self.card_number = card_number
        self.name_on_card = name_on_card
        self.opt = options
    
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

    def _opencv_element(self, name_element: str) -> tuple | str:
        while True:
            self._restart_url()
            if coord:=pyautogui.locateOnScreen(f'{name_element}.png'):
                return coord
            elif any(['us_' in name_element, 'buy' in name_element]):
                if pyautogui.locateOnScreen(path.join(self.opt._dir, 'coming_soon.png')):
                    return 'Coming Soon'
                pyautogui.scroll(self.opt.scroll_url_size)
            elif any(['continue' in name_element, 'place_' in name_element]):
                pyautogui.scroll(self.opt.scroll)
            elif 'cvv' in name_element:
                pyautogui.scroll(self.opt.scroll_url_cvv)
    

    def _enter_button(self, name: str, _dir: str, upload_url:bool=False) -> bool | str:
        '''Enter button'''
        try:
            logger.info(f'Enter {path.join(_dir, name)}')
            coord = self._opencv_element(name_element=path.join(_dir, name))
            if coord == 'Coming Soon':
                return 'Coming Soon'
            logger.info(f'Upload coord {name} = {coord}')
            pyautogui.moveTo(coord.left + coord.width / 2, coord.top+coord.height / 2, config.moveTo_duration)
            pyautogui.click()
            if upload_url:
                time.sleep(self.opt.sleep_select_url)
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
            if pyautogui.locateOnScreen(path.join(self.opt._dir, 'page_load.png')):
                return True
    
    def _restart_url(self) -> bool:
            if pyautogui.locateOnScreen(path.join(self.opt._dir, 'restart_url.png')):
                pyautogui.press('f5')
                time.sleep(self.opt.sleep_restart_url)
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
            time.sleep(self.opt.sleep_url)
            if backspace:
                pyautogui.press('backspace')
            logger.info(f'Enter url login = {url}')
            pyautogui.write(url, interval=config.duration)
            pyautogui.press('enter')
        except Exception:
            return False