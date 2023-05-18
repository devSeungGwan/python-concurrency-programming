"""
https://www.inflearn.com/course/lecture?courseSlug=%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%99%EC%8B%9C%EC%84%B1-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D&unitId=87549
https://docs.aiohttp.org/en/stable/
pip install aiohttp~=3.7.3
"""

import aiohttp
import asyncio
import time

async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)
        
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    
    print(f"실행 시간: {end - start:.3f}초")