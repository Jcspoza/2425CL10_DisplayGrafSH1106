# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: basic hw test sh1106 i2c - Test writer, usar + fuentes
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Ref 2 : https://github.com/peterhinch/micropython-font-to-py/tree/master
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "sh1106 I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "BHWT sh1106 i2c - Test writer, usar + fuentes"
p_version = "1.0"
p_library = "SH1106  @robert-hh + writer @peterhinch"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
from sh1106 import SH1106_I2C
from writer import Writer

# Font
import inkfree20

WIDTH = const(128)
HEIGHT = const(64)
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# Mejor usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

# 0.1 Objeto I2C y LCD
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

ssd = SH1106_I2C(WIDTH, HEIGHT, i2c, addr = 0x3c, rotate = 0) # valores 0, 90, 180, 270

rhs = WIDTH -1
ssd.line(rhs - 20, 0, rhs, 20, 1)
square_side = 10
ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)

wri = Writer(ssd, inkfree20, verbose = False) # verbose = False to suppress console output
Writer.set_textpos(ssd, 0, 0)  
wri.printstring('Miercoles\n')
wri.printstring('2 Abr 2025\n')
wri.printstring('22.44pm')
ssd.show()
