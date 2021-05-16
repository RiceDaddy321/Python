#! /usr/bin/python3.9
#import pyautogui, sys
from joinbot import parse_csv, zoom_meeting
meetings = parse_csv("meetings.csv")

for meeting in meetings:
    print(meeting['meeting_time'])

""" print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n') """