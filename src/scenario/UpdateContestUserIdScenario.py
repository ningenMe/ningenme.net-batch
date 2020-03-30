import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../service')
import GetAllUserListPageNumService
import UpdateAllUserListPageNumService

def main(site):
    # get user list page num
    allUserListPageNum = GetAllUserListPageNumService.main(site)
    # update user list page num
    UpdateAllUserListPageNumService.main(site,allUserListPageNum)

