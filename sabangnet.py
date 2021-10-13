
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#변수


OderID = 'testMG23'                 #쇼핑몰주문번호
GoodsCode = '100014'                #쇼핑몰 상품품번
Goods = '새우 텀블러'                 #주문 상품명
GoodsN = '2'                        #수량
FssGoodsN = 'MG001'                 #FMS 쇼핔몰연결 상품코드
Pay = '20'                          #결제금액
OderName = 'MG'                     #주문자명

driver = webdriver.Chrome('chromedriver')

#사방넷접속
driver.get("http://www.sabangnet.co.kr/index.html")
time.sleep(1)

#로그인
driver.find_element_by_name('id').send_keys('fss1')
driver.find_element_by_name('passwd').send_keys('fssdev0301!')
driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[3]/div[1]/form/fieldset/div/button[1]').click()
driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[3]/div[1]/fieldset/div/button[1]').click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)
driver.close()
driver.implicitly_wait(10)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#주문서입력화면(건별)
driver.get("http://a200.sabangnet.co.kr/order/Order_input")
driver.find_element_by_css_selector("body > div.page_cls > form > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]").click()

#쇼핑몰정보입력
select = Select(driver.find_element_by_xpath('/html/body/div[4]/form/table[2]/tbody/tr[2]/td[2]/select'))
select.select_by_value('1547')
select1 = Select(driver.find_element_by_xpath('/html/body/div[4]/form/table[2]/tbody/tr[2]/td[4]/select'))
select1.select_by_value('FSS ID_02')

#주문자정보
driver.find_element_by_name('user_name').send_keys("MG")                            #주문자정보_성명
driver.find_element_by_name('user_cel').send_keys('01041964844')                   #주문자정보_핸드폰

#수취인정보
driver.find_element_by_name('receive_name').send_keys("MG")                         #수취인정보_성명
driver.find_element_by_name('receive_cel').send_keys('01041964844')                #수취인정보_핸드폰
driver.find_element_by_xpath('/html/body/div[4]/form/table[6]/tbody/tr[3]/td[2]/img').click()


driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)

#우편번호검색팝업
driver.find_element_by_xpath('//*[@id="frm"]/table[1]/tbody/tr[2]/td[2]/input').send_keys('경기도 부천시 부흥로 49')
driver.find_element_by_xpath('//*[@id="frm"]/table[1]/tbody/tr[2]/td[2]/img').click()
driver.find_element_by_xpath('//*[@id="frm"]/table[2]/tbody/tr[2]/td[2]/a').click()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

#주문상품정보입력
driver.find_element_by_name('order_id1').send_keys(OderID)                                          #쇼핑몰주문번호
driver.find_element_by_xpath('//*[@id="ord_good1"]/tbody/tr[2]/td[2]/img').click()                  #상품코드검색
driver.switch_to.window(driver.window_handles[-1])                                                  #팝업창전환
driver.find_element_by_xpath('//*[@id="prod_frm"]/table/tbody/tr[1]/td[2]/div/a[6]/img').click()    #[1년] 클릭
select1 = Select(driver.find_element_by_xpath('//*[@id="prod_frm"]/table[1]/tbody/tr[5]/td[2]/select')) #검색항목
select1.select_by_value('prod_id')                                                                  #품번코드 항목
driver.find_element_by_name('search_str').send_keys(GoodsCode)                                      #품번코드 입력
driver.find_element_by_xpath('//*[@id="prod_frm"]/table/tbody/tr[5]/td[2]/input[2]').click()        #[검색]클릭
driver.find_element_by_xpath('//*[@id="prod_frm"]/table[2]/tbody/tr[2]/td[6]/input').click()        #[선택]클릭
driver.find_element_by_xpath('/html/body/div/table[3]/tbody/tr[3]/td[6]/input[3]').click()          #옵션선택(수정필요)
driver.switch_to.alert.dismiss()                                                                    #얼럿닫힘
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_name('mall_product_id1').send_keys(FssGoodsN)                                #쇼핑몰상품코드
driver.find_element_by_name('mall_product_name1').send_keys(Goods)                                  #주문상품명
driver.find_element_by_name('sale_cnt1').send_keys(GoodsN)                                          #수량
driver.find_element_by_name('pay_cost1').send_keys(Pay)                                             #결제금액
driver.find_element_by_name('delivery_method1').send_keys('무료')                                    #배공구분
driver.find_element_by_xpath('/html/body/div[4]/form/table[28]/tbody/tr/td/img').click()            #[저장]

time.sleep(1)
driver.refresh()
time.sleep(1)

driver.switch_to.alert.accept()
time.sleep(1)
#
# driver.find_element_by_xpath('//*[@id="prod_frm"]/table[2]/tbody/tr/td[2]/img[1]').click()
#
#
# time.sleep(1)
# driver.switch_to.alert.accept()
#
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[-1])
#
# driver.find_element_by_xpath('/html/body/div/form/center/input').click()
# driver.close()
#
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[0])




