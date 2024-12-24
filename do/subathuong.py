# biểu đồ Phát hiện sự bất thường (Boxplot giữa điểm thi và tình trạng nhập học)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataclean.csv')
plt.figure(figsize=(8, 6))
sns.boxplot(x='Admission Status', y='Admission Test Score', data=df)
plt.title('Điểm thi tuyển sinh theo tình trạng tuyển sinh')
plt.xlabel('Tình trạng nhập học')
plt.ylabel('Admission Test Score')
plt.show()