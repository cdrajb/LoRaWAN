from machine import Pin, UART
import time
import pylorawan

def get_resp(msg):
    ajb=str(msg).split('\r\n')
    i=0
    resp="None"
    for line in ajb:
        if "+" in line and not line.startswith("AT"):
            resp=line.split('+')[1]
        i += 1
    return(resp)

uart = UART(1, 115200, tx=Pin(4), rx=Pin(5))  # use RPI PICO; pins 4,5 are UART1 
modem = pylorawan.LorawanModem(uart, "ASR6501", debug=False)

cmds=("AT+CGMI?", "AT+CGMM?", "AT+CJOINMODE?", "AT+CCLASS?", "AT+CSTATUS?", "AT+CFREQBANDMASK?", "AT+CADR?", "AT+CDEVEUI?", "AT+CAPPEUI?", "AT+CAPPKEY?", "AT+CDEVADDR?","AT+CAPPSKEY?", "AT+CNWKSKEY?")

for cmd in cmds:
    found, resp_text = modem.run_command(command=cmd, wanted_response="OK", tries=1,rx_delay=0.5)
    resp=get_resp(resp_text)
    print(resp)

print()
print("CJOINMODE 0 is OTAA")
print("CCLASS 0 is ClassA")
print("CSTATUS 00 is idle, 03 is data sent OK")
print("See https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lorawan/ASR650X%20AT%20Command%20Introduction-20190605.pdf  for more detail")

