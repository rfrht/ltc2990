#!/usr/bin/python
# 
# LTC 2990 Quad I2C Voltage, Current and Temperature Monitor
# Retrieves LTC2990 register and performs some basic operations.
# Specs: http://www.linear.com/product/LTC2990
# Source: https://github.com/rfrht/ltc2990
#
# Copyright (C) 2015 Rodrigo A B Freire
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.

import smbus
import time
bus = smbus.SMBus(1)   # 512-MB RPi the bus is 1. Otherwise, bus is 0.

# Pro tip: Ensure that ADR0 and ADR1 are grounded. Do not let them
# open. Otherwise, the i2c address will randomly change.a
address = 0x4c         # I2C chip address
mode = 0x5f            # Register 0x01 mode select. V1, V2, V3, V4

try:
  if bus.read_byte_data(address, 0x01) != mode: # If current IC mode != program mode
    bus.write_byte_data(address, 0x01, mode)    # Initializes the IC and set mode
    bus.write_byte_data(address, 0x02, 0x00)    # Trigger a initial data collection
    time.sleep(1)				# Wait a sec, just for init
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
  msb = msb[1:]
  lsb = format(lsb, '08b')
  signal = get_bit(int(msb, 2),6)
  #print "positive:0 negative:1 %s" %signal
  volt = msb[1:] + lsb
  volt = int(volt, 2) * 0.00030518
  return volt


print "Int. Temp. : %s Celsius" %temperature(r4,r5)
print "Voltage V1 : %s V" %voltage(r6,r7)
print "Voltage V2 : %s V" %voltage(r8,r9)
print "Voltage V3 : %s V" %voltage(ra,rb)
print "Voltage V4 : %s V" %voltage(rc,rd)

# If you want to use TR, use the temperature(msb,lsb) function to get the
# value. I.e., if you have set the mode TR1 & TR2 (mode 0x5d),
# Comment the print "Voltage" lines and uncomment these ones:

# TR1
# print "Temperature TR1: %s Celsius" %temperature(r6,r7)
# TR2
# print "Temperature TR2: %s Celsius" %temperature(ra,rb)

# And print the supply voltage:
vin = voltage(re,rf) + 2.5
print "Vin        : %s V" %vin

