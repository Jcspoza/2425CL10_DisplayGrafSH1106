# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: basic hw test Rotary Encoder SIN libreria - Test #0
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2023 04 11
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "Rotary Encoder SIN libreria - Test #0- RE en pins 16 & 17"
p_project = "Rotary Encoder SIN libreria - Test #0"
p_version = "0.0"
p_library = "Ninguna" 
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

import time
from machine import Pin
# =0 Creacion de objetos pin para los dos pines del rotary
# caso a) el circuito hardware no tiene pull-up
# rotaryA = Pin(16, Pin.IN, Pin.PULL_UP)
# rotaryB = Pin(17, Pin.IN, Pin.PULL_UP)

# caso b) el circuito hardware tiene pull-up
rotaryA = Pin(16, Pin.IN) # pull up por circuito
rotaryB = Pin(17, Pin.IN) # pull up por circuito

# 1- inicializamos
A_val_old = 0
B_val_old = 0
print('---------------------------')
print('Fin de la inicializacion.')
print('Gira el RE y veras cambiar la secuencia de los valores de los pines')
print('Si giras a derecha la secuencia tene el orden inverso de girar a al izquierda')
print('Secuencia de giro a la derecha : 11 -> 01 -> 00 -> 10 -> 11')
print('Secuencia de giro a la izquierda : 11 -> 10 -> 00 -> 01 -> 11')

while True:
    A_val = rotaryA.value()
    B_val = rotaryB.value()
    
    if A_val != A_val_old or B_val != B_val_old:
            print(A_val, end='')
            print(B_val)
            A_val_old = A_val
            B_val_old = B_val
    time.sleep(.00001)
    
