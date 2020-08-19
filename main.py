#モジュールインポート
#from concurrent.futures import ThreadPoolExecutor
import random, string
from bs4 import BeautifulSoup
from mechanize import Browser
import requests
import http.cookiejar
import time

#ランダムな配列生成
def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return "".join(randlst)

#アカウントのログパス
LoginID = "Your IDorMainAdress"
LoginPASS = "Your Password"

#動作スレッド数
#max_thread = 3

#Browserオブジェクトを生成
br = Browser()

#CookieJar(Cookie保持)
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

#非ロボット化
br.set_handle_robots(False)

#ユーザーエージェント設定
br.addheaders = [("User-agent", "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19)")]

#プロキシ設定
#br.set_proxies(proxies=proxies)

#アカウントログイン
br.open("https://mobile.twitter.com/session/new", timeout=10.0)
br.select_form(action="/sessions")
br["session[username_or_email]"] = LoginID
br["session[password]"] = LoginPASS
ret = br.submit()
print("Login Success")

#ツイート関数
def tweet():

    #永久ループ
    while True:

        #ツイート
        try:
            br.open("https://mobile.twitter.com/compose/tweet", timeout=10.0)
            req = br.click_link(text="use this link")
            br.open(req)
            br.select_form(action="/compose/tweet")
            br["tweet[text]"] = "@tos " + randomname(10)
            br.submit()
            print("Tweeted" + "@tos " + randomname(10))

        except Exception as e:
            print(e)
            time.sleep(900)

        except KeyboardInterrupt:
            print("Stop")
            input()
            exit()

tweet()

#スレッド設定&作動
#th = ThreadPoolExecutor(max_workers=max_thread)
#th.submit(tweet)
#th.shutdown()
