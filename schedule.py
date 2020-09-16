#!/usr/bin/env python3

import time
import schedule

def data_Structure():
    print("Get ready for data_structure algorithm")

def rest_time():
    print("go and walk for some time or get fresh")

def machine_learning():
    print("Work with machine learning projects")

def rest_time2():
    print("Eat something  or sleep for sometime now")

def java_practise():
    print("Work with the programming skills")

def c_practise():
    print("Practise som logical questions from c")


def nptel():
    print("Machine Learning Mathematics and R programming")

def python():
    print("Work with some skills")

def bedtime():
    print("Go to sleep ASAP")



schedule.every().day.at("03:30").do(data_Structure)


schedule.every().day.at("06:30").do(rest_time)


schedule.every().day.at("12:30").do(rest_time2)


schedule.every().day.at("07:30").do(machine_learning)


schedule.every().day.at("14:00").do(java_practise)


schedule.every().monday.at("16:30").do(c_practise)


schedule.every().monday.at("19:00").do(nptel)


schedule.every().monday.at("22:00").do(python)

schedule.every().monday.at("23:00").do(bedtime)












