# Main

<div align="center"><img src="https://cdnn21.img.ria.ru/images/07e6/05/19/1790576925_0:109:3239:1930_1920x0_80_0_0_31b180b574488a7c70ec43ea5d366cf6.jpg" width="620" height="388" style="display: block; margin: 0 auto;" class="jop-noMdConv"></div>

#  Installation. Produced once.
* Install python, [download url](https://www.python.org/downloads/)
* Install Git, [download url](https://git-scm.com/downloads)
* Install LigthShot, [download url](https://app.prntscr.com/ru/download.html)
* Install Sublime Text [download url](https://www.sublimetext.com/3)
* Moving to the root directory, create a folder and clone the repository into it:
  ```bash
  cd ../..
  mkdir github
  cd github
  git clone https://github.com/Mozheykin/buy_nike.git
  cd buy_nike
  ```
* Install requirements command: 
```python3
pip install -r requirements.txt
```
* I get the position of the browiser icon. \
In the terminal I enter the command:
```python
python test_position.py
```
Hover the mouse over the icon and press enter \
After the received data is written to the configuration file.
* Change config.py
> X = \
> Y = \
> email = '' \
> password = '' \
> Shoe_size = 'us_' \
> Card_number = '' \
> Name_on_card = '' \
> MMYY = '' \
> CVV = ''

* Change data.json
> {\
> &nbsp;&nbsp;&nbsp;&nbsp;"***Title***": [ \
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"***Price:*** $180.00", \
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"***Date:*** 2022-08-12",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"***URL:*** https://www.nike.com/ca/launch/t/air-force-1-low-retro-colour-of-the-month-royal-blue-white"\
&nbsp;&nbsp;&nbsp;&nbsp;],\
}

# Application launch
```python3
python pyautogui_opencv.py
```
# Info
To use the script you need:
1. Install Python
2. Install Git
3. Install LightShot
4. Customize config file
5. Update images from the pictures folder to fit your screen
6. Set up data.json file

**All script is ready to use**
