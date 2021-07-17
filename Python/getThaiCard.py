import json
import os
from datetime import datetime
from ThaiNIDSmartcard import ThaiNIDSmartcard

class getThaiCard:
    def setExportDir(self):
        destination_path = "card." + datetime.now().strftime("%Y%m%d")
        if not os.path.exists(destination_path): os.makedirs(destination_path)
        return destination_path

    def exportJSON(self, export_path="", data={}):
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            print("[Success] Create " + export_path)

    def exportJPGfromHex(self, export_path="", data=[]):
        with open(export_path, "wb") as fphoto:
            for row in data:
                if row : fphoto.write(bytearray(row))
            print("[Success] Create " + export_path)

    def run(self):
        thaiNIDSmartcard = ThaiNIDSmartcard()
        thaiNIDSmartcard.connectToReader(deviceName="Generic USB2.0-CRW")
        if thaiNIDSmartcard.checkIfThaiSmartIDCard():
            datas = thaiNIDSmartcard.getAllData()
            photo = thaiNIDSmartcard.getPhoto()
            print("\n[Completed] ID : " + datas["ID"])
            self.exportJSON(export_path=self.setExportDir() + "/" + datas["ID"] + ".info.json", data=datas)
            self.exportJPGfromHex(export_path=self.setExportDir() + "/" + datas["ID"] + ".photo.jpg", data=photo)

if __name__ == "__main__":
    getThaiCard().run()
