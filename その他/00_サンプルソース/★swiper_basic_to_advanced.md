# Swiper.js 基本〜応用

★ 最新版 **Swiper v12.1.0** (2026/01/28) を使用

## 📚 目次ページ
📺 **[デモ一覧を見る](../../images/index.html)**

---

## ✅ ① フェードエフェクト【シンプル版】

💡 **まずはここから！Swiper.js本来の姿**

★ **用途**: Swiperの学習、シンプルな実装
★ **ポイント**: Swiper.jsの機能のみ、最小限のコード

### 📋 特徴

| 項目 | 内容 |
|------|------|
| Swiper機能 | ✅ フェード、自動再生、矢印、ドット |
| オーバーレイ | ✅ なし |
| テキスト・ボタン | ✅ なし |
| アニメーション | ✅ なし |
| コード量 | 少ない（150行） |
| 学習難易度 | ✅ 簡単 |
| カスタマイズ | ✅ 簡単 |

### HTML
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Swiper - フェードエフェクト【シンプル版：Swiperのみ】</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
  <style>
    /* ✅ これがSwiper.js本来の姿 - 最小限のコード */
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }

    /* Swiperコンテナ */
    .swiper {
      width: 100%;
      height: 100vh;
    }

    /* スライド */
    .swiper-slide {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 48px;
      color: white;
      background: #333;
    }

    /* 画像スタイル */
    .swiper-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  </style>
