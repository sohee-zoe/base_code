import os
 
def mkdir(directory):
    try:
        if not os.path.exists(directory): # 디렉토리 존재 여부확인
            os.makedirs(directory)        # 모든 하위 폴더까지 생성
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
# createFolder('/Users/aaron/Desktop/test')

from pathlib import Path
dir_path = Path("")
# file_path = Path("")
# dir_path.exists()     # 존재 여부 확인
dir_path.mkdir(exist_ok=True, parents=True) # 없으면 생성
