# clip-path で上から下に文字を表示する仕組み

**リビール（Reveal）アニメーション** - 縦書き文字が上から下に書かれていくように見せる手法

★核心の構文を覚える
```css
clip-path: inset(上 右 下 左);
/* 下を100%→0%にすることで、上から下へマスクが外れる */
```

## ★重要ポイント

【★ポイント1: clip-path insetの構文】
```css
clip-path: inset(上 右 下 左);
/* 各辺からどれだけ切り取るか指定 */

/* 例 */
clip-path: inset(0 0 100% 0);
/* 上0、右0、下100%、左0 = 下から100%カット */
```

【★ポイント2: 上から下へ表示する仕組み】
```css
/* 開始: 下を100%隠す */
clip-path: inset(0 0 100% 0);

/* 終了: 全て表示 */
clip-path: inset(0 0 0 0);
```
**結果**: 下部が徐々に見えてくる = 上から下にマスクが外れる

【★ポイント3: アニメーション名称】
- **リビール（Reveal）アニメーション**
- ワイプ（Wipe）アニメーション
- カーテン効果
- テキストライティング効果（縦書きの場合）

---

## HTML

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>縦書き リビールアニメーション</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- 縦書きテキスト -->
  <div class="vertical-text">
    <p class="news_title">お知らせ</p>
    <p class="news_msg">最新情報をお届けします</p>
  </div>
</body>
</html>
```

---

## CSS

```css
/* 縦書き設定 */
.vertical-text {
  writing-mode: vertical-rl;
  font-size: 3rem;
}

.news_title {
  animation: revealRightToLeft 1.5s ease-out forwards;
}

/* 上から下へ表示アニメーション（縦書き用） */
@keyframes revealRightToLeft {
  from {
    clip-path: inset(0 0 100% 0); /* 下を100%隠す = 上から表示開始 */
  }
  to {
    clip-path: inset(0 0 0 0); /* 全て表示 = 下まで進む */
  }
}
```

---

## 動作フロー

1. **開始状態（from）**
   - `clip-path: inset(0 0 100% 0)`
   - 下から100%カット = 上部だけ見える（実質非表示）

2. **アニメーション中**
   - 下のカット量が100%→0%に減少
   - 上から下へ徐々に表示されていく

3. **終了状態（to）**
   - `clip-path: inset(0 0 0 0)`
   - 全て表示

4. **視覚効果**
   - 縦書き文字が「書かれていく」ように見える

---

## 応用例

### 左から右へ表示（横書き用）
```css
@keyframes revealLeftToRight {
  from {
    clip-path: inset(0 100% 0 0); /* 右を100%隠す */
  }
  to {
    clip-path: inset(0 0 0 0);
  }
}
```

### 下から上へ表示
```css
@keyframes revealBottomToTop {
  from {
    clip-path: inset(100% 0 0 0); /* 上を100%隠す */
  }
  to {
    clip-path: inset(0 0 0 0);
  }
}
```

---

## トラブルシューティング

### 症状: アニメーションが動かない
**原因**: `clip-path`に対応していないブラウザ
**対処**: `-webkit-clip-path`も追加

```css
@keyframes revealRightToLeft {
  from {
    -webkit-clip-path: inset(0 0 100% 0);
    clip-path: inset(0 0 100% 0);
  }
  to {
    -webkit-clip-path: inset(0 0 0 0);
    clip-path: inset(0 0 0 0);
  }
}
```

### 症状: 意図しない方向にアニメーション
**原因**: `inset(上 右 下 左)`の順序を間違えている
**対処**: 時計回り（top → right → bottom → left）を覚える
