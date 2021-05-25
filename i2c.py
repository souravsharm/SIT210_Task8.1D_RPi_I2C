from smbus import SMBus
 
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
num= 1
 
print ("Enter 1 for ON and 0 for OFF")
while num== 1:
 
    led= input(">>>>   ")
 
    if led== "1":
        bus_.write_byte(addr, 0x1) # switch it on
    elif led== "0":
        bus_.write_byte(addr, 0x0)
    else:
        i= 0
