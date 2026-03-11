# swiper（スクロールボタンを表示する ↑↓）

```
┌──────────────────────────┐
│        Slide 1           │  ↑
│                          │  ← ナビボタン（上下）
│        Slide 2           │  ↓
└──────────────────────────┘
  ページネーション・スクロールバーも追加可
```

**ポイント**
- `direction: "vertical"` → 縦スクロール
- `swiper-button-prev / next` → ↑↓ナビボタン（HTMLに書くだけで自動表示）
- CDNはjQueryなし・swiper単体でOK

---

**HTML**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="css/work.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css" />
</head>
<body>
  <div class="swiper">
    <div class="swiper-wrapper">
      <div class="swiper-slide">Slide 1</div>
      <div class="swiper-slide">Slide 2</div>
      <div class="swiper-slide">Slide 3</div>
    </div>

    <!-- ページネーション（点々） -->
    <div class="swiper-pagination"></div>

    <!-- ↑↓ナビボタン -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>

    <!-- スクロールバー -->
    <div class="swiper-scrollbar"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
  <script src="js/swiper.js"></script>
</body>
</html>
```

**CSS**
```css
.swiper {
  width: 600px;
  height: 300px;
}

.swiper-slide {
  background-color: yellow;
  background-image: url("../img/image1.png");
}

.swiper-slide:nth-child(2) {
  background-image: url("../img/image2.png");
}

.swiper-slide:nth-child(3) {
  background-image: url("../img/image3.png");
}
```

**JavaScript**
```javascript
const swiper = new Swiper(".swiper", {
  direction: "vertical", // 縦スクロール（横は "horizontal"）
  loop: true,

  pagination: {
    el: ".swiper-pagination",
  },

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  scrollbar: {
    el: ".swiper-scrollbar",
  },
});
```

---
