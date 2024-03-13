import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    # 검색 URL 설정
    search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

    # HTTP 요청 보내고 응답 받기
    response = requests.get(search_url)

    # 응답의 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 블로그 검색 결과 가져오기
    blog_results = soup.find_all('li', {'class':'bx'})

    # 크롤링한 데이터 저장할 리스트 초기화
    blog_data = []

    # 블로그 결과 순회
    for result in blog_results:
        blog_info = {}

        # 블로그명, 블로그 주소 추출
        blog_info['blog_name'] = result.find('a', class_='sub_txt').text
        blog_info['blog_link'] = result.find('a', class_='sub_txt')['href']

        # 제목, 포스팅 날짜 추출
        post_title = result.find('a', class_='api_txt_lines')
        blog_info['title'] = post_title.text
        blog_info['post_date'] = post_title.find_next_sibling('span', class_='sub_time').text

        # 추출한 데이터를 리스트에 추가
        blog_data.append(blog_info)

    return blog_data

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    search_results = crawl_naver_blog(search_keyword)

    print("\n검색 결과:")
    for idx, result in enumerate(search_results, start=1):
        print(f"\n#{idx}")
        print("블로그명:", result['blog_name'])
        print("블로그 주소:", result['blog_link'])
        print("제목:", result['title'])
        print("포스팅 날짜:", result['post_date'])
