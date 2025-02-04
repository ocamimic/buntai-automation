import gspread
from google.oauth2.service_account import Credentials
import random
import numpy

URL = 'https://docs.google.com/spreadsheets/d/19ZNXHML4k84KlfhCj8QfcTH3CjSicviZfvNeKV3E6kc/edit?usp=sharing'
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
template = ['[[tab No.', ']]\n', '\n[[/tab]]\n']
output = '[[tabview]]\n'
j = 0
while j < rowCount:
    output += template[0] + str(j + 1) + template[1] + value[j][contentIndex] + template[2]
    j += 1
output += '[[/tabview]]'
processedSheet = sheet.add_worksheet(title="カンペ", rows=rowCount, cols=colCount)
processedSheet.acell("A1").value = output
