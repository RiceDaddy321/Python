# required modules
import sys
import pyautogui as pyg
import webbrowser as wb
import datetime
import time
#import click
import csv

#Launch meeting: 873, 479
#open-xdg: 1096, 217
#End meeting: 1631, 1019
#confirm: 1579, 1970 OR 845, 526

# functions to format date, time

def parse_csv(file_location):
    with open(file_location, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        meetings = []
        for line in csv_reader:
            meetings.append(line)
      
        return meetings

def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, MM, DD, HH, MM
    return datetime.datetime(given_date[2], given_date[0], given_date[1], given_time[0], given_time[1], given_time[2])

# join the meeting
def join_meeting(zoom_link, meeting_date, meeting_time):

    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    while True:
        wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
        if wait_time_sec <= 0:
            break
        else:
            str1 = "Your ZOOM meeting starts in " + str(wait_time_sec%60) + " seconds!"
            str2 = "Your ZOOM meeting starts in " + str(wait_time_sec/60) + " minutes" + " and " + str(wait_time_sec%60) + " seconds!"

            if wait_time_sec < 60:
                print(str1, end='')
                print('\b' * len(str1), end='', flush=True)
            else:
                print(str2, end='')
                print('\b' * len(str2), end='', flush=True)

    # zoom app related
    wb.get(using='opera').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(5) # given time for the link to show app top-up window
    pyg.click(x=873, y=479, clicks=1, interval=0, button='left') # click on open meeting
    time.sleep(10) # wait for 10 sec
    pyg.click(x=1096, y=217, clicks=1, interval=0, button='left') # open-xdg
    time.sleep(3) # wait for 3 sec
    pyg.click(x=873, y=479, clicks=2, interval=0, button='left') # click on fullscreen

""" @click.command()
@click.option('--zoom_link',
              help="full ZOOM meeting link",
              required=True)

@click.option('--meeting_date',
              help="date of the meeting in the format DD-MM-YYYY",
              required=True)

@click.option('--meeting_time',
              help="time of the meeting in the format HH-MM-SS",
              required=True) """

##
def zoom_meeting():
    print("Initializing everything")
    meetings = parse_csv('/home/jv/Documents/Coding Projects/Python-Scripts/useful/meetings.csv')

    for meeting in meetings:
        join_meeting(meeting['zoom_meeting'], meeting['meeting_date'], meeting['meeting_time'])

if __name__ == '__main__':
    try:
        zoom_meeting()
    except KeyboardInterrupt:
        print("It's treason then...")
        wb.get(using="opera").open("https://www.youtube.com/watch?v=4TvTjTO2hAI", new=2)
        sys.exit()