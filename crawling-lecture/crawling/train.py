from playwright.async_api import async_playwright 
from time import time, sleep
import asyncio

# # 네이버 검색창에 입력한 뒤 스크롤 내리기
# async def naver_search(page, search_keyword = '새싹'):
#     search = await page.wait_for_selector('#query')
#     await search.type(search_keyword)
#     await page.evaluate('() => {window.scrollTo(0,1000);};')

#     execute_search = await page.wait_for_selector('.btn_search')
#     await execute_search.click()
#     await page.wait_for_selector('.sc_page_inner') # 확실하게 된다음에 다음 코드가 실행되어야 하므로 await를 씀
#     await page.evaluate('() => {window.scrollTo(0,1000);};')
    
#     sleep(10)


#로그인하기 
async def login(page, id = "1763571646", pw = "3596guswl!!"):
    id_search = await page.wait_for_selector('#txtMember')
    await  id_search.type('1763571646') # type() : html에서 텍스트를 입력하기위한 메서드
    # pw_search = await page.wait_for_selector('input[type = "password"]')
    # await pw_search.type(pw)


#크롬 켜기 -> 코레인 로그인
async def main():
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.letskorail.com/ebizprd/prdMain.do')
        login_search = await page.wait_for_selector('a[onclick = "return m_login_link()"]')
        await login_search.click()
        # await page.wait_for_selector('.sc_page_inner')
        await login(page, id = "1763571646", pw = "3596guswl!!")
        sleep(10)

if __name__ == '__main__': 
    asyncio.run(main())
