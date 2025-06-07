import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERVICE_KEY = os.getenv("SERVICE_KEY")

# 국가기술자격 종목별 응시수수료 조회
def get_ntq_fee_list(jmcd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getFeeList'
    params = {'serviceKey': SERVICE_KEY, 'jmcd': jmcd}
    return requests.get(url, params=params).content

# 국가기술자격 종목별 일정 조회
def get_ntq_schedule(jmcd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestInformationNTQSVC/getJMList'
    params = {'serviceKey': SERVICE_KEY, 'jmcd': jmcd}
    return requests.get(url, params=params).content

# 국가기술자격 종목별 자격정보
def get_ntq_info(jmCd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryInformationTradeNTQSVC/getList'
    params = {'serviceKey': SERVICE_KEY, 'jmCd': jmCd}
    return requests.get(url, params=params).content

# 국가전문자격 종목 조회
def get_professional_qual_list():
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryListNationalQualifcationSVC/getList'
    params = {'serviceKey': SERVICE_KEY}
    return requests.get(url, params=params).content

# 국가전문자격 시험일정 조회
def get_professional_test_dates(seriesCd: str):
    url = 'http://openapi.q-net.or.kr/api/service/rest/InquiryTestDatesNationalProfessionalQualificationSVC/getList'
    params = {'serviceKey': SERVICE_KEY, 'seriesCd': seriesCd}
    return requests.get(url, params=params).content

# 과정평가형자격 정보 조회
def get_cq_list(pageNo: int = 1, numOfRows: int = 10):
    url = 'https://c.q-net.or.kr/openapi/cjmlist.do'
    params = {'serviceKey': SERVICE_KEY, 'pageNo': pageNo, 'numOfRows': numOfRows, 'type': 'json'}
    return requests.get(url, params=params).content

# 과정평가형자격 종목별 자격정보 조회
def get_cq_info(jmCd: str):
    url = 'https://c.q-net.or.kr/openapi/cqualinfo.do'
    params = {'serviceKey': SERVICE_KEY, 'jmCd': jmCd, 'type': 'json'}
    return requests.get(url, params=params).content

# 과정평가형자격 외부평가 일정정보 조회
def get_cq_schedule(year: str = '2025', pageNo: int = 1, numOfRows: int = 10):
    url = 'https://c.q-net.or.kr/openapi/cschinfo.do'
    params = {'serviceKey': SERVICE_KEY, 'pageNo': pageNo, 'numOfRows': numOfRows, 'year': year, 'type': 'json'}
    return requests.get(url, params=params).content