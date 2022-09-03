from main import logger
from sender_command import CMD
from typing import NamedTuple
from config import config


def login(login_url:str, class_: CMD, opt: NamedTuple) -> None:
    '''Login in nike.com'''
    class_._open_url(url=login_url, open_tab=True)
    class_._enter_write_edittext('password', opt._dir, opt.password)
    class_._enter_write_edittext('email', opt._dir, opt.email)
    class_._enter_button('sign_in', opt._dir)


def _cart(url_cart:str, class_: CMD, opt:NamedTuple) -> None:
    '''Go cart and confirm buy'''
    class_._open_url(url=url_cart, select_url=True, backspace=True)
    class_._enter_button(name='member_checkout', _dir=opt._dir, upload_url=True)
    class_._enter_button(name='continue', _dir=opt._dir, upload_url=True)
    class_._enter_button(name='arrives', _dir=opt._dir)
    class_._enter_button(name='continue', _dir=opt._dir, upload_url=True)
    class_._enter_button(name='continue1', _dir=opt._dir, upload_url=True)
    class_._enter_write_edittext(name='cvv', _dir=opt._dir, text=opt.cvv)
    if not config.Credit_card_in_site:
        class_._enter_write_edittext(name='mmyy', _dir=opt._dir, text=opt.mmyy)
        class_._enter_write_edittext(name='card_number', _dir=opt._dir, text=opt.card_number)
        class_._enter_write_edittext(name='name_on_card', _dir=opt._dir, text=opt.name_on_card)
    class_._enter_button(name='place_order', _dir=opt._dir)


def buy(data_json:str, shoe_size:str, url_cart:str, class_: CMD, opt:NamedTuple, screenshot:bool=False) -> bool:
    download_json = class_._open_json(_dir_json=path.join(opt._dir_config, data_json))
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
