import tkinter as tk
from tkinter import *
import APIModule as api


def open_new_window():
    new_window = Toplevel(root)
    new_window.title("현재 상영작 정보")
    new_window.geometry("400x300")
    tk.Label(new_window, text="현재 상영작 정보입니다.").pack(padx=10, pady=10)

    # 새 창에 버튼 추가
    closeButton = tk.Button(new_window, text="닫기", command=new_window.destroy)
    getMovieListButton = tk.Button(
        new_window, text="영화정보 불러오기", command=getMovieList(new_window))
    closeButton.pack(pady=20)
    getMovieListButton.pack(pady=20)


def getMovieList(new_window):
    movieList = api.getListFamous()
    listbox = tk.Listbox(new_window, height=10, width=40)
    for item in movieList:
        result = str(item[0]) + "," + item[1] + "," + item[2]
        listbox.insert(tk.END, result)
    listbox.pack()
    listbox.bind(listbox.bind(
        "<Double-1>", lambda event: selectMovie(event, new_window)))


def getMovieListbyName(new_window, moviename):
    movieList = api.getMovieDetailByName(moviename)
    listbox = tk.Listbox(new_window, height=10, width=60)
    for item in movieList:
        result = str(item[0]) + "," + item[1] + "," + item[2]
        listbox.insert(tk.END, result)
    listbox.pack()
    listbox.bind(listbox.bind(
        "<Double-1>", lambda event: selectMovie(event, new_window)))


def selectMovie(event, new_window):
    movieDetailText.delete(1.0, tk.END)
    global date
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        movieId = data.split(",")[0]
        response = api.getMovieDetailByMovieId(movieId)
        movieDetailText.insert(tk.END, response["줄거리"])
        date = response["개봉일"]
    new_window.destroy()


def open_new_window2():
    new_window = Toplevel(root)
    new_window.title("제목으로 검색하기")
    new_window.geometry("800x600")
    movie_Name = movieName.get("1.0", "end-1c")
    getMovieListbyName(new_window, movie_Name)


# 메인화면 root
root = tk.Tk()
root.title("영화 정보 검색 프로그램")
root.geometry("800x600")

button1 = tk.Button(root, text="현재 상영작 조회하기", command=open_new_window)
button1.grid(row=1, column=2, pady=10)

movieName = tk.Text(height=1, width=20)
movieName.grid(row=2, column=2, padx=10)
button2 = tk.Button(root, text="영화 제목으로 정보검색",
                    command=lambda: open_new_window2())
button2.grid(row=2, column=4)

movieDetailText = tk.Text(height=20, width=70, spacing2=10, spacing3=10)
movieDetailText.grid(row=3, column=2)

closeButton = tk.Button(text="닫기", command=quit)
closeButton.grid(row=10, column=8, pady=10)

# Run the main loop
root.mainloop()
