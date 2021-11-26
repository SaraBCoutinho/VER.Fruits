import ufirebase as firebase
import network
from machine import Pin
import gc
gc.collect()
ssid = " "
password =" "
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print("Conectado")
print(station.ifconfig())
led = Pin(2, Pin.OUT)
while True:
    Ledpython=firebase.put("https://verfruitsdatabase-default-rtdb.firebaseio.com/frutas.json")
   
        
    