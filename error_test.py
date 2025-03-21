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
from findStock import FindStock
import time
from datetime import datetime
from StockMange import insertStock, updateStock, findStock
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# url3 = "https://www.nicerating.com/disclosure/gradedRates.do"
# res3 = requests.get(url3)
# soup3 = BeautifulSoup(res3.text, "html.parser")

# # print(soup3)

# # ## 할인율(BBB- 회사채 5년 수익률) 구하기

# # ts4 = soup3.select_one('#dBody > section > div.tbl_type01 > table > tbody > tr:nth-child(10) > td:nth-child(7)').text
# # ts4 = soup3.select_one('#jsMdiContent > div > div.CI-GRID-AREA.CI-GRID-ON-WINDOWS.CI-GRID-CLICKED > div.CI-GRID-WRAPPER > div.CI-GRID-MAIN-WRAPPER > div.CI-GRID-BODY-WRAPPER > div > div > table > tbody > tr:nth-child(10) > td:nth-child(2)').text
# print(res3)
# # print(soup3)
# # print(ts4)

# ## 할인율(BBB- 회사채 5년 수익률) 구하기 => 3년 수익률로 변경(25.03.08)
# ts4 = soup3.select_one('#dBody > section > div.tbl_type01 > table > tbody > tr:nth-child(10) > td:nth-child(7)').text
# DCRate = float(ts4)
# # print(DCRate)
# # print(type(DCRate))

# #dBody > section > div.tbl_type01 > table > tbody > tr:nth-child(10) > td:nth-child(7)

import pandas as pd

# 웹 페이지 URL
url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"

# 요청 보내기
session = requests.Session()
response = session.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 수익률 테이블 선택 (수익률 탭: con_tab1)
table = soup.select_one("#con_tab1 table")

# 'BBB-' 등급 행만 탐색
for row in table.select("tbody tr"):
    cols = [col.text.strip().replace("%", "") for col in row.select("td")]
    if cols and cols[0] == "BBB-":
        five_year_yield = cols[8]  # 5년 수익률은 9번째 열 (0부터 시작)
        print(f"BBB- 등급 5년 수익률: {five_year_yield}%")
        DCRate = float(five_year_yield)
        print(DCRate)