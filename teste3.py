import pyautogui
import win32gui

point = pyautogui.locateCenterOnScreen('Resources/teste.png')
print( point )
pyautogui.click(point)
#pyautogui.click()