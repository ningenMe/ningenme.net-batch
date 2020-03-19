import sys
import os
sys.path.append(os.path.dirname(__file__)+'/../lib')
sys.path.append(os.path.dirname(__file__)+'/../domain')
import Log
import AtcoderPageDomain

def main():
    AtcoderPage = AtcoderPageDomain.AtcoderPageDomain()
    rankingPageNum = AtcoderPage.getRankingPageNum()
    if(rankingPageNum == -1):
        Log.error(os.path.basename(__file__) + "failed get ranking page num\n")
        sys.exit(0)
    Log.info(rankingPageNum)
    return 1