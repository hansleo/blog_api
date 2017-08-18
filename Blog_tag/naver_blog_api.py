import os
import sys
import json
import urllib.request
import SQL_util
client_id = "DZ7SHYiA1Oq53gV4hEuF"
client_secret = "4C3VkZcbZ3"
encText = urllib.parse.quote("태그 -호이어")

for idx in range(151, 1000, 50):
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=50&start=" + str(idx) # json 결과
    print(url)
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        result_js = json.loads(response.read().decode('utf-8'))
        print(result_js)
        for item_idx in range(0, len(result_js['items'])):
            link = (result_js['items'][item_idx]['link']).replace("'", '')
            title = result_js['items'][item_idx]['title'].replace("'", '')

            input_data = "'"+link+"', '"+title+"', 0"
            SQL_util.insert(input_data, 'naver_blog_api')

    else:
        print("Error Code:" + rescode)
        break
