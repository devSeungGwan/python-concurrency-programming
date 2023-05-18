"""
https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/unit/87546

IO Bound
* I: input / O: output
* 프로그램이 실행될 때 실행속도가 I/O에 의해 제한됨을 의미한다.
* 사용자, 네트워크 등에 의해 발생
"""

def io_bound_func():
    input_value = input("값을 입력해주세요.")
    return int(input_value) + 100

if __name__ == "__main__":
    # 사용자가 입력을 해야하는 상황 
    # 입력을 하지 않으면 IO Bound가 발생한다.
    result = io_bound_func()
    print(result)
