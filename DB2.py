# DB1.py

import sqlite3

#연결 인스턴스
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\sample.db")

#커서 인스턴스
cur = con.cursor()

#테이블 구조 생성
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);") #파일이 없을경우에만 만들도록 명령어 수정함.

#1건 테이블 입력
cur.execute("insert into PhoneBook values ('홍길동', '010-222');")

# 입력 파라메터 처리
name = "박문수"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))

#여러건 입력
datalist = (("tom", "010-111"), ("dsp", "010-333"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

print(cur.fetchone())
print(cur.fetchmany(2))
print(cur.fetchall())


#쓰기 작업을 종료(sqlite에서는 입력후 반드시 수행 필요)
con.commit()