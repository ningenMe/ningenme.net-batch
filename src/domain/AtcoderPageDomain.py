from urllib import request
from bs4 import BeautifulSoup
import sys
import os
import re
sys.path.append(os.path.dirname(__file__)+'/../lib')
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
