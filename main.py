import gspread
from google.oauth2.service_account import Credentials
import random
import numpy

URL = input("スプレッドシートのURL: ")
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = Credentials.from_service_account_file(
    'python/gss/gss_credential.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
sheet = gc.open_by_url(URL)
ansSheet = sheet.worksheet("フォームの回答 1")
rawValue = ansSheet.get_all_values()#リストとして回答データを取得。
value = rawValue[1:]#質問のタイトル部分を消去
rowCount = len(value)#回答の数
colCount = len(rawValue[0])#質問の数

contentIndex = numpy.argmax(value[0])#もっとも回答が長いところを本文として取得

i = 0
randNum = []#作品ごとに乱数を与えるための空リスト
while i < rowCount:
    randNum.append(random.random())
    i += 1
shuffled = [x for _,x in sorted(zip(randNum,value))]#ランダムな順番に並べ替え。shuffledの値はそれぞれ[0:乱数,1:著者名…contentIndex:本文]となる

output = '[[tabview]]\n'
authorAns = []
#それぞれ出力用の枠を初期化。
j = 0
while j < rowCount:
    output += '[[tab No.' + str(j + 1) + ']]\n' + shuffled[j][contentIndex] + '\n[[/tab]]\n'
    authorAns.append('\nNo.' + str(j + 1) + ': ' + str(shuffled[j][1]))
    j += 1
output += '[[/tabview]]\n'
file = open('python/gss/文体集計出力.txt', 'a', encoding='UTF-8')
toWrite = ['本文ココから↓\n', output, '==========\n本文ココまで\n著者回答ココから↓']
file.writelines(toWrite)
file.writelines(authorAns)
file.close
print('出力完了！')
