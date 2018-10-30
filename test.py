import os
import io
import Image
import binascii
from smartcard.System import readers
from smartcard.util import HexListToBinString, toHexString, toBytes


# tis-620 to utf-8
def thai2unicode(data):
    result = ''
    if isinstance(data, list):
        for d in data:
            result += unicode(chr(d),"tis-620")
    else :
        result = data.decode("tis-620").encode("utf-8")
    return result.strip();

def getData(cmd, req = [0x00, 0xc0, 0x00, 0x00]):
    data, sw1, sw2 = connection.transmit(cmd)
    data, sw1, sw2 = connection.transmit(req + [cmd[-1]])
    return [data, sw1, sw2];


SELECT = [0x00, 0xA4, 0x04, 0x00, 0x08]
THAI_CARD = [0xA0, 0x00, 0x00, 0x00, 0x54, 0x48, 0x00, 0x01]

# CID
CMD_CID = [0x80, 0xb0, 0x00, 0x04, 0x02, 0x00, 0x0d]


# get all the available readers
r = readers()
reader = r[0]
print("Using:", reader)

connection = reader.createConnection()
connection.connect()
atr = connection.getATR()
print("ATR: " + toHexString(atr))
if (atr[0] == 0x3B & atr[1] == 0x67):
	req = [0x00, 0xc0, 0x00, 0x01]
else:
	req = [0x00, 0xc0, 0x00, 0x00]



apdu = SELECT + THAI_CARD
data, sw1, sw2 = connection.transmit(apdu)
print("data :", data, "SW : %02X %02X" % (sw1, sw2))

# CID
data = getData(CMD_CID, req)
cid = thai2unicode(data[0])
print("CID: " + cid)
