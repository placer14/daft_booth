import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte_data(0x20,0x00,0x00)

bus.write_byte_data(0x20,0x14,0x00)

for MyData in range(1,8):
   bus.write_byte_data(0x20,0x14,MyData)
   print MyData
   time.sleep(1)

bus.write_byte_data(0x20,0x14,0x00)