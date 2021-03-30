# import machine
# from machine import ADC
# import time
# import socket
#
# print('RUN: main.py')
# =========================================================

# import time
# from machine import ADC, Pin
#
# adc = ADC(Pin(35))
#
# while True:
#     value = adc.read()
#     print(value)
#     time.sleep(3)

#==========================================================

# import time
# import sys
# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BOARD)
# inpt = 35
# GPIO.setup(inpt, GPIO.IN)
# rate_cnt = 0
# tot_cnt = 0
# minutes = 0
# constant = 0.10
# time_new = 0.0
#
# print('Water Flow - Approximate')
# print('Control c to exit')
#
# while True:
#     time_new = time.time() + 60
#     rate_cnt = 0
#     while time.time() <= time_new:
#         if GPIO.input(inpt) != 0:
#             rate_cnt += 1
#             tot_cnt += 1
#         try:
#             print(GPIO.input(inpt), end='')
#         except KeyboardInterrupt:
#             print('\nCTRL C - Exiting nicely')
#             GPIO.cleanup()
#             sys.exit()
#     minutes += 1
#     print('\nLiters / min', round(rate_cnt * constant, 4))
#     print('\nTotal liters', round(tot_cnt * constant, 4))
#     print('\nTime (min & clock) ', minutes, '\t', time.asctime(time.localtime()))
#
# GPIO.cleanup()
# print('DONE')

import socket
import time
import machine
import random

IP = '192.168.137.175'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

global value
value = 0
global state
state = 'up'

ledrood = machine.Pin(32, machine.Pin.OUT)
ledoranje = machine.Pin(33, machine.Pin.OUT)
ledgroen = machine.Pin(25, machine.Pin.OUT)
ledblauw = machine.Pin(26, machine.Pin.OUT)


def get_msg():
    global value
    global state
    if value >= 20:
        state = 'down'
    elif value <= 0:
        state = 'up'
    if state == 'up':
        value += 1
    elif state == 'down':
        value -= 1
    return str(value)


global stateblue
stateblue = True

while True:
    s.send(bytes(get_msg(), "utf-8"))
    print('message sent')
    time.sleep(0.5)

    msgback = s.recv(1024)
    msgback.decode('utf-8')
    print(msgback)

    if msgback == b'red':
        ledrood.on()
        ledoranje.off()
        ledgroen.off()
    elif msgback == b'orange':
        ledrood.off()
        ledoranje.on()
        ledgroen.off()
    elif msgback == b'green':
        print('testgroen')
        ledrood.off()
        ledoranje.off()
        ledgroen.on()

    if msgback == b'blueOn':
        global stateblue
        if stateblue == True:
            ledblauw.on()
            stateblue = False
        elif stateblue == False:
            ledblauw.off()
            stateblue = True




