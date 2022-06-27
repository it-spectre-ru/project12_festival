import json
import requests
from bs4 import BeautifulSoup
import lxml
import json
import os


headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

proxies = {
        'https': f'http://{os.getenv("LOGIN")}:{os.getenv("PASSWORD")}@194.28.211.142:9630'
    }

# collect all fest URL
fest_urls_list = []

# for i in range(0, 192, 24):
for i in range(0, 24, 24):
  url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=24%20Jan%202021&to_date=&where%5B%5D=2&where%5B%5D=3&where%5B%5D=4&where%5B%5D=6&where%5B%5D=7&where%5B%5D=8&where%5B%5D=9&where%5B%5D=10&maxprice=500&o={i}&bannertitle=May'
  
  req = requests.get(url=url, headers=headers, proxies=proxies)
  json_data = json.loads(req.text)
  html_response = json_data["html"]

  with open(f'data/index_{i}.html', 'w') as file:
    file.write(html_response)

  with open(f'data/index_{i}.html') as file:
    src = file.read()

  soup = BeautifulSoup(src, 'lxml')
  cards = soup.find_all('a', class_='card-details-link')

  for item in cards:
    fest_url = 'https://www.skiddle.com' + item.get('href')
    fest_urls_list.append(fest_url)

print(fest_urls_list)

