from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import time
from bs4 import BeautifulSoup


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

##[실패] user agent를 이용해 우회해봤지만 실패함
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# chrome_options.add_argument('user_agent =' + user_agent)

##[실패] 디버깅 모드로 해봤으나 실패....
# chrome_browser = subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe '
#                                   r'--remote-debugging-port=9222 '
#                                   r'--user-data-dir="C:\Temp\chrome"')

# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

# 페이지 로딩이 완료될 때 까지 기다리는 코드
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get(url='https://www.macrotrends.net/stocks/charts/HSY/hershey/total-share-holder-equity')
# driver.set_window_size(1920, 1016)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'lxml')
ts2 = soup.select_one('#main_content > div:nth-child(2) > span > ul > li:nth-child(1) > strong:nth-child(1)').text
print(ts2)
driver.quit()



# # class name으로 찾기
# driver.find_element(By.CLASS_NAME,'gLFyf')
# # tag name으로 찾기
# driver.find_element(By.TAG_NAME,'textarea')
# # id로 찾기
# driver.find_element(By.ID,'APjFqb')
# # XPath로 찾기
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
# # 클릭하기
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/span[1]/input').click()
# # 값 입력하기
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/span[1]/input').send_keys("hsy")
# # 클릭하기
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/span[2]/button/span').click()
# # 키보드 입력하기
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)