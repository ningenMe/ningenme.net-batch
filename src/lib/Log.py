import sys
import datetime
import pathlib
import requests
import json
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../conf')
import Env

def write(log_level,message):
    now      = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H:%M:%S")
    filepath = str(path.parent) + "/../../log/" + now.strftime("%Y-%m-%d") + ".txt"
    message  = log_level + " " + date_str + " " + str(message) + "\n"
    file = open(filepath,'a')
    file.write(message)
    file.close()

def slack(channel,message):
    url = Env.SLACK_WEBHOOK_URL
    requests.post(url, data = json.dumps({
        "channel": channel,
        "text"   : message
    }));


def info(message=""):
    write("INFO",message)
    slack("#log-info",message)

def error(message=""):
    write("ERROR",message)
    slack("#log-error",message)

if __name__ == "__main__":
    info("テスト")