# biểu đồ phân bố điểm thi nhập học
 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'dataclean.csv'  
data = pd.read_csv(file_path)
plt.figure(figsize=(8, 5))
sns.histplot(data['Admission Test Score'], bins=20, kde=True, color='blue')
plt.title('Phân bố điểm thi nhập học')
plt.xlabel('Điểm thi nhập học')
plt.ylabel('Tần suất')
plt.show()

#