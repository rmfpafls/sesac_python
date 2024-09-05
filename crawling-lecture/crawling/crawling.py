from playwright.async_api import async_playwright 
from time import time, sleep
import asyncio

# 네이버 검색창에 입력한 뒤 스크롤 내리기
async def naver_search(page, search_keyword = '새싹'):
    search = await page.wait_for_selector('#query')
    await search.type(search_keyword)
    await page.evaluate('() => {window.scrollTo(0,1000);};')

    execute_search = await page.wait_for_selector('.btn_search')
    await execute_search.click()
    await page.wait_for_selector('.sc_page_inner') # 확실하게 된다음에 다음 코드가 실행되어야 하므로 await를 씀
    await page.evaluate('() => {window.scrollTo(0,1000);};')
    
    sleep(10)

#크롬 켜기 
async def main():
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.naver.com')
        await naver_search(page, search_keyword = '새싹')

if __name__ == '__main__': 
    asyncio.run(main())
