import tkinter as tk
from tkinter import Toplevel
import APIModule as api


def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Window1")
    new_window.geometry("400x300")
    tk.Label(new_window, text="This is a new window").pack(padx=10, pady=10)

    # 새 창에 버튼 추가
    closeButton = tk.Button(
        new_window, text="닫기", command=new_window.destroy)
    getMovieListButton = tk.Button(
        new_window, text="영화정보 불러오기", command=getMovieList(new_window))
    closeButton.pack(pady=20)
    getMovieListButton.pack(pady=20)


def getMovieList(new_window):
    movieList = api.getListFamous()
    listbox = tk.Listbox(new_window, height=10, width=40)
    for item in movieList:
        listbox.insert(tk.END, item[0])
    listbox.pack()


def open_new_window2():
    new_window2 = Toplevel(root)
    new_window2.title("New Window2")
    new_window2.geometry("400x300")
    tk.Label(new_window2, text="This is a new window").pack(padx=10, pady=10)


# Main window
root = tk.Tk()
root.title("영화 정보 검색 프로그램")
root.geometry("800x600")

# Create buttons
button1 = tk.Button(root, text="현재 상영작 조회하기", command=open_new_window)
button1.pack(pady=20)

button2 = tk.Button(root, text="영화 제목으로 정보검색", command=open_new_window2)
button2.pack(pady=20)

# Run the main loop
root.mainloop()
