def conect():
    import network
    ssid = ""
    password = " "
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected()==True:
        print("Conectado")
        return
    
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected()==False:
        pass
    print("conexão bem sucedida")
    print(station.ifconfig())