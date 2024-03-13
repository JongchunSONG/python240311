<<<<<<< HEAD
# 파이썬을 사용해서 윈도우의 다운로드된 폴더에서 *.jpg, *.jpeg를 
# \images폴더로 이동, *.csv, *.xlsx파일은 \data폴더로, 
# *.txt, *.doc, *.pdf는 \docs폴더로
# *.zip은 \archive폴더로 이동하는 코드를 생성해줘. 
# 해당 폴더가 없으면 생성해야 하고
# 다운로드 폴더는 C:\Users\student\Downloads를 사용함. 

import os
import shutil

# 다운로드된 폴더 경로
download_folder = 'C:\\Users\\MTR-M\\Downloads'

# 대상 폴더들
image_folder = 'C:\\Users\\MTR-M\\Downloads\\images'
data_folder = 'C:\\Users\\MTR-M\\Downloads\\data'
docs_folder = 'C:\\Users\\MTR-M\\Downloads\\docs'
archive_folder = 'C:\\Users\\MTR-M\\Downloads\\archive'

# 폴더 생성 함수
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 정리 함수
def organize_files():
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        if filename.lower().endswith(('.jpg', '.jpeg')):
            create_folder(image_folder)
            shutil.move(file_path, os.path.join(image_folder, filename))
        elif filename.lower().endswith(('.csv', 'xls' '.xlsx')):
            create_folder(data_folder)
            shutil.move(file_path, os.path.join(data_folder, filename))
        elif filename.lower().endswith(('.hwp', '.hwpx','.txt', '.docx','.doc', '.pdf')):
            create_folder(docs_folder)
            shutil.move(file_path, os.path.join(docs_folder, filename))
        elif filename.lower().endswith('.zip'):
            create_folder(archive_folder)
            shutil.move(file_path, os.path.join(archive_folder, filename))

# 파일 정리 실행
organize_files()
=======
# 파이썬을 사용해서 윈도우의 다운로드된 폴더에서 *.jpg, *.jpeg를 
# \images폴더로 이동, *.csv, *.xlsx파일은 \data폴더로, 
# *.txt, *.doc, *.pdf는 \docs폴더로
# *.zip은 \archive폴더로 이동하는 코드를 생성해줘. 
# 해당 폴더가 없으면 생성해야 하고
# 다운로드 폴더는 C:\Users\student\Downloads를 사용함. 

import os
import shutil

# 다운로드된 폴더 경로
download_folder = 'C:\\Users\\MTR-M\\Downloads'

# 대상 폴더들
image_folder = 'C:\\Users\\MTR-M\\Downloads\\images'
data_folder = 'C:\\Users\\MTR-M\\Downloads\\data'
docs_folder = 'C:\\Users\\MTR-M\\Downloads\\docs'
archive_folder = 'C:\\Users\\MTR-M\\Downloads\\archive'

# 폴더 생성 함수
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 정리 함수
def organize_files():
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        if filename.lower().endswith(('.jpg', '.jpeg')):
            create_folder(image_folder)
            shutil.move(file_path, os.path.join(image_folder, filename))
        elif filename.lower().endswith(('.csv', 'xls' '.xlsx')):
            create_folder(data_folder)
            shutil.move(file_path, os.path.join(data_folder, filename))
        elif filename.lower().endswith(('.hwp', '.hwpx','.txt', '.docx','.doc', '.pdf')):
            create_folder(docs_folder)
            shutil.move(file_path, os.path.join(docs_folder, filename))
        elif filename.lower().endswith('.zip'):
            create_folder(archive_folder)
            shutil.move(file_path, os.path.join(archive_folder, filename))

# 파일 정리 실행
organize_files()
>>>>>>> a043eced272f3a326eb0e4b73652828117d7482c
