import requests
import random

ran=random.randint(1,11)

if ran==1 :
    code='016010'
    toshi="札幌"

if ran==2 :
    code='040010'
    toshi="仙台"

if ran==3 :
    code='150010'
    toshi="新潟"

if ran==4 :
    code='130010'
    toshi="東京"

if ran==5 :
    code='230010'
    toshi="名古屋"

if ran==6 :
    code='260010'
    toshi="京都"

if ran==7 :
    code='270000'
    toshi="大阪"

if ran==8 :
    code='340010'
    toshi="広島"

if ran==9 :
    code='370000'
    toshi="高松"

if ran==10 :
    code='400010'
    toshi="福岡"

if ran==11 :
    code='471010'
    toshi="那覇"


url='https://weather.tsukumijima.net/api/forecast/city/'+code
r=requests.get(url)

maxtem=r.json()["forecasts"][1]["temperature"]["max"]["celsius"]

yosou=input(toshi+"の翌日の最高気温予報値（セルシウス温度・整数値）を予想してください。")
if yosou==maxtem :
    print("正解！"+toshi+"の翌日の最高気温予報値は"+str(maxtem)+"度です！")
else :
    print("不正解…"+toshi+"の翌日の最高気温予測値は"+str(maxtem)+"度です！")