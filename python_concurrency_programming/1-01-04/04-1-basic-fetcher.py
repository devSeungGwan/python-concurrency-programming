"""
https://2.python-requests.org/en/master/user/advanced/#id1
pip install requests
https://www.inflearn.com/course/lecture?courseSlug=%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D&unitId=87549
"""

import requests
import time

def fetcher(session, url):
    with session.get(url) as response:
        return response.text
    
    
def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
    
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    
    print(f"실행 시간: {end - start:.3f}초")