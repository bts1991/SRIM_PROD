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


# def request(StockNo, CoNm):
#     url1 = "https://www.macrotrends.net/stocks/charts/"+StockNo+"/"+CoNm+"/total-share-holder-equity"
#     res1 = requests.get(url1)
#     soup1 = BeautifulSoup(res1.text, "html.parser")

#     return [soup1, url1]

# StockNo = 'HSY'
# CoNm = 'hershey'

# requestResult = request(StockNo, CoNm)

# ## 기준일자 구하기 - 성공
# soup1 = requestResult[0]
# url1 = requestResult[1]

# print(soup1)
# print(url1)

# baseDate = (soup1.select_one('#main_content > div:nth-child(2) > span > ul'))
# # print(baseDate)
# baseDate2=soup1.find_all('li', attrs = {'id':'main_content'})
# # print(baseDate2)

# equity = soup1.select_one('#main_content > div:nth-child(2) > span > ul > li:nth-child(1) > strong:nth-child(1)')
# print(equity)


# res2 = requests.get('https://finance.yahoo.com/quote/HSY/balance-sheet')
# print(res2)
# soup2 = BeautifulSoup(res2.text, "html.parser")
# print(soup2)


# res2 = requests.get('https://www.macrotrends.net/stocks/charts/HSY/hershey/revenue', headers={'User-agent': 'Mozilla/5.0'})
# print(res2)
# soup2 = BeautifulSoup(res2.text, "html.parser")
# print(soup2)

url = "https://macrotrends-finance.p.rapidapi.com/quotes/dividend/dates/%7Bsymbol%7D"

querystring = {"range":"1y","interval":"1d"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "macrotrends-finance.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())