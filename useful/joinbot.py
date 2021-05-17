#! /usr/bin/python3.9
# required modules
import sys
import alive_progress
from alive_progress.styles.internal import THEMES
import pyautogui as pyg
import webbrowser as wb
import datetime
import time
#import click
import csv
from alive_progress import alive_bar

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

def datetime_to_seconds(datetime_obj:datetime.datetime, precision:int=1):
    return (((datetime_obj.year * 365.25 + datetime_obj.day)*24+datetime_obj.hour)*60+datetime_obj.minute)*60+datetime_obj.second+datetime_obj.microsecond/1000000

# join the meeting
def join_meeting(zoom_link, meeting_date, meeting_time, meeting_name):

    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    """ wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    str2 = "Your ZOOM meeting starts in " + str(wait_time_sec/60) + " minutes" + " and " + str(wait_time_sec%60) + " seconds!"
    print(str2)
    time.sleep(wait_time_sec) """
    initial = datetime_to_seconds(datetime.datetime.now())
    total = datetime_to_seconds(required_datetime) - initial
    count = 0

    with alive_bar(int(total), title=meeting_name, bar='filling') as bar:
        while count < total or count == 0:
            
            """ str1 = "Your ZOOM meeting starts in " + str(wait_time_sec%60) + " seconds!"
            str2 = "Your ZOOM meeting starts in " + str(wait_time_sec/60) + " minutes" + " and " + str(wait_time_sec%60) + " seconds!" """
            count = datetime_to_seconds(datetime.datetime.now())-initial
            time.sleep((1000000-datetime.datetime.now().microsecond)/1000000)
            bar()


    # zoom app related
    wb.get(using='opera').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(2) # given time for the link to show app top-up window
    pyg.click(x=873, y=479, clicks=1, interval=0, button='left') # click on open meeting
    time.sleep(2) # wait for 10 sec
    pyg.click(x=1096, y=217, clicks=1, interval=0, button='left') # open-xdg
    time.sleep(1) # wait for 3 sec
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
        datetime_now = datetime.datetime.now()
        meeting_datetime = given_datetime(format_date(meeting['meeting_date']), format_time(meeting['meeting_time']))
        
        if meeting_datetime > datetime_now:
            join_meeting(meeting['zoom_meeting'], meeting['meeting_date'], meeting['meeting_time'], meeting["meeting_name"])
        else:
            print("You missed " + meeting['meeting_name'] + "!")
            continue

if __name__ == '__main__':
    try:
        zoom_meeting()
    except KeyboardInterrupt:
        print("It's treason then...")
        wb.get(using="opera").open("https://www.youtube.com/watch?v=4TvTjTO2hAI", new=2)
        sys.exit()
    except ValueError:
        print("Your meeting has already started or you missed your automatic join time!")
        sys.exit()