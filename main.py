

import selenium

from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver')
#------------------------- 설정
id = "mgpark"
pw = "shlove40541!"
sName = "MK001"                     #상품명
#sSelect = 상품구분(본품/사은품/부자재)
sCode = "MK001"                     #단품상품코드
sbCode = "MK001"
cstCd = "04614"                        #고객사코드
giftDiv = "본품"
#--------------------------설명끝

driver.get('https://fms.fassto.ai/')                 #웹 열기
driver.implicitly_wait(time_to_wait=2)              #2초 대기
driver.find_element_by_name('loginId').send_keys(id)      #아이디
driver.find_element_by_name('psWd').send_keys(pw)              #암호
driver.implicitly_wait(time_to_wait=3)
driver.find_element_by_class_name('btn_login').click()          #로그인 버튼클릭

driver.implicitly_wait(time_to_wait=5)
driver.find_element_by_xpath('//*[@id="side_header"]/nav/ul/li[1]/a/strong').click()  #상품관리 메뉴클릭
driver.find_element_by_xpath('//*[@id="side_header"]/nav/ul/li[1]/ul/li[1]/a').click()  #상품등록
driver.implicitly_wait(time_to_wait=2)
driver.find_element_by_name('cstCd').send_keys(cstCd)                   #고객사코드 입력
driver.implicitly_wait(time_to_wait=2)
driver.find_element_by_xpath('//*[@id="btnSearch"]').click()                    #조회 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
driver.find_element_by_xpath('//*[@id="btnNew"]').click()                  #단품상품 등록 버튼 클릭


driver.implicitly_wait(time_to_wait=2)

mg = driver.find_element_by_id('giftDiv').find_element_by_id('divGodBasicContent')

mg.click()
driver.find_element_by_css_selector('#giftDiv > option:nth-child(2)').click()









