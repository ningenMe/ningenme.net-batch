import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import AtcoderUserDomain

def main(site, userIdList):
    if site == "atcoder":
        atcoderUser = AtcoderUserDomain.AtcoderUserDomain()
        atcoderUser.updateUserId(userIdList)    
    return