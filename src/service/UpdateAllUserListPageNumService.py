import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import BatchDomain

def main(site, userListPageNum = -1):
    if userListPageNum == -1:
        Log.error(str(path.parent) + " failed\n")
        sys.exit(0)

    batchDomain = BatchDomain.BatchDomain()
    batchDomain.updateUserListPageNum(site,userListPageNum)    
    return