import APIModule as api
from tkinter import *


while True:
    print("""
---------------------------------------------------------------------------------------------------------------------------------------------------------------
환영합니다. 영화정보 검색 서비스입니다.
    1. 현재 상영작 검색
    2. 제목으로 영화정보 검색하기
    3. 프로그램 종료
---------------------------------------------------------------------------------------------------------------------------------------------------------------

          """)
    service = input("원하는 서비스는 ? : ")
    # 1번일땐 현재 상영작들 검색
    if service == "1":
        api.getListFamous()

    # 2번일땐
    elif service == "2":
        movieName = input("검색하고싶은 영화 제목을 입력하세요 : ")
        api.getMovieDetailByName(movieName)

    # 그 외에는 종료
    else:
        print("프로그램을 종료합니다.")
        break
