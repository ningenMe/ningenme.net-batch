import sys
import pathlib
import time
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../service')
import GetUserIdNumService

def main(site):
    # get current and all user id num
    currentUserIdNum,allUserIdNum = GetUserIdNumService.main(site)
    # get user id list
    # proccess user info
    # update user id num