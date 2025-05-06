# Programa: Codigo Minimo para display sh1106 i2c 
from machine import Pin, I2C
import sh1106

# 0.0 - Constates globales
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
# Conexion alternativa a I2C1
# I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

# Creacion del objeto display
display = sh1106.SH1106_I2C(WIDTH,
                            HEIGHT,
                            i2c,
                            res = None,
                            addr = 0x3c,
                            rotate = 0) # valores 0, 90, 180, 270
display.sleep(False) # equivale a encender el display
# se puede usar alternativamentge : display.poweron()
display.fill(0)
display.text('Codigo minimo', 0, 0, 1)
display.show()
