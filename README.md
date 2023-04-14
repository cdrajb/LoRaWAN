# LoRaWAN
LoRaWAN library (extended for ASR6501) and associated code

The LoRaWAN library pylorawan.py (python) is based on https://github.com/phoughton/pylorawan/blob/main/pylorawan.py (which supports RAK3172), with some modifications and extended to also support ASR6501 (tested with M5 LoRaWAN868)

The examples are for a Pi Pico with either of the tested LoRaWAN devices and a DHT11 temperature & humidity sensor attached, and will send the readings to The Things Network (TTN).  

M5_reset.py turns off autojoin and logging to put the M5 LoRaWAN868 into a known state ready for configuration

readM5config.py reads and prints a number of the registers, for reference and to check that serial communication to the device is working

m5-temphumid.py configures the LoRaWAN device, joins TTN, and sends DHT11 readings every 15 minutes
