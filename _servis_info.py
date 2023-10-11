url_bad_list = [f'https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/bad/perpage/10/page/{i}/' for i in range(1, 41)] +\
[f'https://www.kinopoisk.ru/film/373314/reviews/ord/date/status/bad/perpage/10/page/{i}/' for i in range(1, 6)] +\
[f"https://www.kinopoisk.ru/film/841813/reviews/ord/rating/status/bad/perpage/10/page/{i}/" for i in range(1, 13)] +\
[f"https://www.kinopoisk.ru/film/413447/reviews/ord/rating/status/bad/perpage/10/page/{i}/" for i in range(1, 28)] +\
[f"https://www.kinopoisk.ru/film/695548/reviews/ord/rating/status/bad/perpage/10/page/{i}/" for i in range(1, 16)] +\
[f"https://www.kinopoisk.ru/film/396473/reviews/ord/rating/status/bad/perpage/10/page/{i}/" for i in range(1, 5)]

url_good_list = [f'https://www.kinopoisk.ru/film/535341/reviews/ord/date/status/good/perpage/10/page/{i}/' for i in range(1, 42)] + \
[f'https://www.kinopoisk.ru/film/435/reviews/ord/date/status/good/perpage/10/page/{i}/' for i in range(1, 41)] +\
[f'https://www.kinopoisk.ru/film/649917/reviews/ord/date/status/good/perpage/10/page/{i}/' for i in range(1, 21)]

cookies = {
    'gdpr': '0',
    '_ym_uid': '16448528461072416669',
    'yandex_login': 'volodia.kostsoff',
    'yandexuid': '9509181571644702675',
    'yuidss': '9509181571644702675',
    'mda_exp_enabled': '1',
    'i': '4K5UtGWdMvmU6fCN65xm2XMIcTei8OTaTABNGdNB61zqu1cCS7Eq42siWAu7LK+j0WHNNnfbFMRvPKP/TN+BP25KTkg=',
    '_csrf': 'RiZC3BhQBLSPKi5y6uBQAAW1',
    'desktop_session_key': '694cf4975f5a16e0ccacec8d73bc03adce9d708ac82f7417ad8ebbc21ebeab5429e6a3d0669de8b493a8a1a8389fd88e17b24edda9dd5fce77cfa289f42267654afd7c0e39127ee2976b20d06f0b5e31ce0e5ab5d012a6316972c711063be0a0',
    'desktop_session_key.sig': 'oEFo80NiXqoNOerTs1iy8A1L-Z0',
    'PHPSESSID': 'a062c5170080946dfd7b6f15fb8c7f9a',
    'yandex_gid': '11159',
    'uid': '73847494',
    'yp': '1689433083.yu.9509181571644702675',
    'ymex': '1691938683.oyu.9509181571644702675',
    'location': '1',
    '_csrf_csrf_token': 'cgOZ1Kb2MNgOfSiUudZtJJIUcLblhnTli6cElInZP9U',
    'coockoos': '1',
    'L': 'AFpUemVITXxpUWcOBHNQQGNBfHVeVHAGPTkZNw9eG2lZVjsbQRUkCw==.1693395746.15450.365239.a3f14ae52a683aa181c046fdb7db5fa1',
    'my_perpages': '%5B%5D',
    'tc': '11',
    'mobile': 'no',
    'crookie': 'FAKVZOys5z/Rz3DH7FxVMPVFSznPaep34g8uI94DBQBa/XDkRTowjUFSpbijSTheyHSPfUom+m0iI/5hX9yr+SHQkCs=',
    'cmtchd': 'MTY5NjQ0NjQ4Njc0Nw==',
    'ya_sess_id': '3:1696478370.5.0.1644747716039:Pg9-sA:6.1.2:1|424384460.-1.2|1689188215.18788622.2.2:18788622|30:10219410.590420.ak8PSttUZoYv7p5FKk5tdT35s-Y',
    'sessar': '1.1182.CiDVVioI3dW2yqIjhGV9u-atWm5oCIEmQdT26mqLSb-OfQ.K7uDT_uGmgs7UPeAKxcljhllswIdW-uzHxHuDhYp5NY',
    'ys': 'udn.cDp2b2xvZGlhLmtvc3Rzb2Zm#c_chck.1842562488',
    'mda2_beacon': '1696478370662',
    '_ym_d': '1696494621',
    '_yasc': 'lGwG7mVJM3tTv12DwzfMFtysWLXQR8oggBWHPXF4ytD84JYoWl1/wcGheFY4/F7T7Q==',
}


headers = {
    'authority': 'www.kinopoisk.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # 'cookie': 'gdpr=0; _ym_uid=16448528461072416669; yandex_login=volodia.kostsoff; yandexuid=9509181571644702675; yuidss=9509181571644702675; mda_exp_enabled=1; i=4K5UtGWdMvmU6fCN65xm2XMIcTei8OTaTABNGdNB61zqu1cCS7Eq42siWAu7LK+j0WHNNnfbFMRvPKP/TN+BP25KTkg=; _csrf=RiZC3BhQBLSPKi5y6uBQAAW1; desktop_session_key=694cf4975f5a16e0ccacec8d73bc03adce9d708ac82f7417ad8ebbc21ebeab5429e6a3d0669de8b493a8a1a8389fd88e17b24edda9dd5fce77cfa289f42267654afd7c0e39127ee2976b20d06f0b5e31ce0e5ab5d012a6316972c711063be0a0; desktop_session_key.sig=oEFo80NiXqoNOerTs1iy8A1L-Z0; PHPSESSID=a062c5170080946dfd7b6f15fb8c7f9a; yandex_gid=11159; uid=73847494; yp=1689433083.yu.9509181571644702675; ymex=1691938683.oyu.9509181571644702675; location=1; _csrf_csrf_token=cgOZ1Kb2MNgOfSiUudZtJJIUcLblhnTli6cElInZP9U; coockoos=1; L=AFpUemVITXxpUWcOBHNQQGNBfHVeVHAGPTkZNw9eG2lZVjsbQRUkCw==.1693395746.15450.365239.a3f14ae52a683aa181c046fdb7db5fa1; my_perpages=%5B%5D; tc=11; mobile=no; crookie=FAKVZOys5z/Rz3DH7FxVMPVFSznPaep34g8uI94DBQBa/XDkRTowjUFSpbijSTheyHSPfUom+m0iI/5hX9yr+SHQkCs=; cmtchd=MTY5NjQ0NjQ4Njc0Nw==; ya_sess_id=3:1696478370.5.0.1644747716039:Pg9-sA:6.1.2:1|424384460.-1.2|1689188215.18788622.2.2:18788622|30:10219410.590420.ak8PSttUZoYv7p5FKk5tdT35s-Y; sessar=1.1182.CiDVVioI3dW2yqIjhGV9u-atWm5oCIEmQdT26mqLSb-OfQ.K7uDT_uGmgs7UPeAKxcljhllswIdW-uzHxHuDhYp5NY; ys=udn.cDp2b2xvZGlhLmtvc3Rzb2Zm#c_chck.1842562488; mda2_beacon=1696478370662; _ym_d=1696494621; _yasc=lGwG7mVJM3tTv12DwzfMFtysWLXQR8oggBWHPXF4ytD84JYoWl1/wcGheFY4/F7T7Q==',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
}


dictionary_with_the_responses = {}



