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
    """
        1)Получаем интересующий контент, а именно текст комментов и их название в 2 соответсвующие списка
        2)Создаем словарь, в котором ключ - это число от 1 до 1000, а значение - название коммента в первой строке, далее сам комментарий
        3)В случае, когда названия коммента нет - в первая строка именуется как "noname response"
    """
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
    """
        1) Из служебной информации берем список ссылок на страницы с отзывами 
        2) Возвращаем кортеж с 2 словарями 
    """
    temp_good_dict = {}
    temp_bad_dict = {}
    for url in _servis_info.url_bad_list:
        temp_bad_dict.update(content_of_this_page(scraping_page(url), len(temp_bad_dict)))
    for url in _servis_info.url_good_list:
        temp_good_dict.update(content_of_this_page(scraping_page(url), len(temp_good_dict)))
    return (temp_good_dict, temp_bad_dict)


def response_write_to_file(dictionarys):
    """
        1) Записываем в файл
        2) Здесь должно быть понятно почему я сделал ключи именно такими, это очень упростило задачу
    """
    for i in range(len(dictionarys[1])):
        with open(f"Dataset/Bad/{'{:04}'.format(i)}.txt", "w", encoding="utf-8") as file:
            file.write(dictionarys[1].get(i))

    for i in range(len(dictionarys[0])):
        with open(f"Dataset/Good/{'{:04}'.format(i)}.txt", "w", encoding="utf-8") as file:
            file.write(dictionarys[0].get(i))






response_write_to_file(get_full_dictionary())
















