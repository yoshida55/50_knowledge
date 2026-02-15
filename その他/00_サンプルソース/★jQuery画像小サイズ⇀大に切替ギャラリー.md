# jQuery画像小サイズ⇀大に切替ギャラリー

jQueryでサムネイルクリック時に大きな画像エリアに表示する画像切り替えギャラリー。

---

## HTML

```html
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>画像切り替え</title>
    <link rel="stylesheet" href="css/画像の切替セクション.css" />
  </head>
  <body>
    <!-- ===============================================
         画像切り替えセクション
         =============================================== -->
    <section class="gallery_area">
      <!-- 大きな画像 -->
      <!-- ★ object-fit は img タグに設定する必要がある（div では効かない） -->
      <img alt="大きな画像" class="gallery_main" />

      <!-- 小さな画像　flex -->
      <div class="gallery_thumbnails">
        <img src="img/image1.png" alt="画像1" class="gallery_img" />
        <img src="img/image2.png" alt="画像2" class="gallery_img" />
        <img src="img/image3.png" alt="画像3" class="gallery_img" />
        <img src="img/image1.png" alt="画像4" class="gallery_img" />
        <img src="img/image2.png" alt="画像5" class="gallery_img" />
      </div>
    </section>

    <!-- 画像の切り替えのライブラリ読み込み -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="js/画像の切替セクション.js"></script>
  </body>
</html>
```

---

## CSS

```css
/* ┌─────────────────────────────────────────┐
   │ 画像切り替えセクション                  │
   │ - 上に大きな画像表示エリア              │
   │ - 下に小さい画像を横並び                │
   │ - クリックで上の画像を切り替え          │
   └─────────────────────────────────────────┘ */

.gallery_area {
  width: 80%;
  margin: 0 auto;
  padding-top: 50px;
}

/* 大きな画像 */
.gallery_main {
  display: block;
  width: 100%;
  height: 400px;
  margin-bottom: 20px;
  background-color: #eee;

  /* ★ object-fit: contain で画像全体を表示（余白あり） */
  /* ★ object-fit: cover なら余白なし（画像の一部切れる） */
  object-fit: contain;
}

/* 小さな画像　flex */
.gallery_thumbnails {
  display: flex;
  justify-content: space-between;

  /* ★ gap で画像間の余白を設定 */
  gap: 10px;
}

.gallery_img {
  /* ★ calc で gap を考慮した幅計算 */
  /* ★ 公式: calc((100% - (gap × (枚数 - 1))) / 枚数) */
  width: calc((100% - (10px * 4)) / 5); /* 5枚の画像と4つのgapを考慮して幅を計算 */
  height: 200px;
  margin-top: 20px;
  cursor: pointer;

  /* ★ サムネイルは cover で縦横比統一 */
  object-fit: cover;
}
```

---

## JavaScript

```javascript
// 画像切り替え機能
$(function () {
  // サムネイル画像をクリックしたとき
  $(".gallery_img").on("click", function () {
    // クリックした画像のsrcを取得

    // ★ attr() は HTML要素の属性（attribute）を取得または設定するメソッド
    // ★ $("img").attr("src");  // "photo.jpg" を取得
    // ★ $("img").attr("alt");  // "写真" を取得

    const src = $(this).attr("src");

    // ★ html() で全体生成より attr("src") で属性変更の方が効率的
    // メイン画像エリアに表示
    $(".gallery_main").attr("src", src);
  });
});
```

---

## よくある間違い

### ❌ エラー1: object-fit が効かない
**原因:** div に object-fit を設定している
```css
.gallery_main {  /* div */
  object-fit: contain;  /* ❌ 効かない */
}
```

**対処:** img タグに変更して object-fit を設定
```html
<img class="gallery_main" />  <!-- img に変更 -->
```
```css
.gallery_main {  /* img */
  object-fit: contain;  /* ✅ 動く */
}
```

### ❌ エラー2: gap を使うと画像がはみ出る
**原因:** width を固定値で設定している
```css
.gallery_img {
  width: 18%;  /* gap分を考慮していない */
}
```

**対処:** calc で gap 分を引く
```css
.gallery_img {
  width: calc((100% - (10px * 4)) / 5);
}
```

### ❌ エラー3: 画像切り替えが非効率
**原因:** html() で毎回 img タグを生成
```javascript
$(".gallery_main").html('<img src="' + src + '">');
```

**対処:** attr() で src だけ変更
```javascript
$(".gallery_main").attr("src", src);
```

---

## 重要ポイントまとめ

### ★ object-fit は img・video などの置換要素にのみ有効
- div には効かない
- img タグに直接設定する

### ★ Flex gap + width は calc で計算
- 公式: `calc((100% - (gap × (枚数 - 1))) / 枚数)`
- gap 分を引いて均等割り

### ★ attr() で属性の取得・設定
- 取得: `$(elem).attr("src")`
- 設定: `$(elem).attr("src", value)`
- html() より効率的

### ★ object-fit の種類
- `contain`: 画像全体表示、余白あり
- `cover`: 余白なし、画像の一部切れる
