# Email Check Code

import re

# 이메일 주소 체크 함수
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(pattern, email) is not None

# 10개의 샘플 데이터 생성
sample_emails = [
    'user@example.com',
    'john.doe@gmail.com',
    'info@company.co.kr',
    '12345@test',
    'invalid.email',
    'test@email@domain.com',
    'user@-example.com',
    'user@.example.com',
    'user@localhost',
    '@example.com'
]

# 이메일 주소 체크 및 결과 출력
for email in sample_emails:
    if is_valid_email(email):
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")
