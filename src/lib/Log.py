import sys
import datetime
import pathlib
import requests
import json
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../conf')
import Env

def write(message):
    now      = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H:%M:%S")
    filepath = str(path.parent) + "/../../log/" + now.strftime("%Y-%m-%d") + ".txt"
    file = open(filepath,'a')
    file.write(message)
    file.close()

def slack(channel,message):
    url = Env.SLACK_WEBHOOK_URL
    requests.post(url, data = json.dumps({
        "channel": channel,
        "text"   : str(message)
    }));

def makeMessage(log_level,message):
    now      = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H:%M:%S")
    message = log_level + " " + date_str + " " + str(message) + "\n"
    return message

def info(message=""):
    message = makeMessage("INFO",message)
    write(message)
    slack("#log-info",message)

def error(message=""):
    message = makeMessage("ERROR",message)
    write(message)
    slack("#log-error",message)

def debug(message=""):
    message = makeMessage("DEBUG",message)
    write(message)
    slack("#log-debug",message)

if __name__ == "__main__":
    debug("テスト")