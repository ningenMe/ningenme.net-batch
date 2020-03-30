import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import AtcoderPageDomain

def main(site):
    userListPageNum = -1
    if site == "atcoder":
        atcoderPage = AtcoderPageDomain.AtcoderPageDomain()
        userListPageNum = atcoderPage.getRankingPageNum()

    if userListPageNum == -1:
        Log.error(str(path.parent) + " failed get ranking page num\n")
        sys.exit(0)
    return userListPageNum