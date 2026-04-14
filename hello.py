# 関数を作る（処理をまとめて名前をつける）
def check_price(name, price):
    if price >= 10000:
        print(f"{name}は{price}円 → 高い！")
    else:
        print(f"{name}は{price}円 → お手頃")

# 関数を使う
check_price("ワイヤレスイヤホン", 8900)
check_price("スマートウォッチ", 32000)
check_price("USBケーブル", 500)