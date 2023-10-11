import requests
from bs4 import BeautifulSoup as BS
import _servis_info


def scraping_page(URL):
    """
        1)Делаем get запрос, получаем html код страницы с помощью request
        2)Функция возвращает объект BS, для дальнейшей работы с контентом
    """
    return BS(requests.get(URL, cookies=_servis_info.cookies, headers=_servis_info.headers).content, 'html.parser')


def content_of_this_page(html):
    temp_dict = {}
    name_response_list = html.find_all("p", class_="sub_title")
    response_content_list = html.find_all("span", class_="_reachbanner_")
    for i in range(len(response_content_list)):
        if name_response_list[i].text != "":
            temp_dict.update({name_response_list[i].text.strip(): response_content_list[i].text.strip()})
        else: 
            temp_dict.update({"Название отзыва": response_content_list[i].text.strip()})
    return temp_dict
    

def get_full_dictionary():
    temp_good_dict = {}
    temp_bad_dict = {}
    temp_bad_dict.update(content_of_this_page(scraping_page(_servis_info.url_bad_list[0])))
    temp_good_dict.update(content_of_this_page(scraping_page(_servis_info.url_good_list[0])))
    return {'good response' : temp_good_dict, 'bad response' : temp_bad_dict}


print(get_full_dictionary())