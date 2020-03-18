#coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup
import sys
sys.path.append('../lib')
import log

def kick():
    print(sys.path)

    #url
    url = "http://www.yomiuri.co.jp/"

    #get html
    html = request.urlopen(url)

    #set BueatifulSoup
    # soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    # #get headlines
    # mainNewsIndex = soup.find("ul", attrs={"class", "list-main-news"})
    # headlines = mainNewsIndex.find_all("span", attrs={"class", "headline"})

    # #print headlines
    # for headline in headlines:
    #     print(headline.contents[0], headline.span.string)

if __name__ == "__main__":
    kick()