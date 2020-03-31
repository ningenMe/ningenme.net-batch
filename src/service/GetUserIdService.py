import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import AtcoderPageDomain

def main(site,index):
    userIdList = []
    if site == "atcoder":
        atcoderPage = AtcoderPageDomain.AtcoderPageDomain()
        userIdList = atcoderPage.getUserIdList(index)

    if not userIdList:
        Log.error(str(path.parent) + " failed")
        sys.exit(0)
    return userIdList