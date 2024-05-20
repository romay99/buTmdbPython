import requests
import textwrap
import APIKey

apiToken = APIKey.key  # API 키 값
header = {"Authorization": apiToken}  # API 키를 Http header 에 설정한다.


def getListFamous():  # 현재 상영작 리스트
    url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1&region=KR"
    response = requests.get(url, headers=header).json()
    movieList = []
    for movie in response['results']:
        title = movie['title']
        releaseDate = movie['release_date']
        originalLanguage = movie['original_language']
        movieList.append((title, releaseDate, originalLanguage))
        print(f"제목: {title}, 개봉일: {releaseDate} , 개봉 국가 : {originalLanguage}")
    return movieList


def getMovieDetailByName(movieName):  # 영화 제목으로 영화정보 검색
    url = "https://api.themoviedb.org/3/search/movie?query=" + \
        movieName+"&include_adult=false&language=ko-KR&page=1"
    response = requests.get(url, headers=header).json()

    if len(response['results']) == 0:  # 검색결과가 존재하지 않는다면 함수 종료
        print("잘못된 입력입니다. 영화제목을 다시한번 확인해주세요 ")
        return ""

    moviesList = []
    for index, movie in enumerate(response['results']):
        title = movie['title']
        releaseDate = movie['release_date']
        originalLanguage = movie['original_language']
        print(f"( {index + 1} ) 제목: {title}, {releaseDate} , {originalLanguage}")
        moviesList.append(movie['id'])
    findNum = int(input("찾으시는 영화가 몇번 영화에요? : "))
    # MovieId 값으로 영화 상세정보 하기
    getMovieDetailByMovieId(str(moviesList[findNum-1]))


def getMovieDetailByMovieId(movieId):  # 영화 ID 값으로 영화정보 검색
    url = "https://api.themoviedb.org/3/movie/" + movieId + "?language=ko-KR"
    response = requests.get(url, headers=header).json()
    movieName = response["title"]
    movieOverview = response["overview"]
    if len(movieOverview) == 0:
        movieOverview = "줄거리가 존재하지 않습니다."

    movieOverviewWrap = textwrap.fill(movieOverview, width=60)
    movieReleaseDate = response["release_date"]
    movieRunTime = response["runtime"]
    print(f"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
 영화 제목 : {movieName} || 개봉일 : {movieReleaseDate} ||  상영시간 : {movieRunTime} min
------------------------------------------------------------------------------------------------------------------------------------------------------------------

  {movieOverviewWrap}

          """)
