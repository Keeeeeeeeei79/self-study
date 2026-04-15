# SQL 学習メモ — SELECT / WHERE / JOIN

学習日：2026-04-15  
教材：[SQL 初級課題集 ShopDB](https://keeeeeeeeei79.github.io/self-study/SQL-Beginner-Exercises.html)

---

## 使用テーブル（ShopDB）

| テーブル | 主なカラム |
|---|---|
| customers | customer_id, name, email, city, age |
| products | product_id, name, category, price, stock |
| orders | order_id, customer_id, product_id, quantity, order_date, status |

---

## 課題一覧と解答

### 課題1：全顧客を取得する

```sql
SELECT * FROM customers;
```

**ポイント：** `*` はすべての列を意味する。

---

### 課題2：商品名と価格だけ取得する

```sql
SELECT name, price FROM products;
```

**ポイント：** 取得したい列名をカンマ区切りで指定する。

---

### 課題3：東京の顧客だけ取得する

```sql
SELECT * FROM customers WHERE city = '東京';
```

**ポイント：** 文字列の条件はシングルクォートで囲む。

---

### 課題4：価格が10,000円以上の商品を取得する

```sql
SELECT * FROM products WHERE price >= 10000;
```

**ポイント：** 数値の比較には `>=`（以上）を使う。

---

### 課題5：ステータスが「shipped」の注文を取得する

```sql
SELECT * FROM orders WHERE status = 'shipped';
```

**ポイント：** WHERE で文字列条件を指定する。

---

### 課題6：顧客名と注文IDを一緒に取得する（JOIN）

```sql
SELECT customers.name, orders.order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
```

**ポイント：**
- 別々のテーブルにあるデータをまとめるのが JOIN の役割
- `JOIN テーブル名 ON 共通キー` で結合する
- `テーブル名.列名` と書くとどのテーブルの列か明示できる

---

### 課題7：顧客名・商品名・注文数を取得する（3テーブルJOIN）

```sql
SELECT customers.name, products.name, orders.quantity
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;
```

**ポイント：**
- 3テーブルをつなぐときは、両方のFKを持つ `orders` を起点にする
- JOIN を2回書くことで3テーブルを結合できる
- 同名の列（name）は `テーブル名.name` で区別する（必須）

---

### 課題8：大阪の顧客の注文を取得する（JOIN + WHERE）

```sql
SELECT orders.order_id, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE customers.city = '大阪';
```

**ポイント：**
- JOIN の後に WHERE を追加して絞り込む
- 書く順番：`SELECT → FROM → JOIN → WHERE`

---

## まとめ：学んだこと

| 構文 | 用途 |
|---|---|
| `SELECT *` | 全列取得 |
| `SELECT 列名` | 特定の列を取得 |
| `WHERE 条件` | 行の絞り込み |
| `JOIN ... ON` | テーブルの結合 |
| `テーブル名.列名` | 同名列の区別 |

### SQLの書く順番
```
SELECT   → 取得する列
FROM     → 起点テーブル
JOIN     → 結合
WHERE    → 絞り込み
```

---

## 次に学ぶこと

- `GROUP BY` / 集計関数（COUNT, SUM, AVG）
- `ORDER BY`（並び替え）
- `LEFT JOIN`（一致しない行も取得）
- サブクエリ
