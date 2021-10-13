

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver')

driver.get('https://fss-test.imweb.me/')

#0번째이미지선택
driver.find_elements_by_css_selector('.item-overlay')[0].click()

#옵션선택
driver.find_element_by_xpath('//*[@id="prod_options"]/div/div/div[2]/label/span/span').click()

#수량삭제
driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE)

#주문수량입력
Qty = '2'
driver.find_element_by_xpath('//*[@id="prdOption0"]/div/div[2]/div[1]/div/input').send_keys(Qty)

#구매하기버튼클릭
driver.find_element_by_xpath('//*[@id="prod_goods_form"]/div[8]/a[1]').click()

time.sleep(1)

#팝업전환
driver.switch_to.window(driver.window_handles[-1])

#로그인/비밀번호입력
ID = 'fss@fssuniverse.com'
PASSWORD = 'fss1234!@'
driver.find_element_by_xpath('//*[@id="cocoaModal"]/div/div/article/form/div[1]/div[1]/input').send_keys(ID)
driver.find_element_by_xpath('//*[@id="cocoaModal"]/div/div/article/form/div[1]/div[2]/input').send_keys(PASSWORD)

#로그인버튼클릭
driver.find_element_by_xpath('//*[@id="cocoaModal"]/div/div/article/form/p/button').click()

#팝업전환
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)

#구매하기버튼클릭
driver.find_element_by_xpath('//*[@id="prod_goods_form"]/div[8]/a[1]').click()

time.sleep(1)

#전체동의체크박스선택
driver.find_element_by_xpath('//*[@id="order_form_wrap"]/div[2]/div[4]/div/div[1]/label/span').click()

#결제하기버튼클릭
driver.find_element_by_xpath('//*[@id="order_form_wrap"]/div[2]/a').click()