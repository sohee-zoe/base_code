from datetime import datetime

start_time = datetime.now()
#
# 실행시간 측정을 원하는 코드 입력
#
end_time = datetime.now()

elapsed_time = (end_time - start_time).total_seconds()
# datetime.timedelta은 int 연산 불가능하므로 초단위로 변환


# import time
# start_time = time.time()

# end_time = time.time()
# sec = end_time - start_time

# print(f"elapsed_time: {timedelta(seconds=sec)}")
# # 0:00:00 형태
