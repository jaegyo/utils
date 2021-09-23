# 베트남 oled log file 생성 프로그램. (1일 1로그)
# 210923 j 처음 만듦
# todo -
#  윈도우, 리눅스 디렉토리 구분자가 달라. header를 계속 찍음.
#  파일을 하나만 만듦. 날짜별로 만들어야 함 (옵션별로 시간단위로 찍을수도 있음)
#  기능을 펑션으로 구분하였으니. main 함수로 정리가 필요함

import csv
from datetime import date, datetime
import os
import time
import random
import sys

log_directory = './logs'
file_has_header = True
pcb_barcode = 0


# log파일은 날짜 기준으로 명명
today = date.today().strftime('%Y%m%d')

if not os.path.exists(log_directory):
    os.mkdir(log_directory)

filename = log_directory + '/' + today + '.txt'
if not os.path.exists(filename):
    file_has_header = False


def make_csv_header():
    header = [
        'PCB Barcode',
        'Time Stamp',
        'Job File',
        'Cycle Time',
        'Paste ID',
        'Stencil ID',
        'Squeegee ID',
        'Product Count',
        'Squeegee Count',
        'Mask Count',
        'Paste Count',
        'Board X Size',
        'Board Y Size',
        'Board Thickness',
        'Fiducial Mark 1 X',
        'Fiducial Mark 1 Y',
        'Fiducial Mark 2 X',
        'Fiducial Mark 2 Y',
        'Use Top Clamp',
        'Use Board Suction',
        'Mask Size',
        'Number Of Teaching Mark',
        'Read Stencil Mark',
        'WorkTable Printing Height Offset',
        'Separation Mode',
        'Work Separation Speed',
        'Work Separation Distance',
        'Work Separation Delay',
        'Squeegee Separation Speed',
        'Squeegee Sepration Distance',
        'Double Printing Option',
        'Printing Direction',
        'Start Offset',
        'Stop Offset',
        'Down Offset',
        'Squeegee Pressure',
        'Squeegee Speed',
        'N Print Count',
        'N Print Distance',
        'Auto Cleaning Count',
        'Manual Cleaning Count',
        'Check Solder Count',
        'Check Solder hr',
        'Check Stencil Count',
        'Check Stencil hr',
        'Cleaning Option Count',
        'Cleaning Start Offset',
        'Cleaning End Offset',
        'Cleansing Supply Time',
        'Paper Winding Distance',
        'Cleaning Speed',
        'Machine Wait Time Over',
        'Auto Cleaning',
        'Manual Cleaning',
        'Check Solder Paste',
        'Check Stencil',
        'Temp',
        'Squeegee Pressure AVG',
        'Suqeegee Pressure Min',
        'Suqeegee Pressure Max',
        'Mask Barcode',
        'Humidity',
        'Hera ID',
        'BackupBlock ID',
        'RearSqueegee ID',
        'RearSqueegee Count',
        'Paste Using Time',
        'BackupPin ID',
        'Cleanser Low Level',
        'Paste Part Num',
        '1D Barcode',
        'PCB Barcode 2',
        'PCB Barcode Reader Top',
        'PCB Barcode Reader Bottom',
        'Air Level'
    ]
    return header


def make_csv_data(pcb_barcode):
    csv_data = ['']*74

    csv_data[0] = pcb_barcode
    csv_data[1] = datetime.now().strftime('%Y%m%d%H%M%S')
    csv_data[2] = f'DKT\SDC\AM681XV01 MAIN_REV 3.3_R1.Job'
    csv_data[3] = format(random.uniform(20, 99), '.3f')
    csv_data[7] = pcb_barcode + 1500
    csv_data[8] = pcb_barcode + 1600
    csv_data[9] = pcb_barcode + 1700
    csv_data[10] = pcb_barcode + 1800
    csv_data[11] = 320
    csv_data[12] = 240
    csv_data[13] = 1
    csv_data[14] = 4.895
    csv_data[15] = 15.09
    csv_data[16] = 308.515
    csv_data[17] = 225.49
    csv_data[18] = 'NOT USE'
    csv_data[19] = 'NOT USE'
    csv_data[20] = '650 x 550 (mm)'
    csv_data[21] = 2
    csv_data[22] = 'Allways'
    csv_data[23] = 0
    csv_data[24] = 'Table first'
    csv_data[25] = 3
    csv_data[26] = 3
    csv_data[27] = 1
    csv_data[28] = 3
    csv_data[29] = 3
    csv_data[30] = 'NOT USE'
    csv_data[31] = 'Forward' if pcb_barcode % 2 else 'Backward'
    csv_data[32] = 54.5
    csv_data[33] = 5
    csv_data[34] = 1.5
    csv_data[35] = 11
    csv_data[36] = 120
    csv_data[37] = 0
    csv_data[38] = 0
    csv_data[39] = 6
    csv_data[40] = 30
    csv_data[41] = 0
    csv_data[42] = 0
    csv_data[43] = 0
    csv_data[44] = 0
    csv_data[45] = 2
    csv_data[46] = 35
    csv_data[47] = 15
    csv_data[48] = 0.1
    csv_data[49] = 35
    csv_data[50] = 50
    csv_data[51] = 40
    csv_data[52] = 0 if pcb_barcode % 6 else 1
    csv_data[53] = 0
    csv_data[54] = 0
    csv_data[55] = 0
    csv_data[56] = 23.3
    csv_data[57] = format(random.uniform(10, 12), '.3f')
    csv_data[58] = format(random.uniform(10, 12), '.3f')
    csv_data[59] = format(random.uniform(10, 12), '.3f')
    csv_data[60] = 0
    csv_data[61] = format(random.uniform(50, 58), '.1f')
    csv_data[62] = 0 if pcb_barcode % 6 else 1
    csv_data[65] = 0
    csv_data[66] = '00:00:00'
    csv_data[68] = 0

    return csv_data


while True:
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_has_header:
            writer.writerow(make_csv_header())
        writer.writerow(make_csv_data(pcb_barcode))
        pcb_barcode += 1  # pcb_barcode는 1씩 증가한다.

    rand_time = random.randint(25, 35)
    time.sleep(rand_time)
