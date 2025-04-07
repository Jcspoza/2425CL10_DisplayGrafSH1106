# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: Show graphic commnads I2C oledsh sh1106 & framebuffer library - Carrusel
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 03 09
# Licencia : CC BY-NC-SA 4.0
# Add Learning topics : Design a progrma to mange a menu + use functions as objets
# Ref: https://www.coderdojotc.org/micropython/displays/graph/03-basic-drawing/
# Ref 2 : https://www.esploradores.com/oledsh_ssd1306/
# Ref 3 : https://docs.micropython.org/en/latest/library/framebuf.html
# 1.0 

from os import uname
# Informative block - start
p_keyOhw = "SH1106 I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "Graphic commands show carrusel -i2c 1-default pins"
p_version = "1.0"
p_library = "SH1106  @robert-hh"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
import array # necesario para coor de poligonos 
from utime import sleep_ms

# 0.0 - Constates y varaibles globales
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

def show_rect():
    """Display in oledsh a rectangule 20 x 16"""
    oledsh.rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    return "Rectangulo 20x16"

def show_Frect():
    """Display in oledsh a filled rectangule 20 x 16"""
    oledsh.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    return "Rect Lleno 20x16"

def show_invert():
    """Invert Display """
    oledsh.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    oledsh.invert(1)
    return "Invierte oledsh"

def show_normal():
    """Invert Display """
    oledsh.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    oledsh.invert(0)
    return "Normal oledsh"
    
def show_circ():
    """Display in oledsh a circule r= 20"""
    oledsh.ellipse(WIDTH//2, HEIGHT//2, 20, 20, 1) # x0, y0, radius, color
    return "Circulo r=30"

def show_ellipse():
    """Display in oledsh an ellipse rx= 40, ry=20"""
    oledsh.ellipse(WIDTH//2, HEIGHT//2, 40, 20, 1) # x0, y0, radius X, radius Y, color
    return "Ellipse (40,20)"

def show_QFellipse():
    """Display in oledsh a 1/4 ellipse rx= 40, ry=20"""
    oledsh.ellipse(WIDTH//2, HEIGHT//2, 40, 20, 1, True, 10) # x0, y0, radius X, radius Y, color, filled
    # last param is quarter ellipse indicator 1bit last 4
    # 0001 top right
    # 0010 top left
    # 0100 bottom left
    # 1000 bottom right
    return "Ellip 2q (40,20)"

def show_triangle():
    """Display in oledsh a triangle """
    cor = array.array('h',[60, 0, 30, 40, 90, 40])
    oledsh.poly(0, 10, cor, 1) 
    return "Triangle (63,10)"

def show_pentagono():
    """Display in oledsh a pentagono """
    cor = array.array('h',[60, 0, 15, 20, 30, 40, 90, 40, 105, 20])
    oledsh.poly(0, 10, cor, 1) # x0, y0, coor[x0,y0, x1,y1, x2, y2...], color
    return "Pentagon (63,10)"

MENU = [show_rect,
        show_circ,
        show_ellipse,
        show_triangle,
        show_pentagono,
        show_Frect,
        show_QFellipse,
        show_invert,
        show_normal]

      
# 0.1 Objeto I2C y LCD
# Mejor usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
print('Info del bus i2c: ',i2c)

oledsh = sh1106.SH1106_I2C(WIDTH, HEIGHT , i2c, addr = 0x3c, rotate = 0) # constructor - I2C direccion 3C por defecto
oledsh.sleep(False)
# 1- Programa Principal - Presentacion
oledsh.fill(0) # clear screen
oledsh.show()

oledsh.fill(0)
oledsh.text("Test", (WIDTH - len("Test")*8) // 2, 0)
oledsh.text("de", (WIDTH - len("de")*8) // 2, 16)
oledsh.text("Comand Graficos", (WIDTH - len("Comand Graficos")*8) // 2, 32)
oledsh.text("version " + p_version, 0, 48)
oledsh.show()
sleep_ms(3000)
oledsh.fill(0)
oledsh.show()

try:
    while True:
        oledsh.fill(0)
        oledsh.text("Test de graficos",0,0,1)
        oledsh.show()
        
        for opcion in range(len(MENU)):
            orden = MENU[opcion]
            msgL8 = orden()
            oledsh.text(msgL8, (WIDTH - len(msgL8)*8) // 2, 55, 1)
            oledsh.show(True) # hace que se actualicen todas las paginas, si no no funciona
            sleep_ms(5000)
            oledsh.fill(0)
            oledsh.text("Test de graficos",0,0,1)
            oledsh.show()
                   
except KeyboardInterrupt: #  si CTRL+C se presiona - > limpiar display
    oledsh.fill(0)
    oledsh.show()

