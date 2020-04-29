import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import BatchDomain

def main(site):
    batchDomain      = BatchDomain.BatchDomain()
    currentUserIdNum = batchDomain.getCurrentUserListPageNum(site)    
    allUserIdNum     = 
    if site == "atcoder":
        atcoderUser = AtcoderUserDomain.AtcoderUserDomain()
        atcoderUser.updateUserId(userIdList)    
 
    return currentUserIdNum,allUserIdNum