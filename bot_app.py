from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 업데이트

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime as dt
import time
import os

dlist = {
    0:'월',
    1:'화',
    2:'수',
    3:'목',
    4:'금',
    5:'토',
    6:'일'
}
#음성 인식 기능
def stt_mod():
    r = sr.Recognizer()  #마이크 인식
    with sr.Microphone() as source:  #마이크의 음성을 넣어 주기
        print('음성 입력 중...')
        audio = r.listen(source) #마이크로부터 음성을 듣기
    # 구글 API로 인식 (하루 50회)
    text = r.recognize_google(audio, language='ko')
    print(text)
    return text
#text를 말하는 기능
def tts_mod(stext):
    tts = gTTS(text=stext, lang='ko')
    tts.save('mod.mp3') #mp3 저장
    playsound('mod.mp3') #mp3 재생
    os.remove('mod.mp3') #mp3 삭제

#검색 기능
def search(test_str):
    #크롬 드라이버 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options) 

    # 구글 열기
    url = 'https://www.google.co.kr/'
    driver.get(url)

    time.sleep(1) # 로딩 시간
    #구글 검색
    element = driver.find_element(By.NAME,'q')
    element.send_keys(test_str)
    element.submit()
    #검색이 끝나면 나오는 음성
    tts_mod(f'{test_str}의 검색이 완료 됬습니다.')

#카카오톡 열기 기능
def kakao():
    #카카오톡 기본 설치 경로
    os.chdir(r'C:\Program Files (x86)\Kakao\KakaoTalk') 
    #카카오톡 열기
    os.system('KakaoTalk.exe')
    #project폴더로 이동
    os.chdir(r'C:\Users\useun\OneDrive\바탕 화면\project_end')
    #다시 경로 이동
    tts_mod('카카오톡이 열렸습니다.')

# kakao()

#현재 시간 & 날짜
def dayt():
    x = dt.datetime.now()
    #년/월/일/요일/시/분/초라는 튜플 p에 담기
    p = x.strftime("%Y년 %m월 %d일"),dlist[x.weekday()]+'요일',x.strftime("%H시 %M분 %S초")
    #튜플형태 제거
    p = ','.join(p)
    #확인용
    print(p) 
    #p의 내용 읽기
    tts_mod(p)


#현재 날씨
def weather(test_str):
    #크롬 드라이버 준비
    chrome_options = Options()
    chrome_options.add_argument("headless") #백그라운드에서 작업
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #구글 열기
    url = 'https://www.google.co.kr/'
    driver.get(url)

    #검색
    element = driver.find_element(By.NAME,'q')
    element.send_keys(test_str)
    element.submit()

    #날씨 정보 가져오기
    m = driver.find_element(By.XPATH,'//*[@id="wob_loc"]').text #지역
    d = driver.find_element(By.XPATH,'//*[@id="wob_dc"]').text #현재 날씨
    str_stt = f'{m}의 날씨는 {d} 입니다.'
    #확인용
    print(str_stt)
    driver.close #창 닫기
    #확인 메세지
    tts_mod(str_stt)

# weather('봉담읍 날씨')