#Biểu đồ tỷ lệ nhập học theo thành phố và giới tính
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(10, 6))
sns.countplot(x='City', hue='Gender', data=df, palette='Set2')
plt.title('Tình trạng nhập học theo thành phố và giới tính')
plt.xlabel('thành phố ')
plt.ylabel('giá trị ')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Gender')
plt.show()

