from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

#변수
driver = webdriver.Chrome('chromedriver')
OderId = 'MG000006'                              #주문번호
MallProductId = 'MG001'                         #쇼핑몰상품코드
ProductName = '청바지'                         #상품명
Qty = '2'                                   #주문수량

#샵링커접속
driver.get('https://ad2.shoplinker.co.kr/index.php')

#로그인
driver.find_element_by_name('user_id').send_keys('FSStest')
driver.find_element_by_name('passwords').send_keys('fssdev12!@')
driver.find_element_by_xpath('/html/body/form/div[1]/div[1]/div[1]/a').click()
time.sleep(1)

#주문서수동등록(화면)
driver.get('http://ad2.shoplinker.co.kr/admin/order/order_insert_screen')
time.sleep(1)

#주문자정보입력
driver.find_element_by_name('user_name').send_keys('MG')          #주문자명
driver.find_element_by_name('user_tel').send_keys('01012345678')  #전화번호
driver.find_element_by_name('user_cel').send_keys('01012345678')  #핸드폰

#수취인정보입력
driver.find_element_by_xpath('//*[@id="uodr_chk"]').click()       #주문자동일체크박스
driver.find_element_by_xpath('//*[@id="orderManualForm"]/table[2]/tbody/tr[4]/td/input[2]').click()


driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)

#우편번호찾기팝업
driver.find_element_by_id('addr_text').send_keys('강남구 테헤란로 79길 6')
driver.find_element_by_id('addr_search').click()
time.sleep(1)
driver.find_element_by_class_name('addr_row').click()            #우편번호선택

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

#주문상품정보
select = Select(driver.find_element_by_name('mall_id'))
select.select_by_value('mall0247')              #쇼핑몰명선택
driver.find_element_by_name('customer_user_id').send_keys('MG')   #쇼핑몰id번호
driver.find_element_by_name('order_id').send_keys(OderId)
driver.find_element_by_name('baesong_type').send_keys('무료')      #배송정보
driver.find_element_by_name('mall_product_id').send_keys(MallProductId)  #쇼핑몰상품코드
driver.find_element_by_name('product_name').send_keys(ProductName)  #상품명
driver.find_element_by_name('quantity').send_keys(Qty)       #주문수량
driver.find_element_by_name('supply_price').send_keys('10') #납품가
driver.find_element_by_name('total_price').send_keys('10')  #주문금액

#샵링커상품검색
driver.find_element_by_xpath('//*[@id="orderManualForm"]/table[3]/tbody/tr[4]/td[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)

#상품명검색
driver.find_element_by_xpath('//*[@id="btn_period_5year"]').click()
driver.find_element_by_name('search_str').send_keys('청바지')
driver.find_element_by_xpath('//*[@id="btn"]').click()
driver.find_element_by_name('No[]').click()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

#주문등록하기버튼클릭
driver.find_element_by_id('save_btn').click()

time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
driver.close()




