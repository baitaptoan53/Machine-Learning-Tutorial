import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.metrics import confusion_matrix
import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox
from tkinter import Spinbox
import plotly.express as px
data = pd.read_csv(
    "./heart_failure_clinical_records_dataset.csv", encoding='latin1')

x = data.values[:, 0:data.shape[1] - 1]
y = data.values[:, data.shape[1] - 1]

# print('Ma trận x = \n', x)
# print('Ma trận y = \n', y)
# chia du lieu thanh 2 phan train va test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.7, test_size=0.3, random_state=0)


def thong_ke_tap_tin():
    data.info()


def show_ti_le_nguoi_tu_vong_tu_tung_do_tuoi():
    fig = px.histogram(data, x="age", color="DEATH_EVENT", marginal="violin",
                       hover_data=data.columns, width=800, height=500, template="plotly_dark")
    fig.show()


def show_cart():
    # Ap dụng thuật toán CART
    clf = DecisionTreeClassifier(
        criterion='gini', random_state=0)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    # print('y_pred = ', y_pred)
    # print('y_test = ', y_test)
    # print('Độ chính xác thuật toán CART= ', clf.score(x_test, y_test)*100, '%')
    # ve cay cart
    plt.figure(figsize=(20, 20))
    tree.plot_tree(clf, filled=True)
    plt.show()
    # confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    # giải  thích ma trận nhầm lẫn
    # hàng thứ nhất là số lượng người sống dự đoán đúng
    # hàng thứ hai là số lượng người chết dự đoán đúng
    # cột thứ nhất là số lượng người sống thực tế
    # cột thứ hai là số lượng người chết thực tế

    # hien thi thong tin tren form
    lbl1 = Label(window, text="Độ chính xác thuật toán CART = ",
                 font=("Arial Bold", 10))
    lbl1.grid(column=0, row=1)
    lbl2 = Label(window, text=clf.score(x_test, y_test)
                 * 100, font=("Arial Bold", 10))
    lbl2.grid(column=1, row=1)
    lb_confusion_matrix = Label(
        window, text="Ma trận nhầm lẫn CART = ", font=("Arial Bold", 10))
    lb_confusion_matrix.grid(column=0, row=2)
    lb_confusion_matrix = Label(window, text=cm, font=("Arial Bold", 10))
    lb_confusion_matrix.grid(column=1, row=2)


# khoi tao bien de luu du lieu nhap vao
age = 0
anaemia = 0
creatinine_phosphokinase = 0
diabetes = 0
ejection_fraction = 0
high_blood_pressure = 0
platelets = 0
serum_creatinine = 0
serum_sodium = 0
sex = 0
smoking = 0
time = 0


