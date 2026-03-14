# スクロールで背景フェードイン - position fixed + z-index -1 + JSセレクタで発火タイミング調整

セクションに入ったとき背景画像がふわっと表示され、出たら消える。
境目をなくすには `position: fixed; z-index: -1` が鉄則。

★核心的な要点
```
position: sticky → 親の中に閉じ込められる → 境目が出る
position: fixed  → 画面全体の背景になる   → 境目が消える
```

## ★重要ポイント

【★ポイント1: sticky → fixed で境目が消える】
```css
.bg {
  position: fixed;   /* sticky だと親要素の上端で境目が出る */
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background: url("../img/bg.jpg") center / cover no-repeat;
  z-index: -1;       /* 全コンテンツの後ろに配置 */
  opacity: 0;
  transition: opacity 1s ease-in-out;
}
.bg.visible {
  opacity: 1;
}
```
`position: fixed` にすることで `.bg` が画面全体の背景になり、どのセクションからも見える。

【★ポイント2: JSセレクタを「深い要素」にして発火を遅らせる】
```js
/* NG: .access_area → 早すぎる（前のセクションでも背景が出る） */
const accessSection = document.querySelector(".access_area");

/* OK: .access_title → ちょうどいい（タイトルが見えたら発火） */
const accessSection = document.querySelector(".access_title");

window.addEventListener("scroll", function () {
  const accessSectionTop = accessSection.getBoundingClientRect().top;
  const windowHeight = window.innerHeight;
  if (accessSectionTop < windowHeight) {
    accessBg.classList.add("visible");    // 背景を表示
  } else {
    accessBg.classList.remove("visible"); // 背景を非表示
  }
});
```
セレクタを深くするほど発火が遅れる。前のセクションで背景が出てしまうときはセレクタをより内側の要素に変更する。
`画像を暗くするテクニック`

【★ポイント3: 複数backgroundはカンマ必須】
```css
/* NG: カンマなし → 画像が無視される */
background: linear-gradient(...) url("../img/bg.jpg") center / cover no-repeat;

/* OK: カンマあり */
background:
  linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),　★←このカンマ
  url("../img/bg.jpg") center / cover no-repeat;
```
前に書いた方が上に重なる（グラデーション → 画像の順）。

---

## HTML
```html
<!-- ACCESS セクション -->
<section class="access_area">
  <div class="bg"></div>　<!-- 背景画像 -->　
  <div class="content">　　<!-- 通過する文字 -->
    <h2 class="access_title">ACCESS</h2>
    <p>PARK SIDE HALL</p>
    <p>〒000-0000 東京都...</p>
    <a href="#" class="access_map">GOOGLE MAP</a>
  </div>
</section>

<script src="js/work.js"></script>
```

## CSS
```css
/* ACCESS エリア */
.access_area {
  position: relative;
  min-height: 100vh;
}

/* 背景画像（固定・全画面・最背面） */
.bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background: url("../img/bg.jpg") center / cover no-repeat;
  z-index: -1;
  /* 最初はかくしておく。javaScriptで目的の要素がみえたら画像を表示 */
  opacity: 0; 
  transition: opacity 1s ease-in-out;
}

/* JS でこのクラスが付いたら表示 */
.bg.visible {
  opacity: 1;
}

/* テキストコンテンツ（背景の上に表示） */
.content {
  position: relative;
  z-index: 1;  /* 背景より高いレイヤーにする--*/
  padding: 10rem 20px;
  box-sizing: border-box;
  color: white;
  text-align: center;
}
```

## JavaScript
```javascript
// 背景の表示・非表示をスクロールで制御
const accessSection = document.querySelector(".access_title"); // 深い要素を指定
const accessBg = document.querySelector(".bg");

window.addEventListener("scroll", function () {
  const accessSectionTop = accessSection.getBoundingClientRect().top;
  const windowHeight = window.innerHeight;

  if (accessSectionTop < windowHeight) {
    accessBg.classList.add("visible");    // セクションに入ったら表示
  } else {
    accessBg.classList.remove("visible"); // セクションを出たら非表示
  }
});
```

---

## 動作フロー
1. 初期状態: `.bg` は `opacity: 0`（非表示）
2. スクロールイベント発火
3. `.access_title` の位置を `getBoundingClientRect().top` で取得
4. 画面内に入ったら `visible` クラスを追加 → `opacity: 1` に変化
5. `transition: opacity 1s` でふわっとフェードイン
6. セクションを出たら `visible` クラスを削除 → フェードアウト

## トラブルシューティング
### エラー: 前のセクションでも背景が出る
**原因**: `querySelector` の対象が `.access_area` など外側の要素になっている
**対処**: より内側の要素（`.access_title` など）に変更する

### エラー: 画像が表示されない（真っ黒）
**原因**: `background` に複数値を書くときカンマが抜けている
**対処**: `linear-gradient(...), url(...)` のようにカンマで区切る

### エラー: 境目（横線）が見える
**原因**: `position: sticky` になっている（親要素の中に閉じ込められている）
**対処**: `position: fixed; left: 0; width: 100%;` に変更する
