import pyautogui
import time

pyautogui.keyDown('win')                                                                #houd de windowstoets ingedrukt
pyautogui.press('m')                                                                    #drukt twee maals op de arrow-down knop  
pyautogui.keyUp('win')                                                                  #laat de windowstoets weer los
pyautogui.hotkey('win', 'r') 
pyautogui.write('https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran', interval=.1)
#schrijf 'https://github.com/new' in het run tekstveld
pyautogui.hotkey('enter')                                                               #druk op 'enter' op de link te openen
