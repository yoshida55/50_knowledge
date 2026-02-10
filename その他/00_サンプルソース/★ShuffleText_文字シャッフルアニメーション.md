# ShuffleText.js - 文字シャッフルアニメーション

日本製のテキストアニメーションライブラリ。文字がランダムに変化してから最終テキストに収束する演出を実現。

★ CDN読み込みだけで使える
★ ローディング・タイトル演出に最適
★ 数字カウントアップ・ハッカー風UIに活用可能

## 基本実装

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ShuffleText Basic</title>
</head>
<body>
    <!-- アニメーション対象 -->
    <h1 class="shuffle-target">WELCOME</h1>

    <!-- ライブラリ読み込み -->
<!-- shuffle-text v0.5.1 -->
    <script src="https://unpkg.com/shuffle-text@0.5.1/build/shuffle-text.js"></script>
</body>
</html>
```

```javascript
// 基本的な使い方
const element = document.querySelector('.shuffle-target');
const shuffle = new ShuffleText(element);

// アニメーション開始
shuffle.start();

// テキスト変更してアニメーション
shuffle.setText('NEW TEXT');
```

## 主要オプション付き実装

```javascript
// オプション設定
const shuffle = new ShuffleText(element);

// ★ 主要プロパティ
shuffle.duration = 600;              // アニメーション時間(ms)
shuffle.fps = 30;                    // フレームレート
shuffle.emptyCharacter = '-';        // 空白文字
shuffle.sourceRandomCharacter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; // ランダム文字

shuffle.start();
```

## 実用例1: ページ読み込み時の自動実行

```html
<h1 class="title">LOADING...</h1>
```

```javascript
window.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('.title');
    const shuffle = new ShuffleText(title);

    shuffle.duration = 800;
    shuffle.start();
});
```

`動画イメージ`
★動画中の最初の「LOADING...」と「途中の黒いまるがおちてこないのをイメージ」★★
<video controls width="600">
  <source src="../../images/chrome_TVnJAHhbls.mp4" type="video/mp4">
</video>








## 実用例2: クリックでテキスト変更

```html
<h1 class="click-text">Click Me!</h1>
<button id="changeBtn">テキスト変更</button>
```

```javascript
const text = document.querySelector('.click-text');
const shuffle = new ShuffleText(text);
const btn = document.getElementById('changeBtn');

const messages = ['HELLO!', 'WELCOME!', 'NICE!', 'COOL!'];
let index = 0;

btn.addEventListener('click', () => {
    index = (index + 1) % messages.length;
    shuffle.setText(messages[index]);
});
```
`動画イメージ`

<video controls width="600">
  <source src="../../images/chrome_HM7OFUycwA.mp4" type="video/mp4">
</video>






## 実用例3: 数字カウントアップ風

```html
<div class="counter">0</div>
```

```javascript
const counter = document.querySelector('.counter');
const shuffle = new ShuffleText(counter);

shuffle.sourceRandomCharacter = '0123456789'; // 数字のみ
shuffle.duration = 1000;

let count = 0;
setInterval(() => {
    count += 10;
    shuffle.setText(count.toString());
}, 2000);
```

## 実用例4: ハッカー風UI

```html
<div class="hacker-text">SYSTEM INITIALIZED</div>
```

```css
.hacker-text {
    font-family: 'Courier New', monospace;
    color: #00ff00;
    background: #000;
    padding: 20px;
    font-size: 24px;
    letter-spacing: 2px;
}
```

```javascript
const hacker = document.querySelector('.hacker-text');
const shuffle = new ShuffleText(hacker);

shuffle.sourceRandomCharacter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*';
shuffle.duration = 1200;
shuffle.fps = 20;

const commands = [
    'SYSTEM INITIALIZED',
    'CONNECTING TO SERVER',
    'ACCESS GRANTED',
    'DATA TRANSFER COMPLETE'
];

let i = 0;
setInterval(() => {
    i = (i + 1) % commands.length;
    shuffle.setText(commands[i]);
}, 3000);
```

## イベントリスナー付き

```javascript
const shuffle = new ShuffleText(element);

// ★ アニメーション完了時の処理
shuffle.addEventListener('complete', () => {
    console.log('アニメーション完了！');
});

shuffle.start();
```

## 複数要素に一括適用

```html
<h2 class="shuffle">Title 1</h2>
<h2 class="shuffle">Title 2</h2>
<h2 class="shuffle">Title 3</h2>
```

```javascript
const elements = document.querySelectorAll('.shuffle');

elements.forEach((el, index) => {
    const shuffle = new ShuffleText(el);
    shuffle.duration = 600;

    // 順番に実行（遅延付き）
    setTimeout(() => {
        shuffle.start();
    }, index * 200);
});
```

## ★ よくある使い方まとめ

| 用途 | duration | sourceRandomCharacter |
|------|----------|----------------------|
| タイトル演出 | 600-800 | 英数字 |
| ローディング | 1000-1500 | 記号混在 |
| 数字カウント | 800-1000 | 0-9のみ |
| ハッカー風 | 1200-2000 | 英数字+記号 |

## CDNリンク

```html
<!-- 最新版 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/shuffle-text/0.3.0/shuffle-text.min.js"></script>

<!-- または -->
<script src="https://unpkg.com/shuffle-text@0.3.0/build/shuffle-text.min.js"></script>
```

## 参考
- GitHub: https://github.com/ics-ikeda/shuffle-text
- 作者: ICS (日本)
