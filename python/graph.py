import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

products = [
    {"name": "ワイヤレスイヤホン", "price": 8900, "stock": 45},
    {"name": "スマートウォッチ", "price": 32000, "stock": 12},
    {"name": "USBケーブル", "price": 500, "stock": 200},
    {"name": "タブレット", "price": 58000, "stock": 8},
]

df = pd.DataFrame(products)



plt.style.use("bmh")
japanize_matplotlib.japanize()

plt.bar(df["name"], df["price"])
plt.title("商品別価格")
plt.xlabel("商品名")
plt.ylabel("価格（円）")
plt.savefig("graph.png")  # 追加！
plt.show()