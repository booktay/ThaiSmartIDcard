const { ThaiCardReader, EVENTS, MODE } = require('@privageapp/thai-national-id-reader')
const { fs } = require("fs")

const reader = new ThaiCardReader()
reader.readMode = MODE.PERSONAL_PHOTO
reader.autoRecreate = true
reader.startListener()

reader.on(EVENTS.DEVICE_CONNECTED, () => {
  console.log("Device Connect")
})

reader.on(EVENTS.DEVICE_DISCONNECTED, () => {
  console.log("Device Disconnect")
})

reader.on(EVENTS.CARD_INSERTED, () => {
  console.log("Insert Card")
})

reader.on(EVENTS.CARD_REMOVED, () => {
  console.log("Remove Card")
})

reader.on(EVENTS.READING_INIT, () => {
  console.log("Prepared Reading Card")
})

reader.on(EVENTS.READING_START, () => {
  console.log("Start Reading Card")
})

reader.on(EVENTS.READING_PROGRESS, (obj) => {
  if (obj.step <= 5 || obj.step === 25) {
    console.log("In Progress Reading Card [" + obj.step + "/" + obj.of + "]")
  }
})

reader.on(EVENTS.READING_COMPLETE, (obj) => {
  console.log("Complete Reading Card")
  console.log(obj)
  
  // fs.writeFile("raw", obj, function (err) {
  //   if (err) throw err;
  //   console.log('Saved Raw!');
  // });

  // var image = new Image();
  // image.src = obj.photo;
  // fs.writeFile("raw.jpg", image, function (err) {
  //   if (err) throw err;
  //   console.log('Saved JPEG!');
  // });
})



