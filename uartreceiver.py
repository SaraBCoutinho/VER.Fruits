import machine

uart = machine.UART(1, 115200)

# Create a global variable to hold the receive data in serial
strMsg = ''

# This is the main loop
while True:
	# if there is character in receive serial buffer
    if uart.any() > 0:
    	# Read all the character to strMsg variable
        strMsg = uart.read()
        # Debug print to REPL
        print(strMsg)