from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

numb = 1

print ("On Console enter 1,2,3 for the lights and 0 for OFF ")
while numb == 1:

	ledstate = input(":: ")

	if ledstate == "1":
		bus.write_byte(addr, 0x1)
	elif ledstate == "0":
		bus.write_byte(addr, 0x0)
	elif ledstate == "2":
		bus.write_byte(addr, 0x2) 
	elif ledstate == "3":
		bus.write_byte(addr, 0x3) 
	else:
		numb = 0
