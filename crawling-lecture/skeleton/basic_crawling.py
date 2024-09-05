import requests 
from bs4 import BeautifulSoup

def crawl_breaking_news_list(): #제목이랑 링크를 가지고와서 프린트
    news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014907888'

    response = requests.get(news_url) # response를 받아오는 애 

    if response.status_code == 200: # 이건 크롤링할 때 그냥 공식임
        soup = BeautifulSoup(response.text, 'html.parser') 
        # response.text 사이트에서 컨트롤 u를 하면 나오는 코드 전체 

        td = soup.find('td', {'class' : 'content'})

        for li in td.find_all('li'): 
            try:
                if li['data-comment'] is not None:
                    a = li.find('a')
                    link = a['href']
                    text = a.text
                    print(link, text)
            except KeyError: 
                pass
                

def crawl_ranking_news(): #인기순 #모든 언론사의 링크랑 제목을 가지고 와라 
    ranking_url = 'https://news.naver.com/main/ranking/popularDay.naver'

    response = requests.get(ranking_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
    # 강사님 풀이 
        for div in soup.find_all('div', {'class': "rankingnews_box"}):
            press_name = div.find('strong')

            for li in div.find_all('li'):
                content = li.find('div', {'class': 'list_content'})
                if content is not None:
                    a = content.find('a')
                    print(a['href'], a.text)


"""
    #내가 짠 코드 
        td = soup.find('div',{'class' : 'rankingnews _popularWelBase _persist'})
        #print(td)

        for div_lst in td.find_all('div', {"class": "rankingnews_box"}):
            for a_lst in div_lst.find_all('a'):
                news = a_lst.find('strong', {'class': "rankingnews_name"})
                if news is not None:
                    print(news.text)
                    
            for li_lst in div_lst.find_all('li'):
                    a = li_lst.find('a')
                    if a is not None:
                        link = a['href']
                        text = a.text
                        print(link, text)
            print("\n")
"""


if __name__ == '__main__':
    # crawl_breaking_news_list()
    crawl_ranking_news()