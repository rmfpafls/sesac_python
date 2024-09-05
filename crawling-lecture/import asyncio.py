# pip install aiohttp
import asyncio
import aiohttp
import requests 
from bs4 import BeautifulSoup
from time import time, sleep

def crawl_press_names_and_codes(): 
    """Make the dict that have press code as key, and press name as value. Crawl from https://media.naver.com/channel/settings. 
    """
    begin = time()
    url = 'https://media.naver.com/channel/settings'
    code2name = {}
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for li in soup.find_all('li', {'class': 'ca_item _channel_item'}):
            press_name = li.find('div', {'class': 'ca_name'}).text
            press_code = li['data-office']
            code2name[press_code] = press_name 
            # print(press_code, press_name)
    end = time()
    print(end - begin)
    return code2name 


async def afetch_journalist_list(press_code, session):
    response = await session.get(url) # 크롬창에 url을 친 것. 결과가 나올 때까지 기다림
    # do something with response
    url = f'https://media.naver.com/journalists/whole?officeId ={press_code}'
    print(url)
    response = await session.get(url)

    if response.status == 200:
        # do something here
        print('good!')
        text = await response.text()
        soup = BeautifulSoup(response.text, 'html.parser')
        journalist_list = []

        for li in soup.find_all('li', {'class': 'journalist_list_content_item'}):
            info = li.find('div', {'class':'journalist_list_content_title'})
            a = info.find('a')
            journalist_name = a.text.strip(' 기자')# strip() : 특정 문자열을 제거하는 메서드
            journalist_link = a['href']
            journalist_list.append(journalist_name, journalist_link)
        
        await asyncio.sleep(0.1) # 한번에 사이트에 많은걸 요청하면  막기때문에 sleep을 줘야된다 
        return journalist_list

    await response.release()

async def acrawl_journalist_info_pages(code2name):
    session = aiohttp.ClientSession()

    tasks = [afetch_journalist_list(url, session) for press_code in code2name ]

    results = await asyncio.gather(*tasks)

    for res in results: 
        print(res)

    await session.close()

if __name__ == '__main__':
    code2name = crawl_press_names_and_codes()
    begin = time() 
    asyncio.run(acrawl_journalist_info_pages(code2name))
    end = time()
    print(end-begin)