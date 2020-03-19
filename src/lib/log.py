import datetime
import os

def write(log_level,message):
    now      = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H:%M:%S")
    filepath = os.path.dirname(__file__) + "/../../log/" + now.strftime("%Y-%m-%d") + ".txt"
    message  = log_level + " " + date_str + " " + str(message) + "\n"
    file = open(filepath,'a')
    file.write(message)
    file.close()

def info(message=""):
    write("INFO",message)

def error(message=""):
    write("ERROR",message)