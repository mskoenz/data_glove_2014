#---------------------------name----------------------------------------
TARGET = core

ARDLIBS = Wire

MODEL = ATMega20MHz


#~ PORT = /dev/ttyACM0
PORT = /dev/ttyUSB0
BAUD = 57600

OPT = s

include /home/msk/ArduinoMin/makefile/Master_Makefile.mk
