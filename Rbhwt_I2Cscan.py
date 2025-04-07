# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: Test HW basico Scan bus i2c
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : 
# Ref librerias: 
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0


from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "Test HW basico Scan bus i2c"
p_version = "1.0"
p_library = "Nothing"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C

FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# Mejor usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

print(i2c)
print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices
device_count = len(devices)
if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')
for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))
