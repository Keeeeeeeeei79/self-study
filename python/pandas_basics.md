# Python pandas 基礎まとめ

## 前提：辞書とリスト

```python
# 辞書（dictionary）= キーと値のペア
product = {
    "name": "ワイヤレスイヤホン",
    "price": 8900,
    "stock": 45
}

# 辞書から値を取り出す
print(product["name"])
print(f'価格: {product["price"]}円')

# 辞書のリスト = テーブルっぽいデータ
products = [
    {"name": "ワイヤレスイヤホン", "price": 8900, "stock": 45},
    {"name": "スマートウォッチ", "price": 32000, "stock": 12},
    {"name": "USBケーブル", "price": 500, "stock": 200},
    {"name": "タブレット", "price": 58000, "stock": 8},
]

# for文で全商品を表示
for p in products:
    print(f'{p["name"]} - {p["price"]}円（在庫{p["stock"]}個）')
```

---

## pandas基礎

### ① DataFrameを作る

```python
import pandas as pd

df = pd.DataFrame(products)
print(df)
```

- `df` は DataFrame の略（慣習的な変数名）
- DataFrameはExcelの表のような2次元データ

---

### ② 列を取り出す

```python
# 1列だけ取り出す
print(df["price"])

# 複数列を取り出す
print(df[["name", "price"]])
```

---

### ③ 絞り込み（フィルタリング）

```python
# 価格が10000円以上の商品だけ表示
print(df[df["price"] >= 10000])

# 在庫が10個以下の商品だけ表示
print(df[df["stock"] <= 10])
```

**仕組み：**
- 内側 `df["price"] >= 10000` → 各行にTrue/Falseを返す
- 外側 `df[...]` → Trueの行だけ残す

---

### ④ 新しい列を追加する

```python
# 在庫金額（price × stock）を新しい列として追加
df["total"] = df["price"] * df["stock"]
print(df)
```

- 存在しない列名を指定すると新しく作られる
- Excelで新列に計算式を入れるイメージ

---

### ⑤ 並び替え（ソート）

```python
# totalが高い順に並び替え
print(df.sort_values("total", ascending=False))
```

- `ascending=False` = 降順（高い順）
- `ascending=True` = 昇順（低い順）※デフォルト

---

### ⑥ 集計する

```python
# 合計
print(df["total"].sum())

# 平均
print(df["price"].mean())

# 統計情報をまとめて表示
print(df.describe())
```

| メソッド | 意味 |
|---|---|
| `.sum()` | 合計 |
| `.mean()` | 平均 |
| `.describe()` | 件数・平均・最大・最小・標準偏差など |

**describe()の見方：**

| 項目 | 意味 |
|---|---|
| count | データの件数 |
| mean | 平均 |
| std | バラつき（標準偏差） |
| min | 最小値 |
| 25% / 50% / 75% | 下から25% / 50% / 75%の値 |
| max | 最大値 |

---

## 今日のまとめ

| やったこと | コード |
|---|---|
| DataFrameを作る | `pd.DataFrame(リスト)` |
| 列を取り出す | `df["列名"]` |
| 絞り込み | `df[df["列名"] 条件]` |
| 列を追加 | `df["新列名"] = 計算` |
| 並び替え | `df.sort_values("列名", ascending=False)` |
| 集計 | `.sum()` / `.mean()` / `.describe()` |
