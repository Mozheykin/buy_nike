import pyautogui
import json
import config

def main() -> None:
    position = pyautogui.position()
    #newposition = (position.x + 200, position.y)
    newposition = (position.x, position.y)
    pyautogui.moveTo(newposition)
    print(newposition)
    



if __name__ == '__main__':
    main()