# 横流れリボンアニメーション - flexで横並び+nth-child(even)で2段+translate3dでループ

背景に半透明のリボンが横に流れ続けるアニメーション。flexで横並びにして、偶数番目を下にずらすだけで2段に見せる。

★ ループの核心式：`translate3d(-34rem, 0, 0)` の `-34rem` = リボン1枚の `width` と同じ値にする

```css
transform: translate3d(-34rem, 0, 0); /* 1枚分ずらす → 次のリボンが元の位置に来てループ */
```

---

## ★重要ポイント

【★ポイント1: display: flex は親に書く】
```css
.overview_flow_ribbons {
  display: flex; /* 子のspanが横並びになる。自分自身には影響しない */
  gap: 9rem;     /* 子どもたちの間隔をまとめて指定（marginより楽） */
}
```
`display: flex` は「自分の子要素を横並びにする」スイッチ。自分自身の見た目は変わらない。

【★ポイント2: gap は親に書くだけで子全員の間隔が決まる】
```css
gap: 9rem; /* flex/grid がないと効かない。marginと違って子1つずつに書かなくていい */
```
`margin` は子に1個ずつ書く必要がある。`gap` は親に1行書くだけで全員に効く。

【★ポイント3: nth-child(even) で偶数だけ下にずらして2段に見せる】
```css
.overview_flow_ribbons span:nth-child(even) {
  transform: translateY(5.2rem); /* 偶数番目だけ下にずれる → グリッドなしに2段に見える */
  background: rgba(255, 255, 255, 0.34);
}
```
```
span1（上段）  span3（上段）  span5（上段）
      span2（下段）  span4（下段）
```
`nth-child(2)` だと2番目だけ。`nth-child(even)` にすると2・4・6番目…全部に効く。

【★ポイント4: translate3d でGPU処理になりなめらかになる】
```css
@keyframes flow-ribbons {
  from { transform: translate3d(0, 0, 0); }
  to   { transform: translate3d(-34rem, 0, 0); }
}
/* translateX(-34rem) より translate3d を使うとGPUが処理してカクつかない */
```
`translate3d(X, Y, Z)` の Z に `0` を入れるだけでGPU処理になる。アニメーションには積極的に使う。

【★ポイント5: ループは「1セット分の幅 = ずらす距離」にする】
```css
.overview_flow_ribbons span {
  width: 34rem; /* この値と */
}
@keyframes flow-ribbons {
  to { transform: translate3d(-34rem, 0, 0); } /* この値を必ず合わせる */
}
```
1枚分ずれると次のリボンが元の位置に来るので、つなぎ目が見えずにループする。  
⚠ `width` を変えたら `translate3d` の値も必ずセットで変える。

---

## CSS

```css
/* 背景を流れる半透明の横長リボン装飾 */
.overview_flow_ribbons {
  position: absolute;
  top: 2.4rem;
  left: 0;
  z-index: 0;
  display: flex; /* 子のspanを横並びにする */
  gap: 9rem;     /* spanとspanの間隔 */
  animation: flow-ribbons 18s linear infinite; /* 18秒でループし続ける */
  pointer-events: none; /* クリック判定をなくす（装飾なので） */
}

/* リボン1枚のサイズと見た目 */
.overview_flow_ribbons span {
  display: block;
  width: 34rem;  /* ← translate3d の値と必ず合わせる */
  height: 7.2rem;
  background: rgba(255, 255, 255, 0.5);
  box-shadow: 0 1.2rem 3rem rgba(23, 27, 32, 0.04);
}

/* 偶数番目だけ下にずらして2段に見せる */
.overview_flow_ribbons span:nth-child(even) {
  transform: translateY(5.2rem);
  background: rgba(255, 255, 255, 0.34);
}

/* 横に流れるアニメーション本体 */
@keyframes flow-ribbons {
  from {
    transform: translate3d(0, 0, 0); /* translate3d でGPU処理になりなめらか */
  }
  to {
    transform: translate3d(-34rem, 0, 0); /* 1枚分（34rem）だけ左に移動してループ */
  }
}
```

## HTML

```html
<!-- 親要素に position: relative と min-height が必要 -->
<div class="overview_flow_ribbons">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
</div>
```

---

## 動作フロー

1. span が flex で横一列に並ぶ
2. 偶数番目（2・4・6…）が `translateY` で下段にずれる → 2段に見える
3. `flow-ribbons` アニメーションで全体が左に `-34rem` 移動し続ける
4. 1枚分ずれると次のリボンが元の位置に来る → つなぎ目なしにループ

---

## 補足

### Q. `width: max-content` はいる？
→ `display: flex` にするとリボンが自動的に広がるので、なくても動く。あると「明示的に折り返さない」と宣言できる。

### Q. `will-change: transform` はいる？
→ アニメーションがカクつく場合は効果あり。スムーズなら不要。スマホでは逆に重くなることもある。

### Q. `translate3d` と `translateX` の違いは？
→ 結果は同じだが `translate3d` はGPUで処理されるためなめらか。アニメーションには `translate3d` を使う方が丁寧。
