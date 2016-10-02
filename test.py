import gatt_bluetooth as ble


device = ble.BTLEDevice("EF:B9:CA:A5:A5:6C")

def notification_handler(handle, value):
    if handle == device._handles["ctrl-pt"]:
        print(value)

device.connect()
print("connected")
device.char_list()
print("char discovered")
device.subscribe(device._handles["ctrl-pt"], notification_handler)
device.char_write(device._handles["ctrl-pt"], [0x01], True)
device.run()
