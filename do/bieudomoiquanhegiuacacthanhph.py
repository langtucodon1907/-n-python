#Biểu đồ mối quan hệ giữa thành phố và tình trạng nhập học  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(8, 6))
sns.countplot(x='City', hue='Admission Status', data=df)
plt.title('Tình trạng tuyển sinh theo thành phố')
plt.xlabel('thành phố')
plt.ylabel('giá trị')
plt.xticks(rotation=45, ha='right')
plt.show()
