import random

#주식 회사 리스트 선언
Sm_Enter = [20950, 53000, 40400, 45850, 36600, 43250, 22900, 38600, 48050, 32850, 30600]
Yg_Enter = [74000, 98000, 62600, 60000, 47500, 43800, 26200, 29600, 43500, 31600, 45350]
Naver_It = [200000, 212000, 241000, 675000, 716000, 628000, 758000, 910000, 136000, 179500, 343000]
Nc_It = [192500, 294500, 138000, 198500, 202000, 234500, 304000, 442000, 468500, 636000, 953000]
Cellt_Bio = [35900, 37550, 25650, 44750, 40700, 112100, 100200,	315700,	219000,	165000,	324000]
Hanmi_Bio = [74500, 64000, 138000, 140500, 97800, 701000, 288000, 597000, 434000, 281000, 383000]
Ottogi_Food = [129000, 160000, 237500, 394000, 569000, 1414000, 650000, 770000, 779000,	507000,	561000]
LG_bty = [407000, 478000, 607000, 478000, 688000, 991000, 879000, 1177000, 1265000, 1258000, 1557000]
Kg_che=[9270, 7430, 11250, 17200, 16800, 14150, 14050, 26950, 16750, 12000, 21800]
Hmm_ship=[33550, 28850, 20450, 14150, 10250, 2850, 7680, 4620, 4005, 3475, 13650]

#년도별 힌트 리스트 선언
Hint_2012 = ["소녀시대, 샤이니 등 주력 연예인들이 일본 시장에 성공적으로 안착", "케이팝 인기에 덩달아 엔터종목 투자열풍 버블 우려도", "콘솔게임 온라인화 추세 엔씨. 넥슨 등 기회"]
Hint_2013 = ["SM과 크라제가 설립한 에스엠크라제의 치킨플랜차이즈 '치맥' 사업철수", "승리 스캔들' 영향? YG엔터 주가 하락세", "게임업종의 대세가 온라인에서 모바일 기반으로 이동한 만큼 PC 게임업체들의 주가가 곤두박질", "한미약품 미국 제약사 스펙트럼 2380만달러 기술 이전"]
Hint_2014=[" SNS 주가 날개, 한국 네이버 등에도 긍정영향 기대", "발빠른 사업전환 주가날았다, 신작 인터넷 게임 '블러드앤소울'이 중국 내 일평균 매출 50억 초과", "셀트리온 첫 신약인 종합독감치료제 'CT-P27'이 타미플루에 내성을 가진 인플루엔자에도 효과적", "국내 화장품 수익성 악화", "대한민국 조선업 부진으로 주가 하락"]
Hint_2015=["지드래곤 구설수 마다 주가 출렁? 소속 스타에 대한 의존 비중 줄이고 사업다각화에 박차", "식품 원자재 가격 하락과 히트 상품"]
Hint_2016=["셀트리온의 램시마 늦어도 내년 상반기 미국 식품의약국(FDA) 자문위원회의 권고와 판매 승인 예상","한미약품 5조원에 달하는 기술이전 계약 체결","화장품 브랜드 '후' 중국인들 사이 돌풍","선박 공급 과잉 지속과 글로벌 해운 업체들 운임 낮추기 시작"]
Hint_2017=["사드리스크, 중국 한류 금지령에 연예기획사와 화장품 주가 '추풍낙엽'", "사드리스크 : 손놓은 한류, 주가도 추풍낙엽", "식품 원자재 가격 하락 대비 영업이익 증가율 저조"]
Hint_2018=["중국의 금한령 완화의 기대감으로 주가 강세", "네이버 주가 더 간다, 라인 성장에 인공지능 투자도 성과로 성장동력마련", "2018년 중 출시될 신규 게임으로 인해 실적성장, 모바일 라인업 확대 및 해외 매출 비중 확대 ", "셀트리온 헬스케어 우호적인 수급환경 예상, 693억원 규모 판매계약에 주가 급등", "중국 사드 보복에 따른 유커 급감", "KG에너켐 인수하며 2차 전지 소재산업 진출"]
Hint_2019=["블랙핑크 유튜브 구독자 급증으로 뉴미디어 성장에 수혜보는 YG","Naver 실적 부진에 공매도까지..모바일 개편, 액면분할에도 주가 부양 '역부족'과 노조 리스크 '겹악재'", "KG그룹 동부제철 인수"]
Hint_2020=["연초부터 불거진 버닝썬게이트 이슈로 신인그룹들의 글로벌 성과마저 왜곡", "신작 매출 1위 꿰찬 엔씨소프트…‘리니지2M’ 돌풍에 ‘택진이 형’ 대박 날까", "코스피 시장 공매도 금액 상위종목 셀트리온 이름 올려 ", "한미약품 당뇨신약 수출 계획 무산", "식품 면제품 매출 하락세"]
Hint_2021=["Naver 목표주가 높아져, 쇼핑과 웹툰부분 매출 가파른 증가세", "NC 신작 기대감 선반영 시작, 증권가 '내년'에 집중하라", "코로나 치료제 허가신청 주가 급등", "GM 전기차 투자 계획소식", "초대형 컨테이너선 투입과 백신 수출 물량 급증"]

