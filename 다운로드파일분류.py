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
