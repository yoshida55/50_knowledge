# 📘 Omodakaya.jp CSS実践リファレンス

> 実際のプロフェッショナルサイトから学ぶ、再利用可能なCSSパターン集

---

## 目次
1. [デザインシステム（CSS変数）](#1-デザインシステムcss変数)
2. [レスポンシブ設計戦略](#2-レスポンシブ設計戦略)
3. [レイアウトパターン](#3-レイアウトパターン)
4. [コンポーネント実装例](#4-コンポーネント実装例)
5. [アニメーション/トランジション](#5-アニメーショントランジション)
6. [実践的な学習のコツ](#6-実践的な学習のコツ)

---

## 1. デザインシステム（CSS変数）

### 🎨 なぜCSS変数を使うのか
- **一箇所変更で全体に反映** → メンテナンス性が大幅向上
- **テーマの切り替えが容易** → ダークモード対応なども簡単
- **可読性が高い** → `#6B6B5B` より `var(--c-blk-1)` の方が意味が明確

### 📐 Omodakayaの変数定義パターン

```css
/* ===== 色の定義 ===== */
:root {
    /* 基本色（接頭辞: c = color） */
    --c-blk-1: #6B6B5B;           /* メインテキスト色 */
    --c-primary-1: #103381;        /* プライマリーカラー（青） */
    --c-primary-2: rgba(16, 51, 129, 0.2);  /* プライマリー薄め */
    
    /* グレースケール */
    --c-gray-1: #DDDDDD;           /* ボーダー用 */
    --c-gray-2: #EBE7E1;           /* 背景用（薄いベージュ） */
    --c-gray-3: rgb(245, 245, 245);/* 背景用（薄いグレー） */
}
```

**💡 命名規則のコツ**
- `--c-` = color（色）
- `--f-` = font（フォント）
- `--space-` = spacing（余白）
- 数字は「濃さ」や「サイズ」を表す（1が標準、2が薄い/小さい）

```css
/* ===== フォントの定義 ===== */
:root {
    --f-serif: "Noto Serif JP", serif;     /* 明朝体（見出し用） */
    --f-sans: "dnp-shuei-gothic-gin-std", sans-serif;  /* ゴシック体（本文用） */
    --f-en: "Manrope", "dnp-shuei-gothic-gin-std", sans-serif;  /* 英数字用 */
}
```

```css
/* ===== レイアウト用変数 ===== */
:root {
    --view: 1296px;        /* コンテンツ最大幅 */
    --space-vrt: 120px;    /* 縦方向の余白 */
    --space-hor: 20px;     /* 横方向の余白（左右マージン） */
}

/* 画面サイズに応じて余白を変更 */
@media screen and (min-width: 768px) {
    :root {
        --space-vrt: 160px;
        --space-hor: 40px;
    }
}

@media screen and (min-width: 1025px) {
    :root {
        --space-vrt: 240px;
        --space-hor: 80px;
    }
}
```

**🎯 実装のポイント**
- 変数を変更するだけで、全画面サイズの余白が一括変更できる
- メディアクエリ内で変数を再定義することで、レスポンシブに対応

---

## 2. レスポンシブ設計戦略

### 📱 モバイルファースト設計

**基本の考え方**
1. **デフォルト = スマホ（〜767px）**
2. **タブレット（768px〜1024px）**で拡張
3. **PC（1025px〜）**でさらに拡張

```css
/* ===== モバイルファーストの実例 ===== */

/* 1. まずスマホのスタイルを書く（メディアクエリなし） */
body {
    font-size: 14px;  /* スマホサイズ */
}

/* 2. タブレット以上で上書き */
@media screen and (min-width: 768px) {
    body {
        font-size: 15px;  /* タブレットサイズ */
    }
}

/* 3. PC以上でさらに上書き */
@media screen and (min-width: 1025px) {
    body {
        font-size: 16px;  /* PCサイズ */
    }
}
```

### 🎯 ブレークポイント一覧

```css
/* ===== Omodakayaのブレークポイント ===== */

/* スマホ */
/* 〜767px: メディアクエリなし（デフォルト） */

/* タブレット */
@media screen and (min-width: 768px) { }
@media screen and (max-width: 1024px) { }

/* PC */
@media screen and (min-width: 1025px) { }

/* 大画面PC */
@media (min-width: 1456px) {  /* 1296px(コンテンツ幅) + 160px(余白) */
    /* 超大画面での余白調整など */
}
```

### 💡 レスポンシブレイアウトの実例

```css
/* ===== 縦並び→横並びへの切り替え ===== */
.container-split {
    display: flex;
}

/* スマホ: 縦並び */
@media screen and (max-width: 1024px) {
    .container-split {
        flex-direction: column;
        gap: 60px;
    }
}

/* PC: 横並び */
@media screen and (min-width: 1025px) {
    .container-split {
        gap: 50px;
    }
    
    .container-split__heading {
        width: calc(280/1296 * 100%);  /* 比率計算 */
    }
    
    .container-split__inner {
        flex: 1;  /* 残りのスペースを埋める */
    }
}
```

**📐 比率計算の技**
- `calc(280/1296 * 100%)` = 全体幅1296pxのうち280pxを占める比率
- 親要素のサイズが変わっても比率を維持できる

---

## 3. レイアウトパターン

### 🧩 コンテナパターン

#### パターン1: 基本コンテナ（左右余白付き）

```css
.container-sec {
    width: calc(100% - var(--space-hor) * 2);  /* 左右に余白 */
    max-width: var(--view);  /* 最大幅を制限 */
    margin: var(--space-vrt) auto;  /* 上下に余白、左右は中央揃え */
}
```

**使用例**
```html
<section class="container-sec">
    <h2>セクション見出し</h2>
    <p>本文テキスト...</p>
</section>
```

#### パターン2: 全幅背景付きコンテナ

```css
.container-sec--bg {
    /* 背景色を画面いっぱいに広げたい場合 */
    padding: var(--space-vrt) var(--space-hor);
    position: relative;
    z-index: 0;
}

/* 大画面では左右の余白を調整 */
@media (min-width: 1456px) {
    .container-sec--bg {
        padding: var(--space-vrt) calc((100% - var(--view))/2);
    }
}
```

### 📦 グリッドレイアウト

```css
/* ===== 商品一覧のグリッド ===== */
.product-index {
    --row: 3;  /* 列数を変数化 */
    display: grid;
    grid-template-columns: repeat(var(--row), 1fr);  /* 均等な列 */
    overflow: hidden;
    padding-top: 1px;
}

/* タブレット: 4列 */
@media (min-width: 801px) {
    .product-index {
        --row: 4;
    }
}

/* PC: 5列 */
@media (min-width: 1101px) {
    .product-index {
        --row: 5;
    }
}
```

**🎯 グリッドレイアウトのメリット**
- 変数を変えるだけで列数変更
- `1fr` = 利用可能なスペースを均等分割
- Flexboxより複雑なレイアウトに向いている

### 🔄 Flexboxパターン

#### パターン1: 上下中央揃え

```css
.center-box {
    display: flex;
    flex-direction: column;  /* 縦方向に並べる */
    justify-content: center; /* 縦方向の中央 */
    align-items: center;     /* 横方向の中央 */
    min-height: 100vh;       /* 画面いっぱいの高さ */
}
```

#### パターン2: 左右配置（片方固定、片方伸縮）

```css
.split-layout {
    display: flex;
}

.split-layout__sidebar {
    width: 280px;  /* 固定幅 */
    flex-shrink: 0; /* 縮小しない */
}

.split-layout__main {
    flex: 1;  /* 残りのスペースを埋める */
}
```

---

## 4. コンポーネント実装例

### 🔘 ボタンコンポーネント

```css
/* ===== 基本的なリンクボタン ===== */
.btn-link {
    display: flex;
    align-items: center;
    gap: 5px;
    color: var(--c-primary-1);
    line-height: 1.5;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 0.1em;
}

@media screen and (min-width: 768px) {
    .btn-link {
        font-size: 17px;
        gap: 10px;
    }
}

/* ホバー時のアニメーション */
.btn-link:hover > span {
    text-decoration: underline;
    text-decoration-thickness: 1px;
}
```

**HTML例**
```html
<a href="#" class="btn-link">
    <span>もっと見る</span>
    <span class="arrow-link"></span>
</a>
```

### 🏷️ カードコンポーネント

```css
/* ===== 商品カード ===== */
.product-index__block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
    padding: 15px 12px;
    border: solid var(--c-gray-1);
    border-width: 0 0 1px 0;  /* 下線のみ */
    position: relative;
    transition: background-color 0.1s;
}

/* ホバー時の背景色変更 */
.product-index__block[href]:hover {
    background-color: var(--c-gray-3);
}

/* 画像のズームアニメーション */
.product-index__block[href]:hover .product__thumb {
    scale: 1.1;
}
```

### 📰 ニュース一覧

```css
.news-index__block {
    display: flex;
    gap: 15px;
    padding: 30px 0;
    border-top: 1px solid var(--c-gray-1);
    position: relative;
}

/* サムネイル */
.news-index .news__thumb {
    align-self: center;
    width: calc(128/336 * 100%);  /* 比率指定 */
    min-width: 128px;
    max-width: 180px;
}

/* 本文エリア */
.news-index .news__details {
    flex: 1;  /* 残りスペースを埋める */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
}
```

---

## 5. アニメーション/トランジション

### ✨ 基本的なトランジション

```css
/* ===== ホバー時のフェードアウト ===== */
.hover-fade {
    transition: opacity 0.2s;
}

.hover-fade:hover {
    opacity: 0.8;
}
```

### 🎬 スクロールアニメーション（フェードイン）

```css
/* ===== 画面に入ったときにフェードイン ===== */
.js-inview-fadein {
    opacity: 0;
    translate: 0 10px;  /* 少し下から */
    transition: opacity, translate;
    transition-duration: 1s;
}

.js-inview-fadein.inviewed {
    opacity: 1;
    translate: 0 0;
}
```

**JavaScript側で`.inviewed`クラスを追加**

### 🌊 無限スクロールアニメーション

```css
/* ===== ショップ情報のスクロール ===== */
.shop-info > .shop-info__inner {
    animation: infinity-scroll-left 20s infinite linear both;
}

@keyframes infinity-scroll-left {
    from {
        translate: 0 0;
    }
    to {
        translate: -100% 0;  /* 自分の幅分だけ左に移動 */
    }
}
```

**HTML構造**
```html
<div class="shop-info">
    <div class="shop-info__inner">
        <div class="shop-info__block">内容1</div>
        <div class="shop-info__block">内容2</div>
        <!-- 複製要素 -->
        <div class="shop-info__inner">
            <div class="shop-info__block">内容1</div>
            <div class="shop-info__block">内容2</div>
        </div>
    </div>
</div>
```

### 🎯 矢印アニメーション

```css
/* ===== 矢印が流れるアニメーション ===== */
@keyframes arrow_anim1 {
    0% {
        translate: 0 0;
    }
    50% {
        opacity: 0;
        translate: 50% 0;  /* 右に消える */
    }
    50.1% {
        opacity: 0;
        translate: -50% 0;  /* 左から出現 */
    }
    100% {
        opacity: 1;
        translate: 0 0;
    }
}

.arrow-link:after {
    animation: arrow_anim1 750ms;
}
```

---

## 6. 実践的な学習のコツ

### 🛠️ DevToolsでの分析方法

#### ステップ1: 要素を選択
1. 右クリック → 「検証」
2. 要素パネルで該当要素を選択

#### ステップ2: 適用されているスタイルを確認
```
Styles パネル:
├─ element.style  ← インラインスタイル
├─ .product-index__block  ← クラススタイル
├─ *  ← ユニバーサルセレクタ
└─ Inherited from...  ← 継承されたスタイル
```

#### ステップ3: Computed（計算済み）タブで最終値を確認
- `margin: 30px 0` が実際どう計算されているか
- 継承元も追跡できる

### 📝 効率的な模写の手順

#### 1. 全体構造を把握
```
├─ header（固定ヘッダー）
├─ main
│   ├─ section（余白付きコンテナ）
│   │   ├─ h2（見出し）
│   │   └─ div（コンテンツ）
│   └─ section
└─ footer
```

#### 2. 大枠から作る
1. **HTML骨組み** → セマンティックタグで構造化
2. **レイアウト** → FlexboxまたはGridで配置
3. **余白** → margin/paddingで調整
4. **装飾** → 色・フォント・ボーダーなど

#### 3. 細部を作り込む
- ホバーアニメーション
- レスポンシブ対応
- 細かい余白調整

### 🎨 よく使うパターンの暗記

#### 中央揃え（Flexbox版）
```css
.center {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

#### 画像を親要素いっぱいに広げる
```css
.fill-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: 50% 50%;
}
```

#### ホバー時の透明度変更
```css
.hover-item {
    transition: opacity 0.2s;
}
.hover-item:hover {
    opacity: 0.8;
}
```

### 📚 段階的な学習ロードマップ

#### レベル1: 基礎固め
- [ ] ボックスモデル理解
- [ ] Flexbox基本（縦・横並び）
- [ ] 色・フォントの指定
- [ ] 余白調整（margin/padding）

#### レベル2: レイアウトマスター
- [ ] Flexboxの高度な使い方（space-between, flex: 1など）
- [ ] Grid基礎（repeat, 1fr）
- [ ] ポジショニング（absolute/relative）
- [ ] レスポンシブ対応（メディアクエリ）

#### レベル3: 応用テクニック
- [ ] CSS変数活用
- [ ] トランジション/アニメーション
- [ ] 疑似要素（::before/::after）
- [ ] 複雑なセレクタ

#### レベル4: 実践
- [ ] 実際のサイト模写
- [ ] DevToolsでの検証スキル
- [ ] パフォーマンス最適化
- [ ] ブラウザ互換性対応

---

## 🔑 重要な原則まとめ

### 1. モバイルファーストで書く
```css
/* ❌ 悪い例 */
.box { width: 1000px; }
@media (max-width: 768px) {
    .box { width: 100%; }
}

/* ✅ 良い例 */
.box { width: 100%; }
@media (min-width: 769px) {
    .box { width: 1000px; }
}
```

### 2. 変数を使って管理する
```css
/* ❌ 同じ色を何度も書く */
.header { background: #103381; }
.button { background: #103381; }
.link { color: #103381; }

/* ✅ 変数で一元管理 */
:root { --primary: #103381; }
.header { background: var(--primary); }
.button { background: var(--primary); }
.link { color: var(--primary); }
```

### 3. 命名規則を統一する
```css
/* BEM風 */
.block { }
.block__element { }
.block--modifier { }

/* 例: ニュースカード */
.news-card { }
.news-card__title { }
.news-card__image { }
.news-card--featured { }
```

### 4. コメントで構造を明示
```css
/* ========================================
   セクション: ヘッダー
======================================== */

/* ----- サブセクション: ナビゲーション ----- */
.header__nav { }

/* ----- サブセクション: ロゴ ----- */
.header__logo { }
```

---

## 📖 参考資料

### CSS学習リソース
- [MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/CSS) - 公式リファレンス
- [Can I use](https://caniuse.com/) - ブラウザ対応確認

### 便利ツール
- Chrome DevTools - 要素検証・スタイル確認
- Firefox Developer Tools - グリッドレイアウトの可視化が優秀

---

## ✅ チェックリスト（模写時に確認）

### HTML構造
- [ ] セマンティックタグを使用（header, main, sectionなど）
- [ ] 適切なクラス名を付与
- [ ] 画像にalt属性を設定

### CSS実装
- [ ] レスポンシブ対応（3ブレークポイント以上）
- [ ] ホバーアニメーション実装
- [ ] 余白の統一感（変数使用）
- [ ] フォントサイズの階層化

### 品質チェック
- [ ] DevToolsで各画面サイズを確認
- [ ] 実機確認（可能なら）
- [ ] HTML/CSSバリデーター通過
- [ ] 不要なコードの削除

---

**🎓 最後に**

このリファレンスは、omodakaya.jpの実装から抽出した「プロが使う実践パターン」です。

一度にすべて理解しようとせず、
1. 簡単なパターンから真似する
2. わからない部分はDevToolsで確認
3. 繰り返し手を動かす

この3ステップで着実にスキルアップしていきましょう！
