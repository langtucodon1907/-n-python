import pandas as pd
import tkinter as tk
from tkinter import ttk


# Đọc dữ liệu từ CSV
df = pd.read_csv('dataclean.csv')

# Lấy các giá trị duy nhất của City và Gender để hiển thị trong ComboBox
cities = df['City'].dropna().unique().tolist()
gender = df['Gender'].dropna().unique().tolist()

# Cửa sổ chính
win = tk.Tk()
win.title('Hồ sơ HCMUTE')
win.geometry('1410x700')

# Phần ô đầu cho hồ sơ tuyển sinh HCMUTE
frame1 = tk.Frame(win, bg='#3A5FCD')
frame1.pack(fill='x')
label1 = tk.Label(frame1, text='HỒ SƠ TUYỂN SINH', bg='#3A5FCD', fg='white', font=("Arial", 30)).pack(pady=30)

# Phần frame bên trái (menu)
frame2 = tk.Frame(win, width=300, bg='#1E90FF')
frame2.pack(side='left', fill='y')

# Phần bên phải để hiển thị nội dung
frame3 = tk.Frame(win, bg='#FFFFFF')
frame3.pack(side='right', fill='both', expand=True)

# Các button chính trong menu
buttonqdsts = tk.Button(frame2, text='Danh sách tuyển sinh', bg='#C6E2FF', command=lambda: show_list_page(0))
buttonqdsts.pack(pady=10, padx=20, fill='x')

buttonqlhs = tk.Button(frame2, text='Quản lí hồ sơ tuyển sinh', bg='#C6E2FF')
buttonqlhs.pack(pady=10, padx=20)

buttonbctk = tk.Button(frame2, text='Báo cáo và thống kê', bg='#C6E2FF')
buttonbctk.pack(pady=10, padx=20, fill='x')

buttonkqxt = tk.Button(frame2, text='Kết quả xét tuyển', bg='#C6E2FF')
buttonkqxt.pack(pady=10, padx=20, fill='x')

buttonlogout = tk.Button(frame2, text='Đăng xuất', bg='#C6E2FF', command=win.quit)
buttonlogout.place(x=20, y=500)

# Cài đặt phân trang
a = 10  # Số dòng mỗi trang
b = 0  # Trang hiện tại

# Hàm hiển thị danh sách tuyển sinh với phân trang
def show_list_page(page): 
    global b
    b = page
    c = page * a 
    d = c + a 
    page_data = df.iloc[c:d+1] 

    for widget in frame3.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame3, columns=('STT', 'Name', 'Age', 'Gender', 'Admission Test Score', 'High School Percentage', 'City', 'Admission Status'), show="headings")
    tree.place(x=10, y=80, width=1150, height=400)

    tree.heading('STT', text='STT')
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')
    tree.heading('Admission Test Score', text='Admission Test Score')
    tree.heading('High School Percentage', text='High School Percentage')
    tree.heading('City', text='City')
    tree.heading('Admission Status', text='Admission Status')

    tree.column('STT', width=50, anchor='center')
    tree.column('Name', width=150, anchor='center')
    tree.column('Age', width=80, anchor='center')
    tree.column('Gender', width=100, anchor='center')
    tree.column('Admission Test Score', width=150, anchor='center')
    tree.column('High School Percentage', width=150, anchor='center')
    tree.column('City', width=150, anchor='center')
    tree.column('Admission Status', width=150, anchor='center')

    for index, row in page_data.iterrows():
        tree.insert('', 'end', values=(index + 1, row['Name'], 
        row['Age'], row['Gender'], row['Admission Test Score'], 
        row['High School Percentage'], row['City'], row['Admission Status']))
    frame4 = tk.Frame(frame3)
    frame4.pack(fill='x', pady=10)
    if b > 0:
        trangtruoc = tk.Button(frame4, text='Trang trước', command=lambda: show_list_page(b - 1))
        trangtruoc.pack(side='left', padx=10)
    total_pages = (len(df) // a) + (1 if len(df) % a != 0 else 0)
    page_label = tk.Label(frame4, text=f"Trang {b + 1} / {total_pages}")
    page_label.pack(side='left', padx=10)
    if d < len(df):
        trangsau = tk.Button(frame4, text='Trang sau', command=lambda: show_list_page(b + 1))
        trangsau.pack(side='right', padx=10)

    nutthoat = tk.Button(frame3, text="Thoát")
    nutthoat.place(x=250, y=500)
win.mainloop()    