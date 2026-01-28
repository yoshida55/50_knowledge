# 🔧 Omodakaya模写 - トラブルシューティングガイド

> よくあるエラーと解決方法をまとめた実践的FAQ

---

## 目次
1. [レイアウトの問題](#1-レイアウトの問題)
2. [グリッドの問題](#2-グリッドの問題)
3. [レスポンシブの問題](#3-レスポンシブの問題)
4. [画像の問題](#4-画像の問題)
5. [アニメーションの問題](#5-アニメーションの問題)
6. [その他の問題](#6-その他の問題)

---

## 1. レイアウトの問題

### ❌ 問題: 商品カードが横に並ばない

**症状**
```
商品が縦に1列に並んでしまう
```

**原因**
- `display: grid`が効いていない
- CSS変数`--row`が定義されていない

**✅ 解決方法**

**確認1: グリッドが適用されているか**
```css
/* style.cssに以下があるか確認 */
.product-index {
    display: grid;
    grid-template-columns: repeat(var(--row), 1fr);
}
```

**確認2: CSS変数が定義されているか**
```css
/* style.cssの最初に以下があるか確認 */
.product-index {
    --row: 3;
}
```

**確認3: CSSファイルが読み込まれているか**
```html
<!-- index.htmlに以下があるか確認 */
<link rel="stylesheet" href="style.css">
```

**デバッグ方法**
```css
/* 一時的に追加して確認 */
.product-index {
    background-color: red;  /* 赤くなればCSSが効いている */
}
```

---

### ❌ 問題: カード内の要素が変な位置にある

**症状**
```
日付や商品名が重なる
画像が変な位置に表示される
```

**原因**
- Flexboxの設定ミス
- `flex-direction`が正しくない

**✅ 解決方法**

```css
.product-index__block {
    display: flex;
    flex-direction: column;  /* 縦方向に並べる */
    justify-content: space-between;  /* 上下に配置 */
    gap: 10px;  /* 要素間の余白 */
}
```

**DevToolsで確認**
1. 要素を右クリック → 検証
2. Layoutタブで`flex`が表示されているか確認
3. Flexboxのビジュアルツールで配置を確認

---

### ❌ 問題: 余白が効かない

**症状**
```
margin: 20px; を書いたのに余白が出ない
padding: 10px; が効いていない
```

**原因**
- リセットCSSがない
- `box-sizing`の問題
- 親要素の制約

**✅ 解決方法**

**確認1: box-sizingの設定**
```css
/* style.cssの最初に追加 */
* {
    box-sizing: border-box;
}
```

**確認2: リセットCSS**
```css
* {
    margin: 0;
    padding: 0;
}
```

**デバッグ方法**
```css
/* 一時的に極端な値で確認 */
.product-index__block {
    margin: 100px !important;  /* 効いていれば巨大な余白ができる */
}
```

---

## 2. グリッドの問題

### ❌ 問題: グリッドのボーダーが重なる

**症状**
```
グリッド線が二重になる
ボーダーが太く見える
```

**原因**
- 隣接する要素のボーダーが重なっている

**✅ 解決方法**

**方法1: 疑似要素を使う（推奨）**
```css
.product-index__block:before {
    content: "";
    display: block;
    width: calc(100% + 2px);
    height: 1px;
    background-color: var(--c-gray-1);
    position: absolute;
    top: -1px;
    left: -1px;
    z-index: 1;
}

.product-index__block:after {
    content: "";
    display: block;
    width: 1px;
    height: calc(100% + 2px);
    background-color: var(--c-gray-1);
    position: absolute;
    top: -1px;
    right: -1px;
    z-index: 1;
}
```

**方法2: border-collapseを使う（テーブルの場合）**
```css
table {
    border-collapse: collapse;
}
```

---

### ❌ 問題: グリッドが画面からはみ出る

**症状**
```
横スクロールバーが出る
カードが画面外に消える
```

**原因**
- `overflow: hidden`がない
- 親要素の幅が指定されていない

**✅ 解決方法**

```css
.product-index {
    overflow: hidden;  /* はみ出た部分を隠す */
}

/* または親要素に幅を指定 */
.container-sec {
    width: calc(100% - var(--space-hor) * 2);
    max-width: 1296px;
    margin: auto;
}
```

---

### ❌ 問題: 列数が変わらない

**症状**
```
画面サイズを変えても3列のまま
```

**原因**
- メディアクエリが効いていない
- CSS変数が再定義されていない

**✅ 解決方法**

**確認1: メディアクエリの順番**
```css
/* ❌ 悪い例: 順番が逆 */
@media (min-width: 1101px) {
    .product-index { --row: 5; }
}
@media (min-width: 801px) {
    .product-index { --row: 4; }
}

/* ✅ 良い例: 小さい順に書く */
.product-index {
    --row: 3;  /* デフォルト */
}

@media (min-width: 801px) {
    .product-index { --row: 4; }
}

@media (min-width: 1101px) {
    .product-index { --row: 5; }
}
```

**確認2: DevToolsで画面幅を確認**
```
F12 → デバイスツールバー
→ 画面幅を表示して確認
801px以上になっているか？
```

---

## 3. レスポンシブの問題

### ❌ 問題: スマホで文字が小さすぎる

**症状**
```
スマホで見ると文字が読めない
```

**原因**
- viewportメタタグがない
- font-sizeが小さすぎる

**✅ 解決方法**

**確認1: HTMLにviewportタグがあるか**
```html
<!-- index.htmlの<head>内に必須 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**確認2: モバイルファーストで記述**
```css
/* ❌ 悪い例 */
body { font-size: 16px; }
@media (max-width: 767px) {
    body { font-size: 12px; }  /* 小さすぎ */
}

/* ✅ 良い例 */
body { font-size: 14px; }  /* スマホ */
@media (min-width: 768px) {
    body { font-size: 15px; }  /* タブレット */
}
@media (min-width: 1025px) {
    body { font-size: 16px; }  /* PC */
}
```

---

### ❌ 問題: タブレットで中途半端なレイアウト

**症状**
```
768pxでレイアウトが崩れる
```

**原因**
- ブレークポイントの設定が曖昧
- 768pxと769pxで重複している

**✅ 解決方法**

**明確なブレークポイント**
```css
/* スマホ（〜767px） */
/* メディアクエリなし */

/* タブレット（768px〜1024px） */
@media screen and (min-width: 768px) {
    /* スタイル */
}

/* PC（1025px〜） */
@media screen and (min-width: 1025px) {
    /* スタイル */
}
```

**DevToolsで確認**
```
767px → スマホレイアウト
768px → タブレットレイアウト
1024px → タブレットレイアウト
1025px → PCレイアウト
```

---

### ❌ 問題: 横スクロールバーが出る

**症状**
```
画面に収まらず横スクロールできてしまう
```

**原因**
- 固定幅の要素がある
- `width: 100%`と`padding`の併用

**✅ 解決方法**

**方法1: box-sizingを使う**
```css
* {
    box-sizing: border-box;  /* paddingを含めた幅計算 */
}
```

**方法2: calcで計算**
```css
.container {
    width: calc(100% - 40px);  /* 左右20pxずつマージン */
}
```

**方法3: max-widthを使う**
```css
.container {
    max-width: 1296px;  /* 最大幅を制限 */
    margin: auto;
}
```

**デバッグ方法**
```css
/* 一時的に追加して原因を特定 */
* {
    outline: 1px solid red;
}
```

---

## 4. 画像の問題

### ❌ 問題: 画像が表示されない

**症状**
```
画像の場所に何も表示されない
壊れた画像アイコンが出る
```

**原因**
- パスが間違っている
- ファイル名の大文字小文字が違う
- 画像ファイルが存在しない

**✅ 解決方法**

**確認1: パスが正しいか**
```html
<!-- フォルダ構造 -->
project/
├── index.html
└── images/
    └── products/
        └── 001.jpg

<!-- ❌ 間違ったパス -->
<img src="images/product/001.jpg">  <!-- productではなくproducts -->

<!-- ✅ 正しいパス -->
<img src="images/products/001.jpg">
```

**確認2: 大文字小文字**
```html
<!-- ❌ 001.JPG と 001.jpg は別ファイル -->
<img src="images/products/001.jpg">  <!-- ファイル名: 001.JPG -->

<!-- ✅ 完全一致させる -->
<img src="images/products/001.JPG">
```

**確認3: DevToolsでエラー確認**
```
F12 → Consoleタブ
→ "404 Not Found" エラーがないか確認
```

---

### ❌ 問題: 画像の縦横比がおかしい

**症状**
```
画像が縦長・横長に伸びる
正方形にならない
```

**原因**
- `aspect-ratio`が効いていない
- `object-fit`の指定ミス

**✅ 解決方法**

```css
.product__thumb {
    width: 100%;
    aspect-ratio: 1;  /* 正方形 */
    object-fit: contain;  /* 画像全体を表示 */
    /* または */
    object-fit: cover;  /* 枠に合わせてトリミング */
}
```

**古いブラウザ対応**
```css
/* aspect-ratio非対応の場合 */
.product__thumb {
    width: 100%;
    height: 0;
    padding-bottom: 100%;  /* width と同じ高さ */
    position: relative;
}

.product__thumb img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
}
```

---

### ❌ 問題: 画像が荒い・ぼやける

**症状**
```
画像が粗くてギザギザ
ぼやけて見える
```

**原因**
- 元画像のサイズが小さい
- 拡大しすぎ

**✅ 解決方法**

**推奨画像サイズ**
```
商品画像: 500×500px 以上
ロゴ: 200×200px 以上
ヒーロー画像: 1920×1080px 以上
```

**一時的な対処（プレースホルダー使用）**
```html
<!-- グレーボックスで代用 -->
<div style="width: 100%; aspect-ratio: 1; background: #ddd;"></div>
```

---

## 5. アニメーションの問題

### ❌ 問題: ホバーアニメーションが効かない

**症状**
```
マウスを乗せても何も変わらない
```

**原因**
- セレクタが間違っている
- `transition`がない
- `a`タグに`href`属性がない

**✅ 解決方法**

**確認1: セレクタ**
```css
/* ❌ 間違い */
.product-index__block:hover {
    background-color: gray;
}

/* ✅ 正しい（hrefがある場合のみ） */
.product-index__block[href]:hover {
    background-color: gray;
}
```

**確認2: transition**
```css
.product-index__block {
    background-color: white;
    transition: background-color 0.2s;  /* 必須 */
}

.product-index__block[href]:hover {
    background-color: gray;
}
```

**確認3: href属性**
```html
<!-- ❌ href がない -->
<a class="product-index__block">

<!-- ✅ href がある -->
<a href="#" class="product-index__block">
```

---

### ❌ 問題: 画像のズームがカクカクする

**症状**
```
画像が滑らかに拡大しない
動きがカクつく
```

**原因**
- `transition`の設定が不適切
- `scale`ではなく`transform`を使っている

**✅ 解決方法**

**方法1: scaleを使う（推奨）**
```css
.product__thumb {
    transition: scale 0.4s;  /* スムーズ */
}

.product-index__block[href]:hover .product__thumb {
    scale: 1.1;
}
```

**方法2: transformを使う**
```css
.product__thumb {
    transition: transform 0.4s;
}

.product-index__block[href]:hover .product__thumb {
    transform: scale(1.1);
}
```

**方法3: GPUアクセラレーションを有効化**
```css
.product__thumb {
    transform: translateZ(0);  /* GPUを使う */
    will-change: scale;  /* 最適化ヒント */
}
```

---

### ❌ 問題: アニメーション速度が変えられない

**症状**
```
0.4s と書いても速度が変わらない
```

**原因**
- `transition-duration`の位置が間違っている
- 単位がない

**✅ 解決方法**

```css
/* ❌ 間違い */
.product__thumb {
    transition: scale;  /* 速度がない */
}

/* ✅ 正しい */
.product__thumb {
    transition: scale 0.4s;  /* 0.4秒 */
}

/* または */
.product__thumb {
    transition-property: scale;
    transition-duration: 0.4s;
}
```

**速度のバリエーション**
```css
transition: scale 0.1s;  /* 速い */
transition: scale 0.3s;  /* 普通 */
transition: scale 0.6s;  /* ゆっくり */
transition: scale 1s;    /* とてもゆっくり */
```

---

## 6. その他の問題

### ❌ 問題: CSS変数が効かない

**症状**
```
var(--c-primary-1) が表示されない
色が反映されない
```

**原因**
- 変数が定義されていない
- スコープが間違っている
- ブラウザが古い

**✅ 解決方法**

**確認1: 変数の定義**
```css
/* style.cssの最初に定義 */
:root {
    --c-primary-1: #103381;
}
```

**確認2: 使用方法**
```css
/* ❌ 間違い */
color: --c-primary-1;

/* ✅ 正しい */
color: var(--c-primary-1);
```

**確認3: DevToolsで確認**
```
F12 → Computed → Filter
→ --c-primary-1 と入力
→ 値が表示されるか確認
```

---

### ❌ 問題: コードが長すぎて読めない

**症状**
```
どこに何があるか分からない
編集したい場所が見つからない
```

**原因**
- コメントがない
- 整理されていない

**✅ 解決方法**

**コメントで区切る**
```css
/* ========================================
   商品グリッド
======================================== */
.product-index {
    /* スタイル */
}

/* ----- カードスタイル ----- */
.product-index__block {
    /* スタイル */
}

/* ----- 画像スタイル ----- */
.product__thumb {
    /* スタイル */
}
```

**VS Codeの便利機能**
```
Ctrl + F: 検索
Ctrl + Shift + F: 全体検索
Ctrl + /: コメントアウト
Alt + ↑/↓: 行を移動
```

---

### ❌ 問題: ブラウザで確認できない

**症状**
```
HTMLをダブルクリックしても開かない
ブラウザで真っ白
```

**原因**
- ファイルの拡張子が間違っている
- 文字コードの問題

**✅ 解決方法**

**確認1: ファイル拡張子**
```
❌ index.html.txt
❌ index.htm
✅ index.html
```

**確認2: 文字コード**
```html
<!-- HTMLファイルの先頭に必須 -->
<meta charset="UTF-8">
```

**確認3: ブラウザで開く**
```
1. ファイルを右クリック
2. 「プログラムから開く」
3. Chrome または Firefox を選択
```

---

## 🚀 デバッグの基本フロー

### ステップ1: 問題を特定する
```
「何が」おかしいのか明確にする
例: 「画像が表示されない」
　　「グリッドが3列にならない」
```

### ステップ2: DevToolsで確認
```
F12 → Elements → 該当要素を選択
→ Styles パネルで適用されているCSSを確認
→ 打ち消し線があれば上書きされている
```

### ステップ3: 一時的に削除して確認
```css
/* 問題のある箇所をコメントアウト */
/* display: grid; */
```

### ステップ4: 段階的に戻す
```css
/* 1つずつコメントを外して動作確認 */
display: grid;
/* grid-template-columns: repeat(3, 1fr); */
```

### ステップ5: 解決したら記録
```
「この問題は○○が原因だった」
「次は○○をチェックする」
```

---

## 📚 学習リソース

### 公式ドキュメント
- [MDN Web Docs](https://developer.mozilla.org/ja/) - CSS/HTMLリファレンス
- [Can I use](https://caniuse.com/) - ブラウザ対応確認

### デバッグツール
- Chrome DevTools - 最も多機能
- Firefox Developer Tools - グリッドビジュアライザが優秀

### 質問サイト
- [Stack Overflow](https://stackoverflow.com/) - 英語
- [teratail](https://teratail.com/) - 日本語

---

## 💡 予防策

### 1. こまめに確認
```
コードを書く → ブラウザで確認
の繰り返し（5分ごと）
```

### 2. Git でバックアップ
```bash
git add .
git commit -m "グリッドレイアウト完成"
```

### 3. コメントを残す
```css
/* 2024-01-15: グリッドを3列から5列に変更 */
.product-index {
    --row: 5;
}
```

### 4. 段階的に進める
```
一度にすべて書かない
→ 1つずつ確認しながら進める
```

---

**🎯 困ったときは**

1. このガイドで該当する問題を探す
2. DevToolsで確認
3. リファレンスを見る
4. それでも解決しない場合は休憩

**焦らず、1つずつ確実に進めましょう！**
