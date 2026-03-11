jQuery fadeOut/fadeIn - サムネイルクリックで画像をフェード切り替え

サムネイル画像をクリックすると、メイン画像がフェードアウト→src変更→フェードインで切り替わる。

★ようするにfadeOutのコールバック（第2引数のfunction）の中でsrc変更＋fadeInする
```javascript
$(".gallery_main").fadeOut(1000, function () {
  $(this).attr("src", imgSrc).fadeIn(300);
});
```

## ★重要ポイント

【★ポイント1: fadeOutのコールバック関数で順番制御】
```javascript
// fadeOut(速度, コールバック関数)
// → フェードアウトが「完了してから」中の処理が実行される
$(".gallery_main").fadeOut(1000, function () {
  // ここはフェードアウト完了後に実行される
  $(this).attr("src", imgSrc).fadeIn(300);
});
```
コールバックを使わないとフェードアウト中に画像が変わってしまう。第2引数のfunctionが「完了後に実行」のカギ。

【★ポイント2: メソッドチェーンで属性変更→フェードイン】
```javascript
// .attr() と .fadeIn() を1行でつなげる
$(this).attr("src", imgSrc).fadeIn(300);
// ↑ src変更        ↑ フェードイン
```
`$(this)` はコールバック内ではfadeOutした要素自身（`.gallery_main`）を指す。

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
    <section class="gallery_area">
      <!-- 大きな画像 -->
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
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="js/画像切り替え.js"></script>
  </body>
</html>
```

## CSS
```css
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
  object-fit: contain;
}

/* 小さな画像　flex */
.gallery_thumbnails {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

.gallery_img {
  width: calc((100% - (10px * 4)) / 5);
  height: 200px;
  margin-top: 20px;
  cursor: pointer;
  object-fit: cover;
}
```

## JavaScript
```javascript
// 下段の画像をクリックすると、上段の画像が切り替わる。
$(function () {
  // サムネイル画像をクリックしたときの処理
  $(".gallery_img").on("click", function () {
    // クリックされたサムネイル画像のsrc属性を取得
    const imgSrc = $(this).attr("src");

    // ★メイン画像をフェードアウトしてから、src属性を変更し、再度フェードインする
    $(".gallery_main").fadeOut(1000, function () {
      // ★メイン画像のsrc属性を変更 + フェードイン（メソッドチェーン）
      $(this).attr("src", imgSrc).fadeIn(300);
    });
  });
});
```

---

## 動作フロー
1. サムネイル画像(`.gallery_img`)をクリック
2. クリックした画像のsrcを`imgSrc`に保存
3. メイン画像(`.gallery_main`)が1秒かけてフェードアウト
4. フェードアウト完了後、コールバック内でsrcを差し替え
5. 差し替え後、0.3秒かけてフェードイン
