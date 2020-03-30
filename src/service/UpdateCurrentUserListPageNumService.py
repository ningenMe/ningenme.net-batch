import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import BatchDomain

def main(site, userListPageNum):
    batchDomain = BatchDomain.BatchDomain()
    batchDomain.updateCurrentUserListPageNum(site,userListPageNum)    
    return