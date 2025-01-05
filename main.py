import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ CSV
df = pd.read_csv('dataclean')

# Lấy các giá trị duy nhất của City và Gender để hiển thị trong ComboBox
cities = df['City'].dropna().unique().tolist()
gender = df['Gender'].dropna().unique().tolist()

# Cửa sổ chính  
win = tk.Tk()
win.title('Hồ sơ HCMUTE')
win.geometry('1500x700')
win.resizable(False, False)

# Phần ô đầu cho hồ sơ tuyển sinh HCMUTE
frame1 = tk.Frame(win, bg='#104E8B')
frame1.pack(fill='x')
label1 = tk.Label(frame1, text='HỒ SƠ TUYỂN SINH', bg='#104E8B', fg='white', font=("Arial", 30)).pack(pady=30)

# Phần frame bên trái (menu)
frame2 = tk.Frame(win, width=300, bg='#104E8B')
frame2.pack(side='left', fill='y')

# Phần bên phải để hiển thị nội dung
frame3 = tk.Frame(win, bg='#F0FFFF')
frame3.pack(side='right', fill='both', expand=True)

# Các button chính trong menu
buttonqdsts = tk.Button(frame2, text='Danh sách tuyển sinh', bg='#4682B4',  fg='white',font=("Arial", 14), command=lambda: show_list_page(0))
buttonqdsts.pack(pady=10, padx=20, fill='x')

buttonqlhs = tk.Button(frame2, text='Quản lí hồ sơ tuyển sinh',  bg='#4682B4',  fg='white',font=("Arial", 14), command=lambda: anvao())
buttonqlhs.pack(pady=10, padx=20)

buttonbctk = tk.Button(frame2, text='Báo cáo và thống kê',  bg='#4682B4',  fg='white',font=("Arial", 14),command=lambda: bctk())
buttonbctk.pack(pady=10, padx=20, fill='x')

buttonkqxt = tk.Button(frame2, text='Kết quả xét tuyển', bg='#4682B4',  fg='white',font=("Arial", 14),command=lambda: kqxt())
buttonkqxt.pack(pady=10, padx=20, fill='x')

buttonlogout = tk.Button(frame2, text='Đăng xuất', bg='#4682B4',  fg='white',font=("Arial", 14), command=win.quit)
buttonlogout.place(x=20, y=500)
# Cài đặt phân trang
a = 10  # Số dòng mỗi trang
b = 0  # Trang hiện tại

# Hàm hiển thị danh sách tuyển sinh với phân trang
def show_list_page(page): 
    global b
    b = page
    c = page * a #STT dòng đầu tiên
    d = c + a    #STT dòng cuối cùng
    page_data = df.iloc[c:d] 

    for widget in frame3.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame3, columns=('STT', 'Name', 'Age', 'Gender'
                                         , 'Admission Test Score', 'High School Percentage'
                                         , 'City', 'Admission Status'), show="headings")
    tree.place(x=10, y=80, width=1200, height=400)
#Đặt tiêu đề cho các cột
    tree.heading('STT', text='STT')
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')
    tree.heading('Admission Test Score', text='Admission Test Score')
    tree.heading('High School Percentage', text='High School Percentage')
    tree.heading('City', text='City')
    tree.heading('Admission Status', text='Admission Status')
