#
# csv format dumy log를 생성한다.
#
# 210828    j   처음 만듦
# 향후 :
# - 디렉토리별로 만들고. 파일명도 시간등으로 명명한다.
# - 생성주기를 결정한다. (하루에 한번 떨어지는 거, 5분 단위로 떨어지는 거)
# - csv column의 내용을 다양하게 한다. 날짜, 숫자 random, 범주 random 등으로.
# - 파일이 생성되어 있으면 header는 있다고 보자

import csv
import sys
from datetime import date, datetime
import time

start_time = time.time()

filename = './eggs.csv'
header = ['name', 'area', 'country_code2', 'country_code3']
data = ['afghanistan', 652090, 'af', 'afg']
data2 = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

header_02 = []
data_02 = []
csv_column_count = 100
csv_row_count = 3000

# # 준비물 - random 관련
# print(date.today())
# print(datetime.now())
# print(time.time())

# header, data를 리스트로 작업할지, 아니면 text로 작업할지 결정하자.


def make_csv_headers(column_cnt):
    for i in range(0, column_cnt):
        tmpData = 'column' + str(i)
        header_02.append(tmpData)

    return header_02


def make_csv_datas(column_cnt, row_cnt):
    for i in range(0, row_cnt):
        tmpList = []
        for j in range(0, column_cnt):
            tmpData = str(i) + str(j)
            tmpList.append(tmpData)
        data_02.append(tmpList)

    return data_02


with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(make_csv_headers(csv_column_count))
    writer.writerows(make_csv_datas(csv_column_count, csv_row_count))
    print('작업 완료')

# # csv file read
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

end_time = time.time()
print('프로그램 수행 시간 (mSec): {}'.format((end_time-start_time)*1000))
