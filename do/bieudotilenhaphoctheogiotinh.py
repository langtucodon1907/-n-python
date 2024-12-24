# biểu đồ tỉ lệ nhập học theo giới tính 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', hue='Admission Status', data=df)
plt.title('Tình trạng tuyển sinh theo giới tính')
plt.xlabel('Giới tính')
plt.ylabel('giá trị')
plt.show()