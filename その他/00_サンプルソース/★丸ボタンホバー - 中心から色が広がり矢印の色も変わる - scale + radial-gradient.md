# 丸ボタンホバー - 中心から色が広がり矢印の色も変わる

丸ボタンにホバーすると、中心から外側に向かって色が広がり、矢印の色も変わるアニメーション。

★これだけ覚える
```css
.arrow_icon::before { transform: scale(0); }       /* 通常：見えない */
.arrow_icon:hover::before { transform: scale(1); }  /* ホバー：中心から広がる */
.arrow_icon:hover { color: #111; }                   /* ホバー：矢印の色も変わる */
```

## HTML
```html
<span class="arrow_icon">→</span>
```

---

## ★重要ポイント

【★ポイント1: scale(0) → scale(1) で中心から広がる】
```css
/* ::before を丸全体に重ねて、scale で大きさを制御 */
.arrow_icon::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 0%, #fff 44%, #00b4f7 100%);
  transform: scale(0);       /* ★ 通常は縮小して見えない */
  transition: transform 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
  z-index: -1;               /* ★ 矢印テキストの奥 */
}

.arrow_icon:hover::before {
  transform: scale(1.02);    /* ★ 中心から外に広がる */
}
```
scale(0)=見えない → scale(1)=元サイズ = 中心から広がるアニメーション

【★ポイント2: isolation: isolate で z-index: -1 が消えない】
```css
.arrow_icon {
  position: relative;
  overflow: hidden;
  isolation: isolate;   /* ★ これがないと z-index: -1 が親の背景より奥に消える */
}
```
`isolation: isolate` = 新しい重なり文脈を作る → `-1` でも親の背景より奥にいかない

【★ポイント3: 矢印の色は color を変えるだけ】
```css
.arrow_icon {
  color: #fff;                       /* 通常：白 */
  transition: color 0.3s ease;       /* ★ 滑らかに変化 */
}

.arrow_icon:hover {
  color: #111;                       /* ★ ホバー：黒に */
}
```

---

## CSS
```css
/* ========================================
   丸ボタン ホバーで中心から色が広がる
   - ::before を scale(0→1) で広げる
   - z-index: -1 で矢印の奥に配置
   - isolation: isolate で消えない
   ======================================== */

/* --- 丸ボタン本体 --- */
.arrow_icon {
  background: #111;              /* 通常の背景色（黒） */
  color: #fff;                   /* 矢印の色（白） */
  border-radius: 50%;
  width: 4rem;
  height: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;            /* ★ ::before の基準点 */
  overflow: hidden;              /* ★ はみ出し防止 */
  isolation: isolate;            /* ★ z-index:-1 が消えないように */
  transition: color 0.3s ease;   /* ★ 矢印の色変化を滑らかに */
}

/* --- 中心から広がる色（::before） --- */
.arrow_icon::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 0%, #fff 44%, #00b4f7 100%);
  transform: scale(0);           /* ★ 通常は見えない */
  transition: transform 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
  z-index: -1;                   /* ★ 矢印テキストの奥 */
}

/* --- ホバー時 --- */
.arrow_icon:hover::before {
  transform: scale(1.02);        /* ★ 中心から外に広がる */
}

.arrow_icon:hover {
  color: #111;                   /* ★ 矢印を白→黒に */
}
```
