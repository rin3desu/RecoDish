from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.parse
import time

#食材を入力
ingredient = input("検索したい食材を入力して下さい：")
encoded_ingredient = urllib.parse.quote(ingredient)
url = f"https://cookpad.com/search/{encoded_ingredient}"

#ChromeDriverのパス
service = Service(executable_path="C:\\Users\\rinse\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

#Chromeブラウザ起動
driver = webdriver.Chrome(service=service)
driver.get(url)

#ページ読み込み待機
time.sleep(5)

#レシピタイトルの要素を取得
recipes = driver.find_elements(By.CSS_SELECTOR, ".block-link_main")

# レシピ結果を表示
if recipes:
  print(f"\n「{ingredient}」を使ったレシピ一覧：")
  for i, recipe in enumerate(recipes,1):
    title = recipe.text.strip()
    link = recipe.get_attribute("href")
    print(f"{i}.{title}\n {link}")
else:
  print("レシピが見つかりませんでした")

# 終了待機（エンターを押すまでブラウザも閉じない）
input("\n→ ブラウザで結果を確認したらEnterを押して終了してください：")
#ブラウザを終了
#driver.quit()