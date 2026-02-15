# jQueryアコーディオン（slideToggle + flex対応）

jQueryを使ったシンプルなアコーディオンメニュー実装。

---

## HTML

```html
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>募集職種</title>
    <link rel="stylesheet" href="css/accodion.css" />
  </head>
  <body>
    <header class="header_area">
      <!-- アコーディオンヘッダー -->
      <div class="header_container">
        <h2 class="header_title">Webディレクター</h2>
        <div class="header_button"></div>
      </div>

      <!-- アコーディオン詳細 -->
      <div class="header_item">
        <h3 class="header_item_title">仕事内容</h3>
        <p class="header_item_description">テキストテキストテキストテキストテキスト</p>
      </div>
      <div class="header_item">
        <h3 class="header_item_title">応募資格</h3>
        <p class="header_item_description">テキストテキストテキストテキストテキスト</p>
      </div>
    </header>

    <!-- ★ jQueryは必ずaccordion.jsより前に読み込む！ -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="js/accordion.js"></script>
  </body>
</html>
```

---

## CSS

```css
/* アコーディオンヘッダー */
.header_area {
  width: 80%;
  height: auto;
  margin: 0 auto;
}

.header_container {
  width: 100%;
  height: 80px;
  padding-left: 20px;

  background-color: orange;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid black;
  cursor: pointer;
}

/* ★ CSSでインラインの文字を変更する際は、疑似要素を利用する！
   （おそらく通常のクラスのプロパティではcontent:"文字"が使えない） */
.header_button::after {
  content: "―";
  padding-right: 50px;
}

/* アコーディオン詳細 */
.header_item {
  width: 65%;
  height: 80px;
  padding-left: 20px;

  background-color: white;

  /* ★ displayプロパティは1つだけ！2つ書くと後の方で上書きされる */
  display: none; /* 初期非表示 */
  align-items: center;
  justify-content: space-between;
}

/* ★ クラスが追加された際の書き方は「.クラス名.クラス名」空白をいれない！！
   例: .header_item.active { ... } */
```

---

## JavaScript

```javascript
// JQERYで実装。Windowsが読み込まれたあとに、アコーディオンの機能を実装するためのコードです。
$(function () {
  // アコーディオンのタイトル要素をクリックしたときのイベントリスナーを設定します。
  $(".header_container").on("click", function () {
    // ★ next() は1個だけ、nextAll() は全ての兄弟要素を取得
    var content = $(this).nextAll(".header_item");

    // ★ スライドトグル: $(this).next(".acc-panel").slideToggle(200);
    //   スライドの切り替えを表す。
    content.slideToggle(300, function () {
      // 開いた時にflexレイアウトを適用
      // ★ slideToggle だけだと display: block になるため、flex を明示的に指定
      if ($(this).is(":visible")) {
        $(this).css("display", "flex");
      }
    });
  });
});

/* ★ クラスを切り替えるロジックは element.classList.toggle と書く。
   クラスリストがつくことに注意！！！
   例: element.classList.toggle("active"); */
```

---

## よくあるエラー

**❌ jQuery is not defined**
- jQueryが読み込まれていない
- `<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>` を追加

**❌ アコーディオンが最初から表示**
- CSS で `display: none` より後に `display: flex` を書いている
- `display: none` だけを配置

**❌ 1つしか開閉しない**
- `next()` を使っている
- `nextAll()` に変更

**❌ レイアウトが崩れる**
- slideToggle は `display: block` にする
- コールバック内で `css('display', 'flex')` を適用
