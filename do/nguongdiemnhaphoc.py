 # biểu đồ Xác định ngưỡng điểm nhập học
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(8, 6))
sns.histplot(df['Admission Test Score'], kde=True, color='green')
plt.axvline(df['Admission Test Score'].median(), color='red', linestyle='dashed', linewidth=2, label='Median')
plt.axvline(df['Admission Test Score'].mean(), color='blue', linestyle='dashed', linewidth=2, label='Mean')
plt.title('Phân bố điểm thi tuyển sinh theo ngưỡng')
plt.xlabel('Điểm thi tuyển sinh')
plt.ylabel('')
plt.legend()
plt.show()