</head>
<body>
  <!-- ✅ Swiper本体 -->
  <div class="swiper">
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/667EEA/FFF?text=Slide+1" alt="スライド1">
      </div>
      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/F093FB/FFF?text=Slide+2" alt="スライド2">
      </div>
      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/4BC0C8/FFF?text=Slide+3" alt="スライド3">
      </div>
      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/FEAC5E/333?text=Slide+4" alt="スライド4">
      </div>
    </div>

    <!-- ナビゲーション矢印 -->
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>

    <!-- ページネーション -->
    <div class="swiper-pagination"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
  <script>
    /* ✅ Swiper.js の初期化（シンプル版） */
    const swiper = new Swiper('.swiper', {
      // フェードエフェクト
      effect: 'fade',
      fadeEffect: {
        crossFade: true,
      },

      // 基本設定
      speed: 1000,
      loop: true,

      // 自動再生
      autoplay: {
        delay: 4000,
        disableOnInteraction: false,
      },

      // ページネーション
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },

      // ナビゲーション
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  </script>
</body>
</html>
```

📺 **[シンプル版デモを見る](../../images/swiper_demo4_fade_simple.html)**

### 💡 学習ポイント

1. **Swiperの本質が理解できる**
   - 余計な装飾がないため、Swiperの機能だけに集中できる
   - コードが短くて読みやすい

2. **カスタマイズの出発点**
   - このシンプル版をベースに、必要な機能だけを追加していける
   - デモ④のような多機能版は、このシンプル版の発展形

3. **比較学習**
   - デモ④と比較することで、Swiper機能とカスタム機能の違いが明確に
   - 「何がSwiperで、何がCSSか」を理解できる

---

## 🥇 ② サムネイル付きスライダー

★ **用途**: ECサイト商品画像、ギャラリー表示
★ **ポイント**: メインスライダーとサムネイルを連動

### HTML
```html
<!DOCTYPE html>
<html lang="ja">
<head>``
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Swiper - サムネイル付きスライダー</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
  <style>
    body {
      margin: 0;
      padding: 20px;
      font-family: Arial, sans-serif;
      background: #f5f5f5;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      color: #333;
      margin-bottom: 30px;
    }
    /* メインスライダー */
    .swiper-main {
      margin-bottom: 10px;
    }
    .swiper-main .swiper-slide {
      height: 400px;
      background: #ddd;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .swiper-main .swiper-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    /* サムネイルスライダー */
    .swiper-thumbs {
      height: 100px;
      box-sizing: border-box;
      padding: 10px 0;
    }
    .swiper-thumbs .swiper-slide {
      height: 80px;
      opacity: 0.4;
      cursor: pointer;
      transition: opacity 0.3s;
    }
    .swiper-thumbs .swiper-slide-thumb-active {
      opacity: 1;
      border: 2px solid #007aff;
    }
    .swiper-thumbs .swiper-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    /* ナビゲーション矢印 */
    .swiper-button-next,
    .swiper-button-prev {
      color: #007aff;
      background: white;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .swiper-button-next:after,
    .swiper-button-prev:after {
      font-size: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🥇 サムネイル付きスライダー</h1>

    <!-- メインスライダー -->
    <div class="swiper swiper-main">
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          <img src="https://placehold.co/800x400/4A90E2/FFF?text=Product+1" alt="商品1">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/800x400/E24A4A/FFF?text=Product+2" alt="商品2">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/800x400/4AE290/FFF?text=Product+3" alt="商品3">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/800x400/E2D44A/FFF?text=Product+4" alt="商品4">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/800x400/9B4AE2/FFF?text=Product+5" alt="商品5">
        </div>
      </div>
      <!-- ナビゲーション矢印 -->
      <div class="swiper-button-next"></div>
      <div class="swiper-button-prev"></div>
    </div>

    <!-- サムネイルスライダー -->
    <div class="swiper swiper-thumbs">
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          <img src="https://placehold.co/100x80/4A90E2/FFF?text=1" alt="サムネイル1">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/100x80/E24A4A/FFF?text=2" alt="サムネイル2">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/100x80/4AE290/FFF?text=3" alt="サムネイル3">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/100x80/E2D44A/FFF?text=4" alt="サムネイル4">
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/100x80/9B4AE2/FFF?text=5" alt="サムネイル5">
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
  <script>
    // サムネイルスライダー初期化（先に初期化）
    const swiperThumbs = new Swiper('.swiper-thumbs', {
      spaceBetween: 10,
      slidesPerView: 4,
      freeMode: true,
      watchSlidesProgress: true,
    });

    // メインスライダー初期化
    const swiperMain = new Swiper('.swiper-main', {
      spaceBetween: 10,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      thumbs: {
        swiper: swiperThumbs, // サムネイルと連動
      },
    });
  </script>
</body>
</html>
```

📺 **[デモを見る](../../images/swiper_demo1_thumbnail.html)**

---

## 🥈 ③ 自動再生 + プログレスバー

★ **用途**: ヒーローバナー、キャンペーン告知
★ **ポイント**: 自動再生 + 進行状況の可視化

### HTML
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Swiper - 自動再生 + プログレスバー</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }
    .hero-container {
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }
    .swiper {
      width: 100%;
      height: 100%;
    }
    .swiper-slide {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      background: #000;
    }
    .swiper-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.7;
    }
    .slide-content {
      position: absolute;
      text-align: center;
      color: white;
      z-index: 10;
    }
    .slide-content h2 {
      font-size: 48px;
      margin: 0 0 20px 0;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .slide-content p {
      font-size: 24px;
      margin: 0;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    /* プログレスバー */
    .autoplay-progress {
      position: absolute;
      left: 0;
      bottom: 0;
      z-index: 10;
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.3);
    }
    .autoplay-progress-fill {
      height: 100%;
      background: #007aff;
      width: 0;
      transition: width 0.1s linear;
    }
    /* ページネーション */
    .swiper-pagination-bullet {
      width: 12px;
      height: 12px;
      background: white;
      opacity: 0.5;
    }
    .swiper-pagination-bullet-active {
      opacity: 1;
      background: #007aff;
    }
    /* ナビゲーション */
    .swiper-button-next,
    .swiper-button-prev {
      color: white;
    }
    /* 一時停止/再生ボタン */
    .play-pause {
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 20;
      background: rgba(0, 0, 0, 0.5);
      color: white;
      border: 2px solid white;
      padding: 10px 20px;
      cursor: pointer;
      font-size: 16px;
      border-radius: 5px;
      transition: background 0.3s;
    }
    .play-pause:hover {
      background: rgba(0, 122, 255, 0.8);
    }
  </style>
</head>
<body>
  <div class="hero-container">
    <div class="swiper">
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          <img src="https://placehold.co/1920x1080/FF6B6B/FFF?text=Campaign+1" alt="キャンペーン1">
          <div class="slide-content">
            <h2>春の新作コレクション</h2>
            <p>最大50% OFF セール開催中</p>
          </div>
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/1920x1080/4ECDC4/FFF?text=Campaign+2" alt="キャンペーン2">
          <div class="slide-content">
            <h2>限定アイテム入荷</h2>
            <p>数量限定！お早めに</p>
          </div>
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/1920x1080/FFE66D/333?text=Campaign+3" alt="キャンペーン3">
          <div class="slide-content">
            <h2>会員登録で10%OFF</h2>
            <p>今すぐ登録してお得にお買い物</p>
          </div>
        </div>
        <div class="swiper-slide">
          <img src="https://placehold.co/1920x1080/A8E6CF/333?text=Campaign+4" alt="キャンペーン4">
          <div class="slide-content">
            <h2>送料無料キャンペーン</h2>
            <p>3000円以上のご購入で</p>
          </div>
        </div>
      </div>

      <!-- ナビゲーション -->
      <div class="swiper-button-next"></div>
      <div class="swiper-button-prev"></div>

      <!-- ページネーション -->
      <div class="swiper-pagination"></div>
    </div>

    <!-- プログレスバー -->
    <div class="autoplay-progress">
      <div class="autoplay-progress-fill"></div>
    </div>

    <!-- 一時停止/再生ボタン -->
    <button class="play-pause">⏸ 一時停止</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
  <script>
    const progressFill = document.querySelector('.autoplay-progress-fill');
    const playPauseBtn = document.querySelector('.play-pause');

    const swiper = new Swiper('.swiper', {
      spaceBetween: 0,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      on: {
        autoplayTimeLeft(s, time, progress) {
          // プログレスバーを更新（0%→100%）
          progressFill.style.width = (1 - progress) * 100 + '%';
        },
      },
    });

    // 一時停止/再生ボタン
    let isPlaying = true;
    playPauseBtn.addEventListener('click', () => {
      if (isPlaying) {
        swiper.autoplay.stop();
        playPauseBtn.textContent = '▶ 再生';
      } else {
        swiper.autoplay.start();
        playPauseBtn.textContent = '⏸ 一時停止';
      }
      isPlaying = !isPlaying;
    });
  </script>
</body>
</html>
```

📺 **[デモを見る](../../images/swiper_demo2_autoplay.html)**

---

## 🥉 ④ フェードエフェクト【多機能版】

⚠ **注意**: このデモは**Swiper以外の機能も多数含む**応用例です

### 📋 含まれる機能

| 分類 | 機能 | 説明 |
|------|------|------|
| ✅ Swiper | フェードエフェクト | `effect: 'fade'` |
| ✅ Swiper | 自動再生 | `autoplay` |
| ✅ Swiper | ナビゲーション矢印 | `navigation` |
| ✅ Swiper | ページネーション | `pagination` |
| ❌ カスタム | 画像オーバーレイ | `.slide-overlay` |
| ❌ カスタム | テキスト・ボタン | `.slide-content` |
| ❌ カスタム | 下から上アニメ | `@keyframes fadeInUp` |
| ❌ カスタム | 情報パネル | `.info-panel` |
| ❌ カスタム | カスタムデザイン | 各種スタイル |

💡 **Swiperのみのシンプル版は [デモ①](#-①-フェードエフェクトシンプル版) を参照**

★ **用途**: 背景スライドショー、イメージ切替（多機能）
★ **ポイント**: フェード + 多くのカスタム機能

### HTML
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Swiper - フェードエフェクト</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      overflow: hidden;
    }
    .swiper {
      width: 100%;
      height: 100vh;
    }
    .swiper-slide {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .swiper-slide img {
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .slide-overlay {
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.3);
      z-index: 1;
    }
    .slide-content {
      position: relative;
      z-index: 2;
      text-align: center;
      color: white;
      padding: 40px;
      animation: fadeInUp 1s ease-out;
    }
    .slide-content h2 {
      font-size: 56px;
      margin: 0 0 20px 0;
      font-weight: bold;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    }
    .slide-content p {
      font-size: 24px;
      margin: 0 0 30px 0;
      text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }
    .slide-content .btn {
      display: inline-block;
      padding: 15px 40px;
      background: #007aff;
      color: white;
      text-decoration: none;
      border-radius: 50px;
      font-size: 18px;
      transition: background 0.3s;
      box-shadow: 0 4px 15px rgba(0,122,255,0.4);
    }
    .slide-content .btn:hover {
      background: #0056b3;
    }
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    /* ページネーション（カスタムスタイル） */
    .swiper-pagination {
      bottom: 30px !important;
    }
    .swiper-pagination-bullet {
      width: 50px;
      height: 4px;
      border-radius: 2px;
      background: white;
      opacity: 0.5;
      transition: all 0.3s;
    }
    .swiper-pagination-bullet-active {
      opacity: 1;
      width: 80px;
      background: #007aff;
    }
    /* ナビゲーション矢印 */
    .swiper-button-next,
    .swiper-button-prev {
      color: white;
      background: rgba(0, 0, 0, 0.3);
      width: 60px;
      height: 60px;
      border-radius: 50%;
      transition: background 0.3s;
    }
    .swiper-button-next:hover,
    .swiper-button-prev:hover {
      background: rgba(0, 122, 255, 0.8);
    }
    .swiper-button-next:after,
    .swiper-button-prev:after {
      font-size: 24px;
    }
  </style>
</head>
<body>
  <div class="swiper">
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/667EEA/FFF?text=Nature+Scene+1" alt="自然風景1">
        <div class="slide-overlay"></div>
        <div class="slide-content">
          <h2>美しい自然</h2>
          <p>心安らぐ風景をお届けします</p>
          <a href="#" class="btn">詳しく見る</a>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/F093FB/FFF?text=Nature+Scene+2" alt="自然風景2">
        <div class="slide-overlay"></div>
        <div class="slide-content">
          <h2>四季の移ろい</h2>
          <p>季節ごとの魅力を感じて</p>
          <a href="#" class="btn">詳しく見る</a>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/4BC0C8/FFF?text=Nature+Scene+3" alt="自然風景3">
        <div class="slide-overlay"></div>
        <div class="slide-content">
          <h2>癒しの空間</h2>
          <p>特別なひとときを</p>
          <a href="#" class="btn">詳しく見る</a>
        </div>
      </div>

      <div class="swiper-slide">
        <img src="https://placehold.co/1920x1080/FEAC5E/333?text=Nature+Scene+4" alt="自然風景4">
        <div class="slide-overlay"></div>
        <div class="slide-content">
          <h2>絶景スポット</h2>
          <p>一生に一度は見たい景色</p>
          <a href="#" class="btn">詳しく見る</a>
        </div>
      </div>
    </div>

    <!-- ナビゲーション矢印 -->
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>

    <!-- ページネーション -->
    <div class="swiper-pagination"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
  <script>
    const swiper = new Swiper('.swiper', {
      effect: 'fade', // ★ フェードエフェクト
      fadeEffect: {
        crossFade: true, // クロスフェード有効化
      },
      speed: 1000, // 切り替え速度（ミリ秒）
      loop: true,
      autoplay: {
        delay: 4000,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  </script>
</body>
</html>
```

📺 **[多機能版デモを見る](../../images/swiper_demo3_fade.html)**

---

## 📚 参考リンク

- [Swiper公式サイト](https://swiperjs.com/)
- [API Documentation](https://swiperjs.com/swiper-api)
- [CDN - jsDelivr](https://www.jsdelivr.com/package/npm/swiper)

---

## 💡 応用アイデア

### その他のエフェクト
- `effect: 'cube'` - 3Dキューブ回転
- `effect: 'coverflow'` - Coverflowエフェクト
- `effect: 'flip'` - カードフリップ
- `effect: 'creative'` - カスタムエフェクト

### よく使うオプション
```javascript
{
  direction: 'vertical',    // 縦スライド
  slidesPerView: 3,        // 表示枚数
  spaceBetween: 30,        // スライド間隔
  centeredSlides: true,    // 中央配置
  grabCursor: true,        // グラブカーソル
  keyboard: true,          // キーボード操作
  mousewheel: true,        // マウスホイール操作
}
```
