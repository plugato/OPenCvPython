import os
import pyscreenshot as ImageGrab
import cv2
import pyautogui, sys
import win32gui

def getState():
    imagem = screenshot('NoxPlayer')
    imagem.save('Resources/foo2.png', 'png')

    img_rgb = cv2.imread('Resources/foo2.png')
    #img_rgb = cv2.rotate(img_rgb, 2)
    cv2.imwrite('Resources/foo2.png', img_rgb)

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    return img_rgb


def inputScreen(x, y):

   if x:
       pyautogui.move(x, y)
       pyautogui.click()

   print( x,y)

def inputScreen(coords):
   if coords[0]:
        pyautogui.move( coords[0], coords[1])
        pyautogui.click()
        print( coords[0], coords[1])


def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            try:
                win32gui.SetForegroundWindow(hwnd)
                x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                x, y = win32gui.ClientToScreen(hwnd, (x, y))
                x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                im = pyautogui.screenshot(region=(x, y, x1, y1))
                return im
            except NameError:
                return ""
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im




