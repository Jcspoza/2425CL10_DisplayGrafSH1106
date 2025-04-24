# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: basic hw test sh1106 i2c - 3 switchs test with int
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 => SDA0 & SCL0 400khz + 3 sw pins 18, 19 & 20"
p_project = "Test HW basico - Test de los 3 pulsadores con interrupciones"
p_version = "1.0"
p_library = "Ninguna"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
# import sh1106
import utime  

# 0. 1 Definition de los 3 switchs
listaPul = ['confirm', 'back', 'push']

CONFIRM = 18
BACK = 19
PUSH = 20
# confPul = Pin(CONFIRM, Pin.IN) # pull up por circuito
# backPul = Pin(BACK, Pin.IN) # pull up por circuito
# pushPul = Pin(PUSH, Pin.IN) # pull up por circuito

confPul = Pin(CONFIRM, Pin.IN, Pin.PULL_UP) # pull up por sw
backPul = Pin(BACK, Pin.IN, Pin.PULL_UP) # pull up por sw
pushPul = Pin(PUSH, Pin.IN, Pin.PULL_UP) # pull up por sw

# 0.2 Internal led config for flashing
intled = Pin("LED", Pin.OUT)
intled.on()

# 0.3 Configura interrupciones asociadas a los pulsadores
teclas = [] # guarda las teclas presionadas
last_time = 0 # guarda la ultima marca de tiempo en que se presiono el pulsador

def manejaPulsadores(pin):
    
    global teclas, last_time
    new_time = utime.ticks_ms()
    # Si ha pasado mas de 200ms desde el ultimo evento, temenos un nuevo evento. Evita los REBOTES
    if utime.ticks_diff(new_time, last_time) > 400: 
        teclas.append(listaPul[int(str(pin).split(",")[0][8:]) - CONFIRM])
        # Si la interrupcion vien del pulsador 'back' en GPIO19
        # objeto 'pin' devuelve por ejemplo 'Pin(GPIO19, mode=IN)' si lo pasamos a str
        # slip(",") parte por la coma en una lista ['Pin(GPIO19', ' mode=IN)']
        # [0][8:] toma del primero de la lista los caracteres del 8 al final, y lo pasa a int
        # 'Pin(GPIO19'[8:] -> '19'
        # y resta el valor de CONFIRM = 18 , dando 1
        # busca en listaPul[1] => 'back'
        last_time = new_time
        
confPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

backPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

pushPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

while True:
    print('hago cosas y hago parpadear el led')
    utime.sleep(1)
    if teclas != []:
        for t in teclas:
            print(t)
        teclas = []
            
    intled.toggle() # cambia el led de encendido a apagado y viceversa

