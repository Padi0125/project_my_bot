import bot_app as app
#STT에 띄어쓰기 없을 경우
while 1:
    say1 = app.stt_mod() #STT로 텍스트 가져오기
    say1_list = say1.split(' ') #불러온 텍스트
    print(say1_list) #test출력
    if say1_list[0] == '시리야': #AI 이름 불러야 작동
        print(say1_list) #test출력
        try:
            for i in range(len(say1_list)): 
                if say1_list[i][0] == '검' and say1_list[i][1] == '색':  
                    app.search(say1_list[1:i])   #검색 APP실행
                    break
            if '카카오톡' in say1_list:
                app.kakao()   #카카오톡 APP실행
            elif '시간' in say1_list or '날짜' in say1_list:
                app.dayt()    #시간 APP실행
            elif '날씨' in say1_list:
                app.weather(say1_list[1:])  #날씨 APP실행
            elif '쉬어' in say1_list: 
                app.tts_mod('프로그램이 종료 됩니다. 다음에 또봐요!')   
                break #프로그램 종료
        except:
            app.tts_mod('인식을 못 했습니다... 다시 시도해 주세요')
    else:
        pass