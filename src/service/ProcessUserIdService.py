import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import time
import Log
import UpdateCurrentUserListPageNumService
import GetUserIdService
import UpdateUserIdService

def main(site,begin,end):
    for index in range(begin,end+1):
        # get
        userIdList = GetUserIdService.main(site,index)
        # update
        UpdateUserIdService.main(site,userIdList)
        # update
        UpdateCurrentUserListPageNumService.main(site,index)
        # sleep
        Log.debug(index)
        time.sleep(3)

