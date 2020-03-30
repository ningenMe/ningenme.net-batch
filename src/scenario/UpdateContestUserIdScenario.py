import sys
import pathlib
import time
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../service')
import GetAllUserListPageNumService
import UpdateAllUserListPageNumService
import GetCurrentUserListPageNumService
import UpdateCurrentUserListPageNumService
import ProcessUserIdService

def main(site):
    # get user list page num
    allUserListPageNum = GetAllUserListPageNumService.main(site)
    # update user list page num
    UpdateAllUserListPageNumService.main(site,allUserListPageNum)
    # 
    currentUserListPageNum = GetCurrentUserListPageNumService.main(site)
    # for begin -> end
    begin = currentUserListPageNum+1
    end   = allUserListPageNum
    ProcessUserIdService.main(site,begin,end)
    # current -> 0
    UpdateCurrentUserListPageNumService.main(site,0)

