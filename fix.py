#!/usr/bin/env python3
TIME_DIFFERENCE = -8
OLD_FILENAME="old.srt"
NEW_FILENAME="new.srt"
# A simple script that adjusts the time for subrip subtitle files.

import time
from datetime import timedelta
from datetime import datetime

def change_time(time_string, time_difference):
    time_string = time_string.decode("utf-8")
    before = datetime.strptime(time_string, "%H:%M:%S,%f")
    change = timedelta(seconds=time_difference)
    after = before + change
    new_time_string = after.strftime("%H:%M:%S,%f")[:-3]
    return new_time_string

with open(OLD_FILENAME, "rb") as f:
    data = f.readlines()
with open(NEW_FILENAME, "wb") as f:
    new = True
    for line in data:
        newline = line
        cleaned = line.strip()
        # A blank line
        if not cleaned:
            new = True
        # The integer below it
        elif new and cleaned.isdigit():
            pass
        # The timestamp
        elif new:
            new = False
            split = cleaned.split(bytes(" --> ".encode("utf-8")))
            reconstructed = "{} --> {}".format(change_time(split[0], TIME_DIFFERENCE), change_time(split[1], TIME_DIFFERENCE)) + "\n"
            newline = reconstructed.encode("utf-8")
            print(reconstructed)
        # The lines of dialogue
        else:
            pass
        f.write(newline)

