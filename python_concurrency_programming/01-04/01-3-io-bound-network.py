"""
https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/unit/87546
"""


import requests

def io_bound_func():
    result = requests.get("https://google.com")
    return result

if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()
        print(result)
