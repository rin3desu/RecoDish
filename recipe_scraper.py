import requests
from bs4 import BeautifulSoup
import urllib.parse

#食材を入学
ingredient = input("検索したい食材を入力して下さい：")

#URLエンコード
encoded_ingredient = urllib.parse.quote(ingredient)
url = f"https://cookpad.com/search/{encoded_ingredient}"

response = requests.get(url)

#正常にアクセスできたかチェック
if response.status_code == 200:
  #HTMLを解析
  soup = BeautifulSoup(response.text, 'html.parser')

  #レシピタイトルを探す
  titles = soup.find_all("a", class_="block-link_main")

  #タイトルを表示
  if titles:
    print(f"\n「{ingredient}」を使ったレシピ一覧：")
    for i, title in enumerate(titles,1):
      text = title.get_text(strip=True)
      link = "https://cookpad.com" + title.get("href")
      print(f"{i}. {text}")
  else:
    print("レシピが見つかりませんでした")
else:
  print("クックパッドにアクセスできませんでした。")