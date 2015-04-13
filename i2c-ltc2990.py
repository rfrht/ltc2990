#!/usr/bin/python -x
# 
# LTC 2990 Quad I2C Voltage, Current and Temperature Monitor
# Retrieves LTC2990 register and performs some basic operations.
# Specs: http://www.linear.com/product/LTC2990
# By: Rodrigo Freire
# Date: 2014 Apr 13
#

import smbus
bus = smbus.SMBus(1)   # 512-MB RPi the bus is 1. Otherwise, bus is 0.
address = 0x4f         # I2C chip address
mode = 0x5f            # Register 0x01 mode select. V1, V2, V3, V4

try:
  r1 = bus.read_byte_data(address, 0x01)     # Retrieve current mode select
  if r1 != mode:                             # If current mode != R1
    bus.write_byte_data(address, 0x01, mode) # Initializes the IC

except IOError, err:
  print err

bus.write_byte_data(address, 0x02, 0x00) # Trigger a data collection

r0 = bus.read_byte_data(address, 0x00) # Status
r1 = bus.read_byte_data(address, 0x01) # Control - mode select
r4 = bus.read_byte_data(address, 0x04) # Temp. Int. MSB
r5 = bus.read_byte_data(address, 0x05) # Temp. Int. LSB
r6 = bus.read_byte_data(address, 0x06) # V1, V1 - V2 or TR1 MSB
r7 = bus.read_byte_data(address, 0x07) # V1, V1 - V2 or TR1 LSB
r8 = bus.read_byte_data(address, 0x08) # V2, V1 - V2 or TR1 MSB
r9 = bus.read_byte_data(address, 0x09) # V2, V1 - V2 or TR1 LSB
ra = bus.read_byte_data(address, 0x0a) # V3, V3 - V4 or TR2 MSB
rb = bus.read_byte_data(address, 0x0b) # V3, V3 - V4 or TR2 LSB
rc = bus.read_byte_data(address, 0x0c) # V4, V3 - V4 or TR2 MSB
rd = bus.read_byte_data(address, 0x0d) # V4, V3 - V4 or TR2 LSB
re = bus.read_byte_data(address, 0x0e) # Vcc MSB
rf = bus.read_byte_data(address, 0x0f) # Vcc LSB

# Check for a specific bit value
def get_bit(number, bit):
  return (number >> bit) & 1 

def temperature(msb,lsb):
  msb = format(msb, '08b')
  msb = msb[3:]
  lsb = format(lsb, '08b')
  temp = msb + lsb
  temp = int(temp, 2)/16
  return temp

def voltage(msb,lsb):
  msb = format(msb, '08b')
  # print "Raw MSB: %s" %msb
  msb = msb[1:]

  lsb = format(lsb, '08b')
  #print "Raw LSB: %s" %lsb

  signal = get_bit(int(msb, 2),6)
  #print "positive:0 negative:1 %s" %signal
  #print "msb: %s" %msb[1:]
  #print "lsb: %s" %lsb

  volt = msb[1:] + lsb

  #print "volt: %s" %volt
  volt = int(volt, 2) * 0.00030518
  #print volt
  return volt

print "Temperature: %s Celsius" %temperature(r4,r5)

print "Voltage V1 : %s V" %voltage(r6,r7)
print "Voltage V2 : %s V" %voltage(r8,r9)
print "Voltage V3 : %s V" %voltage(ra,rb)
print "Voltage V4 : %s V" %voltage(rc,rd)

vin=voltage(re,rf) + 2.5
print "Vin        : %s V" %vin

