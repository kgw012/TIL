import requests
from telegram import sendMessage
from decouple import config

def checkDust(stationName):
    serviceKey = config('dust_serviceKey')
    dataTerm = 'DAILY'

    url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey={serviceKey}&stationName={stationName}&dataTerm={dataTerm}&returnType=json'
    response = requests.get(url).json()
    return response['response']['body']['items'][0]['pm10Value']

# 미세먼지 msg
stationName = '강남구'
pm10Value = checkDust(stationName)
dust_msg = f'{stationName}의 미세먼지 농도는 {pm10Value}입니다.'
sendMessage(dust_msg)