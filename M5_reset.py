from machine import Pin, UART
import time
import pylorawan

uart = UART(1, 115200, tx=Pin(4), rx=Pin(5))  # use RPI PICO; pins 4,5 are UART1 
modem = pylorawan.LorawanModem(uart, "ASR6501", debug=False)

print("Rebooting, resetting join config, and setting log level to 0")

found, resp_text = modem.run_command(command=f"AT+IREBOOT=0", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
i=0
for line in ajb:
    if "IREBOOT" in line:
        print(line)
    elif "OK" in line:
        print("OK")
    i += 1

found, resp_text = modem.run_command(command=f"AT+ILOGLVL=0", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
i=0
for line in ajb:
    if "ILOGLVL" in line:
        print(line)
    elif "OK" in line:
        print("OK")
    i += 1

found, resp_text = modem.run_command(command=f"AT+CJOIN=0,0,10,8", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
i=0
for line in ajb:
    if "CJOIN" in line:
        print(line)
    elif "OK" in line:
        print("OK")
    i += 1
	