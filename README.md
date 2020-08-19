# random-tos.tweet
Generate random strings to increase the number of tweets in @tos format

ランダムに指定した文字数の英数混合文字列を生成して@tosを入れてメンション形式でツイートします。
Mobile版TwitterはHTML版が存在しているのでSeleniumを使用せずにスクレイピングすることができます。

Generates a mixed alphanumeric string of a specified number of characters randomly and tweets it in a mentioning format with @tos.
Twitter for Mobile has an HTML version, so you can scrape it without using Selenium.

# Used Library
random,bs4,mechanize,requests,http.cookiejar,time
