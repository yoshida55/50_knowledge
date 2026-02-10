# AOS.js - スクロールアニメーション

★ 最新版 **AOS v3.0.0-beta.6** を使用

## 📚 目次ページ
📺 **[デモ一覧を見る](../../images/index.html)**

---

## ✅ ① シンプル版【まずはここから】

💡 **まずはここから！AOS.js本来の姿**

★ **用途**: AOS.jsの学習、シンプルな実装
★ **ポイント**: AOS.jsの機能のみ、最小限のコード

### 📋 特徴

| 項目 | 内容 |
|------|------|
| AOS機能 | ✅ fade、duration、delay、once |
| カスタムCSS | ✅ 最小限 |
| コード量 | 少ない |
| 学習難易度 | ✅ 簡単 |
| カスタマイズ | ✅ 簡単 |

### HTML
```html
<div class="container">
  <h1>AOS.js シンプル版</h1>

  <!-- 基本的なフェードイン（data-aos="fade"のみ） -->
  <div class="box" data-aos="fade">
    <h2>基本フェード</h2>
    <p>data-aos="fade" を指定するだけで、スクロール時にフェードイン表示されます。これがAOS.jsの最もシンプルな使い方です。</p>
  </div>

  <div class="spacer"></div>

  <!-- 持続時間を指定（data-aos-duration） -->
  <div class="box" data-aos="fade" data-aos-duration="1000">
    <h2>持続時間の指定</h2>
    <p>data-aos-duration="1000" で1秒かけてフェードイン。持続時間は50〜3000ミリ秒で指定できます。</p>
  </div>

  <div class="spacer"></div>

  <!-- 遅延を指定（data-aos-delay） -->
  <div class="box" data-aos="fade" data-aos-duration="800" data-aos-delay="200">
    <h2>遅延の指定</h2>
    <p>data-aos-delay="200" で0.2秒遅らせて開始。要素を順次表示する際に便利です。</p>
  </div>

  <div class="spacer"></div>

  <!-- 1回のみ実行（data-aos-once） -->
  <div class="box" data-aos="fade" data-aos-duration="800" data-aos-once="true">
    <h2>1回のみ実行</h2>
    <p>data-aos-once="true" で、スクロールで1回だけアニメーション実行。デフォルトは何度でも実行されます。</p>
  </div>

  <div class="spacer"></div>
</div>
```

