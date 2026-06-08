#Smart WhatsApp Personal Assistant

import pywhatkit as pw
import schedule
import time

number = input("Enter phone number with country code: ")
name = input("Enter your name: ")

def morning_message():
    pw.sendwhatmsg_instantly(
        number,f" Good Morning {name}! Have a great day ahead!"
        )

def study_reminder():
    pw.sendwhatmsg_instantly(
        number,f" Hey {name}, it's time to study!"
        )

def lunch_message():
    pw.sendwhatmsg_instantly(
        number,f" Hi {name}, it's lunchtime! Enjoy your meal."
        )

def evening_message():
    pw.sendwhatmsg_instantly(
        number,f" Good Evening {name}! Hope your day is going well."
        )

def bedtime_message():
    pw.sendwhatmsg_instantly(
        number,f" Good Night {name}! Sleep well."
        )


schedule.every().day.at("07:00").do(morning_message)
schedule.every().day.at("10:00").do(study_reminder)
schedule.every().day.at("14:03").do(lunch_message)
schedule.every().day.at("18:00").do(evening_message)
schedule.every().day.at("22:00").do(bedtime_message)

print(" Smart WhatsApp Personal Assistant Started...")
