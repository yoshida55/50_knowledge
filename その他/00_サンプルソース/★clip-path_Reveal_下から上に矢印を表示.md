# clip-path Reveal（下から上） - ホバーで要素を下から上に表示する


## 🔗 デモファイル  ↓↓↓　シンプルにこれを流用してOK
- [▶ デモを見る](./clip-path_Reveal_下から上_demo.html)
[プレビュー](http://localhost:54321/preview-20260224-072456.html)


ホバー時に背景色やアイコンを下から上へ「めくれ上がるように」表示するRevealエフェクト。
**最初はアイコン表示 → ホバーで一瞬消えて下から上に再Reveal。**

★ `inset(100% 0 0 0)` → `inset(0 0 0 0)` で下から上へReveal
★ 「消えて→再表示」の2ステップは `transition` 不可 → `@keyframes` 必須

## ★重要ポイント

【★ポイント1: inset() の方向（直感と逆）】
```css
/* 下から上 = 上を100%削ってスタート */
clip-path: inset(100% 0 0 0); /* 開始：全部非表示 */
clip-path: inset(0 0 0 0);    /* 終了：全部表示 */

/* inset(top right bottom left) */
/* top=100% → 上から100%削る → 下から見え始める */
```
`inset(100% 0 0 0)` は「上から100%削る」= 下から見え始める（直感と逆）。

【★ポイント3: アイコンを span でラップ】
```html
<div class="footer_arrow">
  <span class="footer_arrow_icon">↑</span>
</div>
```
アイコン自体を動かすには `<span>` でラップして clip-path を設定する。

【★ポイント4: transition では2ステップ不可 → @keyframes】
```css
/* ❌ transition は A→B の1方向のみ */
/* 「消えてから再表示」はできない */

/* ✅ @keyframes で複数ステップを定義 */
@keyframes arrow-reveal {
  0%   { clip-path: inset(0 0 0 0); }    /* 表示（通常状態） */
  1%   { clip-path: inset(100% 0 0 0); } /* 瞬時消去 */
  100% { clip-path: inset(0 0 0 0); }    /* 下から上に表示 */
}
```
`transition` は1方向のみ。複数ステップが必要なら `@keyframes`。

【★ポイント5: 0%→1% 瞬時消去トリック】
```css
@keyframes arrow-reveal {
  0%   { clip-path: inset(0 0 0 0); }
  1%   { clip-path: inset(100% 0 0 0); } /* ← 1%で瞬時に切替 */
  100% { clip-path: inset(0 0 0 0); }
}
```
`0% → 1%` の区間が短すぎて目に見えない → 「パッと消えてReveal」に見える。

---

## HTML
```html
<div class="footer_arrow">
  <span class="footer_arrow_icon">↑</span>
</div>
```

## CSS
```css
.footer_arrow {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 4rem;
  height: 5rem;

  font-size: 1.5rem;

  border: 0.1rem solid #8b6914;
  border-radius: 45%;
  color: #da6d00;

  position: relative;
  overflow: hidden;
  isolation: isolate;
}

/* アイコンのReveal（@keyframes 必須） */
.footer_arrow_icon {
  display: block;
  /* 初期状態：表示 */
}

.footer_arrow:hover .footer_arrow_icon {
  animation: arrow-reveal 0.5s ease forwards;
}

@keyframes arrow-reveal {
  0%   { clip-path: inset(0 0 0 0); }    /* 表示 */
  1%   { clip-path: inset(100% 0 0 0); } /* 瞬時消去 */
  100% { clip-path: inset(0 0 0 0); }    /* 下から上にReveal */
}
```

---

## 動作フロー
1. 初期状態：矢印アイコン（↑）表示
2. ホバー開始
3. `<span>`（アイコン）が @keyframes で一瞬消えて下から上にReveal



## 応用：方向バリエーション
| 方向 | 開始状態 |
|------|----------|
| 下から上 | `inset(100% 0 0 0)` |
| 上から下 | `inset(0 0 100% 0)` |
| 右から左 | `inset(0 100% 0 0)` |
| 左から右 | `inset(0 0 0 100%)` |
