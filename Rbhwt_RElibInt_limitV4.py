# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: basic hw test Rotary Encoder con libreria con Handler- Test #4 limite y vuleve
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : micropython-rotary
# Ref librerias: https://github.com/MikeTeachman/micropython-rotary
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "Rotary Encoder con libreria - Test #2- RE en pins 16 & 17"
p_project = "Rotary Encoder con libreria con Handler - Test #2 - limite y vuelve"
p_version = "1.0"
p_library = "micropython-rotary @miketeachman" 
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin

# 0 definicion del handler y led
step = None
# 0.2 Internal led config for flashing
intled = Pin("LED", Pin.OUT)
intled.on()

def manejaRE():
    global step
    step = r.value()
    print("Nuevo valor de step =", step)

#1- los 2 pines del Rotary Encoder, si el incremento es decremento -> invertir
TRA = 16
TRB = 17

#2- Creacion  del objeto
r = RotaryIRQ(
    pin_num_clk=TRB,
    pin_num_dt=TRA,
    min_val=0,
    max_val=5,
    reverse=False,
    incr=1,
    range_mode=RotaryIRQ.RANGE_WRAP,
    # pull_up=True, # si pull up por circuito -> comenta
    half_step=False,
    )

r.add_listener(manejaRE)

print('---------------------------')
print('Fin de la inicializacion : con Handler y RANGE_WRAP')
print('Va escribiendo y flaseandoel led interno')
print('Gira el RE y observa aparece el cambio de "steep" (0 a 5 y vuleve a empezar)')

    
while True:
    print('Hago cosas y hago parpadear el led')
    time.sleep(2)              
    intled.toggle() # cambia el led de encendido a apagado y viceversa
