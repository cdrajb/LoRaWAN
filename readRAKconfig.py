from machine import Pin, UART
import time
import pylorawan

# reads the current LORAWAN settings (and checks serial communications to the RAK3172 module)

uart = UART(1, 115200, tx=Pin(4), rx=Pin(5))  # use RPI PICO; pins 4,5 are UART1 
modem = pylorawan.LorawanModem(uart, "RAK3172", debug=False)

found, resp_text = modem.run_command(command=f"AT+deveui=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
found, resp_text = modem.run_command(command=f"AT+appeui=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
found, resp_text = modem.run_command(command=f"AT+appkey=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
found, resp_text = modem.run_command(command=f"AT+band=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0]+" (band 4 is EU868)")
found, resp_text = modem.run_command(command=f"AT+class=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
found, resp_text = modem.run_command(command=f"AT+njm=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
found, resp_text = modem.run_command(command=f"AT+nwm=?", wanted_response="OK", tries=1,rx_delay=0.5)
ajb=str(resp_text).split('+')[1].split('\r')
print(ajb[0])
