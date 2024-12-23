import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

frame3 = tk.Frame(win, bg='#FFFFFF')
frame3.pack(side='right', fill='both', expand=True)

def kqxt():
    for widget in frame3.winfo_children():
        widget.destroy()


    labelten = tk.Label(frame3, text='Name:', bg='#FFFFFF')
    labelten.place(x=20, y=10)
    
    entryten = tk.Entry(frame3, bg='#CCFFFF')
    entryten.place(x=160, y=10)

    labeltuoi = tk.Label(frame3, text='Age:', bg='#FFFFFF')
    labeltuoi.place(x=20, y=40)

    entrytuoi = tk.Entry(frame3, bg='#CCFFFF')
    entrytuoi.place(x=160, y=40)

    labelgender = tk.Label(frame3, text='Gender:', bg='#FFFFFF')
    labelgender.place(x=20, y=70)

    entrygender = tk.Entry(frame3, bg='#CCFFFF')
    entrygender.place(x=160, y=70)

    labelcity = tk.Label(frame3, text='City:', bg='#FFFFFF')
    labelcity.place(x=20, y=100)

    entrycity = tk.Entry(frame3, bg='#CCFFFF')
    entrycity.place(x=160, y=100)

    labelthpt = tk.Label(frame3, text='Admission Test Score:', bg='#FFFFFF')
    labelthpt.place(x=20, y=130)

    entrythpt = tk.Entry(frame3, bg='#CCFFFF')
    entrythpt.place(x=160, y=130)

    labeldh = tk.Label(frame3, text='High School Percentage:', bg='#FFFFFF')
    labeldh.place(x=20, y=160)

    entrydh = tk.Entry(frame3, bg='#CCFFFF')
    entrydh.place(x=160, y=160)

    buttonthoat = tk.Button(frame3, text="Thoát ", command=hide_content)
    buttonthoat.place(x=10, y=500)

    # Nút Tra cứu
    buttontk = tk.Button(frame3, text="Tra cứu", bg='#CCFFFF', command=lambda: show_result(entryten.get(), entrytuoi.get(), entrygender.get(), entrythpt.get(), entrydh.get(), entrycity.get()))
    buttontk.place(x=300, y=160)

    # Khung hiển thị kết quả
    frame5 = tk.Frame(frame3, bg='#CCFFFF')
    frame5.place(x=10, y=200, width=1150, height=200)
    
def show_result(name, age, gender, admission_test_score, high_school_percentage, city):
    # Kiểm tra nếu có trường nào bị thiếu thông tin
    if not name or not age or not gender or not admission_test_score or not high_school_percentage or not city:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin")
        return

    try:
        # Kiểm tra và chuyển đổi dữ liệu
        age = int(float(age))  # Chuyển đổi tuổi sang int từ float nếu cần
        admission_test_score = float(admission_test_score)  # Điểm có thể là float
        high_school_percentage = float(high_school_percentage)  # Tỷ lệ tốt nghiệp có thể là float
    except ValueError:
        # Nếu có lỗi khi chuyển đổi dữ liệu
        messagebox.showwarning("Lỗi!!!!", "Nhập sai kiểu dữ liệu")
        display_result(admission_status)
        return

    # Tìm kiếm dữ liệu trong dataframe
    result = df[
        (df['Name'].str.lower() == name.lower()) &
        (df['Age'] == age) &
        (df['Gender'].str.lower() == gender.lower()) &
        (df['City'].str.lower() == city.lower())
    ]
    
    # Kiểm tra kết quả tìm thấy
    if result.empty:
    # Nếu DataFrame rỗng (không có dữ liệu), hiển thị thông báo không tìm thấy
        messagebox.showwarning("Lỗi!!!!", "Không tìm thấy thông tin thí sinh")
    else:
    # Nếu DataFrame không rỗng (có dữ liệu), lấy giá trị 'Admission Status'
        admission_status = result['Admission Status'].values[0]
    
    # Hiển thị kết quả trong frame3
    display_result(admission_status)

def display_result(admission_status):
    # Hiển thị kết quả xét tuyển
    label_result = tk.Label(frame3, text=f"Kết quả xét tuyển của thí sinh là: {admission_status}", bg='#CCFFFF', font=("Arial", 16))
    label_result.place(x=20, y=200)

# Hàm ẩn nội dung trong (khi nhấn "Thoát")
def hide_content():
    for widget in frame3.winfo_children():
        widget.destroy()

