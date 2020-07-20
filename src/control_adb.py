import os

import cv2


def getState():
    os.system(os.getcwd() + '/Resources/nox_adb  shell screencap -p /sdcard/foo.png')
    os.system(os.getcwd() + '/Resources/nox_adb  pull /sdcard/foo.png ' + os.getcwd() + '/Resources/foo.png > nul ')

    img_rgb = cv2.imread('Resources/foo.png')
    img_rgb = cv2.rotate(img_rgb, 2)
    cv2.imwrite('Resources/foo.png', img_rgb)


    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    return img_rgb


def inputScreen(x, y):
    # print(os.getcwd() + '/Resources/nox_adb shell input tap ' + str(x) + ' ' + str(y))
    os.system(os.getcwd() + '/Resources/nox_adb  shell input tap ' + str(x) + ' ' + str(y))


def inputScreen(coords):
    os.system(os.getcwd() + '/Resources/nox_adb  shell input tap ' + str(coords[0]) + ' ' + str(coords[1]))