### CSS
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 60px 20px 40px;
}
.container {
  max-width: 800px;
  margin: 0 auto;
}
h1 {
  text-align: center;
  color: white;
  font-size: 48px;
  margin-bottom: 60px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.box {
  background: white;
  padding: 40px;
  margin-bottom: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.box h2 {
  color: #667eea;
  margin-bottom: 15px;
  font-size: 28px;
}
.box p {
  color: #666;
  line-height: 1.8;
  font-size: 16px;
}
.spacer {
  height: 100vh;
}
```

### JavaScript
```javascript
// AOS初期化（最小限の設定）
AOS.init({
  duration: 800,  // デフォルト持続時間
  once: false,    // 何度でも実行（スクロールで繰り返し）
  offset: 120     // トリガーオフセット（要素が画面に入る位置）
});
```

---

## 🥇 ② フェードエフェクト集

💡 **用途**: 上下左右からのフェードイン実装

★ **ポイント**: 4方向のフェードエフェクト

### 📋 特徴

| 項目 | 内容 |
|------|------|
| AOS機能 | ✅ fade-up/down/left/right |
| 実務での用途 | ✅ カード一覧、セクション表示 |

### HTML
```html
<div class="container">
  <h1>フェードエフェクト集</h1>

  <!-- 下から上へ -->
  <div class="box" data-aos="fade-up">
    <h2>↑ Fade Up</h2>
    <p>下から上へフェードイン。最もよく使われるエフェクトです。</p>
  </div>

  <div class="spacer"></div>

  <!-- 上から下へ -->
  <div class="box" data-aos="fade-down">
    <h2>↓ Fade Down</h2>
    <p>上から下へフェードイン。見出しやヘッダー要素に適しています。</p>
  </div>

  <div class="spacer"></div>

  <!-- 右から左へ -->
  <div class="box" data-aos="fade-left">
    <h2>← Fade Left</h2>
    <p>右から左へフェードイン。画像とテキストを組み合わせる際に効果的です。</p>
  </div>

  <div class="spacer"></div>

  <!-- 左から右へ -->
  <div class="box" data-aos="fade-right">
    <h2>→ Fade Right</h2>
    <p>左から右へフェードイン。交互に表示する際に使います。</p>
  </div>

  <div class="spacer"></div>
</div>
```

### CSS
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  padding: 60px 20px 40px;
}
.container {
  max-width: 800px;
  margin: 0 auto;
}
h1 {
  text-align: center;
  color: white;
  font-size: 48px;
  margin-bottom: 60px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.box {
  background: white;
  padding: 40px;
  margin-bottom: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.box h2 {
  color: #f5576c;
  margin-bottom: 15px;
  font-size: 28px;
}
.box p {
  color: #666;
  line-height: 1.8;
  font-size: 16px;
}
.spacer {
  height: 100vh;
}
```

### JavaScript
```javascript
AOS.init({
  duration: 1000,  // 少し長めのアニメーション
  once: false,
  offset: 120
});
```

---

## 🥈 ③ スライドエフェクト集

💡 **用途**: スライド・ズーム・回転アニメーション

★ **ポイント**: 多彩なエフェクトを試す

### 📋 特徴

| 項目 | 内容 |
|------|------|
| AOS機能 | ✅ slide/zoom/flip |
| 実務での用途 | ✅ 注目要素、特別なセクション |

### HTML
```html
<div class="container">
  <h1>スライドエフェクト集</h1>

  <!-- 下からスライド -->
  <div class="box" data-aos="slide-up">
    <h2>⬆ Slide Up</h2>
    <p>下からスライドイン。フェードより動きが大きく目立ちます。</p>
  </div>

  <div class="spacer"></div>

  <!-- 上からスライド -->
  <div class="box" data-aos="slide-down">
    <h2>⬇ Slide Down</h2>
    <p>上からスライドイン。ドロップダウン風の演出に。</p>
  </div>

  <div class="spacer"></div>

  <!-- ズームイン -->
  <div class="box" data-aos="zoom-in">
    <h2>🔍 Zoom In</h2>
    <p>ズームイン。注目を集めたい要素に使います。</p>
  </div>

  <div class="spacer"></div>

  <!-- 回転 -->
  <div class="box" data-aos="flip-left">
    <h2>🔄 Flip Left</h2>
    <p>左回転。派手な演出が必要な場合に。</p>
  </div>

  <div class="spacer"></div>
</div>
```

### CSS
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #4bc0c8 0%, #c779d0 100%);
  padding: 60px 20px 40px;
}
.container {
  max-width: 800px;
  margin: 0 auto;
}
h1 {
  text-align: center;
  color: white;
  font-size: 48px;
  margin-bottom: 60px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.box {
  background: white;
  padding: 40px;
  margin-bottom: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.box h2 {
  color: #4bc0c8;
  margin-bottom: 15px;
  font-size: 28px;
}
.box p {
  color: #666;
  line-height: 1.8;
  font-size: 16px;
}
.spacer {
  height: 100vh;
}
```

### JavaScript
```javascript
AOS.init({
  duration: 1200,  // さらに長めのアニメーション
  once: false,
  offset: 120
});
```

---

## 🥉 ④ 多機能版【応用例】

💡 **用途**: 実務での実装パターン

★ **ポイント**: 複数エフェクト組み合わせ、順次表示

### 📋 特徴

| 項目 | 内容 |
|------|------|
| AOS機能 | ✅ 複数エフェクト + delay + easing |
| 実務での用途 | ✅ LP、ポートフォリオサイト |
| コード量 | 多い |

### HTML
```html
<div class="container">
  <h1 data-aos="zoom-in" data-aos-duration="1000">AOS.js 多機能版</h1>

  <p class="subtitle" data-aos="fade-up" data-aos-delay="300">
    複数のエフェクトとオプションを組み合わせた応用例
  </p>

  <div class="spacer"></div>

  <!-- カード一覧の順次表示 -->
  <h2 class="section-title" data-aos="fade-down">カード一覧（順次表示）</h2>

  <div class="card-grid">
    <div class="card" data-aos="fade-up" data-aos-delay="0">
      <h3>カード 1</h3>
      <p>遅延0ms。最初に表示されます。</p>
    </div>

    <div class="card" data-aos="fade-up" data-aos-delay="100">
      <h3>カード 2</h3>
      <p>遅延100ms。少し遅れて表示。</p>
    </div>

    <div class="card" data-aos="fade-up" data-aos-delay="200">
      <h3>カード 3</h3>
      <p>遅延200ms。順次表示の完成。</p>
    </div>
  </div>

  <div class="spacer"></div>

  <!-- イージングの違い -->
  <h2 class="section-title" data-aos="fade-down">イージングのカスタマイズ</h2>

  <div class="box" data-aos="fade-right" data-aos-easing="linear">
    <h3>Linear</h3>
    <p>一定速度で動きます。</p>
  </div>

  <div class="spacer-small"></div>

  <div class="box" data-aos="fade-right" data-aos-easing="ease-in-out">
    <h3>Ease In Out</h3>
    <p>ゆっくり始まり、ゆっくり終わります。</p>
  </div>

  <div class="spacer"></div>
</div>
```

### CSS
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #feac5e 0%, #c779d0 50%, #4bc0c8 100%);
  padding: 60px 20px 40px;
}
.container {
  max-width: 1000px;
  margin: 0 auto;
}
h1 {
  text-align: center;
  color: white;
  font-size: 48px;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.subtitle {
  text-align: center;
  color: white;
  font-size: 18px;
  margin-bottom: 60px;
}
.section-title {
  text-align: center;
  color: white;
  font-size: 32px;
  margin-bottom: 40px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}
.card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.card h3 {
  color: #feac5e;
  margin-bottom: 15px;
  font-size: 24px;
}
.card p {
  color: #666;
  line-height: 1.6;
}
.box {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.box h3 {
  color: #c779d0;
  margin-bottom: 10px;
  font-size: 24px;
}
.box p {
  color: #666;
  line-height: 1.6;
}
.spacer {
  height: 100vh;
}
.spacer-small {
  height: 30px;
}
```

### JavaScript
```javascript
AOS.init({
  duration: 800,
  once: false,     // 何度でも実行
  offset: 120,
  easing: 'ease-out-cubic'  // デフォルトイージング
});
```

---

## 📖 主な属性とオプション

### data-aos（エフェクトタイプ）
```html
<!-- フェード系 -->
<div data-aos="fade">基本フェード</div>
<div data-aos="fade-up">下から上へ</div>
<div data-aos="fade-down">上から下へ</div>
<div data-aos="fade-left">右から左へ</div>
<div data-aos="fade-right">左から右へ</div>

<!-- スライド系 -->
<div data-aos="slide-up">下からスライド</div>
<div data-aos="slide-down">上からスライド</div>

<!-- その他 -->
<div data-aos="zoom-in">ズームイン</div>
<div data-aos="flip-left">左回転</div>
```

### その他のオプション
```html
<!-- 持続時間 -->
<div data-aos="fade-up" data-aos-duration="1000">1秒</div>

<!-- 遅延 -->
<div data-aos="fade-up" data-aos-delay="500">0.5秒後</div>

<!-- イージング -->
<div data-aos="fade-up" data-aos-easing="ease-in-out">イージング</div>

<!-- 1回のみ -->
<div data-aos="fade-up" data-aos-once="true">1回のみ</div>
```

## 🔗 デモファイル
- [シンプル版](../../images/aos_demo1_scroll_simple.html)
- [フェードエフェクト集](../../images/aos_demo2_fade.html)
- [スライドエフェクト集](../../images/aos_demo3_slide.html)
- [多機能版](../../images/aos_demo4_advanced.html)

## 📖 公式リソース
- [公式サイト](https://michalsnik.github.io/aos)
- [GitHub](https://github.com/michalsnik/aos)
- [Demo & Examples](https://michalsnik.github.io/aos/#examples)

---

**作成日**: 2026-02-10
**CDN**: AOS v3.0.0-beta.6
