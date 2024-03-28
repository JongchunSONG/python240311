from bs4 import BeautifulSoup

html = '''
<html>
    <head>
    </head>
    <body>
        <h1>스마트스토어</h1>
            <div class='sale'>
                <p id='notebook1' class='devices'>
                    <span class='name'> 맥북에어m1 </span>
                    <span class='price'> 980000원 </span>
                    <span class='inventory'> 5개 </span>
                    <span class='store'> 스마트컴퓨터 </span>
                    <a href='http://www.naver.com'> 홈페이지 </a>
                </p>
            </div>
            <div class='after'>
                <p id='notebook2' class='devices'>
                    <span class='name'> 맥북프로 </span>
                </p>
            </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# id로 태그 찾기
ids_notebook1 = soup.select('#notebook1')
print(ids_notebook1)

# class로 태그 찾기
class_price = soup.select('.price')
print(class_price)

# span 태그이면서 class가 price인 태그 찾기
tags_span_class_price = soup.select('span.price')
print(tags_span_class_price)

# 상위 구조 활용
print("---상위 구조 사용---")
# 맥북에어만 선택하기 위해 상위 태그 정보 포함
tags_notebook1_name = soup.select('#notebook1 > span.name')
print(tags_notebook1_name) 

# 태그 위치로 찾기: 직접 자식과 모든 자손 비교
tags_notebook_direct_child = soup.select('div.sale > #notebook1 > span.name')
tags_notebook_all_descendants = soup.select('div.sale span.name')
print(tags_notebook_direct_child)
print(tags_notebook_all_descendants)

# 태그 그룹에서 첫 번째 태그만 선택
first_name_tag = soup.select('span.name')[0]
print(first_name_tag)

# span.name 태그를 순회하여 모두 출력
for name_tag in soup.select('span.name'):
    print(name_tag)

# 선택한 태그에서 텍스트와 속성값 가져오기
a_tag = soup.select('a')[0]
print(a_tag.text)  # 텍스트 내용 출력
print(a_tag['href'])  # href 속성값 출력
