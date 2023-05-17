"""
https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/unit/87546

CPU 바운드
* 프로그램이 실행될 떄 실행 속도가 CPU 속도에 의해 제한됨을 의미한다.
* 정말 복잡한 수학 수식을 계산하는 경우에 컴퓨터의 실행속도가 느려진다.
"""

def cpu_bound_func(number: int):
    total = 1
    arrange = range(1, number + 1)

    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k

    return total

if __name__ == "__main__":
    # 50 * 50 * 50 번의 순회를 돌게 됩니다.
    # 해당 과정에서 엄청난 양의 정수를 곱하게 됩니다.
    result = cpu_bound_func(50)
    print(result)