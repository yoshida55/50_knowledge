# 📅 Omodakaya.jp 商品一覧ページ模写 - 段階的作業手順

> 初心者でも迷わず進められる、ステップバイステップガイド

---

## 🎯 完成目標

**商品一覧ページの再現**
- スマホ（3列）→ タブレット（4列）→ PC（5列）のレスポンシブグリッド
- ホバーアニメーション付き
- プロレベルの余白・配置

**推定作業時間：8〜12時間**（初心者の場合）

---

## 📂 プロジェクト準備

### ステップ0: フォルダ構成

```
omodakaya-project/
├── index.html          ← HTMLファイル
├── style.css           ← CSSファイル
└── images/             ← 画像フォルダ
    ├── logo.png
    ├── icon-shop.svg
    ├── icon-mail.svg
    └── products/
        ├── 001.jpg
        ├── 002.jpg
        └── ...
```

### 画像の準備

**方法1: プレースホルダーを使う（推奨）**
```html
<!-- グレーボックスで代用 -->
<div style="width: 100%; aspect-ratio: 1; background: #ddd;"></div>
```

**方法2: フリー素材を使う**
- [Unsplash](https://unsplash.com/) - 商用利用OK
- [Pixabay](https://pixabay.com/) - 完全フリー

---

## 📆 作業スケジュール

### 【1日目】HTML構造作成（2〜3時間）

#### ✅ やること
1. HTMLファイルの基本構造
2. ヘッダー・メイン・フッター
3. 商品グリッドの骨組み

#### 📝 具体的な手順

**1-1. HTMLファイル作成**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商品一覧 - おもだか屋</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- ここに内容を追加していく -->
</body>
</html>
```

**1-2. ヘッダー追加**
```html
<header class="pageheader">
    <div class="pageheader__logo">
        <a href="/">ロゴ</a>
    </div>
</header>
```

**1-3. メインコンテンツの枠**
```html
<main>
    <section class="kv-second">
        <h1>商品一覧</h1>
    </section>
    
    <section class="container-sec">
        <!-- ここに商品グリッドを追加 -->
    </section>
</main>
```

**1-4. 商品グリッド（まず3個だけ）**
```html
<div class="product-index">
    <!-- 商品1 -->
    <a href="#" class="product-index__block">
        <div class="product__date">2024.01.15</div>
        <div style="width: 100%; aspect-ratio: 1; background: #ddd;"></div>
        <div class="product__data">
            <dl>
                <dt>商品名</dt>
                <dd>サイズ情報</dd>
            </dl>
        </div>
    </a>
    
    <!-- 商品2 -->
    <a href="#" class="product-index__block">
        <div class="product__date">2024.01.14</div>
        <div style="width: 100%; aspect-ratio: 1; background: #ddd;"></div>
        <div class="product__data">
            <dl>
                <dt>商品名</dt>
                <dd>サイズ情報</dd>
            </dl>
        </div>
    </a>
    
    <!-- 商品3 -->
    <a href="#" class="product-index__block">
        <div class="product__date">2024.01.13</div>
        <div style="width: 100%; aspect-ratio: 1; background: #ddd;"></div>
        <div class="product__data">
            <dl>
                <dt>商品名</dt>
                <dd>サイズ情報</dd>
            </dl>
        </div>
    </a>
</div>
```

**✅ 1日目の確認ポイント**
- [ ] HTMLファイルをブラウザで開ける
- [ ] テキストが表示されている
- [ ] グレーボックスが3つ並んでいる

---

### 【2日目】CSSリセット＆基本スタイル（2〜3時間）

#### ✅ やること
1. CSS変数の定義
2. リセットCSS
3. 基本のフォント・色設定

#### 📝 具体的な手順

**2-1. style.css作成**
```css
/* ========================================
   CSS変数（色・フォント・余白）
======================================== */
:root {
    /* 色 */
    --c-blk-1: #6B6B5B;
    --c-primary-1: #103381;
    --c-gray-1: #DDDDDD;
    --c-gray-2: #EBE7E1;
    --c-gray-3: rgb(245, 245, 245);
    
    /* フォント */
    --f-sans: "Hiragino Sans", "Meiryo", sans-serif;
    
    /* 余白 */
    --space-vrt: 120px;
    --space-hor: 20px;
}

/* タブレット以上 */
@media screen and (min-width: 768px) {
    :root {
        --space-vrt: 160px;
        --space-hor: 40px;
    }
}

/* PC以上 */
@media screen and (min-width: 1025px) {
    :root {
        --space-vrt: 240px;
        --space-hor: 80px;
    }
}
```

**2-2. リセットCSS**
```css
/* ========================================
   リセット
======================================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--f-sans);
    color: var(--c-blk-1);
    line-height: 2;
    font-size: 14px;
}

@media screen and (min-width: 768px) {
    body { font-size: 15px; }
}

@media screen and (min-width: 1025px) {
    body { font-size: 16px; }
}

a {
    color: inherit;
    text-decoration: none;
}

img {
    max-width: 100%;
    height: auto;
    vertical-align: bottom;
}
```

**✅ 2日目の確認ポイント**
- [ ] CSSが読み込まれている（文字色が変わった）
- [ ] 余白がリセットされている
- [ ] フォントが適用されている

---

### 【3日目】グリッドレイアウト作成（3〜4時間）

#### ✅ やること
1. 商品グリッドの配置
2. レスポンシブ対応（3列→4列→5列）
3. カード内部のレイアウト

#### 📝 具体的な手順

**3-1. グリッドレイアウト**
```css
/* ========================================
   商品グリッド
======================================== */
.product-index {
    --row: 3;  /* デフォルト3列 */
    display: grid;
    grid-template-columns: repeat(var(--row), 1fr);
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

**3-2. カードのスタイル**
```css
.product-index__block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
    padding: 15px 12px;
    border: solid var(--c-gray-1);
    border-width: 0 0 1px 0;
    position: relative;
    transition: background-color 0.1s;
}

/* タブレット以上 */
@media screen and (min-width: 768px) {
    .product-index__block {
        padding: 20px;
        gap: 20px;
    }
}

/* PC以上 */
@media screen and (min-width: 1025px) {
    .product-index__block {
        padding: 30px;
    }
}
```

**3-3. グリッドのボーダー**
```css
/* 上のボーダー */
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

/* 右のボーダー */
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

**✅ 3日目の確認ポイント**
- [ ] スマホで3列表示
- [ ] タブレットで4列表示
- [ ] PCで5列表示
- [ ] グリッド線が綺麗に表示

**確認方法**
1. DevToolsを開く（F12）
2. デバイスツールバーをクリック（Ctrl+Shift+M）
3. 375px → 768px → 1200pxと変えて確認

---

### 【4日目】細部のスタイリング（2〜3時間）

#### ✅ やること
1. 日付・商品名・サイズ情報のスタイル
2. 画像のアスペクト比
3. 余白の微調整

#### 📝 具体的な手順

**4-1. 日付のスタイル**
```css
.product__date {
    font-family: "Georgia", serif;
    font-size: 8px;
    letter-spacing: 0.05em;
    line-height: 1;
}

@media screen and (min-width: 768px) {
    .product__date { font-size: 10px; }
}

@media screen and (min-width: 1025px) {
    .product__date { font-size: 12px; }
}
```

**4-2. 画像のスタイル**
```css
.product__thumb {
    width: 100%;
    aspect-ratio: 1;  /* 正方形 */
    object-fit: contain;  /* 画像全体を表示 */
    transition: scale 0.4s, rotate 0.4s;
}
```

**4-3. 商品データのスタイル**
```css
.product__data {
    font-size: 10px;
    line-height: 1.5;
}

@media screen and (min-width: 768px) {
    .product__data { font-size: 11px; }
}

@media screen and (min-width: 1025px) {
    .product__data { font-size: 12px; }
}

.product__data > dl {
    display: flex;
    flex-direction: column;
    gap: 0.25em;
}

.product__data > dl > dt {
    font-weight: 500;
}

.product__data > dl > dd {
    font-size: 0.9em;
    opacity: 0.7;
}
```

**✅ 4日目の確認ポイント**
- [ ] 文字サイズが適切
- [ ] 画像が正方形
- [ ] 商品名と説明のスタイルが区別できる

---

### 【5日目】ホバーアニメーション（1〜2時間）

#### ✅ やること
1. カード背景色の変化
2. 画像のズーム効果
3. トランジションの調整

#### 📝 具体的な手順

**5-1. ホバー時の背景色**
```css
.product-index__block[href]:hover {
    background-color: var(--c-gray-3);
}
```

**5-2. 画像のズーム**
```css
.product-index__block[href]:hover .product__thumb {
    scale: 1.1;  /* 1.1倍に拡大 */
}
```

**5-3. スムーズなアニメーション**
```css
.product-index__block {
    transition: background-color 0.1s;
}

.product__thumb {
    transition: scale 0.4s, rotate 0.4s;
}
```

**✅ 5日目の確認ポイント**
- [ ] ホバーで背景色が変わる
- [ ] 画像がズームする
- [ ] アニメーションがスムーズ

---

### 【6日目】ヘッダー・フッター（2〜3時間）

#### ✅ やること
1. ヘッダーの固定
2. フッターのレイアウト
3. ナビゲーション

#### 📝 具体的な手順

**6-1. ヘッダー固定**
```css
.pageheader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.9);
    z-index: 100;
}

/* ヘッダーの高さ分だけbodyにpaddingを追加 */
body {
    padding-top: 80px;
}
```

**6-2. フッター**
```css
.pagefooter {
    padding: 70px 20px 15px;
    margin-top: 120px;
}

@media screen and (min-width: 768px) {
    .pagefooter {
        padding: 70px 30px 20px;
        margin-top: 140px;
    }
}

@media screen and (min-width: 1025px) {
    .pagefooter {
        padding: 100px 70px 30px;
        margin-top: 160px;
    }
}
```

**✅ 6日目の確認ポイント**
- [ ] ヘッダーがスクロールしても固定
- [ ] フッターが最下部に配置
- [ ] リンクが機能する

---

### 【7日目】最終調整・検証（2〜3時間）

#### ✅ やること
1. 全画面サイズでの確認
2. 不要なコードの削除
3. コメントの追加

#### 📝 確認項目

**7-1. DevToolsで検証**
```
チェックする画面サイズ:
□ 375px (iPhone)
□ 768px (iPad縦)
□ 1024px (iPad横)
□ 1200px (ノートPC)
□ 1920px (デスクトップ)
```

**7-2. 動作確認**
```
□ ホバーアニメーション
□ リンクのクリック
□ 画像の読み込み
□ スクロール動作
□ グリッドの配置
```

**7-3. コード品質**
```
□ インデント統一
□ コメント追加
□ 不要なコード削除
□ HTML/CSSバリデーション
```

---

## 🎯 完成後のチェックリスト

### 機能面
- [ ] スマホ（3列）→タブレット（4列）→PC（5列）のグリッド
- [ ] ホバー時の背景色変更
- [ ] 画像のズームアニメーション
- [ ] ヘッダー固定
- [ ] フッター配置

### 品質面
- [ ] 全ブレークポイントで崩れなし
- [ ] アニメーションがスムーズ
- [ ] コードが整理されている
- [ ] コメントが適切

### 学習面
- [ ] Gridレイアウトの理解
- [ ] CSS変数の活用
- [ ] レスポンシブ設計の理解
- [ ] ホバーアニメーションの実装

---

## 📚 困ったときの解決フロー

### 1. まずDevToolsで確認
```
右クリック → 検証 → Elementsタブ
→ Stylesパネルで適用されているCSSを確認
```

### 2. リファレンスを確認
- `omodakaya-css-reference.md` を参照
- 元サイトのCSSと比較

### 3. トラブルシューティング参照
- `omodakaya-troubleshooting.md` を確認

### 4. 段階的にコメントアウト
```css
/* 問題のある箇所を特定 */
/* .product-index { display: grid; } */
```

---

## 💡 時短テクニック

### 1. Emmetを使う
```
.product-index__block*10
→ 10個のブロックを一気に生成
```

### 2. CSSスニペット
```css
/* デバッグ用ボーダー（一時的に使う） */
* { outline: 1px solid red; }
```

### 3. ライブリロード
- VS Code拡張機能「Live Server」を使用
- 保存するとブラウザが自動更新

---

## 🎉 完成したら

### 次のステップ
1. **詳細ページを作る** - 単一商品ページ
2. **トップページを作る** - より複雑なレイアウト
3. **JavaScriptを追加** - スライダー、モーダルなど

### ポートフォリオに追加
```
完成したらGitHubにアップロード:
1. git init
2. git add .
3. git commit -m "Omodakaya商品一覧ページ完成"
4. git remote add origin [URL]
5. git push -u origin main
```

---

**🏆 完成おめでとうございます！**

この手順を完走できたら、あなたは「実践的なレスポンシブサイト」を作れる実力があります。

次のプロジェクトに進みましょう！
