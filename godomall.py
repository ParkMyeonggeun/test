
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#변수설정
driver = webdriver.Chrome('chromedriver')								#웹드라이버설정
godNm = "새우 텀블러"														#상품명
Qty = "2"															    #수량

#고도몰사이트접속
driver.get("http://fssdev01.godomall.com/")
driver.implicitly_wait(time_to_wait=2)

#상품명입력검색
driver.find_element_by_id('search_form').send_keys(godNm)
serch = driver.find_element_by_id('search_form')
serch.send_keys(Keys.RETURN)
driver.implicitly_wait(time_to_wait=2)

#상품이미지클릭
driver.find_element_by_class_name('middle').click()
driver.implicitly_wait(time_to_wait=2)

#셀렉트박스선택
for i in driver.find_elements_by_css_selector(".chosen-single"):
	i.find_element_by_xpath('//*[@id="frmView"]/div/div/div[2]/div/dl/dd/div/a').click()
driver.implicitly_wait(time_to_wait=2)

#상품옵션선택
driver.find_element_by_xpath('''//*[@id="frmView"]/div/div/div[2]/div/dl/dd/div/div/ul/li[3]''').click()

#상품수량입력
driver.find_element_by_name('goodsCnt[]').send_keys(Keys.BACKSPACE)
driver.find_element_by_name('goodsCnt[]').send_keys(Qty)

#구매버튼클릭
driver.find_element_by_xpath('//*[@id="frmView"]/div/div/div[4]/div/button[3]').click()

#로그인
driver.find_element_by_id('loginId').send_keys('fss_customer')
driver.find_element_by_id('loginPwd').send_keys('fssdev0301!')
driver.find_element_by_xpath('//*[@id="formLogin"]/div[1]/div[1]/button').click()
driver.implicitly_wait(time_to_wait=5)

#결제동의체크박스선택
driver.find_element_by_css_selector("#frmOrder > div > div.order_cont > div.order_view_info > div.payment_progress > div.payment_final > div.payment_final_check > div > label").click()

#결제하기버튼클릭
driver.find_element_by_xpath('//*[@id="frmOrder"]/div/div[2]/div[4]/div[4]/div[3]/div[3]/button').click()







