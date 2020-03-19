from urllib import request
from bs4 import BeautifulSoup
import sys
import re
import pathlib

path = pathlib.Path(__file__)
sys.path.append(str(path.parent)+'/../lib')
import Log

class AtcoderPageDomain:
    rankingUrl = "https://atcoder.jp/ranking"

    def getRankingPageNum(self):
        rankingPageNum = -1
        try:
            html = request.urlopen(AtcoderPageDomain.rankingUrl)
            tags = BeautifulSoup(html, "html.parser").find_all("a", href=re.compile("page"))
            for tag in tags:
                rankingPageNum = max(rankingPageNum,int(tag.text))
        except Exception as e:
            Log.error(e)
            return -1
        return rankingPageNum        
