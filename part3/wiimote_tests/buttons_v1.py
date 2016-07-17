import cwiid, time
wii = cwiid.Wiimote()
wii.rpt_mode = cwiid.RPT_BTN
while(True):
  buttons = wii.state['buttons']
  if buttons & cwiid.BTN_A:
      print("A pressed, go forwards")
  if buttons & cwiid.BTN_B:
      print("B pressed, go backwards")

