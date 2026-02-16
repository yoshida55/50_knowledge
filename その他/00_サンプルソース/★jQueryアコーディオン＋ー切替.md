# jQueryアコーディオン＋/ー切替

クリックでアコーディオン開閉 + ＋/ーを切替える実装パターン。

★ようするに `.text()` と `.text("＋")` は別物。$(this) で共通化できる
if (plusObj.text() === "＋") {

## ★重要ポイント

【★ポイント1: `.text("＋")` vs `.text()` — セッターとゲッターの違い】
```javascript
// ❌ セッター（値をセットする）→ 常にtruthy → if文で使うと常にtrue
if (plusObj.text("＋")) {

// ✅ ゲッター（値を取得して比較する）
if (plusObj.text() === "＋") {
```
引数あり = セット、引数なし = 取得。if文で比較するなら引数なし。

【★ポイント2: `$(function(){})` は1回だけ実行される】
```javascript
$(function () {
  // ① ここは1回だけ実行（初期化 + イベント登録）
  $(".plus").text("＋");

  $("#work").click(function () {
    // ② ここはクリックのたびに毎回実行される
  });
});
```
クリック時にJSファイルを上から再実行するわけではない。登録された関数だけ呼ばれる。

【★ポイント3: `$(this)` + `.next()` + `.find()` で共通化】
```javascript
$("#work, #work1, #work2").click(function () {
  var content = $(this).next();                      // 隣の兄弟要素
  var plusObj = $(this).find(".plus, .plus1, .plus2"); // 子要素から探す

  content.slideToggle();
  if (plusObj.text() === "＋") {
    plusObj.text("ー");
  } else {
    plusObj.text("＋");
  }
});
```
3つの個別処理を1つにまとめられる。$(this) = クリックされた要素自体。

【★ポイント4: CSSの `::after` とJSの `.text()` を混ぜない】
```css
/* CSSで＋を出す場合 */
.plus1::after { content: "＋"; }
```
```javascript
// JSでも＋を出すと二重になる
$(".plus1").text("＋"); // ← ＋が2個表示される
```
どちらか片方で統一すること。

---

## HTML
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="css/jquery.css" />
  </head>
  <body>
    <h2>募集職種</h2>

    <div id="work">
      <div class="web">1. WEBディレクター</div>
      <div class="plus"></div>
    </div>
    <div class="accordion-content">
      <div class="work_list">
        <p class="job">仕事内容</p>
        <p class="description">テキストテキスト</p>
      </div>
    </div>

    <div id="work1">
      <div class="web1">2. WEBデザイナー</div>
      <div class="plus1"></div>
    </div>
    <div class="accordion-content1">
      <div class="work_list">
        <p class="job">募集職種</p>
        <p class="description">テキストテキスト</p>
      </div>
    </div>

    <div id="work2">
      <div class="web2">3. プログラマー</div>
      <div class="plus2"></div>
    </div>
    <div class="accordion-content2">
      <div class="work_list">
        <p class="job">募集職種</p>
        <p class="description">テキストテキスト</p>
      </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="js/jquery.js"></script>
  </body>
</html>
```

## CSS
```css
.accordion-content,
.accordion-content1,
.accordion-content2 {
  display: none;
}

#work, #work1, #work2 {
  width: 80%;
  height: 2rem;
  margin-left: 2rem;
  border-top: black solid 1px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.plus, .plus1, .plus2 {
  margin-right: 1rem;
}
```

## JavaScript
```javascript
$(function () {
  $(".plus, .plus1, .plus2").text("＋"); // ← 初期表示

  // 全アコーディオンを一つにまとめる
  $("#work, #work1, #work2").click(function () {
    var content = $(this).next();
    var plusObj = $(this).find(".plus, .plus1, .plus2");

    content.slideToggle();

    if (plusObj.text() === "＋") {
      plusObj.text("ー");
    } else {
      plusObj.text("＋");
    }
  });
});
```

---

## 動作フロー
1. ページ読み込み → `$(function(){})` で初期化（＋表示 + クリックイベント登録）
2. ユーザーがクリック → `.click(function(){})` の中だけ実行
3. `$(this).next()` で隣のcontent取得 → `slideToggle()` で開閉
4. `plusObj.text()` で現在の値を取得 → ＋/ーを切替

## トラブルシューティング
### エラー: ＋が2個表示される
**原因**: CSSの `::after { content: "＋" }` とJSの `.text("＋")` が両方ある
**対処**: どちらか片方に統一する

### エラー: クリックしても＋がーに変わらない
**原因**: `.text("＋")` をif文の条件に使っている（セッターなので常にtrue）
**対処**: `.text() === "＋"` に変更（引数なしで取得して比較）

### エラー: `.contents()` を使うとslideToggleが壊れる
**原因**: `.contents()` はテキストノード含む全子ノードを個別返却する
**対処**: `.contents()` を外して要素自体を取得する
