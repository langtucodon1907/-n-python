def datacombobox(): 
        laycity = combo1.get()
        laygender = combo2.get()
        locdata = df[(df['City'] == laycity) & (df['Gender'] == laygender)]

        for item in tree.get_children():
            tree.delete(item)

        if not locdata.empty:
            locdata.insert(0, 'STT', range(1, len(locdata) + 1))

            for _, row in locdata.iterrows():
                tree.insert('', 'end', values=(row['STT'], row['Name'], row['Age'], row['Gender'], row['Admission Test Score'], row['High School Percentage'], row['City'], row['Admission Status']))
        else:
            tree.insert('', 'end', values=("Không có dữ liệu thỏa mãn yêu cầu!",) * 8)

    btn = tk.Button(frame3, text="Tìm kiếm", command=datacombobox)
    btn.place(x=600, y=10)

    buttonthem = tk.Button(frame3, text="Thêm", command=lambda: show_tkinter_new())
    buttonthem.place(x=20, y=50)

    buttonxem = tk.Button(frame3, text="Xóa", command=lambda: delete_selected_row(tree))
    buttonxem.place(x=100, y=50)

    buttonxep = tk.Button(frame3, text="Cập nhật")
    buttonxep.place(x=160, y=50)

    buttonthoat = tk.Button(frame3, text="Thoát", command=hide_content)
    buttonthoat.place(x=250, y=50)
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
    def save_data():
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
        dfnew = pd.DataFrame([[name, age, gender, admission_test_score, high_school_percentage, city, admission_status]],
                                columns=df.columns)
        df = pd.concat([df, dfnew], ignore_index=True)#Đây là phương thức của Pandas dùng để nối
        #(concat) hai hoặc nhiều DataFrame lại với nhau.

        # Cập nhật Treeview
        show_list_page(b)
        tkinternew.destroy()

    # Nút Lưu
    save_button = tk.Button(tkinternew, text="Lưu", command=save_data)
    save_button.place(x=160, y=300)

# Hàm xóa dòng trong Treeview
def delete_selected_row(tree):
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Chưa chọn dòng", "Vui lòng chọn dòng cần xóa.")
    