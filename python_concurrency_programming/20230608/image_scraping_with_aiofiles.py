"""
웹 크롤링: 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑: 웹에서 데이터를 수집하는 프로그램
"""
import asyncio
import os

import aiofiles
import aiohttp
from dotenv import load_dotenv


async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]
    
    os.makedirs("./images", exist_ok=True)
    
    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)

async def fetcher(session, url, iteration):
    headers = {
        "X-Naver-Client-Id": os.getenv("NAVER_CLIENT_ID"),
        "X-Naver-Client-Secret": os.getenv("NAVER_CLIENT_SECRET")
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [items["link"] for items in items]
        
        await asyncio.gather(*[img_downloader(session, img) for img in images])
        
async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetcher(session, url, itr) for itr, url in enumerate(urls)])
        
        
if __name__ == "__main__":
    load_dotenv(verbose=True)
    asyncio.run(main())