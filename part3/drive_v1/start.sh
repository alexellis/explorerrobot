#!/bin/sh
sudo hciconfig hci0 up
sudo systemctl start bluetooth
sudo hcitool scan

cd /home/pi/explorerrobot/part3/drive_v1/
/usr/bin/python ./app.py

