# 疑似要素で棒線の先に矢印をつくる - content文字はズレる（::after横線 + ::beforeくの字）

疑似要素（::after / ::before）を使って「横線＋矢印の先端」を作る方法。
→ などの文字を使うとフォント幅でズレるため、図形だけで作るのが正解。

★ズレない理由：両方 content:"" （空）にして図形で描く。文字を使わない。

## ★重要ポイント

【★ポイント1: content文字（→）を使うとズレる】
```css
/* ❌ これはズレる */
.link::after {
  content: "→";  /* 文字の幅がフォントによって変わるためズレる */
}
```
→ はあくまで「文字」。フォントによって幅が変わるため、横線と位置を合わせるのが難しい。

【★ポイント2: 両方 content:"" にして図形で作るとズレない】
```css
/* ✅ これはズレない */
/* 横線 */
.link::after {
  content: "";           /* 空 = 図形として描く */
  height: 1px;
  background-color: white;
  width: 5rem;           /* 線の長さはここだけ変える */
}

/* 矢印の先端（くの字） */
.link::before {
  content: "";           /* 空 = 図形として描く */
  border-top: 1px solid white;
  border-right: 1px solid white;
  transform: rotate(45deg);  /* 45度回転でくの字に */
}
```
両方とも content:"" で「空の箱」を作り、CSSで形を描く。文字を使わないのでズレない。

【★ポイント3: 2つの right 値を合わせる】
```css
/* ::after と ::before を同じ right 値にすると先端がピッタリ合う */
.link::after  { right: 2rem; }  /* 横線の右端 */
.link::before { right: 2rem; }  /* 矢印の先端も同じ位置 */
```
right の値を同じにすることで、線の右端に矢印がピッタリ来る。

---

## CSS（完全版）

```css
.contact_link {
  display: block;
  width: 65rem;
  padding: 3rem 8rem;
  color: #fff;
  text-decoration: none;
  font-size: 1.4rem;
  margin: 0 auto 2rem auto;
  cursor: pointer;
  border: 0.1rem solid white;
  position: relative;  /* 疑似要素の基準になるので必須 */
}

/* 横線 */
.contact_link::after {
  content: "";
  position: absolute;
  top: 50%;
  right: 2rem;
  width: 5rem;           /* 線の長さ */
  height: 1px;
  background-color: white;
  transform: translateY(-50%);
}

/* 矢印の先端（くの字） */
.contact_link::before {
  content: "";
  position: absolute;
  top: 50%;
  right: 2rem;           /* ::after と同じ値 */
  width: 0.7rem;
  height: 0.7rem;
  border-top: 1px solid white;
  border-right: 1px solid white;
  transform: translateY(-50%) rotate(45deg);
}
```

---

## HTML

```html
<section class="contact_area">
  <h2 class="under_title">CONTACT</h2>
  <a href="#" class="contact_link">出展に関するお問い合わせ</a>
  <a href="#" class="contact_link">その他のお問い合わせ</a>
</section>
```

---

## 動作フロー

1. .contact_link に position: relative を設定（疑似要素の基準点）
2. ::after で height: 1px + background-color → 横線を描く
3. ::before で border + rotate(45deg) → くの字の矢印を描く
4. 両方に同じ right 値を指定 → 線の右端に矢印がピッタリ合う

## トラブルシューティング

### 線と矢印がズレる
**原因**: ::after と ::before の right 値が合っていない
**対処**: 両方を同じ right 値にする

### 矢印が見えない
**原因**: 親要素に position: relative がない
**対処**: .contact_link に position: relative を追加
