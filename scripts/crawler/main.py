import requests
import re
from bs4 import BeautifulSoup

# 目标网页的URL
url = 'https://leetcode.cn/studyplan/programming-skills/'

# 发起GET请求
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all(id='__NEXT_DATA__')
script0 = result[0]
strScript = str(script0)
print(type(strScript))
# match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', str(script0), re.DOTALL)
# print(match)