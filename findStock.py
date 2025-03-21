import os
import json
import re
from flask import Flask, render_template, request, redirect, jsonify
from bson import json_util
from bson.json_util import dumps
# from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect
from flask.json import jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
# import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from urllib.parse import urlencode, unquote
import requests
# import pandas as pd
import math
# import numpy as np
import xmltodict
from pymongo.server_api import ServerApi

# client = MongoClient('localhost', 27017)
# client = MongoClient("mongodb://localhost:27017/")
uri = "mongodb+srv://btsy7331:dygksqhrdma155!@cluster0.dw6olvv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# db = client.test_database
db = client['SRIM'] # test-db라는 이름의 데이터베이스에 접속
main = db.main

def StockNo(CoNm, numOfRows):
        url = "http://apis.data.go.kr/1160100/service/GetKrxListedInfoService/getItemInfo"
        headers = {'accept': 'application/xml'}
        params = {
            'serviceKey': 'COYqtTFUZDHf2qQtliLOSSioIJEosLJTNX3g8PaEC+C0QTs6Jq62vFThZwyhi/iohWNIGwaEA7WJ9KGMf92rkg=='
            , 'ItmsNm': CoNm
            # , 'likeItmsNm': CoNm
            , 'numOfRows': numOfRows
        }
        print("================================ response 시작 ================================")
        response = requests.get(url, headers=headers, params=params, timeout=15)
        # print(response.status_code)
        print("================================ response 종료 ================================")
        print("================================ resDict 시작 ================================")
        resDict = json.loads(json.dumps(xmltodict.parse(response.text), indent=4))
        # resDict의 결과 중 totalCount가 0이면 return
        totalCount = resDict['response']['body']['totalCount']
        if totalCount == 0 :
            data1 = "종목을 찾을 수 없습니다."
        else :
            # print(resDict)
            print("================================ resDict 종료 ================================")
            print("================================ resDict2 시작 ================================")
            resDict2 = resDict['response']['body']['items']['item']
            print(resDict2)
            print("================================ resDict2 종료 ================================")
            #print(resDict2)
            # for k in resDict2:
            #     # print(k['srtnCd']+" "+k['itmsNm'])
            #     print(k)
            data1 = list({k['srtnCd']: k for k in resDict2}.values())
            data2 = data1[0]['srtnCd']
            data3 = data1[0]['itmsNm']

        return data1

def FindStock(CoNm):
    try:
        #print(StockNo(CoNm, 100))
        return StockNo(CoNm, 100)
    except:
        time.sleep(3)
        #print(StockNo(CoNm, 100))
        return StockNo(CoNm, 100)

