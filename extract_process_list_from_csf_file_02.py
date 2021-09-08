#
# csf 파일에서 process list를 추출한다.
#
# 210906    j   처음 만듦
# 210908    j   zip 처리
# 향후 :
# - target file 이름에서 output file 이름을 생성한다.
# - 실행시간이 너무 오래 걸린다. 단축하자 4142mSec 정도, 시스템 부하에 따라 다르다

import sys
from bs4 import BeautifulSoup
import time

print('---- process start ----')
start_time = time.time()

target_file = './DKT_VINA_20210726a.csf'
output_file = './DKT_VINA_20210726a_process_list_01.txt'

with open(target_file, 'r') as f:
    bs_data = BeautifulSoup(f, 'lxml')

# 반환된 값이 소문자로 변환됨, find_all 사용시 소문자로 검색
processnumes = bs_data.find_all('processnum')
processnames = bs_data.find_all('processname')
processtypes = bs_data.find_all('processtype')  # idle - disalbe된 process

with open(output_file, 'w') as f:
    for num, name, type in zip(processnumes, processnames, processtypes):
        f.write(f'{num.string}\t {type.string}\t {name.string}\n')

end_time = time.time()
print('---- process end ----')
print('프로그램 수행 시간 (mSec): {}'.format((end_time-start_time)*1000))
