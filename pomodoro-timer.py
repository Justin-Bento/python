"""
  - [] Create a timer that breaks down in 4 intervals.
       - [] Main work interval. - 25 minutes
       - [] Main short break interval. 5 minutes.
       - [] Main long break interval. 30 minutes.
       - [] Repeat Interaction. 4 times
       - [] After 4 times close or repeate program.

  - [] Ask the user if they want defualt or custom setting.
       - [] Change break and interval time if yes 
       - [] Keep defult break and interval time if no 
  
  - [] System notification for completed times.
       - [] Have a title for short break, work and long break 
       - [] Have a message for short break, work and long break 

  - [] Ask the user if they would like to repeat interaction.
       - [] if user says y repeat interaction.
       - [] if user says no break and close the program.
"""
import time 

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("stop")

countdown(70)

def system_notification(title, message, action):
     pass

def break_intervals_short(short_break):
     pass

def break_intervals_long(long_break):
     pass

def work_intervals(sessions):
     pass