#개인 자산 변수 선언

my_stock_name = [1]
my_stock_price = [1]
my_stock_no = [1]


#게임 시작 함수
def playGame():
    Year = 2011
    Deposit = 500000
    my_money = 500000
    sell = "Y"
    choice = 0
    sell_num = 0
    ran = 0

    for i in range(0, 11):
        #년도별 주식 정보 출력
        print("========================================================")
        print("")
        print(Year ,"년도의 주식 정보 입니다. ")
        print("")
        print("1. SM엔터테이먼트 : ", format(Sm_Enter[i],","))
        print("2. 와이지엔터 : ", format(Yg_Enter[i],","))
        print("3. NAVER : ", format(Naver_It[i],","))
        print("4. 엔씨소프트 : ", format(Nc_It[i],","))
        print("5. 셀트리온 : ", format(Cellt_Bio[i],","))
        print("6. 한미약품 : ", format(Hanmi_Bio[i],","))
        print("7. 오뚜기 : ", format(Ottogi_Food[i],","))
        print("8. LG생활건강 : ", format(LG_bty[i],","))
        print("9. KG케미칼 : ", format(Kg_che[i],","))
        print("10. HMM : ", format(Hmm_ship[i],","))

        print("")
        #다음년도의 주가 힌트 랜덤으로 1개 보여줌
        if Year == 2011:
            ran = random.randint(0, len(Hint_2012)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2012[ran])
        elif Year == 2012:
            ran = random.randint(0, len(Hint_2013)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2013[ran])
        elif Year == 2013:
            ran = random.randint(0, len(Hint_2014)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2014[ran])
        elif Year == 2014:
            ran = random.randint(0, len(Hint_2015)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2015[ran])
        elif Year == 2015:
            ran = random.randint(0, len(Hint_2016)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2016[ran])
        elif Year == 2016:
            ran = random.randint(0, len(Hint_2017)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2017[ran])
        elif Year == 2017:
            ran = random.randint(0, len(Hint_2018)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2018[ran])
        elif Year == 2018:
            ran = random.randint(0, len(Hint_2019)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2019[ran])
        elif Year == 2019:
            ran = random.randint(0, len(Hint_2020)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2020[ran])
        elif Year == 2020:
            ran = random.randint(0, len(Hint_2021)-1)
            print("★ ", Year+1 , "년도의 랜덤 힌트! : ", Hint_2021[ran])
            
            
        print("")    
                           
        #보유 주식이 1개 이상 있을 경우 보유 주식 정보를 출력
        if len(my_stock_name) > 1:
            my_money = Deposit
            #print(my_stock)
            for x in range(1, len(my_stock_name)):
                if my_stock_name[x] == 1:
                    my_money += Sm_Enter[i]*my_stock_no[x]
                    print("보유주식 : SM엔터테이먼트 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 2:
                    my_money += Yg_Enter[i]*my_stock_no[x]
                    print("보유주식 : 와이지엔터 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 3:
                    my_money += Naver_It[i]*my_stock_no[x]
                    print("보유주식 : NAVER ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 4:
                    my_money += Nc_It[i]*my_stock_no[x]
                    print("보유주식 : 엔씨소프트 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 5:
                    my_money += Cellt_Bio[i]*my_stock_no[x]
                    print("보유주식 : 셀트리온 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 6:
                    my_money += Hanmi_Bio[i]*my_stock_no[x]
                    print("보유주식 : 한미약품 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 7:
                    my_money += Ottogi_Food[i]*my_stock_no[x]
                    print("보유주식 : 오뚜기 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 8:
                    my_money += LG_bty[i]*my_stock_no[x]
                    print("보유주식 : LG생활건강 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 9:
                    my_money += Kg_che[i]*my_stock_no[x]
                    print("보유주식 : KG케미칼 ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                elif my_stock_name[x] == 10:
                    my_money += Hmm_ship[i]*my_stock_no[x]
                    print("보유주식 : HMM ", my_stock_no[x],"주 (매입가 : ", my_stock_price[x],")")
                
        #보유주식의 현재 주가 정보를 반영하여 현재 자산 출력
        print("")
        print("현재 자산은 ", format(my_money,","),"원")
        try:
            print("현재 수익률 : ", round((my_money-500000)/500000*100,2),"%")
        except ZeroDivisionError: # 나누기 0 에러 예외처리
            print("현재 수익률 : 0%")
        
        print("")
        
        #보유주식이 1개 이상 있을 경우 매도 여부 확인
        if len(my_stock_name) > 1:
            while True:
                sell = input("▶ 매도하시겠습니까? Y or N : ")
                if sell == "N":
                    print("매도하지 않고 넘어갑니다.")
                    break
                elif sell == "Y":
                    Deposit = my_money
                    #print(Deposit)
                    print("매도 완료되었습니다! ")
                    #매도시 전량 매도 (추후 부분매도 가능하게 보완하고 싶음)
                    my_stock_name.clear()
                    my_stock_price.clear()
                    my_stock_no.clear()
                    my_stock_name.append(1)
                    my_stock_price.append(1)
                    my_stock_no.append(1)
                    break
                else:
                    print("올바른 값을 입력하세요")
            
        print("")
        print("========================================================")
            
        while True:
            #주식 매수 시 코드
            if sell != "Y":
                break
            elif Year == 2021:
                break
            print("")
            choice = int(input("▶ 매수하고자 하는 주식을 선택해주세요(숫자로만 입력하세요) : "))
            sell_num = int(input("▶ 몇 주를 구입하시겠습니까? : "))
            
            if choice == 1:
                if Deposit > Sm_Enter[i]*sell_num:
                    my_stock_name.append(1)
                    my_stock_price.append(Sm_Enter[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Sm_Enter[i]*sell_num)
                        
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 2:
                if Deposit > Yg_Enter[i]*sell_num:
                    my_stock_name.append(2)
                    my_stock_price.append(Yg_Enter[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Yg_Enter[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 3:
                if Deposit > Naver_It[i]*sell_num:
                    my_stock_name.append(3)
                    my_stock_price.append(Naver_It[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Naver_It[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 4:
                if Deposit > Nc_It[i]*sell_num:
                    my_stock_name.append(4)
                    my_stock_price.append(Nc_It[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Nc_It[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 5:
                if Deposit > Cellt_Bio[i]*sell_num:
                    my_stock_name.append(5)
                    my_stock_price.append(Cellt_Bio[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Cellt_Bio[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 6:
                if Deposit > Hanmi_Bio[i]*sell_num:
                    my_stock_name.append(6)
                    my_stock_price.append(Hanmi_Bio[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Hanmi_Bio[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 7:
                if Deposit > Ottogi_Food[i]*sell_num:
                    my_stock_name.append(7)
                    my_stock_price.append(Ottogi_Food[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Ottogi_Food[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 8:
                if Deposit > LG_bty[i]*sell_num:
                    my_stock_name.append(8)
                    my_stock_price.append(LG_bty[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(LG_bty[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 9:
                if Deposit > Kg_che[i]*sell_num:
                    my_stock_name.append(9)
                    my_stock_price.append(Kg_che[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Kg_che[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            elif choice == 10:
                if Deposit > Hmm_ship[i]*sell_num:
                    my_stock_name.append(10)
                    my_stock_price.append(Hmm_ship[i])
                    my_stock_no.append(sell_num)
                    Deposit = Deposit-(Hmm_ship[i]*sell_num)
                else:
                    print("현재 자산이 매수하고자 하는 주식보다 적습니다. 매수 불가능.")
                    break
            else:
                print("잘못 입력하셨습니다")

            sell = input("▶ 추가 매수 하시겠습니까? (Y or N) : ")
                
            print("")
            print("========================================================")
                
    
                  

        Year += 1
        if Year > 2021:
            print("")
            print("★ 최종 수익률은 : ",round((my_money-500000)/500000*100,2), "% 입니다! 축하드립니다! ★")
            print("")
            print("========================================================")
        
        
#게임 설명 함수

def readGame():
    print("========================================================")
    print("")
    print("- 게임 시작시, 개인 기본 자본금 50만원이 주어집니다.")
    print("- 당해년도 주식 가격정보를 참고해 매수할 주식을 [번호]로 선택하여 매수합니다.")
    print("- 다음년도 주식 랜덤 힌트를 확인하고 기존 주식의 매도 여부를 선택합니다. [Y/N] ")
    print(" : 매도를 선택시[Y]보유 주식 전량 매도만 가능하며 매수할 때는 여러 종목을 매수 할 수 있습니다.")
    print("- 매수 또는 매도를 선택 할 때마다 한해의 주가 정보가 업데이트 됩니다.")
    print("- 2021년도 까지의 투자를 마치면 게임이 종료되고 최초 자본금 대비 최종 수익률 확인 및 [게임종료/새 게임을 시작] 할 수 있습니다.")
    print("")
    print("========================================================")
    
        
    
#시작화면


while True:
    print("===================== SMU 주식 게임 ====================")
    print("")

    print("1. 게임시작")
    print("2. 게임설명")
    print("3. 게임종료")
    print("")
    choice = int(input("▶ 원하시는 메뉴를 선택하세요 : "))

    if choice == 1:
        playGame()
    elif choice == 2:
        readGame()
    elif choice == 3:
        print("게임이 종료되었습니다. 감사합니다 :)")
        break
    else:
        print("잘못 입력하셨습니다")



    
    
