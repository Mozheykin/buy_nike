# Webdriver
path_driver = '/home/legal/github/buy_nike/chromedriver'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
headless = False

headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "origin": "https://www.nike.com",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "accept": "*/*",
        "scheme": "https"
    }


cookies = {
		u"_abck": u"3F2E9DA270B440BDDEAF9D3D820475FB~-1~YAAQT7GvwxOEpWOCAQAA62L+sAjTXI3lmQH1CFy1sfMSsw5SEgk+XhlQFnE/hzMEht8kt+gLOfaghi9N9adJESundTlhxYUrklyKwcvcBYb398ZqDEuns4bSE9FAOeT69cJ/0VikjdEKoRUMkhUB56/SWOXrPsVDo9xrqj4taVsWx2n593udyF3hTNNXopPYdpXYgAzezpYSDK/dJTg5bOXpCO5dJLqatQ6zxnfbsqWQFwSsjc8k43f/1t3Ajt7SqG/qM0/6JLbMy9PDPaTplLdIl81IxZmdTsk1czMi+8fdvgxfpW0ZunrtIoIYSLkZlw3QABz4cnW7OIjvTg60k7Ecg5Z2kIQ1cRoqY+z+znQ14SKG6C1A5M9f1sPTDDiyHxZMxh4LF0dyBeX6WPCDPtJottxUW4+X0X6eKzUd6y9SP8w9QIbsU1fC8jueEIR+PMYHadi0ZzoM+JyBeS2ZsWzwWAw=~-1~-1~-1",
		u"bm_sz": u"7A8DFF6D80486C5F2FFE820F27473DFB~YAAQ7LCvw6J2HmOCAQAA5zzZsBARTJ8Q4YyzUBpauKgmMCySaZbnkTPDChUnmY9iXNNgMaIHlKhaDdQIbx3LqktQpJYWpTuS4drsNsvSzNjFry5aaMhunRB0UEc5EvUpy9FxNs0+NECo3E2vbTGjRQm+EY+pWcP3bZupfWPf2t7KU/8yd0IoAC4ujkyoomGNP5OFX5VzFFB4gtwjuzEazFCVwAr2hFDcsrWdAa/nBd2dE1RRFVr9KKi+vSlF4Q0FRV14uJNcOxINN4dMVXovK0LvKK6zeHccEcNTa+/9TJ8k+8Icx60XjkwTWcScVQTk4WPDqf0Y1cD8ykFvY2WeAoL43okmhNonOZg5DoOSphNVOrMVimbdlqRlpXdhDDuUZDrkWF4xtVsC4I/Q2suju+DTwdTf3v3G/b25FHu84nuiHRnbzg==~3159876~4539969",
	}

# Autorization Nike.com
# url_snkrs = 'https://www.nike.com/ca/launch'
url_login = 'https://www.nike.com/ca/member/profile/login?continueUrl=https://www.nike.com/ca/launch'
url_card = 'https://www.nike.com/ca/cart'
email = 'mozheykin.igor@gmail.com'
password = 'C3mqD7hg3uKr43E'

# Shop config
Snkrs = {
    'Rattan and Particle Grey': ['$170.00', '2022-08-11', 'https://www.nike.com/ca/launch/t/air-kukini-rattan-particle-grey'],
    'French Blue': ['$260.00', '2022-08-22', 'https://www.nike.com/ca/launch/t/air-jordan-13-french-blue-emea'],
}
Shoe_size = 'US 11'

# Paymend method
PM_method = 'Credit Card'
Card_number = ''
Name_on_card = ''
MMYY = ''
CVV = ''
Save_card_for_later_use = False
