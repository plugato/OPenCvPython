import random

import time
import cv2
import numpy as np

from src.control_scs import *
from src.img_core import *

#getState()


def continuarBatalha():
    sequenciaIniciarBatalha = [
        'Resources/iniciarBatalha.png',
        'Resources/ProximaFase.png',
        'Resources/okRuna.png',
        'Resources/bau.png',
        'Resources/vitoria.png',
    ]
    templateExec(sequenciaIniciarBatalha)

def iniciarBatalha():
    sequenciaIniciarBatalha = [
        'Resources/teste.png',
    'Resources/batalha.png',
    'Resources/hydeni.png',
    'Resources/ragon.png',
    'Resources/kabir.png',
    'Resources/siz.png',
    'Resources/inicioBatalha.png',
    'Resources/iniciarBatalha.png',

    #'Resources/kabir.png',
    #'Resources/garen.png',
    ]

    templateExec( sequenciaIniciarBatalha )


def templateExec( templateSequence ):
    for x in templateSequence:
        point = pyautogui.locateCenterOnScreen(x)
        pyautogui.click(point)




        #inputScreen( getPossitionTemplate( getState(), cv2.imread( x, 0) ) )
        time.sleep(0.5)



iniciarBatalha()
while True:
    continuarBatalha()
    time.sleep(2)
