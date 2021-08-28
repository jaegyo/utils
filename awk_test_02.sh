#!/bin/bash

#
# csv format log에서 awk를 가지고 간단하게 평균값을 만든다
# csf file encoding 확인후 utf-8에서 작업한다. (현장 log file encoding은 utf16-le)
#
# 210828    j   처음 만듦
# 향후 :
# - 디렉토리내 파일 encoding 확인
# - awk 컬럼을 사전정의, arg 등으로 처리한다       

#참고 - https://recipes4dev.tistory.com/171

clear

start_time=$(date +%s%N)

fname='./dkt_dream_2nd/log_data_printer_line1_20210618.txt'
work_file=$fname

# ## path 명 추출
# echo ${fname%/*}
# ## file 명 추출
# echo ${fname##*/}

if [ -e $fname ] && [ -f $fname ] && [ -s $fname ];then
    # file type, encoding 확인
    file_charset=$(file -bi $fname)
    case ${file_charset##*=} in 
        binary)
            # awk 처리안됨
            echo ${file_charset##*=}
            # utf-8 임시 파일을 만들고
            iconv -f "utf-16 le" -t "utf-8" ${fname} > ${fname}_utf8

            work_file=${fname}_utf8
            ;;
        us-ascii)
            # awk 처리가능
            echo ${file_charset##*=}
            ;;
        *)
            echo '파일 형식을 처리 할 수 없습니다.'
            exit -1
    esac

    # awk 처리 : 헤더 제거후 평균값 계산
    awk --lint -F ',' 'BEGIN {sum=0; n=0} NR!=1 {sum+=$58; ++n} END {printf "sum : %.3f  number : %5d  avg(sum/number) : %.3f\n", sum, n, sum/n}' $work_file
    # 임시 파일 삭제
else
    echo '파일이 존재하지 않습니다'
fi

end_time=$(date +%s%N)
echo '수행시간(milliSec) : ' $((($end_time - $start_time)/(1000*1000)))

exit 0
