import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目标网址
url = "https://c57-sw9.chouhanbusiness.com:2053/#dh"

# 请求网页内容
response = requests.get(url)
if response.status_code != 200:
    print("网页请求失败")
    exit()

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 打印网页内容，检查结构
# print(soup.prettify())

# 假设开奖记录存储在表格中，可以使用类似如下的方法提取数据
# 这里假设网页中的表格有 <table> 标签，且每行数据用 <tr> 标签表示
# 根据你提供的网页实际情况调整选择器
table = soup.find('table')  # 获取表格
rows = table.find_all('tr')  # 获取所有行

# 提取表格数据
data = []
for row in rows:
    cols = row.find_all('td')  # 获取每一列
    cols = [col.text.strip() for col in cols]  # 清理文本
    data.append(cols)

# 将数据转换成 DataFrame（方便保存为 CSV 或处理）
df = pd.DataFrame(data)

# 保存为CSV文件
df.to_csv('开奖记录.csv', index=False, encoding='utf-8')
print("数据已保存为 '开奖记录.csv'")

