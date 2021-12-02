# 정적 웹 크롤링 = butiful soup
# 동적 웹 크롤링 = selenium
# 참고사이트
# 1. https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/
# 2. https://lpla.tistory.com/17
# 3. https://nyeongnyeong.tistory.com/24

# 동적 웹 크롤링을 먼저 작성한 후 '경매 입찰 최적가 계산기'에 추가 할 예정
# 1. 로스트아크 전투 정보실 웹 크롤링(가능여부 확인O)
# 2. 위의 정보를 출력
# 3. 원정대 캐릭터 정보를 참고하여 주간 컨텐츠 수익 예상 출력

# 오류 사항
# 1. 로아와에서 한번에 가져오는 것을 하지 못함.

from selenium import webdriver
driver = webdriver.Chrome('F:/Portfolio/Frontend Developers/python/discord/chromedriver.exe')
# 전투 정보실 링크
url = 'https://lostark.game.onstove.com/Profile/Character/%ED%98%B8%EB%B0%80%EC%9D%B42'

#전투 정보실 페이지 오픈
driver.get(url)

# # 요소 찾기 - 검색창 찾고 키 전송
# search = driver.find_element_by_class_name('input input--profile-search')
# search.send_keys('호밀이2')

# 검색 캐릭터 이름
character_name = driver.find_element_by_class_name('profile-character-info__name')

# 검색 캐릭터 서버 이름
character_server = driver.find_element_by_class_name('profile-character-info__server')

print('+' * 100)
print('캐릭터명 : ',character_name.text, '  서버명 : ',character_server.text[1::])

# 캐릭터 원정대 레벨, 전투 레벨
character_level1 = driver.find_elements_by_class_name('level-info')
for i in character_level1:
    print(i.text)

# 아이템 레벨
character_level2 = driver.find_elements_by_class_name('level-info2')
for i in character_level2:
    print(i.text)

# 보유 캐릭터 버튼 클릭
have_character = driver.find_element_by_css_selector('#lostark-wrapper > div > main > div > div.profile-character-info > button')
have_character.click()



have_ch_num = driver.find_elements_by_css_selector('#expand-character-list')
for i in have_ch_num:
    print(i.text)

# # 로아와 링크
# url2 = 'https://loawa.com/char/%ED%98%B8%EB%B0%80%EC%9D%B42'

# # 로아와 페이지 오픈
# driver.get(url2)

# # 보유캐릭터 탭 클릭
# driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/label[6]').click()

# have_ch = driver.find_element_by_css_selector('#char_clist')
# print(have_ch)