#食材を入力
ingredient = input("検索したい食材を入力してください：")

import urllib.parse
encoded_ingredient = urllib.parse.quote(ingredient)

#クックパッドの検索URL作成
search_url = f"https://cookpad.com/search/{encoded_ingredient}"

# 結果を表示
print(f"このURLをブラウザで開くと、{ingredient} を使ったレシピが見られます！")
print(search_url)