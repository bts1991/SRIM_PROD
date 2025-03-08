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


url3 = "https://www.nicerating.com/disclosure/gradedRates.do"
res3 = requests.get(url3)
soup3 = BeautifulSoup(res3.text, "html.parser")

# print(soup3)

# ## 할인율(BBB- 회사채 5년 수익률) 구하기

ts4 = soup3.select_one('#dBody > section > div.tbl_type01 > table > tbody > tr:nth-child(10) > td:nth-child(7)').text
print(ts4)


DCRate = float(ts4)
print(DCRate)
print(type(DCRate))

# table = soup3.select_one("#tbl_val") # >>> 이것만 성공
# print("table", table)  # None이면 table이 아예 없는 것

# tbody = soup3.select_one("tbody.kap_tbody_data")
# print("tbody", tbody)  # None이면 tbody가 없는 것

# row = soup3.select_one("tbody.kap_tbody_data > tr:nth-child(52)")
# print("row", row)  # None이면 52번째 tr이 없는 것

# cell = soup3.select_one("tbody.kap_tbody_data > tr:nth-child(52) > td:nth-child(10)")
# print("cell", cell)  # None이면 10번째 td가 없는 것

