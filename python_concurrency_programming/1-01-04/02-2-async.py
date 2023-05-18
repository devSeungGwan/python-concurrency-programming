"""
https://www.inflearn.com/course/lecture?courseSlug=%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D&unitId=87547

요청, 처리를 받는 상황에서는 async 가 유리
비동기로 넘어갔을 때 코드가 복잡해지고 유지보수가 어려워질 수 있다.

"""

import time
import asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요")
    print(f"{name} 그릇 수거 완료")
    
async def main():
    # await asyncio.gather(
    #     delivery("A", 5),
    #     delivery("B", 3),
    #     delivery("C", 4),   
    # )
    
    await delivery("A", 5)
    await delivery("B", 3)
    await delivery("C", 4)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    
    print(f"총 소요시간: {end - start}")
    