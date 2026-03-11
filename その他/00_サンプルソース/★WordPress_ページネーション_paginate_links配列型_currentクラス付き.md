# WordPress ページネーション - paginate_links() に type=array を渡すと配列で返る（currentクラス付き・カスタマイズ可）

paginate_links() に `type => 'array'` を渡すと配列で返ってくる。foreach で1個ずつ取り出して自由にカスタマイズできる。

★ `type => 'array'` がないと HTML がそのまま出力されてクラスをつけられない

## ★重要ポイント

【★ポイント1: type => 'array' で配列化する】
```php
$args = array(
    'mid_size' => 1,
    'type'     => 'array'  // ← これがないとHTMLがそのまま出力されカスタマイズ不可
);
$pagination = paginate_links($args);
```
`$pagination` の中身は `['<a href="?page=1">1</a>', '<span class="current">2</span>', ...]` のような HTML文字列の配列。

【★ポイント2: strpos で current を判定してクラスをつける】
```php
if (strpos($page, 'current') !== false) {
    echo '<li class="current">' . $page . '</li>';
} else {
    echo '<li>' . $page . '</li>';
}
```
`strpos` は PHP標準関数。文字列の中に指定の文字があれば位置（数字）を返す、なければ false を返す。

【★ポイント3: 投稿数が少いと表示されない】
管理画面「設定 → 表示設定」で1ページの表示件数を減らして確認する。

---

## PHP（archive.phpのループ外・下に貼る）
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
        // currentページにはクラスを付ける
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

## CSS（参考）
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
5. `<li>` で囲んで出力

## トラブルシューティング
### ページネーションが表示されない
**原因**: 投稿数が表示件数以下
**対処**: 管理画面「設定 → 表示設定」で1ページの件数を減らす（例：2件）
