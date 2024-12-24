#biểu đồ phân phối thành phố
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(7, 7))
city_counts = df['City'].value_counts()
city_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
plt.title('Phân Bố Tuyển Sinh Theo Thành Phố ')
plt.ylabel('')
plt.show()