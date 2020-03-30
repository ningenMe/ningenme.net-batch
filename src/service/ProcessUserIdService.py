import sys
import pathlib
import time
path = pathlib.Path(__file__).resolve()
import UpdateCurrentUserListPageNumService

def main(site,begin,end):
    for i in range(begin,end+1):
    #     # get
    #     # update
        UpdateCurrentUserListPageNumService.main(site,i)
        time.sleep(1)

