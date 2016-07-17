import cwiid, time
wii = cwiid.Wiimote()
wii.rpt_mode = cwiid.RPT_BTN
wii.rumble = True
time.sleep(0.5)
wii.rumble = False

