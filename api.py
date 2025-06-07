import os
import requests

from dotenv import load_dotenv

load_dotenv()

SERVICE_KEY = os.getenv("SERVICE_KEY")

# 국가기술자격 종목별 응시수수료 조회

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getFeeList'
params ={'serviceKey' : SERVICE_KEY, 'jmcd' : '1320' }

response = requests.get(url, params=params)
print(response.content)

# 국가기술자격 종목별 일정 조회

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getJMList'
params ={'serviceKey' : SERVICE_KEY, 'jmcd' : '1320' }

response = requests.get(url, params=params)
print(response.content)

# 국가기술자격 종목별 자격정보

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryInformationTradeNTQSVC/getList'
params ={'serviceKey' : SERVICE_KEY, 'jmCd' : '1320' }

response = requests.get(url, params=params)
print(response.content)

# 국가전문자격 종목 조회

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryListNationalQualifcationSVC/getList'
params ={'serviceKey' : SERVICE_KEY }

response = requests.get(url, params=params)
print(response.content)

# 국가전문자격 시험일정 조회

url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestDatesNationalProfessionalQualificationSVC/getList'
params ={'serviceKey' : SERVICE_KEY, 'seriesCd' : '21' }

response = requests.get(url, params=params)
print(response.content)