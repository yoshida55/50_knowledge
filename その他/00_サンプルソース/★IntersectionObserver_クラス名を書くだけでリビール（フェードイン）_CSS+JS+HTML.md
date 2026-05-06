# IntersectionObserver - クラス名を書くだけでリビール（フェードイン）できるユーティリティパターン

CSS + JS を一度セットアップすれば、HTMLにクラス名を書くだけでスクロールアニメーションが適用できる。

★ CSS で「初期状態 → 表示状態」を定義 / JS が画面内に入ったとき `is_visible` を付ける / HTML はクラス名を書くだけ

---

## ★重要ポイント

【★ポイント1: CSS+JSを1回書けばHTMLはクラス名だけでOK】
```css
.js_soft_reveal {
  opacity: 0;
  transform: translateY(4rem); /* 下4rem からスタート */
  transition: opacity 0.7s ease, transform 0.8s ease;
}
.js_soft_reveal.is_visible {
  opacity: 1;
  transform: none; /* 元の位置に戻る */
}
```
HTMLに `class="js_soft_reveal"` を書くだけで発動する。

【★ポイント2: 方向違いのクラスを増やすときはCSS+JSに1行ずつ追加】
```css
/* 左からスライド版 */
.js_soft_reveal_left {
  opacity: 0;
  transform: translateX(-8rem);
  transition: opacity 0.7s ease, transform 0.8s ease;
}
.js_soft_reveal_left.is_visible {
  opacity: 1;
  transform: none;
}
```
```js
// JSにも必ず1行追加する（書かないと永遠に opacity: 0 のまま）
document.querySelectorAll(".js_soft_reveal_left").forEach((el) => observer.observe(el));
```

【★ポイント3: IntersectionObserver が監視して is_visible を付ける】
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {              // 画面に入ったか
      entry.target.classList.add("is_visible"); // クラスを付ける
      observer.unobserve(entry.target);       // 1回だけ発動（2回目以降スキップ）
    }
  });
}, { threshold: 0.1 }); // 10%見えたら発動
```

---

## HTML
```html
<!-- クラス名を書くだけでOK -->
<div class="js_soft_reveal">下から上にフェードイン</div>
<p class="js_soft_reveal">これも同じアニメーション</p>
<h2 class="js_soft_reveal_left">左からスライドして表示</h2>

<!-- JSの読み込みはbodyの閉じタグ直前 -->
<script src="js/script.js"></script>
```

## CSS（css/style.css）
```css
/* ── スクロールアニメーション共通 ── */

/* 下から上にフェードイン */
.js_soft_reveal {
  opacity: 0;
  transform: translateY(4rem);
  transition:
    opacity 0.7s ease,
    transform 0.8s ease;
}
.js_soft_reveal.is_visible {
  opacity: 1;
  transform: none;
}

/* 左からスライドしてフェードイン */
.js_soft_reveal_left {
  opacity: 0;
  transform: translateX(-8rem);
  transition:
    opacity 0.7s ease,
    transform 0.8s ease;
}
.js_soft_reveal_left.is_visible {
  opacity: 1;
  transform: none;
}
```

## JavaScript（js/script.js）
```js
// スクロールアニメーション（IntersectionObserver）
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is_visible");
        observer.unobserve(entry.target); // 1回だけ発動
      }
    });
  },
  { threshold: 0.1 } // 10%見えたら発動
);

// クラスを増やしたらここに1行追加する
document.querySelectorAll(".js_soft_reveal").forEach((el) => observer.observe(el));
document.querySelectorAll(".js_soft_reveal_left").forEach((el) => observer.observe(el));
```

---

## 動作フロー
1. ページ読み込み時：`js_soft_reveal` クラスの要素は `opacity: 0` で非表示
2. スクロールして要素が10%見える → IntersectionObserver が検知
3. `is_visible` クラスが付く → CSS の transition が発動してフワッと表示
4. `unobserve` で監視終了 → 一度表示した要素は再発動しない

## 補足
### Q. クラスを新しく作っても動かない
→ CSS に追加するだけでなく、JS の `querySelectorAll` にも同じクラス名で1行追加する必要がある。JS が監視リストに入れていないと `is_visible` が付かない。

### Q. フェードインとソフトリビールの違いは？
→ フェードイン = opacity 変化のみ（移動なし）。ソフトリビール = opacity + 移動の組み合わせ。「下から上にフェードイン」のように方向を明示すれば移動を含む意味になる。
