import requests 
from bs4 import BeautifulSoup
import pickle
import os 
from time import time 

def crawl_press_names_and_codes():
    """Make the dict that have press code as key, and press name as value. Crawl from https://media.naver.com/channel/settings. 
        언론 코드를 키로 언론이름을 값으로 만들어라 
    """
    url = 'https://media.naver.com/channel/settings'
    response = requests.get(url)
    code2name = {}


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for li in soup.find_all("li", {"class": "ca_item _channel_item"}):
            press_name = li.find('div', {'class': 'ca_name'}).text
            press_code = li['data-office']
            code2name[press_code] = press_name

            print(press_code, press_name)
    return code2name 
"""       
# 시도
        tp = soup.find('div',{'class' : 'channel_add'})
        code2name = {}

        for lst in tp.find_all('div', {'role': "tabpanel"}):
            #print(lst['class'])
            for ctg in lst.find_all('li'):
                print(ctg, "\n")

                # news_name = lst.find('div', {'class': "ca_name"})
                # data_number = ctg.li['data-office']
                # code2name[data_number] = news_name.text
        print(code2name)
 """               
    


def crawl_journalist_info_pages(code2name):
    """Accepts press code - press name dict, and return dict having press code as key, and 2-tuple of (press name, listof 2-tuple containing journalist name and their link) as value. 

    For now, you DO NOT have to crawl all journalists; for now, it's impossible. 
    Crawl from https://media.naver.com/journalists/. 
    """
    res = {}
    begin = time()

    for press_code, press_name in code2name.items(): 
        url = f'https://media.naver.com/journalists/whole?officeId ={press_code}'
        response = requests.get(url)
        # print('==================')
        # print(press_name, press_code)

        journalist_list = []

        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')

            for li in soup.find_all('li', {'class': 'journalist_list_content_item'}):
                info = li.find('div', {'class':'journalist_list_content_title'})
                a = info.find('a')
                journalist_name = a.text.strip(' 기자')
                journalist_link = a['href']
                journalist_list.append(journalist_name, journalist_link)
        
        res[press_code] = (press_name, journalist_list)
    
    return res 

class Journalist:
    def __init__(self, name, press_code, 
                career_list, 
                graduated_from, 
                no_of_subscribers, 
                subscriber_age_statistics, 
                subscriber_gender_statistics, 
                article_list):
        self.name = name 
        self.press_code = press_code 
        self.career_list = career_list
        self.graduated_from = graduated_from
        self.no_of_subscribers = no_of_subscribers
        self.subscriber_age_statistics = subscriber_age_statistics
        self.subscriber_gender_statistics = subscriber_gender_statistics
        self.article_list = article_list 


def crawl_journalist_info(link):
    """Make a Journalist class instance using the information in the given link. 
    """
    response = requests.get(link)

    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        profile_head = soup.find('div', {'class': 'media_reporter_basic_text'})
        # print(profile_head.find('a')['href'])
        profile_code = profile_head.find('a')['href'].split('/')[-1]
        journalist_name = profile_head.find('h2', {'class': 'media_reporter_basic_name'}).text
        print(profile_code, journalist_name)




if __name__ == '__main__':
    code2info_pickle = 'code2info.pickle'

    crawl_journalist_info('https://media.naver.com/jouralist/006/31564')

    # if code2info_pickle in os.listdir():
    #     begin = time()
    #     code2info = pickle.load(open(code2info_pickle, 'rb'))
    #     end = time()
    #     print(f'{end-begin} sec passed for execution and pickling')
    # else:
    #     begin = time()
    #     code2name = crawl_press_names_and_codes()
    #     code2info = crawl_journalist_info_pages(code2name)
    #     pickle.dump(code2info, open(code2info_pickle, 'wb+'))
    #     end = time()
    #     print(f'{end-begin} sec passed for execution and pickling')
    # for code, (press_name, journalist_list) in code2info.items():
    #     for journalist_name, link in journalist_list:
    #         j = crawl_journalist_info(link)
    #         assert j.name == journalist_name