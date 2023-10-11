import requests
from bs4 import BeautifulSoup as BS
import _servis_info


def scraping_page(URL):
    """
        1)Делаем get запрос, получаем html код страницы с помощью request
        2)Функция возвращает объект BS, для дальнейшей работы с контентом
    """
    return BS(requests.get(URL, cookies=_servis_info.cookies, headers=_servis_info.headers).content, 'html.parser')


def content_of_this_page(html, len_dict):
    temp_dict = {}
    name_response_list = html.find_all("p", class_="sub_title")
    response_content_list = html.find_all("span", class_="_reachbanner_")
    for i in range(len(response_content_list)):
        if name_response_list[i].text != "":
            temp_dict.update({len_dict + i : name_response_list[i].text.strip() + '\n' + response_content_list[i].text.strip()})
        else: 
            temp_dict.update({len_dict + i : 'noname response' + '\n' + response_content_list[i].text.strip()})
    return temp_dict
    

def get_full_dictionary():
    temp_good_dict = {}
    temp_bad_dict = {}
    temp_bad_dict.update(content_of_this_page(scraping_page(_servis_info.url_bad_list[0]), len(temp_bad_dict)))
    temp_good_dict.update(content_of_this_page(scraping_page(_servis_info.url_good_list[0]), len(temp_good_dict)))
    return (temp_good_dict, temp_bad_dict)


def response_write_to_file(dictionarys):
    print(dictionarys[0])
    for i in range(len(dictionarys[1])):
        with open(f"Dataset/Bad/{'{:04}'.format(i)}.txt", "w", encoding="utf-8") as file:
            file.write(dictionarys[1].get(i))

    for i in range(len(dictionarys[0])):
        with open(f"Dataset/Good/{'{:04}'.format(i)}.txt", "w", encoding="utf-8") as file:
            file.write(dictionarys[0].get(i))






response_write_to_file(get_full_dictionary())














'''
def get_full_dictionary():
    temp_good_dict = {}
    temp_bad_dict = {}
    for url in _servis_info.url_bad_list:
        temp_bad_dict.update(content_of_this_page(scraping_page(url)))
        print('Робит')
    else: print("Капча")
    for url in _servis_info.url_bad_list:
        temp_good_dict.update(content_of_this_page(scraping_page(url)))
    return {'good response' : temp_good_dict, 'bad response' : temp_bad_dict}

'''

