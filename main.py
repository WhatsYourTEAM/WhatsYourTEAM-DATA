import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd
import operator

if __name__ == "__main__":
    reboundDict = {}
    stealDict = {}
    threePointDict = {}
    blockDict = {}
    assistDict = {}
    url = "https://sports.news.naver.com/basketball/record/index?category=kbl&year=2022"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("table")
    table = parser_functions.make2d(data)
    df = pd.DataFrame(data=table[1:], columns=table[0])
    print(df)

    for i in range(10):
        reboundDict[df.get("팀")[i]] = float(df.get("리바운드")[i])
        stealDict[df.get("팀")[i]] = float(df.get("스틸")[i])
        threePointDict[df.get("팀")[i]] = float(df.get("3점슛")[i])
        blockDict[df.get("팀")[i]] = float(df.get("블록")[i])
        assistDict[df.get("팀")[i]] = float(df.get("AS")[i])

    print(reboundDict)
    print(stealDict)
    print(threePointDict)
    print(blockDict)
    print(assistDict)

    reboundDict = sorted(reboundDict.items(), key=operator.itemgetter(1), reverse=True)
    stealDict = sorted(stealDict.items(), key=operator.itemgetter(1), reverse=True)
    threePointDict = sorted(threePointDict.items(), key=operator.itemgetter(1), reverse=True)
    blockDict = sorted(blockDict.items(), key=operator.itemgetter(1), reverse=True)
    assistDict = sorted(assistDict.items(), key=operator.itemgetter(1), reverse=True)

    print()
    print("리바운드 상위 3팀 : " + reboundDict[0][0] + ", " + reboundDict[1][0] + ", " + reboundDict[2][0])
    print("스틸 상위 3팀 : " + stealDict[0][0] + ", " + stealDict[1][0] + ", " + stealDict[2][0])
    print("3점슛 상위 3팀 : " + threePointDict[0][0] + ", " + threePointDict[1][0] + ", " + threePointDict[2][0])
    print("블록 상위 3팀 : " + blockDict[0][0] + ", " + blockDict[1][0] + ", " + blockDict[2][0])
    print("어시스트 상위 3팀 : " + assistDict[0][0] + ", " + assistDict[1][0] + ", " + assistDict[2][0])
