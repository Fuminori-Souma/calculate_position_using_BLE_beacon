import asyncio
from bleak import BleakScanner

import bleak.backends.bluezdbus.scanner


def detection_callback(device, advertisement_data):

    global i

    if device.name == 'feasybeaco':
        i = i + 1
        # print(i)
        # print(device.rssi)
        print('No: ', i, ' | RSSI: ', device.rssi)


async def run():

    # d = {"filters": {
    #     "Name": "feasybeaco",
    #     'address': 'DC:0D:DC:74:0B:81',
    #     'RSSI': 100,
    #     'UUIDs': list('FDA50693-A4E2-4FB1-AFCF-C6EB076825')
    # }}
    # fltset = bleak.backends.bluezdbus.scanner.BleakScannerBlueZDBus(**d)
    # fltset.set_scanning_filter()

    scanner = BleakScanner()
    scanner.register_detection_callback(detection_callback)

    await scanner.start()
    await asyncio.sleep(100.0)
    # await scanner.stop()

    # for d in scanner.discovered_devices:
    #     print(d)


i = 0

while(True):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
