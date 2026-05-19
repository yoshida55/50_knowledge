# clip-path Reveal 右から画像がめくれるリビールで現れる・捲れるイメージ（スライドイン）

ページ読み込み時に画像が右からめくれるように現れるアニメーション。JSなし・CSSのみで実装。

★ようするに「右端を100%切り取った状態」→「切り取りゼロ」にアニメーションさせるだけ
clip-path: inset(0 100% 0 0) → inset(0 0% 0 0)

## ★重要ポイント

【★ポイント1: inset の2番目の値が「右から切り取る量」】
```css
/* 最初は右から100%切り取り → 画像が完全に隠れる */
clip-path: inset(0 100% 0 0);

/* アニメーション後は切り取りなし → 画像が全部見える */
clip-path: inset(0 0% 0 0);
```
inset(上 右 下 左) の順。右を100%にすると画像が完全に消える。

【★ポイント2: 親要素に overflow: hidden が必須】
```css
.img_frame {
  overflow: hidden; /* ← これがないとはみ出して見える */
  clip-path: inset(0 100% 0 0);
  animation: img_reveal 1.2s 1.0s cubic-bezier(0.22, 1, 0.36, 1) both;
}
```
`both` = アニメーション前後どちらも keyframes の値を維持する。

【★ポイント3: cubic-bezier(0.22, 1, 0.36, 1) が「捲れる」感の正体】
```css
animation: img_reveal 1.2s 1.0s cubic-bezier(0.22, 1, 0.36, 1) both;
/*                    時間  遅延  イージング（最初ゆっくり→最後一気に）      */
```
最初ゆっくり・最後に一気に動くイージングが「めくれる」感を生む。ease-outに近い。

---

## HTML
```html
<div class="img_frame">
  <img class="img" src="img/sample.png" alt="" />
</div>
```

## CSS
```css
.img_frame {
  overflow: hidden;
  clip-path: inset(0 100% 0 0);
  animation: img_reveal 1.2s 1.0s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@keyframes img_reveal {
  from { clip-path: inset(0 100% 0 0); }
  to   { clip-path: inset(0 0% 0 0); }
}
```

## JavaScript
```javascript
// JSなし。CSSのみで動作。
```

---

## 動作フロー
1. ページ読み込み → `clip-path: inset(0 100% 0 0)` で画像が完全に隠れた状態
2. 1.0s 後にアニメーション開始
3. 右端の切り取りが 100% → 0% に変化 → 右からめくれるように画像が現れる

## 補足
### Q. animation-delay を入れているのはなぜ？
→ ページ読み込み直後にすぐ動くと気づかれにくいため。1秒待つことで「動いた！」と伝わりやすい。

### Q. `both` を外すとどうなる？
→ アニメーション開始前に一瞬画像が見えてしまう。`both` で最初から隠れた状態を維持する。

【関連】→「clip-path Reveal 上から下」で検索（文字を上から下に表示するバージョン）
