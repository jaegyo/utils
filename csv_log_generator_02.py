#
# csv format dumy log를 생성한다.
#
# 210828    j   처음 만듦
# 향후 :
# v 디렉토리별로 만들고. 파일명도 시간등으로 명명한다.
# v 생성주기를 결정한다. (하루에 한번 떨어지는 거, 5분 단위로 떨어지는 거)
#    - 한번에 떨구는건 row 설정후 한번만 실행한다
#    - 시간 단위로 떨구는건. cron을 이용한다
# v csv column의 내용을 다양하게 한다. 날짜, 숫자 random, 범주 random 등으로.
# v 파일이 생성되어 있으면 header는 있다고 보자

import csv
import sys
from datetime import date, datetime
import time
import random
import os

print('---- process start ----')
start_time = time.time()

log_directory = './logs'
file_has_header = True

if not os.path.exists(log_directory):
    os.mkdir(log_directory)

filename = log_directory + '/' + str(date.today()) + '.txt'
if not os.path.exists(filename):
    file_has_header = False

# error 범주 선언
error_categorys = ['범주1', '범주2', '범주3',
                   '범주4', '범주5', '범주6', '범주7', '범주8', '범주9']

# csv column, row 정의
csv_column_count = 10
csv_row_count = 20

# # 준비물 - random 관련
# print(date.today())
# print(datetime.now())

# header, data를 리스트로 작업할지, 아니면 text로 작업할지 결정하자.


def make_csv_header(column_cnt):
    header = []
    for i in range(0, column_cnt):
        tmpData = 'column' + str(i)
        header.append(tmpData)

    # file_has_header = True

    return header


def make_csv_datas(column_cnt, row_cnt):
    csv_data = []
    for i in range(0, row_cnt):
        tmpList = []
        for j in range(0, column_cnt):
            if j == 0:
                tmpData = str(date.today())
            elif j == 1:  # 범주 할당
                tmpData = random.choice(error_categorys)
            elif j == 2:
                tmpData = float('%.3f' % (random.random()))
            elif j == 3:
                tmpData = float('%.3f' % (random.uniform(10, 20)))
            elif j == 4:
                tmpData = random.randint(5, 10)
            else:
                tmpData = str(i) + str(j)

            tmpList.append(tmpData)
        csv_data.append(tmpList)

    return csv_data


with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_has_header:
        writer.writerow(make_csv_header(csv_column_count))
    writer.writerows(make_csv_datas(csv_column_count, csv_row_count))

# # csv file read
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

end_time = time.time()
print('---- process end ----')
print('프로그램 수행 시간 (mSec): {}'.format((end_time-start_time)*1000))
