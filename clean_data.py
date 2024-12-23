import pandas as pd
import numpy as np

#Đọc dữ liệu từ file 'student_admission_record_dirty.csv'
df=pd.read_csv('student_admission_record_dirty.csv')
print(df.isnull().sum() )

#Loại bỏ tất cả các bản ghi(rows) trùng lặp trong bản Dataframe.
#Nếu có các dòng dữ liệu giống hệt nhau, chỉ giữ lại 1 dòng và xoá những dòng còn lại.
df=df.drop_duplicates()

# Thay thế các giá trị trống của cột Name thành 'Không rõ'
df['Name']=df['Name'].fillna('Không rõ')

# Xoá số tuổi bị âm trong cột 'Age'
df=df.drop(df[df['Age'] < 0].index)

# Đếm số dòng trống cột Age 
student_age_null_count=df['Age'].isnull().sum()
# Làm tròn số tuổi trung bình trong cột 'Age'
age_mean=round(df['Age'].mean())
# Điền và lấp các ô trống bằng tuổi trung bình vừa tính
df['Age']=df['Age'].fillna(age_mean)

# Xoá các dòng dữ liệu có giá trị trống trong các cột ATS, HSP,AS 
score_nulls = df[(df['Admission Test Score'].isna()) &
               (df['High School Percentage'].isna()) &
               (df['Admission Status'].isna())].index
df=df.drop(score_nulls)

# Tìm và xoá các dòng bị trống trong cột 'City'
city_nulls=df[df['City'].isna()].index
df=df.drop(city_nulls)

# Điền 'Unknown' vào các hàng bị trống trong cột 'Gender'
df['Gender']=df['Gender'].fillna('Unknown')


df=df[df['Admission Test Score'] > 0] # Loại bỏ các bản ghi có 'Admission Test Score' <= 0
df=df[df['High School Percentage'] > 0] # Loại bỏ các bản ghi có 'High School Percentage' <= 0

# Lưu data_frame vào file 'student_admission_record_clean.csv'
df.to_csv("student_admission_record_clean.csv", sep=',')