def predict_id3():
    # nhap vao 12 thong tin
    lbl1 = Label(window, text="Nhập độ tuổi", font=("Arial Bold", 10))
    lbl1.grid(column=0, row=6)
    txt1 = Entry(window, width=10)
    txt1.grid(column=1, row=6)
    lbl2 = Label(window, text="Nhập anaemia", font=("Arial Bold", 10))
    lbl2.grid(column=0, row=7)
    txt2 = Entry(window, width=10)
    txt2.grid(column=1, row=7)
    lbl3 = Label(window, text="Nhập creatinine_phosphokinase",
                 font=("Arial Bold", 10))
    lbl3.grid(column=0, row=8)
    txt3 = Entry(window, width=10)
    txt3.grid(column=1, row=8)
    lbl4 = Label(window, text="Nhập diabetes", font=("Arial Bold", 10))
    lbl4.grid(column=0, row=9)
    txt4 = Entry(window, width=10)
    txt4.grid(column=1, row=9)
    lbl5 = Label(window, text="Nhập ejection_fraction",
                 font=("Arial Bold", 10))
    lbl5.grid(column=0, row=10)
    txt5 = Entry(window, width=10)
    txt5.grid(column=1, row=10)
    lbl6 = Label(window, text="Nhập high_blood_pressure",
                 font=("Arial Bold", 10))
    lbl6.grid(column=0, row=11)
    txt6 = Entry(window, width=10)
    txt6.grid(column=1, row=11)
    lbl7 = Label(window, text="Nhập platelets", font=("Arial Bold", 10))
    lbl7.grid(column=0, row=12)
    txt7 = Entry(window, width=10)
    txt7.grid(column=1, row=12)
    lbl8 = Label(window, text="Nhập serum_creatinine",
                 font=("Arial Bold", 10))
    lbl8.grid(column=0, row=13)
    txt8 = Entry(window, width=10)
    txt8.grid(column=1, row=13)
    lbl9 = Label(window, text="Nhập serum_sodium", font=("Arial Bold", 10))
    lbl9.grid(column=0, row=14)
    txt9 = Entry(window, width=10)
    txt9.grid(column=1, row=14)
    lbl10 = Label(window, text="Nhập sex", font=("Arial Bold", 10))
    lbl10.grid(column=0, row=15)
    txt10 = Entry(window, width=10)
    txt10.grid(column=1, row=15)
    lbl11 = Label(window, text="Nhập smoking", font=("Arial Bold", 10))
    lbl11.grid(column=0, row=16)
    txt11 = Entry(window, width=10)
    txt11.grid(column=1, row=16)
    lbl12 = Label(window, text="Nhập time", font=("Arial Bold", 10))
    lbl12.grid(column=0, row=17)
    txt12 = Entry(window, width=10)
    txt12.grid(column=1, row=17)

    def ket_qua():
        # kiem tra input da du 12 thong tin chua
        if txt1.get() != "" or txt2.get() != "" or txt3.get() != "" or txt4.get() != "" or txt5.get() != "" or txt6.get() != "" or txt7.get() != "" or txt8.get() != "" or txt9.get() != "" or txt10.get() != "" or txt11.get() != "" or txt12.get() != "":
            age = int(txt1.get())
            anaemia = int(txt2.get())
            creatinine_phosphokinase = int(txt3.get())
            diabetes = int(txt4.get())
            ejection_fraction = int(txt5.get())
            high_blood_pressure = int(txt6.get())
            platelets = int(txt7.get())
            serum_creatinine = float(txt8.get())
            serum_sodium = int(txt9.get())
            sex = int(txt10.get())
            smoking = int(txt11.get())
            time = int(txt12.get())
            # Ap dụng thuật toán ID3
            clf = DecisionTreeClassifier(
                criterion='entropy', random_state=0)
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            du_doan = clf.predict(np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                                             high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]]))[0]
            # show ket qua du doan
            lbl3 = Label(window, text="Kết quả dự đoán = ",
                         font=("Arial Bold", 10))
            lbl3.grid(column=0, row=19)
            lbl4 = Label(window, text=du_doan, font=("Arial Bold", 10))
            lbl4.grid(column=1, row=19)
    btn5 = Button(window, text="Kết quả", command=ket_qua)
    btn5.grid(column=1, row=18)

# viet ham ket qua lay gia tri tu input nguoi dung nhap vao


def show_id3():
    # Ap dụng thuật toán ID3
    clf = DecisionTreeClassifier(
        criterion='entropy', random_state=0)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    # print('y_pred = ', y_pred)
    # print('y_test = ', y_test)
    # ve cay id3
    plt.figure(figsize=(20, 20))
    tree.plot_tree(clf, filled=True)
    plt.show()
    # ma tran nham lan
    cm = confusion_matrix(y_test, y_pred)

    # hien thi thong tin tren form
    lbl1 = Label(window, text="Độ chính xác thuật toán ID3 = ",
                 font=("Arial Bold", 10))
    lbl1.grid(column=0, row=0)
    lbl2 = Label(window, text=clf.score(x_test, y_test)
                 * 100, font=("Arial Bold", 10))
    lbl2.grid(column=1, row=0)
    lbl3 = Label(window, text="Ma trận nhầm lẫn ID3 = ",
                 font=("Arial Bold", 10))
    lbl3.grid(column=0, row=3)
    lbl4 = Label(window, text=cm, font=("Arial Bold", 10))
    lbl4.grid(column=1, row=3)


# tao form
window = tk.Tk()
window.title("NHÓM 7 - 62TH - BÀI TẬP LỚN")
window.geometry('500x500')

btn = Button(window, text="Kết quả thuật toán CART", command=show_cart)
btn.grid(column=0, row=2)

btn1 = Button(window, text="Kết quả thuật toán ID3", command=show_id3)
btn1.grid(column=0, row=3)
btn2 = Button(window, text="Thống kê tập tin tại TERMAINAL",
              command=thong_ke_tap_tin)
btn2.grid(column=0, row=4)
btn3 = Button(window, text="Tỉ lệ người từ vong từ từng độ tuổi",
              command=show_ti_le_nguoi_tu_vong_tu_tung_do_tuoi)
btn3.grid(column=0, row=5)
btn4 = Button(window, text="Dự đoán người đó có bị tử vong không",
              command=predict_id3)
btn4.grid(column=0, row=18)
window.mainloop()