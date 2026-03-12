# WordPress ページネーション - paginate_links() に type=array を渡すと配列で返る（currentクラス付き・カスタマイズ可）

paginate_links() に `type => 'array'` を渡すと配列で返ってくる。foreach で1個ずつ取り出して自由にカスタマイズできる。

★ `type => 'array'` がないと HTML がそのまま出力されてクラスをつけられない

---

## 目次

- [スニペット1: 丸ボタン型（span・CSS付き）← おすすめ](#snippet1)
- [スニペット2: シンプル型（li・最小構成）](#snippet2)

---

## ★重要ポイント

【★ポイント1: $args の書き方（語呂合わせ）】
```php
$args = array(
    'mid_size' => 1,    // 緑（mid）をさす人はナンバーわん
    'type'     => 'array', // タイ人(type)を指す(=>)雨(array)がふる
);
$pagination = paginate_links($args);
```
`$pagination` の中身は `['<a href="?page=1">1</a>', '<span class="current">2</span>', ...]` のような HTML文字列の配列。

【★ポイント2: strpos で current を判定してクラスをつける】
```php
if (strpos($page, 'current') !== false) {
    echo '<span class="current">' . $page . '</span>';
} else {
    echo '<span class="page_numbers">' . $page . '</span>';
}
```
`strpos` は文字列の中に指定の文字があれば位置（数字）を返す、なければ false を返す。

【★ポイント3: .page-numbers（ハイフン）はWordPressが自動でつけるクラス】
```css
/* 自分でつけたクラス（アンダースコア） */
.page_numbers { border: 0.1rem solid black; border-radius: 50%; }

/* WordPressが自動でつけるクラス（ハイフン）← borderは書かない！ダブル丸になる */
.page-numbers { display: flex; justify-content: center; align-items: center; }
```
内側の `<a>` にも `.page-numbers` が自動でつく。両方にborderを書くと**丸が二重**になるので注意。

【★ポイント4: display:flex はブロックも兼ねる】
```css
.current {
  display: flex; /* ← これだけでwidth/heightが効く。blockは不要 */
  justify-content: center;
  align-items: center;
  width: 4rem;
  height: 4rem;
}
```

【★ポイント5: 投稿数が少ないと表示されない】
管理画面「設定 → 表示設定」で1ページの表示件数を減らして確認する。

---

<a id="snippet1"></a>
## スニペット1: 丸ボタン型（span・CSS付き）← おすすめ

### PHP（archive.php の endwhile の下に貼る）
```php
<div class="news_excerpt">
<?php
    $args = array(
        'mid_size' => 1,
        'type'     => 'array',
    );
    $pagination = paginate_links($args);
    foreach($pagination as $page){
        if (strpos($page, 'current') !== false) {
            echo '<span class="current">' . $page . '</span>';
        } else {
            echo '<span class="page_numbers">' . $page . '</span>';
        }
    }
?>
</div>
```

### CSS
```css
/* ページネーション全体：横並び */
.news_excerpt {
  display: flex;
  gap: 0.5rem;
}

/* 現在ページ：黒塗り丸 */
.current {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: black;
  color: white;
  border-radius: 50%;
  width: 4rem;
  height: 4rem;
}

/* 通常ページ：枠だけ丸 */
.page_numbers {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 0.1rem solid black;
  border-radius: 50%;
  width: 4rem;
  height: 4rem;
}

/* WordPressが自動でつけるクラス（borderは書かない！ダブル丸になる） */
.page-numbers {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

<a id="snippet2"></a>
## スニペット2: シンプル型（li・最小構成）

### PHP
```php
<div class="my-pagination"><ul>
<?php
$args = array(
    'mid_size' => 1,
    'type'     => 'array'
);
$pagination = paginate_links($args);

if ($pagination) {
    foreach ($pagination as $page) {
        if (strpos($page, 'current') !== false) {
            echo '<li class="current">' . $page . '</li>';
        } else {
            echo '<li>' . $page . '</li>';
        }
    }
}
?>
</ul></div>
```

### CSS
```css
.my-pagination ul {
    display: flex;
    list-style: none;
    gap: 8px;
}

.my-pagination li a,
.my-pagination li span {
    display: block;
    padding: 4px 12px;
    border: 1px solid #ccc;
}

.my-pagination li.current span {
    background: #333;
    color: #fff;
}
```

---

## 動作フロー
1. `$args` に設定（mid_size・type）を作る
2. `paginate_links($args)` に渡すと HTML文字列の配列が返ってくる
3. `foreach` で1個ずつ取り出す
4. `strpos` で `current` が含まれるか確認 → 今のページなら `class="current"` をつける
5. `<span>` で囲んで出力

## トラブルシューティング
### ページネーションが表示されない
**原因**: 投稿数が表示件数以下
**対処**: 管理画面「設定 → 表示設定」で1ページの件数を減らす（例：2件）

### 丸が二重になる
**原因**: `.page_numbers`（自作）と `.page-numbers`（WordPress自動）の両方に border を書いている
**対処**: `.page-numbers` からは border・width・height・border-radius を削除する
