# DemoFile.py

# 쓰기
f = open("Demo.txt","wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 읽기
f = open("Demo.txt","rt", encoding="utf-8")
result = f.read()
print(result)

# 다시 처음으로 리셋
f.seek(0)
print(f.readline(), end="\n") #print기본 설정
print(f.readline(), end="")   #print후 줄변경을 제외

f.close()