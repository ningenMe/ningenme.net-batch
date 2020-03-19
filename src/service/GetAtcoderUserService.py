import sys
import pathlib
path = pathlib.Path(__file__)
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../domain')
import Log
import AtcoderPageDomain

def main():
    AtcoderPage = AtcoderPageDomain.AtcoderPageDomain()
    rankingPageNum = AtcoderPage.getRankingPageNum()
    if(rankingPageNum == -1):
        Log.error(str(path.parent) + "failed get ranking page num\n")
        sys.exit(0)
    Log.info(rankingPageNum)
    return 1