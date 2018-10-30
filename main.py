from smartcard.System import readers
import binascii

# Thailand ID Smartcard 

# get all the available readers
r = readers()
reader = r[0]
print("Using:", reader)
connection = reader.createConnection()
connection.connect()

# Reset
SELECT = [0x00, 0xA4, 0X04, 0x00, 0x08, 0xA0, 0X00, 0x00, 0x00, 0x54, 0x48, 0x00, 0x01]

data, sw1, sw2 = connection.transmit(SELECT)
print("data :", data, "SW : %02X %02X" % (sw1, sw2))
