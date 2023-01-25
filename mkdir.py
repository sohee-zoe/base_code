import os
 
def mkdir(directory):
    try:
        if not os.path.exists(directory): # 디렉토리 존재 여부확인
            os.makedirs(directory)        # 모든 하위 폴더까지 생성
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
# createFolder('/Users/aaron/Desktop/test')
