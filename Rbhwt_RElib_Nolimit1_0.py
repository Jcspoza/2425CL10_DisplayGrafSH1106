# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: basic hw test Rotary Encoder con libreria - Test #1 - SIN limite
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : micropython-rotary
# Ref librerias: https://github.com/MikeTeachman/micropython-rotary
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "Rotary Encoder con libreria - Test #1- RE en pins 16 & 17"
p_project = "Rotary Encoder con libreria - Test #1"
p_version = "1.0"
p_library = "micropython-rotary @miketeachman" 
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

import time
from rotary_irq_rp2 import RotaryIRQ

# 0- los 2 pines del Rotary Encoder, si el incremento es decremento -> invertir
TRA = 16
TRB = 17

#1- Creacion  del objeto
r = RotaryIRQ(
    pin_num_clk=TRB,
    pin_num_dt=TRA,
    reverse=False,
    incr=1,
    range_mode=RotaryIRQ.RANGE_UNBOUNDED,
    # pull_up=True, # si pull up por circuito -> comenta
    half_step=False,
    )

print('---------------------------')
print('Fin de la inicializacion : RANGE_UNBOUNDED')
print('Gira el RE y observa si el contador "steep" se incrementa o decrementa SIN Limite')
val_old = None 
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print("step =", val_new)

    time.sleep_ms(50)
