
from cv2 import estimateAffine2D
import pyautogui as pt
import os
import time

tiempo_trabajo = 2
tiempo_dormir = 1
salir = True

busqueda = {
    "play":"controll/play.png",
    "reanudar":"controll/reanudar.png",
    "pausa":"controll/pausa.png",
    "pausa_causa":"controll/pausa_causa.png",
    "opciones_inicio":"controll/opciones_inicio.png",
    "opciones_cancelar":"controll/opciones_cancelar.png",
    "detener":"controll/detener.png",
    "aceptar":"controll/aceptar.png",
    "trabajando":"controll/trabajando.png",
    "sin_trabajo":"controll/finalizado.png"

}

def mover(move,click = False):
    
    position = pt.locateCenterOnScreen(move)
    print(position)
    pt.moveTo(position) 
    if click == True:
        pt.click(button="left")
    
    time.sleep(1)
    return position
    pass


def reanudar():
    time.sleep(2)
    print("buscar_play")
    mover(busqueda["play"],True)
    p = mover(busqueda["opciones_inicio"])
    if p != None:
        mover_abajo = pt.Point(0,10)
        pt.moveRel(mover_abajo)
        pt.click(button="left")
        mover(busqueda["opciones_cancelar"])
        mover(busqueda["aceptar"],True)
    else:
        salir = True
    pass

def detener():
    time.sleep(2)
    mover(busqueda["pausa"])
    mover(busqueda["pausa_causa"],True)
    mover(busqueda["detener"],True)
    pass

def detectar(buscar):
    position = pt.locateCenterOnScreen(busqueda[buscar])
    time.sleep(1)
    if position == None:
        return False
    else:
        return True
    pass

while salir == True:

    
    
    
    estado = detectar("trabajando")
    if estado:
        time.sleep(tiempo_trabajo*60)
        print("detener")
        detener()
    time.sleep(1)
    estado = detectar("sin_trabajo")
    if estado:
        time.sleep(tiempo_dormir*60)
        print("reanudar")
        reanudar()
    pass