#Dặt độ rộng cho các cột
    tree.column('STT', width=50, anchor='center')
    tree.column('Name', width=150, anchor='center')
    tree.column('Age', width=80, anchor='center')
    tree.column('Gender', width=100, anchor='center')
    tree.column('Admission Test Score', width=150, anchor='center')
    tree.column('High School Percentage', width=150, anchor='center')
    tree.column('City', width=150, anchor='center')
    tree.column('Admission Status', width=150, anchor='center')

    for index, row in page_data.iterrows():
        tree.insert('', 'end', values=( index + 1,row['Name'], 
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

    nutthoat = tk.Button(frame3, text="Thoát", command=hide_content)
    nutthoat.place(x=50, y=500)

def anvao():
    global combo1, combo2  
    #Khi khai báo biến global thì nghĩa rằng các biến này không phải là các biến cục bộ trong hàm anvao, 
    #mà là các biến toàn cục, có thể được sử dụng ở bất kỳ đâu trong mã của bạn (trong phạm vi toàn bộ chương trình).
    for widget in frame3.winfo_children():
        widget.destroy()

    combo1 = ttk.Combobox(frame3)
    combo1['values'] = cities
    #Nếu muốn hiển thị giá trị có sắn thì dùng current()
    combo1.place(x=130, y=10)
    #Nếu muốn hiển thị giá trị có sắn thì dùng current()
    combo2 = ttk.Combobox(frame3)
    combo2['values'] = gender
    
    combo2.place(x=420, y=10)

    labelcity = tk.Label(frame3, text="Chọn thành phố:")
    labelcity.place(x=20, y=10)

    labelgender = tk.Label(frame3, text="Chọn giới tính:")
    labelgender.place(x=320, y=10)

    tree = ttk.Treeview(frame3, columns=('STT', 'Name', 'Age', 'Gender', 'Admission Test Score', 'High School Percentage', 'City', 'Admission Status'), show="headings")
    tree.place(x=50, y=80, width=1150, height=400)

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

    def datacombobox(): 
        laycity = combo1.get()
        laygender = combo2.get()
        locdata = df[(df['City'] == laycity) & (df['Gender'] == laygender)]

        for item in tree.get_children():
            tree.delete(item)

        if not locdata.empty:
            locdata.insert(0, 'STT', range(1, len(locdata) + 1))

            for _, row in locdata.iterrows():
                tree.insert('', 'end', values=(row['STT'], row['Name'], 
                                               row['Age'], row['Gender'], 
                                               row['Admission Test Score'], row['High School Percentage'], 
                                               row['City'], row['Admission Status']))
        else:
            messagebox.showwarning("Lỗi!!!", "Không có dữ liệu nào được tìm thấy trong file csv")

    btn = tk.Button(frame3, text="Tìm kiếm", command=datacombobox)
    btn.place(x=600, y=10)

    buttonthem = tk.Button(frame3, text="Thêm", command=lambda: show_tkinter_new())
    buttonthem.place(x=20, y=50)

    buttonxem = tk.Button(frame3, text="Xóa", command=lambda: delete_selected_row(tree))
    buttonxem.place(x=100, y=50)

    buttonxep = tk.Button(frame3, text="Sắp xếp tuổi", command=lambda: sort_by_age(tree))
    buttonxep.place(x=160, y=50)

    buttonthoat = tk.Button(frame3, text="Thoát", command=hide_content)
    buttonthoat.place(x=250, y=50)



# Hàm xóa 1 hay nhiều dòng trong Treeview
def delete_selected_row(tree):
    selected_items = tree.selection()  # Lấy tất cả các dòng được chọn
    if selected_items:
        for item in selected_items:
            tree.delete(item)  # Xóa từng dòng
    else:
        messagebox.showwarning("Chưa chọn dòng", "Vui lòng chọn ít nhất một dòng cần xóa.")
def show_tkinter_new():
    tkinternew = tk.Toplevel(win)#là một lớp trong Tkinter,
    #được dùng để tạo một cửa sổ mới (cửa sổ con) có thể hoạt động độc lập với cửa sổ chính.
    tkinternew.title("Thêm Hồ Sơ Mới")
    tkinternew.geometry("400x400")

    # Các Label và Entry để nhập thông tin
    tk.Label(tkinternew, text="Name:",bg="#CCFFFF").place(x=20, y=20)
    entry_name = tk.Entry(tkinternew)
    entry_name.place(x=160, y=20)

    tk.Label(tkinternew, text="Age:",bg="#CCFFFF").place(x=20, y=60)
    entry_age = tk.Entry(tkinternew)
    entry_age.place(x=160, y=60)

    tk.Label(tkinternew, text="Gender:",bg="#CCFFFF").place(x=20, y=100)
    entry_gender = ttk.Combobox(tkinternew, values=gender)
    entry_gender.place(x=160, y=100)

    tk.Label(tkinternew, text="Admission Test Score:",bg="#CCFFFF").place(x=20, y=140)
    entry_admission_test_score = tk.Entry(tkinternew)
    entry_admission_test_score.place(x=160, y=140)

    tk.Label(tkinternew, text="High School Percentage:",bg="#CCFFFF").place(x=20, y=180)
    entry_high_school_percentage = tk.Entry(tkinternew)
    entry_high_school_percentage.place(x=160, y=180)

    tk.Label(tkinternew, text="City:",bg="#CCFFFF").place(x=20, y=220)
    entry_city = ttk.Combobox(tkinternew, values=cities)
    entry_city.place(x=160, y=220)

    tk.Label(tkinternew, text="Admission Status:",bg="#CCFFFF").place(x=20, y=260)
    entry_admission_status = tk.Entry(tkinternew)
    entry_admission_status.place(x=160, y=260)
    # Hàm lưu để thêm dữ liệu 
    def save():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get()
        admission_test_score = entry_admission_test_score.get()
        high_school_percentage = entry_high_school_percentage.get()
        city = entry_city.get()
        admission_status = entry_admission_status.get()

        # Kiểm tra xem người dùng đã nhập đủ thông tin chưa
        if not all([name, age, gender, admission_test_score, high_school_percentage, city, admission_status]):
            messagebox.showwarning("Nhập thiếu thông tin", "Vui lòng điền đầy đủ các thông tin.")
            return

        # Thêm dữ liệu vào DataFrame
        global df
        dfnew = pd.DataFrame([[name, age, gender, admission_test_score, high_school_percentage,
                                city, admission_status]],
                                columns=df.columns)
        df = pd.concat([df, dfnew], ignore_index=True)#Đây là phương thức của Pandas dùng để nối
        #(concat) hai hoặc nhiều DataFrame lại với nhau.

        # Cập nhật Treeview
        show_list_page(b)
        tkinternew.destroy()

    # Nút Lưu
    save_button = tk.Button(tkinternew, text="Lưu", command=save)
    save_button.place(x=160, y=300)

#Phần của Khoa Lại 
def sort_by_age(tree):
    # Truy cập combo1 và combo2 như biến toàn cục
    laycity = combo1.get()
    laygender = combo2.get()
    locdata = df[(df['City'] == laycity) & (df['Gender'] == laygender)]

    if not locdata.empty:
        # Sắp xếp theo tuổi (Age)
        locdata = locdata.sort_values(by='Age', ascending=True)

        # Xóa các dòng cũ trong Treeview
        for item in tree.get_children():
            tree.delete(item)

        locdata.insert(0, 'STT', range(1, len(locdata) + 1))

        # Thêm lại dữ liệu đã sắp xếp vào Treeview
        for _, row in locdata.iterrows():
            tree.insert('', 'end', values=(row['STT'], row['Name'], 
                                           row['Age'], row['Gender'], 
                                           row['Admission Test Score'], row['High School Percentage'], 
                                           row['City'], row['Admission Status']))
    else:
        messagebox.showwarning("Không có dữ liệu", "Không có dữ liệu thỏa mãn yêu cầu để sắp xếp.")    
    
#Biểu đồ mối quan hệ giữa thành phố và tình trạng nhập học
def bieudo1(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='City', hue='Admission Status', data=df)
    plt.title('Tình trạng tuyển sinh theo thành phố')
    plt.xlabel('thành phố')
    plt.ylabel('giá trị')
    plt.xticks(rotation=45, ha='right')
    plt.show()
#Biểu đồ tỷ lệ nhập học theo thành phố và giới tính
def bieudo2(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='City', hue='Gender', data=df, palette='Set2')
    plt.title('Tình trạng nhập học theo thành phố và giới tính')
    plt.xlabel('thành phố ')
    plt.ylabel('giá trị ')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Gender')
    plt.show()
# biểu đồ phân bố điểm thi nhập học
def bieudo3(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Admission Test Score'], bins=20, kde=True, color='blue')
    plt.title('Phân bố điểm thi nhập học')
    plt.xlabel('Điểm thi nhập học')
    plt.ylabel('Tần suất')
    plt.show()
#biểu đồ phân phối thành phố
def bieudo4(df):
    plt.figure(figsize=(7, 7))
    city_counts = df['City'].value_counts()
    city_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
    plt.title('Phân Bố Tuyển Sinh Theo Thành Phố ')
    plt.ylabel('')
    plt.show()

# biểu đồ tỉ lệ nhập học theo giới tính
def bieudo5(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gender', hue='Admission Status', data=df)
    plt.title('Tình trạng tuyển sinh theo giới tính')
    plt.xlabel('Giới tính')
    plt.ylabel('giá trị')
    plt.show()
# biểu đồ Xác định ngưỡng điểm nhập học
def bieudo6(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Admission Test Score'], kde=True, color='green')
    plt.axvline(df['Admission Test Score'].median(), color='red', linestyle='dashed', linewidth=2, label='Median')
    plt.axvline(df['Admission Test Score'].mean(), color='blue', linestyle='dashed', linewidth=2, label='Mean')
    plt.title('Phân bố điểm thi tuyển sinh theo ngưỡng')
    plt.xlabel('Điểm thi tuyển sinh')
    plt.ylabel('')
    plt.legend()
    plt.show()
     
# biểu đồ Phát hiện sự bất thường (Boxplot giữa điểm thi và tình trạng nhập học)
def bieudo7(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Admission Status', y='Admission Test Score', data=df)
    plt.title('Điểm thi tuyển sinh theo tình trạng tuyển sinh')
    plt.xlabel('Tình trạng nhập học')
    plt.ylabel('Admission Test Score')
    plt.show()     


def bctk():
    for widget in frame3.winfo_children():
        widget.destroy()

    buttonbieudo1 = tk.Button(frame3, text="Biểu đồ mối quan hệ giữa thành phố và tình trạng nhập học", width=45, command=lambda: bieudo1(df))
    buttonbieudo1.place(x=10, y=10)

    buttonbieudo2 = tk.Button(frame3, text="Biểu đồ tỷ lệ nhập học theo thành phố và giới tính", width=45, command=lambda: bieudo2(df))
    buttonbieudo2.place(x=10, y=60)

    buttonbieudo3 = tk.Button(frame3, text="Biểu đồ phân bố điểm thi nhập học", width=45, command=lambda: bieudo3(df))
    buttonbieudo3.place(x=10, y=110)

    buttonbieudo4 = tk.Button(frame3, text="Biểu đồ phân phối thành phố", width=45, command=lambda: bieudo4(df))
    buttonbieudo4.place(x=10, y=160)
    
    buttonbieudo5 = tk.Button(frame3, text="Biểu đồ tỉ lệ nhập học theo giới tính", width=45, command=lambda: bieudo5(df))
    buttonbieudo5.place(x=10, y=210)

    buttonbieudo6 = tk.Button(frame3, text="Biểu đồ Xác định ngưỡng điểm nhập học", width=45, command=lambda: bieudo6(df))
    buttonbieudo6.place(x=10, y=260)

    buttonbieudo7 = tk.Button(frame3, text="biểu đồ Phát hiện sự bất thường ", width=45, command=lambda: bieudo7(df))
    buttonbieudo7.place(x=10, y=310)

    buttonthoat = tk.Button(frame3, text="Thoát ", command=hide_content)
    buttonthoat.place(x=10, y=500)

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
        return

    # Tìm kiếm dữ liệu trong dataframe
    result = df[(
        df['Name'].str.lower() == name.lower()) &
        (df['Age'] == age) &
        (df['Gender'].str.lower() == gender.lower()) &
        (df['City'].str.lower() == city.lower())
    ]
    
    # Nếu không tìm thấy thí sinh
    if result.empty:
        messagebox.showwarning("Lỗi!!!!", "Không tìm thấy thông tin thí sinh")
    else:
        # Nếu tìm thấy thí sinh, lấy kết quả xét tuyển
        admission_status = result['Admission Status'].values[0]
        
        # Hiển thị kết quả xét tuyển trong Label
        display_result(admission_status)

def display_result(admission_status):
    # Hiển thị kết quả xét tuyển
    label_result = tk.Label(frame3, text=f"Kết quả xét tuyển của thí sinh là: {admission_status}", bg='#CCFFFF', font=("Arial", 16))
    label_result.place(x=20, y=200)

# Hàm ẩn nội dung trong (khi nhấn "Thoát")
def hide_content():
    for widget in frame3.winfo_children():
        widget.destroy()


win.mainloop()