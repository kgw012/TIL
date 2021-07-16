import requests
from pprint import pprint
from telegram import sendMessage
from decouple import config

query = '닌텐도스위치'
url = f'https://openapi.naver.com/v1/search/shop.json?query={query}'

headers = {
    'X-Naver-Client-Id' : config('X-Naver-Client-Id'),
    'X-Naver-Client-Secret' : config('X-Naver-Client-Secret')
}

response = requests.get(url, headers=headers).json()

min = 1000000
# 1. 반복문을 사용하여 각 제품마다 lprice를 출력
for item in response['items']:
    title = item['title']
    lprice = int(item['lprice'])

    print(title + " : " + str(lprice))
    if(min > lprice):
        min = lprice
        litem = item

ltitle = litem['title']
lprice = litem['lprice']
llink = litem['link']

# 3. 최저가명, 최저가, 최저가 쇼핑몰 링크 출력
print(f"최저가 상품 : {ltitle}({lprice}원), ({llink})")


# 4. 텔레그램으로 출력
msg = f"최저가 상품 : {ltitle}({lprice}원), ({llink})"
sendMessage(msg)