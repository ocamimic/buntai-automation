import gspread
from google.oauth2.service_account import Credentials
import random
import numpy
#スプレッドシートのリンク
URL = ''
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
#ローカルで書いてるときの名残
credentials = Credentials.from_service_account_file(
    'python/gss/gss_credential.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
sheet = gc.open_by_url(URL)
ansSheet = sheet.worksheet("フォームの回答 1")
value = ansSheet.get_all_values()[1:]#リストとして回答データを取得
rowCount = len(value)#回答の数
colCount = len(value[0])#質問の数

contentIndex = numpy.argmax(value[0])
print(contentIndex)
i = 0
randNum = []
while i < rowCount:
    randNum.append(random.random())
    i += 1
shuffled = [x for _,x in sorted(zip(randNum,value))]
template = ['[[tab No.', ']]\n', '\n[[/tab]]\n', '----', '[[include]]']
output = '[[tabview]]\n'
authorAns = []
j = 0
while j < rowCount:
    output += template[0] + str(j + 1) + template[1] + value[j][contentIndex] + template[2]
    authorAns.append(value[1])
    j += 1
output += '[[/tabview]]\n'
file = open('文体集計出力.txt', 'a')
#未完成。テキストファイルで出力する。
#参加者リスト、本文を格納したタブ、番号と著者の対応表
file.write(output)
file.write(template[3])
