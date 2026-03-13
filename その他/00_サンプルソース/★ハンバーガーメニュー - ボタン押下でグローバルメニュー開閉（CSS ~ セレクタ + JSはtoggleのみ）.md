# ハンバーガーメニュー - ボタン押下でグローバルメニュー開閉（CSS ~ セレクタ + JSはtoggleのみ）

ボタンにclassをtoggleするだけ。メニューの表示切り替えはCSSの `~` セレクタだけでできる。

★核心：JSはクラスを付けるだけ。表示切り替えはCSSに任せる
```css
.hamburger_menu.open ~ .global_menu { display: flex; }
```

## ★重要ポイント

【★ポイント1: `~` は「同じ親・後ろの兄弟」に効く】
```css
/* ボタンに .open がついたら、後ろにある nav を表示 */
.hamburger_menu.open ~ .global_menu {
  display: flex;
}
```
`~` は間に別要素が挟まっていてもOK。同じ親の中で後ろにあれば効く。

【★ポイント2: z-index はボタン > メニュー にする（逆にするとXが消える）】
```css
.global_menu    { z-index: 400; }
.hamburger_menu { z-index: 401; } /* 必ずメニューより大きく */
```
逆にするとメニューがボタンを覆い、×ボタンが押せなくなる。

【★ポイント3: バーの × アニメーション（CSS only）】
```css
/* openクラスで1本目を45度回転 */
.hamburger_menu.open .bar:nth-child(1) {
  transform: rotate(45deg);
  top: 1.5rem;
}
/* 2本目を消す */
.hamburger_menu.open .bar:nth-child(2) {
  opacity: 0;
}
/* 3本目を-45度回転 */
.hamburger_menu.open .bar:nth-child(3) {
  transform: rotate(-45deg);
  top: 1.5rem;
}
```

---

## HTML
```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <header class="header_area">
    <!-- ハンバーガーメニュー -->
    <button class="hamburger_menu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>

    <!-- ロゴ -->
    <a class="main_logo">LOGO</a>

    <!-- グローバルメニュー（buttonと同じ親・後ろに置く） -->
    <nav class="global_menu">
      <a href="#" class="global_menu_link">トップ</a>
      <a href="#" class="global_menu_link">会社概要</a>
      <a href="#" class="global_menu_link">採用情報</a>
      <a href="#" class="global_menu_link">お問い合わせ</a>
    </nav>
  </header>

  <script src="js/work.js"></script>
</body>
</html>
```

## CSS
```css
/* ヘッダー全体 */
.header_area {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 20rem;
  background-color: transparent;
  z-index: 500;
}

/* ハンバーガーボタン */
.hamburger_menu {
  position: fixed;
  top: 1.5rem;
  right: 2rem;
  width: 3rem;
  height: 3rem;
  cursor: pointer;
  background-color: black;
  overflow: hidden;
  z-index: 401; /* global_menu(400)より必ず大きく */
}

/* バー（3本線） */
.bar {
  position: absolute;
  display: block;
  transition: 0.3s;
  left: 0;
  height: 0.2rem;
  width: 3rem;
  background: white;
}
.bar:nth-child(1) { top: 0.6rem; }
.bar:nth-child(2) { top: 1.4rem; }
.bar:nth-child(3) { top: 2.2rem; }

/* openクラスで × に変化 */
.hamburger_menu.open .bar:nth-child(1) {
  transform: rotate(45deg);
  top: 1.5rem;
}
.hamburger_menu.open .bar:nth-child(2) {
  opacity: 0;
}
.hamburger_menu.open .bar:nth-child(3) {
  transform: rotate(-45deg);
  top: 1.5rem;
}

/* グローバルメニュー（デフォルト非表示） */
.global_menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 30rem;
  background-color: rgba(0, 0, 0, 0.9);
  display: none;         /* デフォルト非表示 */
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 400;
}

/* ★ ボタンに.openがついたら表示（~ = 同じ親の後ろの兄弟） */
.hamburger_menu.open ~ .global_menu {
  display: flex;
}

/* リンク */
.global_menu_link {
  font-size: 3rem;
  margin-bottom: 2rem;
  color: white;
  text-decoration: none;
}
```

## JavaScript
```javascript
const hamburgerBtn = document.querySelector(".hamburger_menu");

hamburgerBtn.addEventListener("click", function () {
  hamburgerBtn.classList.toggle("open"); // クラスを付けるだけ。表示はCSSに任せる
});
```

---

## 動作フロー
1. クリック → JSが `.hamburger_menu` に `.open` を付ける／外す
2. `.open` あり → CSSの `~` セレクタが `.global_menu` を `display: flex` に
3. バーも同時に × アニメーション

## トラブルシューティング
### × ボタンが消えてメニューを閉じられない
**原因**: `global_menu` の z-index が `hamburger_menu` より大きい
**対処**: `hamburger_menu` の z-index を `global_menu + 1` 以上にする

### `~` セレクタが効かない
**原因**: button と nav が同じ親の中にない、またはnavがbuttonより前にある
**対処**: HTML構造を確認し、同じ親・button の後ろに nav を置く
