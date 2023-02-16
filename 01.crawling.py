from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
from urllib.request import urlopen
import os
import shutil

keyword = str(input("키워드를 입력해주세요:" ))

# 디렉터리 삭제
if os.path.exists(keyword):
        shutil.rmtree(keyword)


# 디렉터리 생성
if not os.path.exists(keyword):
        os.makedirs(keyword)

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(by=By.NAME, value="q")
elem.clear()
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

# 이미지를 최대로 찾기 위해서 스크롤을 계속 아래로 내림
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_elements(by=By.CSS_SELECTOR, value=".mye4qd").click()
            except:
                break

        last_height = new_height
img_tags = driver.find_elements(by=By.CSS_SELECTOR, value=".rg_i.Q4LuWd")
print(f"이미지{len(img_tags)}개 찾았음")
cnt = 1
for img_tag in img_tags:
        try:
            img_tag.click()
            image_url = driver.find_element(
                by=By.XPATH,
                value="//*[@id='islrg']/div[1]/div[2]/a[1]/div[1]/img").get_attribute("src")

            # 이미지 저장
            if cnt < 10:
                filename = f"00{cnt}.jpg"
            elif 10 <= cnt < 100:
                filename = f"0{cnt}.jpg"
            else:
                filename = f"{cnt}.jpg"

            urllib.request.urlretrieve(image_url, f"{keyword}/{filename}")
            print(f"{cnt}개 저장완료")
            cnt = cnt + 1
        except:
            pass

print(f"다운로드 완료")
driver.close()