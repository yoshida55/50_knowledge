## テスト問題  html

これはテストです


### ul li メニューの作り方

メニューやリストを作るときは、ul と li を使います。navタグはメインメニューのときだけ使用します。

```html
<nav class="header_nav">
  <ul class="header_nav_list">
    <li class="header_nav_item">
      <a href="#menu" class="header_nav_link">MENU</a>
    </li>
    <li class="header_nav_item">
      <a href="#about" class="header_nav_link">ABOUT</a>
    </li>
    <li class="header_nav_item">
      <a href="#location" class="header_nav_link">LOCATION</a>
    </li>
  </ul>
</nav>
```

横並びメニューの基本スタイル

```css
.header_nav_list {
  display: flex;
  list-style: none;
  gap: 3rem;
}

.header_nav_link {
  display: block;
  text-decoration: none;
  color: #333;
  font-size: 1.4rem;
  padding: 1rem;
}
```

`display: block` をaタグに指定することで、paddingが効くようになり、クリック範囲が広がります。

縦書きで横並びにする場合

```html
<ul class="footer_location">
  <li class="nav-item">
    <a href="#">０３｜ＸＸＸＸ｜ＸＸＸＸ</a>
  </li>
  <li class="nav-item">
    <a href="#">〒１０６｜００３２　東京都港区六本木５丁目×××××</a>
  </li>
</ul>
```

```css
.footer_location {
  display: flex;
  writing-mode: vertical-rl;
  flex-direction: column;
  gap: 3rem;
}

.nav-item {
  writing-mode: vertical-rl;
}
```

`writing-mode: vertical-rl` で縦書きにし、`flex-direction: column` で横に並べます。これが縦書きで横並びにする時の呪文です。

縦に並べる場合（文字は横のまま）

```css
.header_nav_list {
  display: flex;
  flex-direction: column;
  list-style: none;
  gap: 2rem;
}

.header_nav_link {
  display: block;
  writing-mode: vertical-rl;
  text-decoration: none;
  padding: 1rem 0;
}
```

この場合は、リンクそれぞれが縦書きになって、縦に積み重なります。









<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="30" cy="50" r="20" fill="#f9e2af">
    <animate attributeName="cx" from="30" to="270" dur="2s" repeatCount="indefinite" direction="alternate"/>
  </circle>
</svg>


















▢ 　背景画像は PC と SP で切り替え（`<picture>`タグ or メディア切り替えたい場合は以下のように指定する。
background-image: url("../img/mainvisual-pc.jpg");をするときは
普段とちがって ima src と時と違い　../一度上のフォルダに移動する必要がある

▢ 　ＰＣとスマホで画像を変える場合は、HTML でＳＲＣを指定せずスマホ版で以下のように設定する

<header class="header_area">

```css

★この場合、通常に画像がひろがる
.header_area {
background-image: url("../img/mainvisual-pc.jpg");
background-size: cover; /* 要素いっぱいに広げる */
background-position: center; /* 中央基準で表示 */
}

★　これで設定すると赤玉が画像よりも多くみえる（パディングは内部の背景を広げるためにある。つまり水玉の領域がひろがる）
#school_overview {
  padding: 5rem 0 10rem 0;
  /* 赤い水玉背景（radial-gradientで作る） */
  background-image: url("../img/bg.gif");
  background-size: 75rem 75rem; /* ✅ 固定サイズ */
  background-repeat: repeat; /* ✅ 繰り返し */

  margin-bottom: 10rem;
}
```

▢ ポジションアブソリュートの使い方親に relative、子に absolute を設定します。
親（position: relative）└ 子（position: absolute）← 親を基準に配置される
★ 同じ階層でもできる上は間違い → かならず重ねたい要素をリラティブにする。

HTML 構造-------------------------------------------------

<header class="header_area"> <!-- 親 -->
  <nav>
    <!-- ナビゲーション -->
  </nav>
  ★親のメインヘッダに対して、子階層にセットする
  <div class="header_online">  <!-- 子：これを左下に配置したい -->
    <a href="https://example.com" target="_blank" rel="noopener noreferrer">
      オンラインストアを見る
    </a>
  </div>
</header>
---
ポジションリラティブは子要素に書く必要ある。
.header*area {
position: relative; /* ← これがないと absolute が効かない */
}
/* 子：左下に配置 */
.header*online {
position: absolute; /* 親を基準に配置 */
left: 20px; /* 左から 20px */
bottom: 20px; /* 下から 20px */
}
HTML 構造-------------------------------------------------

▢ 　たてがきは writing-mode: vertical-rl;これは親要素ではなく a タグにかく。

▢ 　 prettier できずいたらすぐ、コパイロットにいってタグをなおしてもらう
▢ 　フレックスは、上にかかれたものから左から順番に記載されることをわすれない。
▢ 　 flex 子フレックスで、width を指定すると、flex1 としているより優先されため、基本、サイズを指定する必要がない場合は flex1 にきめておくと楽。



## 💡 重要ポイント
```
flex: 1 → 「親の中で等分する魔法」
width → 「この幅に固定！」という命令

両方書くと width が勝つ！
```


ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
自分でデザインカンプ
▢ 画面をよこにみて、absolute の回数を減らす。(理由、
★Absolute を減らして、流れ（横方向）で作る理由
壊れないから（一番大事）
Absolute は「画鋲で止める」ようなものです。
画面の大きさが変わると、止めた場所がズレてレイアウトが崩壊します。
流れで作れば、画面に合わせて柔軟に動いてくれます。
計算しなくていいから vertical-rl（縦書きモード）を使えば、
h1（ロゴ）の隣に nav（メニュー）が自動的に並びます。

座標を計算して配置する手間がゼロになります。
結論： 「頑張って配置する」のではなく、「勝手に並ぶようにする」のがプロの書き方です。)

header
h1
nav

▢ 　クラスを直接指定する方法タグ名で省略せず　ネストされたクラス名もかならずかく
a タグにもクラス名をかっく

<div class="online_absolute">
  <a href="#" target="_blank" class="online_link">オンラインストアを見る</a>
</div>

▢ 全体像を把握してまとめてパディングをしかける
▢ 　ぜんたいのメインカラーがあれば最初に BODY でいろをぬっておくそうすると ection のエリアでマージンボトムしたときも色がつく

▢ 更新した時途中からブラウザで表示したい場合飛ぶ　リンクする　遷移する

・URL の最後に、　 about をつける　 #移動　#リロード #遷移 #セクション
http://localhost:5500/#about
・HTML のセクションで ID をふる

<section id="about" class="concept_area">

1. 大事(「１」が本命できなかった「２」をする)`

「１」直った原因（推測）

settings.json に fullReload: true を追加した

CSS 保存時も完全リロードするようになった
window.addEventListener("load")が発火するようになった

Live Server を再起動した

設定が反映されるには再起動が必要
古いキャッシュがクリアされた

VSCode を再起動した

拡張機能が正しく読み込まれた
設定ファイルが確実に反映された

「２」

1. 手順：CSS 保存時もリロードさせる設定
   VS Code で Ctrl + , (カンマ) を押して設定を開く。

上の検索バーに live server full と入力する。

出てきた項目の Live Server > Settings: Full Reload にチェックを入れる（オンにする）。

3. javaScript に以下を追加する(これは多分関係ない)

```JavaScript
window.addEventListener('load', () => {
    setTimeout(() => {
        window.location.hash = "";
        window.location.hash = "footer";
    }, 100);
});
```

▢flex で指定した画像に absolute で文字を配置しようとすると、top bottom などと指定した位置と、表示があわなくなる
Flex だと画像の高さが隣のタイトルに合わせられてしまうので、
align-items: flex-start をかけて高さを画像に合わせる必要がある。

▢ うっかりミスサイズが違うと思ったら、Style CSS でフォントサイズを 1400px に指定しているのを忘れていた。

※設計者は、 「ヘッダーは文字が流れるだけだから、縦書き設定だけで十分」
「商品はスマホでレイアウトをガラッと変えたいし、画像との位置関係を調整したいから、Flexbox という強力なツールを使おう」
と判断して使い分けた、ということです。

▢ 　インライン要素は、display blockブロック要素にすることによって、padding、border、width、height が
すべて正確に計算されるようになる。
よく使うインライン要素

<a>: リンク
<span>: テキストのグループ化（装飾用）
<strong> / <b>: 太字
<em> / <i>: 斜体
<label>: フォームのラベル
<small>: 注釈や細目

▢ 　パディングはあくまで中身の文字と文字というか、要素と外の枠ボックスの距離を取るものである。
もしも自分で分からなくなったら、ボーダーで指定するとイメージが開く。
ボーダーを指定せずに、パディングだけして色だけ指定すると、
枠がない色を作ることができる。

![](2026-01-02-19-55-21.png)

## 🏗 HTML タグの設計図（使い分け）まとめ

### 1. ロゴと見出し

- **h1:** サイトロゴに使用。画像を入れる場合は `h1` で囲む。
  ```html
  <h1 class="logo"><img src="img/logo.svg" alt="ロゴ" /></h1>
  ```
- **h2:** セクションのタイトル。日英併記などは `span` を使い、見出しタグの中にインライン要素として配置する。
  ```html
  <h2 class="news_title">
    <span class="title_news">News</span>
    <span class="title_notice">お知らせ</span>
  </h2>
  ```

### 2. 日付とお知らせ / メニュー (dl, dt, dd)

- **用途:** 「項目名（日付・料理名）」と「値（内容・価格）」がセットの時。
- **暗記:** 「dl」だけ打てばサジェストされるので、それを活用する。
  ```html
  <dl class="news_list">
    <div class="news_item">
      <!-- divで囲むとレイアウトしやすい -->
      <dt>2021.01.01</dt>
      <dd>タイトルタイトル...</dd>
    </div>
  </dl>
  ```

### 3. 見出しと詳細説明 (h2 + p)

- **原則:** 見出しは `h2`、説明の文章は `p`。
- **禁止:** `h2` の中に `div` や `p` などを入れることは文法上禁止（インライン要素のみ OK）。
- **構造:** まとめる場合は全体を `div` で囲む。
  ```html
  <div class="fashion_wrapper">
    <h2 class="fashion_title">Fashion & Style</h2>
    <p class="fashion_description">テキストテキスト...</p>
  </div>
  ```

### 4. ナビゲーション (nav)

- メインメニューの場合だけ `nav` を使用する。通常 `nav > ul > li > a` の構造にする。

---

▢ 　 AI にお願いするとき、サンプル SVG
![](images/2026-01-02-21-20-18.png)

▢GitHub に支持する才能、テンプレート

1. スクリーショットを保存して、立ち上げてお

セクションの画像: 1 画面に収まる範囲のスクリーンショット。
素材（アセット）: 使用する画像ファイル名（例：img/ice-cream.jpg）。
構造の指定: 「ここは dl/dt/dd を使う」「ここは h2 と span の構成」などの指示。



![](images/2026-01-03-11-20-23.png)

※「軸が逆転して、混乱するのは」
writing-mode: vertical-rl 文字が流れる方向

親が縦書き（NG 例）:
flex directon row（本来「横」） → 「上から下」に並ぶようになる。
column（本来「縦」） → 「右から左」に並ぶようになる。
これが「軸が回転して予測不能になる」原因です。
![](images/2026-01-08-06-25-41.png)

▢Position: absolute;をする場合、

前 ■ position: absolute の親子関係とサイズの一致
画像を基準にテキストを配置したい場合、画像そのものではなく、画像とテキストを包む「親ボックス」を基準点（relative）にするのが鉄則です。

なお、まんなかに記載したい場合は

```css
.test{
position:absolute
left: 0;
right: 0;

margin: 0 auto;

top: 50%;
transform: translateY(-50%); /* ★下に着すぎたものを半分↑に戻す */
}
```

## 親要素に relative をかける理由（画像へのテキスト重ね）

1. 構造の考え方
   親ボックス（.concept_card）は、中にある画像（.concept_img）のサイズに合わせて自動的に伸縮します。そのため、「親の枠」と「画像の枠」は基本的に一致します。

メリット: 画像に直接 absolute をかける必要がなく、レイアウトが崩れにくい。
ポイント: relative は「コンセプトイメージ」ではなく「親のカード」に実施する。

2. 実装コード
   <!-- 親：ここで relative を実施する（基準点） -->
   <div class="concept_card">
     <img class="concept_img" src="xxx" alt="X/>
     <!-- 子：親を基準に自由に移動する -->
     <p class="concept_text">テキストテキスト</p>
   </div>

```css
.concept_card {
position: relative; /_ 親：基準点 _/
}

.concept_text {
width: 35rem;
height: 14rem;
position: absolute; /_ 子：親を基準に浮く _/
bottom: 2rem;
left: 2rem;
}

```

3. なぜサイズが一致するのか
   親要素が「ピッタリ重なっている」ように見えるのは、親要素が子要素（画像）のサイズに合わせて伸縮する性質を持っているからです。

この性質を利用することで

、`画像からの距離を測るのではなく、親ボックスからの距離を指定するだけで、意図した位置（左下など）にテキストを正確に配置できます。`

![](2026-01-03-17-02-32.png)

▢ 　大事　暗記　パーセント(%)とレム(rem)の使い分け
使い分けの目安：

文字サイズや余白: rem（画面に合わせて自動拡大縮小）
レイアウトの横幅（カラム）: %（親要素の中での占有率を決定）
![](2026-01-03-17-46-55.png)

▢ 　問題：仕様書で「幅は % 指定」と言われたけど、% にするとデザインカンプとサイズがズレる。

理由：
% は「親の箱の中で何割を占めるか」を決めるだけで、「画像の大きさ」そのものは制御できないから。

解決策：
% と max-width（rem）を同時に指定する。

```css
.concept_card {
  /* 親の中での占有率（仕様書の指示） */
  width: 65%;

  /* 画像の最大サイズをロック（カンプ通りのサイズ） */
  max-width: 63rem;
}
```

![](2026-01-03-18-08-07.png)

「細かい数字」ではなく「見た目のバランス」を守るのがレスポンシブの鉄則です。

## 分かった一番重要なこと　暗記

まず、
width 100％　
max-width: 140rem
max-width を指定する理由としては
前段のスタイル.css とかで

```css
html {
  font-size: calc(10 / 1400 * 100vw);
  /* 画面幅1280pxで10px*/
}
```

これがないことを想定している。
なぜならば、一緒にサイズが伸びてしまうからあまり意味がない。

もしもスタイルＣＳＳで上記の記述があるならば、以下をしていけばいい。

```css
html {
  /* 10px と 計算値のうち、小さい方が採用されます */
  font-size: min(10px, calc(10 / 1400 * 100vw));
}
```

## ▢ 拡張ツールの見方　暗記
紫・・・その紫色の部分は、justify-content: center; によって生じている Flexbox の余白（整列スペース） です。

## ▢ 　マージンとパディングの違い
暗記
親要素から見れば、子要素はパッディングで設定する。子要素同士から見れば、マージンで他の距離を取る。

つまり。おやで最初にパディングを
とるのがわかりやすい。

▢ 　 📝 縦書きレイアウトの失敗メモ　暗記
`Flexbox` を組み合わせる際の落とし穴」**についての非常に重要なメモです。


【失敗の原因：軸の回転】

`現象`: 親要素に writing-mode: vertical-rl を指定すると、Flexboxの「主軸」と「交差軸」が90度回転します。
`結果`: flex-direction: row なのに要素が縦に並んだり、justify-content（横方向のはず）が上下の制御になったりして、配置の計算が予測不能になります。


【正解の鉄則：役割分担】
`親要素`: 配置（Flexbox）を担当。**横書き（デフォルト）**のままにしておくことで、使い慣れたFlexboxのルールで要素を並べられます。
`子要素`: 文字の向き（writing-mode）を担当。子だけに縦書きを適用することで、親の配置ルールを壊さずに文字だけを縦に流せます。
`メリット`: Flexboxが本来の動きをするため、align-items や gap での微調整が直感的かつ確実に行えます。


```css
/* 親：配置（横並び）だけを行う */
.news_area {
  display: flex;
  flex-direction: row-reverse; /* 右から左へ並べる（縦書きの並び順） */
}

/* 子：中身の文字だけを縦書きにする */
.news_title,
.news_wrapper {
  writing-mode: vertical-rl;
}
```
⇀「親は箱を並べる係、子は文字の向きを決める係」と役割を完全に分けるのが、レイアウトを崩さない最大のコツです。

▢ 　うっかりミス子要素が一つだけなのに‘フレックス‘をかけてしまった。

## ▢ 　手書きの図形の書き方
手書きメモの形式

・画面に情報を混在させず、画面下に「クラス名」を記載し「プロパティ」を書くスタイルに統一します。

## ▢ 　パディング のかけかた
覚え方
（余白の目的）　　　　（使うもの全体に）
共通の余白　　　　　　親の padding
子ごとに違う余白　　　子の margin

今回は「他と合わせる」より「実際の構造に合わせる」が優先二重管理を避けた方が、3 ヶ月後の自分が楽です！

以下の場合は、右と下だけパディングをつける。
それ以外は、子でマージンで別々に管理する。
![](2026-01-04-09-13-54.png)

## ▢ 　 writing-mode: vertical-rl
これをかけることによって見方がかわる。flex direction :column;が横配置など

## ▢ 　うっかりミス
見た目が、自分の想定と違うと思った、デザインカンプ 1400px に対して、wrapper でサイズを max-with1200 にしていた。

-----------------------------↑ 上記追記済み　 GitHub インストラクションに

## ▢ メディアクエリ
/_ @media screen and (max-width: 375px) {
_/

## ▢ git ★github ルールに追加する必要なし
1. git の紐づけ

```
git init
git add .
git commit -m "first commit"

git remote add origin https://github.com/あなた/リポジトリ.git



git branch -M main
git push -u origin main

```


2. 最新情報を取得して、強制的に上書き
   git fetch origin
   git reset --hard origin/main

4. コンフリクト

1. 変更マージの下にある。ところでコンフリクトをしている。

もし、クリックして、コンフリクトを解消する。
・カラーのあるところの上に両方マージするみたいな文字がでるのでそれをクリック

・その後、変更マージの右側を＋ボタンをする。

・コミット、プッシュ


## ▢ 　以下のようにして　左右に画像と、その中にテキストを浮かびあがらせるこができる

![](2026-01-05-13-08-39.png)

画像へのテキストオーバーレイ構造
`仕組みの解説`
⇀ 画像とその上に表示したいテキストグループを、1つの「親要素（.img_item）」の中に同居させ、CSSで重ね合わせるレイアウトの手法です。

`各要素の役割`

親要素 (.img_item)
⇀ 重なり合う要素の「基準点（枠）」になります。CSSで position: relative を指定します。

画像 (.newspaper_img)
⇀ 土台となるコンテンツです。

重ねる要素 (.img_overlay)
⇀ 画像の上に浮かせる「膜」のような層です。CSSで position: absolute を指定することで、画像の範囲内の自由な位置（左下や中央など）に配置できます。

`この構造にするメリット`
⇀ 1つのセットとして完結しているため、このセットを .img_container 内でFlexboxなどを使って横並びにしたり、数を増やしたりするのが非常に簡単になります。


```css
/* 実装例のイメージ */
.img_item {
  position: relative; /* 基準にする */
}
.img_overlay {
  position: absolute; /* 親を基準に浮かせる */
  bottom: 0;
  left: 0;
  background: rgba(0,0,0,0.5); /* 背景を半透明にすることが多い */
}
```

## position: absolute で中央配置する方法

必要な 3 つの要素
css.overlay {
position: absolute;
left: 0; /_ 1. 基準の左端 _/
`right: 0;          /* 2. 基準の右端 */`
`width: 30rem;      /* 3. 自分の幅 */`
margin: 0 auto; /_ 4. 余りを均等に _/
}``
なぜ全部必要？
要素役割 left: 0; right: 0;「親の左端〜右端が基準」と伝える width 自分の幅を決める margin: 0 auto;余った幅を左右均等に分ける
イメージ図
親要素（position: relative）
┌─────────────────────────────────┐
│← left:0 right:0 →│
│ │
│ auto │ 30rem │ auto │
│ 余白 │ 要素 │ 余白 │
└─────────────────────────────────┘
注意点

親要素に position: relative; が必要
width または max-width がないと margin: auto は効かない
left: 0; right: 0; がないと基準が分からず中央にならない

縦方向も中央にしたい場合
css.overlay {
position: absolute;
top: 0;
bottom: 0;
left: 0;
right: 0;
width: 30rem;
height: 10rem;
margin: auto; /_ 上下左右すべて均等 _/
}

## Flexbox で両端揃え + 隙間を作る　 space between ですき間をつくることができる

space between width center

基本の書き方

```css
css.container {
  display: flex;
  justify-content: space-between;
}

.item {
  width: 49%; /* 合計98%、残り2%が隙間になる */
}
```

★ なぜ space-between？

1.  `両端に張り付き、隙間が自動調整される`
    ┌──────────── 親要素 ────────────┐
    │ ┌─ 49% ─┐ 2% ┌─ 49% ─┐ │
    │ │ item1 │ ← 隙間 → │ item2 │ │
    │ └───────┘ 自動 └───────┘ │
    ↑ 左端 右端 ↑
    └───────────────────────────────┘

2.  親の幅が変わってもレイアウトが崩れない
3.  隙間を計算しなくていい（自動で調整）

gap との違い
「方法」 「隙間」 「両端」
space-between + 自動 端に張り付く
width: % 調整  
gap: 固定値 固定 端に余白が
できることも

`使い分け`

| やりたいこと   | 書き方                            |
| :------------- | --------------------------------- |
| 両端揃え+隙間  | `space-between` + `width: %`      |
| 均等な固定隙間 | `gap`                             |
| 中央寄せ       | `justify-content: center` + `gap` |

3 つ以上並べる場合

```css
css.item {
  width: 32%;  /* 3つ × 32% = 96%、残り4%が隙間 */
```

}
┌─────────────────────────────────┐
│ ┌ 32% ┐ 2% ┌ 32% ┐ 2% ┌ 32% ┐│
│ │ 1 │ gap │ 2 │ gap │ 3 ││
│ └─────┘ └─────┘ └─────┘│
└─────────────────────────────────┘

# Flexbox の order で要素の順番を入れ替える

1. `基本`

- `order` プロパティで要素の表示順序を変更できる
- 数値が小さいほど前に表示される
- デフォルト値は `0`

2. `使い方`

```css
.parent {
  display: flex;
  flex-direction: column;
}

.item-a {
  order: 2; /* 後に表示 */
}

.item-b {
  order: 1; /* 先に表示 */
}
```

3. `実例：レスポンシブで順序変更`

```css
/* PC: 画像 → テキスト */
/* モバイル: テキスト → 画像 に変更 */

@media screen and (max-width: 896px) {
  .container {
    flex-direction: column;
  }

  .image {
    order: 2;
  }

  .text {
    order: 1;
  }
}
```

## ポイント

- HTML の構造を変えずに表示順だけ変更できる
- レスポンシブ対応で便利
- `flex-direction: column` と組み合わせると縦並びの順序も変えられる

### 問題点 width が指定されたボックスが中央寄せされていなかった（inline 要素も中央寄せされない）

### 原因

- `display: block;`で幅を`56rem`に固定していた
- 親要素の`text-align: center;`はテキストのみ中央寄せする
- ブロック要素自体を中央に配置するには`margin: 0 auto;`が必要

★ つまり、width を指定すると、`margin: 0 auto;`が必要　`text-alian:center;ではだめ！！`

### 解決策

```css
.fashion_description {
  display: block;
  width: 56rem;
  margin: 0 auto; /* 追加 */
  font-size: 1.4rem;
  line-height: 1.7rem;
}
```

### height の使い分け

## 背景画像（background-image）

✅ height を指定する
理由：箱の高さがないと画像が見えない

```css
#fashion {
  background-image: url(../img/fashion.jpg);
  height: 520px; /* 必要 */
}
```

### 普通の画像（<img>タグ）

❌ height を指定しない
理由：画像が元々サイズを持ってる

```css
img {
  width: 100%;
  /* heightは書かない */
}
```

---

## ■ Fashion セクション(画像を背景に、なかにテキストを重ね書きする)の作り方

### NG：<img>タグで画像を入れる
⇀しかもここはDIVにかえないといけない。

### OK：CSS で背景画像にする

```html
Fashion & Style テキスト Read More
```

```css
#fashion {
  background-image: url(../img/fashion.jpg);　★
  background-size: cover;
  height: 520px;
  text-align: center;  /* 中央揃え */
  padding-top: 60px;
}
```

---

## ■ 中央揃え

### NG：Flexbox で均等配置

### OK：text-align: center

```css
text-align: center; /* これだけでOK */
```

---

## ■ 覚えておくこと

- 背景画像 = 自分で高さを作る
- 普通の画像 = 勝手に高さがある
  (高さも指定したい場合、
  `width + height + object-fit: cover`)
- 中央揃え = text-align

## シンプルに背景を画像にして、なかに文字をれいれる方法

![](2026-01-06-09-52-06.png)

1. 画像を親（section 等）で、指定する。

```css
.fashion_area {
  width: 100%;
  height: 60rem;
  background-image: url("../img/fashion.jpg");
  background-size: cover; /* 要素いっぱいに広げる */
  background-position: center; /* 中央基準で表示 */
}
```

2. コンテナで画像まとめる

```css
.fashion_title {
  font-size: 2.4rem;
  font-weight: bold;
}

.fashion_description {
  display: block;
  font-size: 1.4rem;
}

.fashion_btn {
  display: inline-block;
  font-size: 1.2rem;
}
```

以下だけで完成

```html
<section class="fashion_area">
  <div class="fashion_wrapper">
    <h2 class="fashion_title">Fashion & Style</h2>
    <p class="fashion_description">
      テキストテキストテキストテキストテキストテキストテキストテキストテキストテキスト
      テキストテキストテキストテキストテキストテキストテキストテキストテキストテキスト
      テキストテキストテキストテキストテキストテキストテキストテキスト
    </p>
    <p class="fashion_btn">Read More</p>
  </div>
</section>
```

## なぜ、セクションの先頭は ID なのか？

ID クラスでない理由　クラス　セクション

アンカーリンク（ページ内リンク）のため

アンカーリンクはクラスにとぶことができない。

そのために、

<!-- ナビゲーション -->

<a href="#menu">MENU</a>

<!-- セクション -->
<section id="menu">...</section>

とする

## なぜ 100vh で画面いっぱいなのに min-height 100vh があるか。

height: 100vh 高さが画面サイズぴったりで**「固定」**される。 → 中身の文字などが増えると、枠からあふれて（はみ出して）しまう。

min-height: 100vh 高さは**「最低でも」画面サイズ。 → 中身が増えれば、それに合わせて自動で縦に伸びてくれる**。

結論 スマホなどで文字が折り返して縦に長くなっても背景が途切れないよう、min-height: 100vh を使うのが安全です。

## absolute で画面の中央にもってくる　 translateY 　 relative リラティブ　アブソリュート

margin 0 auto transform: translateY(-50%);

以下のようにすると画面中央にくる

```css
.site_title {
  position: absolute;

  right: 0;
  left: 0;

  margin: 0 auto;

  width: 48rem; ⇀これも必要

  top: 50%;
  transform: translateY(-50%); ★下に着すぎたものを半分↑に戻す
}
```

## 拡張機能

1. paste image
   カレントディレクトリではなくて
   特定のフォルダに保存する方法

```txt
VS Codeの設定（Ctrl + ,）で「paste image」と検索し、以下の通り書き換えてください。

Paste Image: Base Path
${currentFileDir} に変更
Paste Image: Path
images に変更

```

2. Restore Editors

VS Code レイアウト復元ショートカット
Editors をインストール

保存　 Restore Editors: Save Editor Layout
ショートカットキー設定

keybindings.json に追加：
json{
"key": "ctrl+alt+s",
"command": "restoreEditors.save"
},
{
"key": "ctrl+alt+r",
"command": "restoreEditors.restore"
}
使い方

保存: レイアウトを作って Ctrl+Alt+S
復元: Ctrl+Alt+R → リストから選択

3. サイドバーを閉じる
   ショートカットキー設定
   keybindings.json に追加：

{
"key": "escape",
"command": "workbench.action.closeSidebar",
"when": "sideBarVisible && !inQuickOpen && !suggestWidgetVisible"
}

4. CSS Navigation
   HTML のクラスをサジェストなどをする。

## 様々な flex のパターン

dd dl dt css jump 上級

・２カラムのメニュー表を作成する
左側にメニュー　　右にもメニュー
しかも、メニューごとに、
商品名・・・・価格

---

COffee food
aice ・・・100 sand・・・200
aice2 ・・ 200 　　 sand2....300

```html
➁menu-content (flex 親) 　 ➂meny_item（小　coffee等「←」flex 親）
　　➃dl(商品名) ⑤dt（価格） ➂.menu-item（小　food等「⇀」flex 親）
```

## h2 の使い方

## 本体自体を動かすときは、これをすれば、margin bottom や padding

をつかわず移動ででる

transform: translateY(2px);

パディングとマージンボトムとの違い
要するに、要素間のサイズとか、そういったものがなくなる。それ自体が動くから。

![](images/2026-01-07-06-18-47.png)!



## テキストなどの幅をサイズに丁度にボックスを調整する

ボタン」や「ラベル」など、背景色をつけつつ中身の文字サイズにピタッと合わせたいときには、inline-block

文字サイズに合わせてボックスのサイズを決めるっていうのをメモ.mdから探してblock = 親の幅いっぱいに広がる箱
inline-block = 中身の幅だけの箱（でも高さと幅を指定できる）


## パララックス　

[プレビュー](http://localhost:54321/preview-20260215-042326.html)

透ける　背景

`background-attachment: fixed;` は背景画像をビューポートに固定するプロパティで、透過効果とは関係ありません。

/* ✨
# `background-attachment: fixed;` の説明

## どういうこと？
背景画像がページのスクロールに追従せず、**画面に貼り付いたまま動かない**状態になります。

## 具体的な動き
- **通常**：ページをスクロールすると背景も一緒に動く
- **fixed**：ページをスクロールしても背景は画面の同じ位置に留まる（コンテンツだけが上下に動く）

## どんな時に使う？

### 1. **パララックス効果**
.hero {
  background-image: url('背景.jpg');
  background-attachment: fixed;
}
→ 背景が固定され、手前のコンテンツだけ動いて奥行き感を演出

/* ✨
# 実際に動くHTMLで説明
[プレビュー](http://localhost:54321/preview-20260214-065437.html)


## 動きの違い

- **🔴 通常部分**：スクロー���で背景も消えていく
- **🟢 固定部分**：スクロールしても背景は画面に張り付いたまま、白いボックスだけが上に移動

→ **「窓から外の景色を見ているような効果」** が `fixed` です！
*/

### 2. **ヘッダー画像の演出**
サイトのトップページなどで、スクロールしても背景画像が動かず、テキストだけが流れていく効果

### 3. **セクション区切り**
各セクション間に固定背景を挟んで、メリハリのあるデザインに

---

**要するに**：「見た目のおしゃれな演出」に使うプロパティです！
*/

##  ★もし画面の途中で固定をいれたい場合 パララックス html
/* ✨
画面の途中でパララックス効果を作る方法は主に2つあります：

## 1. **`background-attachment: fixed;` を使う場合**
そのセクション自体に `fixed` を適用すれば、そのセクションが画面に入ったときに背景が固定されます。

.middle-section {
  background-image: url('image.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 500px;
}

**注意点**: 背景画像は**ビューポート全体**に対して固定されるため、セクションの位置に合わせて `background-position` で調整が必要です。

## 2. **JavaScriptでスクロール連動させる**
より細かい制御が必要な場合は、スクロール量に応じて背景位置を変更します。

window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  document.querySelector('.middle-section').style.backgroundPositionY = 
    (scrolled * 0.5) + 'px';
});

**実務では**: セクションごとに異なる背景を固定したい場合、`fixed` よりもJavaScriptやCSSの `transform` を使った実装の方が制御しやすいことが多いです。
*/

★JavaScriptを使ったときのイメージ！
[プレビュー](http://localhost:54321/preview-20260215-042746.html)



![](images/2026-02-07-16-31-23.png)

## パララックス効果（視差効果）を実装する際に、背景画像をわざと大きく表示（ズームアップ）させている設定です。 html


「画像を拡大して画面に固定することで、スクロールしたときにダイナミックに景色が変わるように見せている」



background-size: 150%;
【なぜ150%に設定するのか】
`理由`: background-attachment: fixed; を使うと、画像が画面（ビューポート）に固定されます。
`挙動`: 固定された画像は、要素の幅ではなく「画面の幅」を基準にサイズが決まるため、通常の cover 指定だと、意図した部分が隠れたり、画像が小さく見えたりすることがあります。
`解決`: 150% のように数値を大きくすることで、画像の一部を拡大し、スクロールした際の変化（奥行き感）をより強調できます。



```css
.parallax_area {
  /* 背景画像を表示するための最低限の高さが必要（03_mistakes 参照） */
  min-height: 50rem;

  /* 背景画像の指定 (ルール4: パスは ../img/ から開始) */
  background-image: url("../img/your-image.jpg");
  background-repeat: no-repeat;
  background-position: center;

  /* パララックスの設定：背景をスクロールに固定する */
  background-attachment: fixed;

  /* 背景サイズの拡大：デザインカンプに合わせて調整 */
  background-size: 150%;
}
```

※　サイドバー左固定などは　 height を使用する

背景のサイズを大きくする。

![](images/2026-01-07-13-10-02.png)


## width を指定して、height を auto にすると自然なかたちになる。 html

# ヘッダータイトル　固定幅　画像指定

とくにボックスに文字があてはまらない時など利用するとよい。また height は基本しようしないので、
その理由からも多用するとよい。



# サイドバーに固定で表示するときの構文

```css
#header {
  width: 300px;
  height: 100vh;  →　これがないと上部にある文字だけ、下にスクロールしても表示されない。
  position: fixed;
  top: 0;　
  left: 0;
  0: 画面の一番上（上端から 0px の位置）に固定。
　0: 画面の一番左（左端から 0px の位置）に固定。
　※top: 0 と left: 0 は、ヘッダーという 「箱そのも　の」を画面の真ん中ではなく、左上の端（0,0）にピタ　ッと置く という意味です。

  padding: 60px 40px;
  background-color: #fff;
  display: flex;
  flex-direction: column;
}
```

## radius で ◯（丸の形の形をつくる） html

```html
<ul class="feature_list">
  <li class="list">
    <a class="radius" href="#">design</a>
  </li>
</ul>
```

```css
/* aタグで大きな〇を作るロジック radius*/
.radius {
  width: 100%;
  border: solid 1px #fff;
  border-radius: 50%; /* ← これで円になる！ */
  color: #fff;
  display: block;
  padding: calc(50% - 11px) 0; /* 上下のパディングで高さを確保 */
}
```

## justify-content: space-between を使用した際は、子要素にサイズを指定できる。間のギャップは、自動！！ html

「子要素にパーセント（%）や
幅（width）を指定することは【可能】であり、むしろ【必須】に近いテクニック」**

なお、要素別にサイズを決めることも可能
3つ以上の要素がある場合：
もし [30%] [10%] [40%] とバラバラな幅で space-between を使うと、それぞれのアイテムの間の隙間（ギャップ）自体は同じサイズになります。

例）
「2カラムのメニュー表」などで、左側を少し狭く、右側を広くしたい時などに活用できるテクニックです。

・子要素の幅を 30% に指定します。
3個並ぶと：30% + 30% + 30% = 90%
残り：100% - 90% = 10%
この余った 10% が、自動的に2つの隙間（各5%）になります。


## 「文字の上下にある『見えない余白』を限界まで削る」

line-height:1

![](images/2026-02-07-00-33-44.png)


大きなボックス（高さがしっかりあるボックス）で line-height: 1; を使うと、**「文字が天井（一番上）にベタッと張り付いた状態」**になります。
(上の余白が消える)



## AI に確認する際の注意事項

・ソースを渡す
・デザインカンプを渡す
・専門用語をつかう。
例）　たとえば台形とか、逆台形とか　調べる





----------------------------------------------------------------


## ▢ ホバー時にレイアウトを崩さない「枠線」の使い分け（outline vs border）
`【何回なソースはシンプルをこころがける】`

AI にたのんで、必要最小限のソースにしてもらって
確実に理解していく。ソースがおおくあると
必ず混乱するので。

結論：
特定の要素をホバーした際に「ガタッ」と周りが動いてしまうのを防ぐには、border ではなく outline を使う。

1. なぜ border はずれるのか？
   border は**「箱の厚み」**として計算されます。

0px から 3px に変えると、その要素自体のサイズが上下左右に 3px ずつ大きくなります。
大きくなった分、隣にある要素や下の要素を「よいしょ」と押し出してしまうため、画面が揺れます。 2. なぜ outline はずれないのか？
outline は**「箱の外側に描かれる線」**であり、計算上のサイズは 0 です。

太さをどれだけ変えても、要素自体の大きさ（占有スペース）は変わりません。
他の要素に干渉しないため、レイアウトが一切崩れません。 3. 実装の比較 4. 便利なプロパティ：outline-offset
outline は標準では「箱の外側」に線がつきますが、outline-offset を使うと位置を調整できます。

outline-offset: -3px; ：線の厚み分だけ内側に食い込ませる（デザインカンプ通りに作りやすい）。
outline-offset: 2px; ：箱から 2px 浮かせて線をつける。

## サイドメニューーから header メニューに変更する

## 固定サイドバーをけす。

## すでにあるものを移動する

え？ポジションアブソリュートしなくても top とか　 left で位置かえられるの？

`答え：positionを指定すれば使える`
top, left, right, bottom は、position を指定すれば使えます：

```css
❌ これはダメ（デフォルトは static） _/

#navi {
left: -300px; /_ 効かない！ _/
}

/_ ✅ これなら OK _/

#navi {
position: fixed; /_ または absolute, relative _/
left: -300px; /_ 効く！ _/
}

```

・強引に画面の左にけす。
![](images/2026-01-09-13-32-08.png)



## 三角形の図形の作り方

```css
すでにある要素に対して、疑似要素で、三角を追加する。なお:afterでもbeforeでも同じ。
  contact_card::after {
  content: "";
  display: block;
  position: absolute;
  /* 三角形のサイズ（お好みで調整してください） */
  width: 2.5rem;
  height: 2.5rem;

  bottom: 0.3rem; /* 下端に配置 */
  right: 0.3rem; /* 右端に配置 */

  /* グラデーションを使って直角三角形を作る魔法の記述 */
  /* 「右下から左上に向かって、50%の位置まで黒、残りは透明」という指定です */
  background: linear-gradient(to top left, #000000 50%, transparent 50%);
  /* カードの枠線の上に重なるように z-index を調整 */
  z-index: 2;
}
```


## トップの画面を固定にして、その下のセクションをスクロールするときに、裏の画面をのこして、重ねて表示させる。　詳細は　./その他/疑問・ソーステストあり md を参照

`ソースをみたいときは、82_CSS_JUMP_上級編_ピカソ`
![](images/2026-01-10-14-23-18.png)

##　命名ルール　規則

▢ 　コメントをしっかりかく。そうすると補完ででてくる。
## ヘッダーを作成するうえでの注意事項

header は
/_ 高さを固定しない（padding 分も含めて自然に） _/
height: auto;
min-height: 6.2rem;

`中身が少ないとき： min-height が優先され、6.2rem の高さになります。`
`中身が増えたとき（文字が改行した時など）： height: auto のおかげで、中身がはみ出さないように高さが 7rem、8rem と自動で伸びます。`

![](images/2026-02-06-22-20-29.png)

★ 基本は auto 動作して まわりのパディングとかなかみの画像にあわせて伸縮する！！

最低ラインを確保して、ふえたときは auto でまわりのサイズにあわせる

## ショートカットキー　ホットキー

ALT L⇀ 　 O 　ライブサーバー
CTRL 　 SHIft O クラス検索
Ctrl+P → ファイル名入力 → Enter → Alt+B → 
ブラウザ表示
CTRL　：　セクション一覧表示
Ctrl+Shift+7: クイズ起動
Ctrl+Shift+M: メモ検索
Ctrl+Shift+l: セクションリスと表示





## 🛠 問題と解決方法

### 問題 2: ブラウザ幅を狭めてもハンバーガーメニューが表示されない

- **原因:**
  - 通常のブラウザウィンドウのサイズ変更では、ビューポート幅が正しく認識されない場合がある。
- **解決方法:** -　画面のズームの幅をかえる。


## 左右　に枠やマージンやパディングがあって、中央のボックス（width）のサイズをセットしたいとき。
##　またそれを中間にもってきたいとき
コンテンツ幅などに多用する
  width: calc(100% - 40rem);
  margin 0 auto


## メニューが２列あって、同じ幅でフォーマットを構築する際の計算式


```css
.price_area
 {
  width: calc(100% - 40rem);　★コンテンツエリア分残すにはこう記載する。
  margin: 0 auto;
}


/* 各カラム（左・右） 共通クラス*/
/* エリア全体 */
.price_area {
  display: flex;
  justify-content: center;
}

.price_column {
  width: 50%;　　　　★半分ずつなので５０パーセント
  padding: 0 3rem;
  text-align: center;
}

/* 左側のカラム 詳細　みぎにボーダーをつけるなど*/　　★　一応中央線もかいておいた
.left_column {
  border-right: 1px solid black;
}

```

## 背景コンテンツエリアの固定背景固定（パララックス風）の表示を記載したいとき前お物理エリアの背景画像分のサイズを確保したい場合、　シンプルなパララックス

※パララックス・・・視差、画面に奥行きや立体感、没入感を出す演出技法のことを指します


```html
  ・ここに背景画像があるとするパララックス。fixed

  <!-- コンテンツエリア -->
  <main class="main"> ★ここで`padding-top` パララックスのサイズ分を指定するとで、透明なすき間をつくる
    <section class="test_area"></section>
    <section></section>
  </main>
```

```css
.main {
  padding-top: 100vh; ★ここが大事
  /* ❌ ここに色があると、上のpadding部分も白くなっちゃう */
  /* background-color: rgba(255, 255, 255, 0.8); */

  /* ⭕️ なので、ここは透明にする（または行ごと消す） */
  background-color: transparent;　★カラーがこれで透明になる。
}

  .test_area{
  width: 100%;
  height: 150rem; ★ここは今テストなのでこうしているが実際はautoなどでつまった分だけふやしていく。★デザインカンプなどで決まっている場合は、min-height を使う

  margin: 0 auto;
  background-color: rgba(46, 12, 160, 0.8);
}

```
}
![](images/2026-01-14-21-35-54.png)



## HTMLの構造

・基本の書き方

`ヘッダーの書き方`
classではなく IDを理由する。

`ログはH1を利用する`
ロゴはH1って、文字ないのになぜか右SEO対策
```html
<h1 class="site-title">
  <a href="#"><img src="img/logo-r.svg" alt="BBB英会話スクール" /></a>
</h1>
```


▢　環境整理  ★環境構築　
SVG表示保存CS+S.ahk　
で使用。　これがあることによって、保存先が以下となる。
★同じツールを家と会社で使い回すための改修
【ポイント　環境変数で環境ごとに以下を設定する】
・KNOWLEDGE_ROOT・・・SVGを保存する先を設定する

ここで取得したフォルダを同じ階層の各プロジェクト用資料などに移動したりする。



## position: fixed はrelativeも兼ねる。つまり、子で Absoluteが指定できる。

✅ position: fixed でも top / right / bottom / left が使える

```css
/* position: fixed = 画面全体を基準に固定 */
.page_container {
    position: fixed;  /* 画面全体を基準 */
    top: 2rem;        /* 上から2rem */
    right: 5rem;      /* 右から5rem */
    z-index: 1200;
}
```

### 📊 fixed vs absolute の違い

| position | 基準 | 画面を伸ばすと |
|----------|------|---------------|
| **fixed** | 画面全体 | 右端からの距離が固定 ✅ |
| **absolute** | 親要素 | 親の幅が変わる → 位置が中央に寄る ❌ |

### 💡 使い分け

```css
/* ❌ absolute: 親要素を基準（画面を伸ばすと位置がズレる） */
#mainVisual_area {
    width: calc(100% - var(--header-side-width)); /* 可変 */
}
.page_container {
    position: absolute;  /* 親要素を基準 */
    right: calc(var(--header-side-width) + 2rem);
    /* → 画面を伸ばすと親の幅が広がる → 中央に寄る */
}

/* ✅ fixed: 画面全体を基準（常に右端から固定距離） */
.page_container {
    position: fixed;  /* 画面全体を基準 */
    right: calc(var(--header-side-width) + 2rem);
    /* → 画面を伸ばしても右端から固定 */
}
```


## サイドバーのメニューの文字列が文字幅だけじゃなくて、文字幅＋残りの余白ありでクリックできてしまう場合

```css
/* メニューリスト 縦 */
.nav_list {
  list-style: none;
  padding: 2rem 0 0; /* 上に2remの余白を指定 */
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 3rem;
  align-items: flex-start; ★ここで制御する。　stretchなどにすると横全体になる
}

```
  ## 動作の違い

### `align-items: flex-start`（現在の設定）
- 子要素を左端に配置
- 子要素の幅 = **コンテンツ（文字）の幅のみ**
- クリック範囲 = 文字部分だけ ✅

### `align-items: stretch`（デフォルト値）
- 子要素を横幅いっぱいに伸ばす
- 子要素の幅 = **サイドバー全体の幅**
- クリック範囲 = 文字 + 右側の余白全体 ❌













```

## JavaScriptでイベントリスナーを実行したときに動かない。


イベントリスナーのクラスはIDで指定する必要がある。

```HTML
<!-- ヘッダー SPののみ表示-->
<header id="header" class="header">
  <div class="log_img"></div>
</header>

```


## なめらか(滑らかに)に移動させたいときは、以下の構文を使う。

ゆっくりと　アニメーション。これは左固定メニューバーから、を外部から引っ張りだして表示させるとき

```css
.header {
  position: fixed;
  background-color: white;
  /* ▼ 変化を滑らかにする設定はここに書く */★
  transition: transform 0.3s ease-in-out;
}


★transitiontransforms.html


.header.hidden {　　　　　　　　　 ★JavaScriptでhiddenにした。
  transform: translateX(-100%);　★要素分移動する
  transition: transform 0.3s ease-in-out;　★なめらかにする
}
```

**`.header` の方だけに書けばOK**です。
/* ✨
# HTMLの例



**動作説明:**
- ボタンを押すと、`.hidden`クラスが付いたり外れたりする
- メニューが左からスルッと出たり隠れたりする
*/




## オーバーレイ、黒いマスクのつけ方

```html
<!-- オーバーレイ　左固定メニューバーを開いた際に暗くする -->
<div id="overlay" class="overlay"></div>
```

```javascript
const hamburger = document.getElementById("hamburger-btn");
hamburger.addEventListener("click", function () {
  overlay.classList.toggle("open");
```

```css
  /* レスポンシブ ハンバーガーメニューがclickされたらオーバーレイ */
  .overlay.open {
    position: fixed;  
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 800;
  }
```



## パララックス、レイヤーを重ねるときに必要なこと, 

・親の要素で、fixed は親1箇所のみ

![](images/2026-02-07-03-38-27.png)




## フレックスボックスにするか、アブソリュートにするかの切り分け

・固定メニュー（ヘッダーがあるような）があって, がある場合、position absolute,　

・ ただ、Flexboxでも、右は下開始、左は上開始とか、そういった柔軟性はある。


## 要素を隠して特定のアクションで出力させたい場合、

```css
.reason_card {
  height: 20rem;
  background: #fff; 
  width: 50%; 
  opacity: 0; ★これでかくしておく。JavaScriptでオンにするまで
  transition: all 0.5s ease-out;　★表示する速度を決める
}

.reason_card--right {　　★これは左右で二つ表示部分があるので、クラスをわけている。
  border-radius: 2rem 0 0 2rem;
  margin-left: auto;　　★ここは直接的に関係ないが、
  　　　　　　　　　　　　左の隙間をすべて埋めるときにこうすると便利。
  transform: translateX(100%); /* ★右に隠す */
}

```

![](images/2026-01-18-07-11-37.png)


## 専門用語

1. お互いに会話している形式
UIデザインでは一般的に**「吹き出し形式」や
「チャットUI」**と呼ばれます。

2. 脇からひゅーっと出る動き
「スライドイン (Slide-in)」**と言います。

3. CTA（Call To Action）は、日本語で「行動喚起」と呼ばれます。

Webサイトにおいて、訪問者に特定の行動（購入、資料請求、会員登録、お問い合わせなど）を促すためのボタンやリンクのことです。


## JavaScriptとHTMLの関係性

![](images/2026-01-18-09-17-05.png)





## 親要素でFlexをかけたときに子要素の幅を指定することが可能


```css


.reason_card {
  display: flex; /* 画像とテキストを横並びにする */
  height: 8rem;
  align-items: center; /* 上下中央揃え */
  justify-content: flex-start; /* ★centerからflex-startに変更 */
  background: #fff; /* 背景を白くする */
  padding: 3rem 3rem 3rem 0rem; /* ★左側のパディングを少し増やして位置を調整 */
  width: 90%; /* カードの幅 */ ★ここで子要素の幅を指定する
  opacity: 0; /* JSで表示するまで隠す */
  transition: all 0.5s ease-out;
  border: 0.5rem solid orange;
  }

```



## javaScriptの基本(学習)

```javascript
`値を取得`
$(window)
$(this)

`メソッド`
fadeIn();  画面に表示

----------------------------------------
特定の位置までスクロールしたら要素をフェードイン
// スクロール位置が **520px** に達した際に、
// jQueryの `fadeIn` を使ってふわっと表示させる。
$(window).on("scroll", function () {
  if ($(this).scrollTop() > 520) {
    // #headerはロゴのハンバーガーの親要素
    $("#header").fadeIn();
  } else {
    $("#header").fadeOut();
  }
});

```

## Flex wrapや2つの列を構成する場合、以下のように作成すると良い。

```css
/* 外側（li）で幅を決める */
.gallery_item {
  width: 48%;
  margin-bottom: 6rem;
}

/* 画像でwidth・heightを指定 */
.gallery_img {
  width: 100%;        /* 親（li）いっぱい */
  height: 250px;      /* 高さ固定 */
  object-fit: cover;  /* 比率を保ちつつ、はみ出た分を切る */
}
```

## 文字を中央によせる。（ボックスを中央によせる。フォントサイズ自体をボックスにする）

```html
<!-- スクロールした段階でしたからタイトルが上にフェードインする -->
<section id="information">
  <h1 class="section_title">
    <p class="section_title_text">INFORMATION</p>
  </h1>
</section>
```

```css
.section_title {
  text-align: center;　★中央に寄せたいときはて、本体ではなくて親要素でする。
  margin-bottom: 5rem;
}

.section_title_text {
  display: inline-block;  ★インラインブロックが要素とwidthを一緒にする。
  position: relative;
  color: #fff;
  font-size: 6rem;
  letter-spacing: 0.25em;
  padding-bottom: 0.35em; /* 文字と線の間 */
}

.section_title_text::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%; /* 文字幅ピッタリ */
  height: 2px;
  background: #fff;
}

```



追加分★★★★★-----------------------

##  住所は<address>タグで囲む

##  共通のクラスを作成した際に一部だけ変更することができる。書き方は以下のようにする。

共通クラス
.section_title {
  text-align: center;
  margin-bottom: 5rem;
}

一部だけ変更したいクラス。このように親のクラス（大事！）をかくことによって、上書きできる
.access_content .section_title {
  margin-bottom: 1rem;
}


## どこを今作業しているか迷うことがあるので、その時には画面、「CSS・画面・HTML!」でリンクを辿ることにする。


## CSSにクラスを書くときは補完(サジェスト)を利用する。クラス名をコピーして、エンターを押して、上のクラス名にまたカーソルを戻す。




##  住所は<address>タグで囲む

##  共通のクラスを作成した際に一部だけ変更することができる。書き方は以下のようにする。

共通クラス
.section_title {
  text-align: center;
  margin-bottom: 5rem;
}

一部だけ変更したいクラス。このように親のクラス（大事！）をかくことによって、上書きできる
.access_content .section_title {
  margin-bottom: 1rem;
}


## どこを今作業しているか迷うことがあるので、その時には画面、「CSS・画面・HTML!」でリンクを辿ることにする。


## CSSにクラスを書くときは補完(サジェスト)を利用する。クラス名をコピーして、エンターを押して、上のクラス名にまたカーソルを戻す。

## モバイルにして、アニメーションなどで画面が広がってなおらない場合は、Windowsの横幅が、規定のサイズをこえて全体によこにそれたら、隠す処理をいれる

  html,
  body {
    overflow-x: hidden;
  }


## transition: width 0.5s ease　**CSSの`transition`プロパティ**について解説

![](images/2026-02-07-00-23-18.png)

[プレビュー](http://localhost:8080/preview-20260214-025304.html)

.mainvisual_img {
  width: 33%;
  height: 100vh;
  /* ↓ これがあると、JSの変更が「アニメーション」になります */
  /**
    transition: width 0.5s ease; 　★
## 何をしているか

JavaScriptで要素の`width`（横幅）を変更したとき、**瞬時に切り替わるのではなく、なめらかにアニメーションさせる**設定です。

## 仕組み

transition: width 0.5s ease;

この1行で：
- **`width`** → 横幅が変化したときに
- **`0.5s`** → 0.5秒かけて
- **`ease`** → 滑らかに（最初と最後がゆっくり）

アニメーションします。

## 具体例

// JSでwidthを変更
element.style.width = '50%';

- **transitionなし** → 33%から50%へ瞬時に変わる
- **transitionあり** → 33%から50%へ0.5秒かけてなめらかに広がる

つまり、**JSで値を変更するだけで自動的にアニメーション効果が付く**ようにするCSSの設定です。
*/




}

## javascriptスクロールをしても、文字が表示されない。

理由
```javascript
$(window).on("scroll load", function () {
  if ($(this).scrollTop() > 100) {
    $("#site_title .site_title_text").addClass("is-show");
  } else {
    $("#site_title .site_title_text").removeClass("is-show");
  }
});

```
scroll ・・・これだけの場合、画面の途中にいても、そこからスクロールした時しか表示されない。

load・・・これがあることによって、
一度チェックを行い、「あ、今すでにスクロール位置が100pxを超えてるな」と判断してタイトルを出してくれます。

この2つをセットで書くことで、**「いつ、どのタイミングでページを開いても、正しい表示状態にする」**ことができます。

[プレビュー](http://localhost:54321/preview-20260215-031026.html)

★スクロールとロードの違い
![](images/2026-02-06-16-54-07.png)


this・・・の中の this
window（ブラウザの画面全体）を指します。

on(イベント名)・・・「〜のとき（イベント発生時）に、この処理を実行せよ」という予約命令です。

`つまり、「画面がスクロールされたときに、その画面自身のスクロール量を取得する」という意味になります。`
（
◎発火タイミング: 画面を「スクロールした時」または「読み込みが完了した時」
◎実行条件: 画面全体（this）のスクロール量が 100px を超えているかどうか
◎処理内容: 条件を満たせばクラスを追加し、満たさなければ削除する）



## aタグに▢で囲むとき、paddingではなくてwidthで横幅を指定する方法

```css
  .contact_msg {
    display: block;(いままでinline-blockだった。)

    width: 100%;
    padding: 4rem 0;
```

ディスプレイをブロックして
widthを１００％にすることによって、画面一杯まで広がる

なぜサイズが一致するのか
`<a> や <span> は「インライン要素」であり、中身の文字数分の幅しか持ちませんが、block に変えることで「一つの大きな箱（ブロック）」になります。`





---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔴 z-index 問題（統合版）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 よくある症状
★要約

親にpoisiton:fixedなどのパララックスをつけたら、親も子も
z-indexをつける。これは必ず対にする！

![](images/2026-02-06-16-50-44.png)


- ハンバーガーメニューがクリックできない
- 要素が他の要素の下に隠れる
- 検証ツールでは押せるのに実画面では押せない
- モーダルやオーバーレイが最前面に来ない

---

## 🔍 原因パターン

### パターン1：親にz-indexがない
```css
/* ❌ ダメな例 */
#header {
  position: fixed;
  /* z-index なし → レイヤー比較に不参加 */
}
.hamburger {
  z-index: 9999; /* 子だけ指定しても意味なし */
}
```

**重要ルール：**
- `position: fixed` の要素は **z-indexを持たないとレイヤー比較に参加しない**（★つまり対で意味がある！！必ず対にする！）
- 子要素に `z-index: 9999` があっても、**親が参加してないと負ける**
---





### パターン2：fixedの親子関係

★基本は親がfixedでその子要素で親要素のなかに
配置するのが基本だから（headerとハンバーガーメニューのように）　
➡　親position : fixedで子はabsoluteにする。

```css
/* ❌ 問題が起きるケース */
/* 親要素：幅 300px、子要素：width 100% + position: fixed */
/* → 子はビューポート基準になり、親の幅が無視される */

.parent {
  width: 300px;
  position: fixed;
}
.child {
  width: 100%;
  position: fixed; /* ← これが原因 */
}
/* 理由：fixedは親要素ではなくビューポート（ブラウザ画面全体）を基準にするため、親要素の幅設定が効かなくなります */
``

**解決策：**
```css
.parent {
  position: fixed;
  width: 300px;
}

.child {
  position: absolute; /* fixed → absolute に変更 */
  width: 100%;        /* これで親の幅が効く */
}
```
  * position: absolute への変更と役割について:
  * 1. 違い： `fixed` は画面全体が基準になるため親の幅を無視しますが、 `absolute` は親を基準にするため親の幅（300px）を守れます。
  * 2. 重要性： 親の箱の中に収めつつ、自由な位置に配置したいなら `absolute` 指定が必須です。

---
### パターン3：位置が画面外
```css
/* ❌ 画面外にあってクリックできない */
.hamburger {
  position: fixed;
  top: -100px; /* 画面の上に隠れてる */
  z-index: 9999;
}
```

→ DevToolsで位置を確認する

---

## ✅ 正しい修正方法

### 1. 親にz-indexを追加
```css
#header {
  position: fixed;
  z-index: 9000; /* ← これで前面に出る */
}
.hamburger {
  z-index: 100; /* 親よりは小さくてOK */
}
```

---

### 2. z-index値の目安
```css
/* 推奨値（プロジェクト内で統一する） */
.main-content {
  z-index: 1;      /* 通常コンテンツ */
}
.fixed-header {
  z-index: 100;    /* 固定ヘッダー */
}
.overlay {
  z-index: 800;    /* オーバーレイ（黒マスク） */
}
.modal {
  z-index: 900;    /* モーダル */
}
.hamburger-menu {
  z-index: 1000;   /* ハンバーガーメニュー */
}
```

### 3. pointer-eventsも併用（推奨）
z-index で重なり順を決めても、「透明なのにクリックを邪魔して下のボタンが押せない」 
というトラブルを防ぐために、この none と auto の切り替えは必須のテクニックです。`とくにオーバレイで使用`

![](images/2026-01-26-07-31-22.png)

```css
.hamburger {
  position: fixed;
  z-index: 1000;
  pointer-events: auto; /* クリック可能にする（その要素を 「マウスや指で触れる状態（通常の状態）」 に戻す設定です。） */
}
背景を黒くする（普段は隠す）
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明の黒 */
  z-index: 800; /* メニュー(1000)より低く、コンテンツ(1)より高く */

  /* 通常時は透明で、かつクリックをすり抜けさせる */
  opacity: 0;
  pointer-events: none; 
  transition: opacity 0.3s;
}

.overlay.open {
  /* メニューが開いたとき：表示してクリックもガードする */
  opacity: 1;
  pointer-events: auto; 
}
```

→ z-indexだけでも回避できるけど、**pointer-events併用が一番安全**

---

## 🔧 デバッグ手順

### 1. DevToolsで確認
1. 要素を右クリック → 検証
2. Computed タブ → z-index の値を確認
3. 親要素も同様に確認

### 2. チェックリスト
- [ ] 親要素に `position` と `z-index` があるか？
- [ ] 子要素の `position` は `absolute` か？（fixedじゃないか）
- [ ] 要素が画面外にないか？
- [ ] 他の要素の `z-index` が大きすぎないか？

---

## 📝 覚えておくこと

1. **`position: fixed` + `z-index` でレイヤーになる**
2. **親に z-index がないと子も道連れで負ける**
3. **検証ツールで押せるのに実画面で押せない → z-index か位置を疑う**
4. **迷ったら z-index: 300 以上をうたがう**
5. **fixedの親子関係では、子は `absolute` にする**

---
トの使い方」セクション


## javaScript バブルソート法

```javascript
function sortArrayAsc(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - 1 - i; j++) {
      // もし左の数値と右の数値が左の数値が大きい場合、入れ替えを行う
      if (arr[j] > arr[j + 1]) {
        let saveBox = arr[j];
        // 入れ替え。大きいデータを右に移動
        arr[j] = arr[j + 1];
        arr[j + 1] = saveBox;
      }
    }
  }
  return arr;
}
```
【プロンプト】
これが理解できないから、SVGでイメージを作成してもらえる？iとかjのながれがわからない

![](images/2026-01-26-20-58-53.png)





## 実務（コーディング）着手前の準備・手順


### 1. 【現状分析】デザインカンプの把握
*   **共通項の抽出**: 全体のデザインを俯瞰し、共通サイズ・整列ルール（Grid）・共通パーツを洗い出す。
（## 共通化する部品はは、部品なので、マージンとかボトムとかできるだけつけないようにする。）

*   〇**ギミック確認**: アニメーションやホバー時の挙動を事前にすべてチェックする。　特に以下のサンプルをみて、z-indexをきめておく

*   **アナログ出力**: 可能であれば印刷。`section事に開始時に構成をたてる。しかも言葉にしておくことでかってにAIがロジックを作成してくれる`手書きで「構造」や「気づき」を書き込むことで理解を深める。⇀`チェックも大事　ベストプラクティス`


### 2. 【タスク管理】仕様のチェックリスト化
〇（仕様書がある場合）`sankou` フォルダに資料を集約し、AI（Claude Code 等）に読み込ませる準備を行う。

*   [ ] **URL情報**: デモサイト、参考URL（デザイン）
*   [ ] [ ] **ビジュアル資料**: 全体スクリーンショット、
*   [ ] **機能要件**: 実装すべき仕様の一覧


### 3. 【AI・効率化】ツールの活用
スクリーンショットを Gemini 等の AI に投げて初期解析・雛形作成を依頼する。
*   **解析範囲**: 「全体図」で全体像を、「細部図」で複雑な箇所の構造を理解させる。
*   **指示出し**: 特徴的な箇所だけメモ（.txt で可）にまとめ、AI に添付。指示と同時に AI に作業進捗を管理（チェック）させる。





### 5. 【設計ルール】レイアウト設計
*   **柔軟な配置**: 同一画面内の要素幅は原則 `%` を使用し、柔軟に並ぶように設計する。
*   **クラスの分離**: 全体の半分（50%）などの基本割合は共通クラスとし、特殊な箇所は個別クラスで上書きして管理する。

*   **クラスの分離**: 共通の変数は、ルートにかきこんでおく。
・コンテンツ幅が指定されている場合は以下のようにかく（デザインの基本として、**「背景（色や画像）」は画面いっぱいの全幅（100%）に広げ、「実際の中身（テキストやカードなど）」はコンテンツ幅（86rem）**に収めて中央に配置します。）

```css
:root {
  /* ▼ ここで「var(--sidebar-width)」を一括管理！ */
  --sidebar-width: 15rem;
}
.aa{
  left: var(--sidebar-width);
}

/* 例：各セクションの共通設定（必要に応じて追加） */
.voice_bg, 
.overview_bg, 
.cta_bg, 
.footer_link_container {
  max-width: 86rem; /* これが「コンテンツ幅 860px」 */
  margin-left: auto;
  margin-right: auto;
}
```

```html
<div class="menu-wrap">
    右
    <div class="menu-col menu-left">　★★ここがポント共通項目とそれ以外をわける
      <div class="menu-section">
        <h3>Coffee</h3>>
      </div>
    </div>
    左
    <div class="menu-col menu-right">

```

![](images/2026-01-13-19-30-37.png)

`【ループ】`




★セクション単位でAIにチェックをしてもらう。
あと、３７５REMにして明らかにおかしいところを
修正する
・センターになっていないとか

★まず、PCを完璧に仕上げる。位置とかいい。⇀後戻りがかなり増えるので！！
▢アニメ―ションが正しく動作しているのか。開始位置は問題ないか。



![](images/2026-01-26-21-39-42.png)




`【コメント】`
・flex なども含めて、サジェストしてくれるのでコメントは詳しく書く
（すべてを書く必要はない。relative と flex はかく）
・  /* ┌─────────────────────────────────────────┐
   │ セクション　 BBBが選ばれる理由　　 背景赤で左右からスライドイン
   └─────────────────────────────────────────┘ */

セクションのコメント直感的にイメージできるぐらい記載する。

`【セマンティック】`

基本的にリスト、複数ならぶものは以下でまとめる
```html
<ul>
  <li>
    <img>
  </li>
    <img>
```

`備考`
・HTML Validato
https://validator.w3.org/nu/#textarea　

・CSS Validator（W3C）
https://jigsaw.w3.org/css-validator/ 

・JSHint
https://jshint.com/ 


`★10分でよいので画面のセクションを`
`自分でイメージできるように暗記する。　かなりスピードに関係する`


`★画像を一つ一つサイズをそろえるより、％で合わせる、サイドのパディングなどが`
`正しければほぼデザインカンプ通りに数値になる`

※専門用語を覚える
・固定サイドメニュー
・逆台形
・グラデーション
・疑似要素（ただの飾り (要素としての意味のないものに使用する。アイコン、下線、枠、吹き出しの三角)
・パララックス（Webデザインにおいて、手前の要素（テキスト等）と奥の要素（背景画像）が異なる速度で動くことを利用して、画面に「奥行き」や「立体感」）
・無限スライダー



【最終チェックリスト】
▢　AIチェック
▢　github,ビジュアライザー,sankouフォルダは削除されているか。
▢　各チェックサイトは通っているか
▢　javaScriptで指定する場合だけ、idをつかう。







## 【前提】ヘッダーを固定して、その中でロゴとメニューを左右に並べたい」という場合、以下のルールになります。（つまりfixedとフレックスボックスを併用する際にきをつけること）

1. (fixedではないflexBox)親ボックスの中に、❌子fixedは置かない⇀　子のfixedが優先されて、意味がなくなるため。
2. しかし、`親が（fixed且つ、flexBox）だったら、子はそれに引きずられてfixedと同じ効果になって ⭕子fixedはよい`。

イメージ図

× ダメなパターン
親（Flex）：「整列して！」
子（Fixed）：「無視！俺は画面の端っこに張り付くぜ！」（親の箱から飛び出す）

〇 正解のパターン
親（Fixed兼Flex）：「俺が画面に張り付く！ 子要素たちはそのまま俺の中で並べ！」
子供たち：「はい！（親の箱の中で、指示通り横に並びつつ固定される

（親fix/flex）で子は、(abosoluteは可能⇀一応子も固定される)

![](images/2026-01-26-23-59-26.png)


## videoなど画像を使う際は、 比率を保ってトリミングするために、heightとwidthを指定した上で、object-fit: cover;を利用する

そうしないと、画像のアスペクト比とずれていた場合でも、伸び縮みすることなく綺麗にうつる。

➡でもよくわかってないからSVGにして
だって、サイズ指定していたら、アスペクト比がずれていたら、枠のなかにはいらなくて、一部画面からきれたりしない？つまり一部の画像がきれて、全ての像がもれなく綺麗におさまるってことにならなくない？

➡おっしゃる通りです！「全ての像がもれなく収まる」わけではなく、**「枠（箱）からはみ出た部分は切り捨てられる（トリミングされる）」**のが object-fit: cover の仕組みです。


## パディングとマージンの違い
1  ボックス自体のサイズはかわらない
2. margin で確保した部分は「ボックスの外側」になる
3. その「外側」の部分は .feature_item の背景色（白）が塗られない 
4. 結果、親要素（.feature_area や body）の背景色が見える ❌


## 構文　プロパティ　ロジック
`display: none`
・  display: none; /* 初期状態では非表示 */
➡  display: block; /*表示 */

`pointer-events`
・　pointer-events:none: 要素を「すり抜け」させます。透明なオーバーレイなどが背後にあるボタンなどのクリックを邪魔しないようにするために使います。

➡pointer-events:auto:　通常の状態に戻します。メニューが開いた時など、再びクリックに反応させたい場合に使います。


【具体的な問題】
特に、「見た目は透明（opacity: 0）だけど、実際には画面を覆っていて裏側の要素が押せない」といったトラブルを解決するために不可欠な設定です。

例）1. ハンバーガーメニューの背景マスク（オーバーレイ）
状況: メニューが開いた時に画面を暗くする div 要素（.overlay や .mask）が、画面全体を覆うように配置されている。
問題: メニューを閉じた際、opacity: 0（透明）にしただけだと、「透明な巨大な壁」が画面の一番手前に居座り続けます。 その結果、背後にあるはずのサイトのボタンやリンクが一切クリックできなくなります。
解決: 非表示時に pointer-events: none を指定することで、クリック操作を下の要素へ「突き抜け」させます。



## grid（flexも同様）でレイアウトすると、３列などサイズがきまっている。その場合、画像で固定サイズ指定する（固い箱のようなもの,rem通りにうまく動作しない）と、３列の幅いにあわずくずれることがある。そのため画像は％で指定するとよい。％なら、問題なく動作する。

`画像は％で指定するとよい（width: 100%）。 その際、高さは必ず height: auto にする。`（そうしないと画像がビヨーンと縦に伸びて変形してしまうから）

質者・画像サイズがデザインカンプととこなる。

例）

```css
/* レスポンシブ対応の画像基本セット（Grid/Flex共通） */
.feature_image {
  width: 100%;       /* 親要素（Grid/Flexの枠）の幅に合わせる */
  height: auto;      /* 幅に合わせて高さも自動調整（比率維持） */

  aspect-ratio: 3 / 2;   /* 【重要】横3:縦2 の比率で枠を確保する */

  object-fit: cover; /* 枠からはみ出る分はトリミングして埋める */
  display: block;    /* 画像下の謎の余白を消すおまじない */
}
```

![](images/2026-01-29-10-12-48.png)


## 可変REMをつかうなら

可変rem使用時	　　　　　　 % or 100% が安全 ✅
固定rem（1rem=10px固定）	rem固定でもOK
見本のCSS	max-width:      100% + %指定




## スライダーについて

★javaScriptの「slidesToShow: 3」とする。常に３つの画像が画面に表示される。そこでimgの幅を１００％で自動的に均等に割り振られることになる。
画像を均等に中央に配置されることになる。


```css


.slider {
 width: 100%;
}

.slider img {
  width: 100%;
  height: 24rem;
  padding: 0 1rem; /* 左右に余白を追加 */
  box-sizing: border-box; /* paddingを幅に含める */
}
```

```javascript
$(function () {
  $(".slider").slick({
    arrows: false,
    autoplay: true,
    adaptiveHeight: true,
    centerMode: true,
    centerPadding: "0.3rem",
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          centerMode: true,
          centerPadding: "5rem",
        },
      },
    ],
  });
});
```

javascriptの「centerPadding」と、CSSの「パディングの違い」

・両社の違い
centerPadding・・・中央を強調	  隣をチラ見せ（0.3remだけ画像をよこから見せる）
![](images/2026-01-29-20-47-00.png)  この画像のようにサイズをあげることによって、画像が小さくなり、横のチラ見できる量が増える

padding	・・・画像に隙間	  均等な隙間
つまり二つ組み合わせる。　基本二つのサイズが一緒になることが多いような気がする。


![](images/2026-01-29-14-06-43.png)


★タブレットにするとずれる。メディアクエリが`767px`
`494`でづれいている。


▢うっかりミス

もしもずれていると, ある特定の位置になると, 画面のサイズ位置がおかしくなる.だから特定の位置だけ, サイズに違和感を感じたら, スタイルCSSと合っているかを確認する. style.cssのサイズとメディアクエリのサイズが異なっていた。


## 実際の画面を模写する場合。
・検証ツールで、cssフォルダのutilityなどのフォルダから
⇀メディアクエリ
⇀コンテンツ幅
⇀セクションの余白
⇀共通の項目
⇀印刷してflexや、abosoluteの構造「勉強中」

などを特定する

・検証ツールで、「要素タブ」を指定し、フレックスを利用しているところを調べる。
・定数をソースのCSSから取得してきて、どこで利用しているかざっくりしらべる。
大体セクション間や、ヘッダーとか。その程度でよし。


## fixed absolute で縦と横をやるときは、  transform: translate(-50%, -50%);　ひとつでまとめないといけない。
★つまり正しく動作しない場合は、同じプロパティがないかチェックする

## <span>は「文の中の一部分だけ色を変えたい」みたいな時に使うものだよ。

## <section class="about_area container_section">
基本のサイズ幅を設定していく　container_section⇀ここにはマージン等を設定。



##  Flex 2階層(階段式)で下揃えするテクニック。かつ、左右の高さをかえる。

Flexで、二段階でflex横並びにしてflex-endをすると両要素が下揃えになる。しかし片側の子要素をheightが100%場合、実際下揃えにならない。「上に子要素が吸い付く。
その場合は孫要素にmargin-top: autoをつけることによって解決する。

【吸い付く理由】子要素の縦フレックスでflex-startがデフォルトになるため、上に配置される
（`justify-content: flex-start` がデフォルト）

【なぜ１００％にするか】親要素の高さ一杯にをあわせるため。`子要素はflexではデフォルト要素分しか高さがない`　height: 100% を指定することで親要素の高さ一杯にひろがる。

![](images/2026-02-03-06-20-30.png)

![](images/2026-02-02-20-44-17.png) 

![](images/2026-02-02-20-40-39.png)

📝 簡潔メモ
🎯 今回の学び：2階層レイアウト
階層構造


親 (.about_area) 
├─ 左子 (.left_container)
│  ├─ メッセージ
│  └─ 猫
└─ 右子 (.right_container)
   ├─ 店内画像
   └─ 説明文
コード

```css
/* 親: 左右を下揃え */
.about_area {
  display: flex;
  align-items: flex-end; /* 左右コンテナを下揃え */
  min-height:60rem 　✖これだと左を１００%にしたとき、基準がないためひろげられない。　height:60rem など固定にする
}

/* 子: 高さ確保 */
.left_container {
  height: 100%;          /* 親の高さいっぱい */
  display: flex;
  flex-direction: column;　★この設定だと左側だけ上に要素があつまる。
}

/* 孫: 下に押す */
.left_cat_img {
  margin-top: auto;      /* 上の余白を最大に */
}
```



## 📌 flexbox子要素を親の高さ100%にする方法 CSS
例）同じボックス内に段差などある場合
![](images/2026-02-13-18-30-18.png)

【結論】
- 親に具体的な高さ（`height`）が必要
- `min-height` だけでは子の `height: 100%` が効かない
- `align-self: stretch` で親の `align-items` を個別に上書き可能
（
設定	　　　　　　　意味	　　　　高さの決まり方
min-height: 60rem	最低60rem確保	内容次第で変動
height: 　　60rem	　必ず60rem	　固定値
➡ `子の height: 100% は 固定値が必要`

➡ min-height は「可変」なので基準にできない）

【具体例】
```css
/* ❌ 効かない */
.about_area {
  display: flex;
  align-items: flex-end;
  min-height: 60rem; /* ← これだけだと子がheight: 100%にならない */
}

.left_container {
  height: 100%; /* 効かない */
}
```

```css
/* ✅ 効く */
.about_area {
  display: flex;
  align-items: flex-end;
  height: 60rem; /* ← 具体的な高さを指定 */
}

.left_container {
  align-self: stretch; /* align-items: flex-endを上書き */
  height: 100%; /* これで親の高さいっぱいに伸びる */
}
```

【補足】
- `min-height` は最小高さの指定で、内容に応じて伸びる
- 子要素の `height: 100%` は親の確定した高さを参照
- `align-self` で個別の子要素だけ配置を変更可能


## アニメーションの付け方　後ろに吸い込まれるような

`親要素、

```css
/* └ 左がメッセージと猫画像列 【縦flex】 */
.left_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  overflow: hidden;　★これをつけることによって、最初画像が大きくなりすぎない`
}

/* 左下の猫 */
.left_cat_img {
  margin-top: auto;
}
/* 左下の猫 */
.left_cat_img.animate {
  /* forwardsは一回だけinfiniteだと何度も繰り返す */
  animation: slideshow 3s forwards; /*★これで３秒のスライドショーが粉われる　★forwardsは一回限り */
  width: 100%;
  height: auto;
}


★ここで時間ごとの表示の設定　３秒でどう動かくか。
@keyframes slideshow {
  0% {
    opacity: 1;
    transform: scale(1.1); /* 最初は少し大きく */
  }
  5% {
    opacity: 1;
  }
  25% {
    opacity: 1;
    transform: scale(1.05); /* 少し縮小 */
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
```

```javascript

window.addEventListener("scroll", function () {
  // スクロールがstore_img要素に到達したか確認

  // store_img要素を取得
  const storeImg = document.querySelector(".store_img");
  const manekiNekoImg = document.querySelector(".left_cat_img");

  // 要素の位置を取得(Bounding・・・境界　RectはRectangle・・・座標・大きさ)
  const rect = storeImg.getBoundingClientRect();
  // 要素の位置を取得(招き猫)
  const rectManekiNeko = manekiNekoImg.getBoundingClientRect();

  // ウィンドウ（表示領域）の高さを取得
  const windowHeight = window.innerHeight;

  // 要素の上端がウィンドウの下端に到達したか確認
  if (rect.top <= windowHeight) {
    // アニメーションを開始
    storeImg.classList.add("animate");
  }

  // 要素の上端がウィンドウの下端に到達したか確認(招き猫)
  if (rectManekiNeko.top <= windowHeight) {
    // アニメーションを開始
    manekiNekoImg.classList.add("animate"); ★ここでクラスをつける
  }
});

```


## 要素の中の文字の高さを調整する

```css
  line-height: 2rem;
```


## 検証ツールの味方
・オレンジ・・・・マージン


## なぜなにもないところでパディングをするか。親にパディングをすることで全体にかかるので一元管理できるのと、グリッドやカード系のレイアウトでは親にパディングするのはほぼ定番パターンです。


・ひとつにパディングをする→かける場所はセクション全体
![](images/2026-02-03-14-01-12.png)



## 画像がない場合は、WEBをひらいて、「新しいtabで画像を開く」でやるとURLでわかる。「https://omodakaya.jp/wp/wp-content/uploads/2026/02/%E3%81%82_%E8%83%8C%E6%99%AF%E3%81%AA%E3%81%97.png」このように　wp-contentなどあればワードプレスの画像


## 縦線を書きたい時、かつボックスのサイズなどとちがってボーダーライトでかけないとき。疑似要素で表示する　aaaa::after 

```css
.weekly_product::after {
  content: "";
  position: absolute;
  right: 0;
  top: 50%; ★　開始位置をずらすことによって中央によせる
  transform: translateY(-50%);
  height: 80%;
  width: 0.1rem;
  background-color: rgb(231, 225, 225);
}
```

## 幅がひろいwidthを文字は文字幅にあわせる
width: fit-content;

![](images/2026-02-06-03-14-54.png)

## display:inline_flexと　display:blockの違い。
・display:blockにすると改行がはいってしまい。
下に並ぶ

・inline-flexをすると横にならぶ
# 具体例

## display: block の場合
<div style="display:block">ボタン1</div>
<div style="display:block">ボタン2</div>
<div style="display:block">ボタン3</div>
**結果：**
ボタン1
ボタン2
ボタン3
縦に並ぶ

---

## display: inline-flex の場合
<div style="display:inline-flex; gap:10px">
  <div>ボタン1</div>
  <div>ボタン2</div>
  <div>ボタン3</div>
</div>
**結果：**
ボタン1  ボタン2  ボタン3
横に並び、gap で間隔調整可能



・さらにflexの役割もあるのでgapなで並べるとよい。
![](images/2026-02-04-13-39-55.png)




##　flexboxとabsoluteの使い分け
・親に overflow: hidden あり	flexbox ✅
（要素を飛び出す場合があるから、flexboxなら飛び出してよい）
・要素を自由に重ねたい	absolute ✅
モーダル・ツールチップ	absolute ✅

![](images/2026-02-04-14-00-48.png)

★　absolute/fixed:** 親要素からはみ出した部分が`切り取られて見えなくなります`
`
- **flexbox:** 通常のレイアウトなので、はみ出した部分も表示されます（意図通りに配置可能）

**具体例：**
.parent {
  overflow: hidden;
  position: relative;
}

.child-absolute {
  position: absolute;
  top: -50px; /* 親の外に出る → 見えない ❌ */
}




## このCSSコードは、**Flexboxコンテナの子要素を縦方向（交差軸方向）に引き伸ばして、コンテナの高さいっぱいに広げる**設定です。

align-items: stretch;

.container {
  display: flex;
  height: 200px;
  align-items: stretch; /* 子要素が200pxの高さになる */
}

![](images/2026-02-04-22-00-25.png)




## 要素のなかの矢印などを縦中央、横中央にもってくる　子要素がなくても大丈夫。
<!-- インラインが子要素となる。 -->

![](images/2026-02-06-03-03-03.png)

```html
<div class="news_link_container">
  <a href="#" class="news_link_msg">もっと見る</a>
  <a href="#" class="news_link">→</a>
</div>
```

```css
.news_link {
  display: block;
  height: 1.5rem;
  width: 3.5rem;

  color: white;
  background-color: rgb(60, 40, 189);
  border-radius: 2rem;

  ★以下の３行★   子要素「⇀」の位置を変える。
  display: flex;
  align-items: center;
  justify-content: center;
}
```
![SVG](./その他/SVG一覧/svg_20260207_124711.svg)
![](images/2026-02-07-12-47-27.png)

![SVG](./その他/SVG一覧/svg_20260207_124210.svg)



## フレックスの子要素は画像などのもとサイズより小さくならない。例えば画像など大きいサイズをうめるときに、想定した配置にならないときは、
.a{
display flex
}

.b{
flex:2;
min-width: 0;　をつける
}

以下。「地図画像」が画面の幅よりおおきいとき！
![](images/2026-02-06-02-59-04.png)



## インライン要素をインライン要素やテーブルセルの垂直方向の配置を指定するCSSプロパティ

 <a href="#" class="google_link">Google Maps<img class="icon_newtab" src="img/icon_newtab.svg" alt="" /></a>

```css
.icon_newtab {
  display: inline-block;
  vertical-align: -0.2rem; ★　これでインライン要素の「縦」位置をかえれる
  margin-left: 0.5rem;
  width: 1.2rem;
  height: 1.2rem;
}
```


## 特定のセクションの下に同じ位置に配置したい場合は、新たにセクションの下にdivをつけることも考える。
    <section>
    </section>

    <!-- ２段目【flex 2列: 店舗情報の枠確有り/枠のみ　アクセス情報のみ】 -->
    <div class="access_container">

![](images/2026-02-06-02-56-45.png)


## フレックスの片方の幅が固定で、残りを幅をすべて等び省略した場合は以下のようにする。
widthとflexを利用する。

.access_by {
  width: 15rem;
  font-size: 1.4rem;
  margin-bottom: 3rem;
}

.access_by_detail {
  flex: 1;
  font-size: 1.4rem;
  margin-bottom: 3rem;
}


📋 今回の学び
❌ 間違い（列ごとにまとめる）

![](images/2026-02-06-11-33-26.png)

<div class="container">
  <div class="labels">        <!-- ラベル列 -->
    <p>電車でお越しの方</p>
    <p>車でお越しの方</p>
    <p>駐車場のご案内</p>
  </div>
  <div class="details">       <!-- 詳細列 -->
    <p>徒歩10分</p>
    <p>名古屋ICから30分<br>赤津ICから5分</p>  ← 2行で高さズレる
    <p>STUDIO 894...</p>
  </div>
</div>
➡ 2行目の高さが変わると3行目がズレる

## （行ごとにペアにする）

<div class="container">
  <div class="row">
    <p class="label">電車でお越しの方</p>
    <p class="detail">徒歩10分</p>
  </div>
  <div class="row">
    <p class="label">車でお越しの方</p>
    <p class="detail">名古屋ICから30分<br>赤津ICから5分</p>
  </div>
  <div class="row">
    <p class="label">駐車場のご案内</p>
    <p class="detail">STUDIO 894...</p>
  </div>
</div>

.container { display: flex; flex-direction: column; }
.row       { display: flex; align-items: flex-start; }
.label     { width: 15rem; }    /* 固定幅 */
.detail    { flex: 1; }         /* 残り全部 */
💡 ポイント3つ
#	内容
1	ラベルと詳細は同じ行（row）にペアで入れる
2	ラベルは width: 固定値 で揃える
3	詳細は flex: 1 で残りスペースを自動で使う」

[プレビュー](http://localhost:54321/preview-20260215-041759.html)


## 横スクロールアニメーション（無限ループ）


---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔖 覚えておくと便利なCSSプロパティ集
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```css
/* クリック制御 */
pointer-events: none;        /* クリックを無効化（すり抜け） */
pointer-events: auto;        /* クリックを有効化（通常状態） */

/* 選択制御 */
user-select: none;           /* テキスト選択を禁止 */
-webkit-user-select: none;   /* Safari対応 */

/* スクロール制御 */
overscroll-behavior: contain;  /* スクロール連鎖を防ぐ */
scroll-behavior: smooth;       /* スムーズスクロール */
scroll-snap-type: x mandatory; /* スナップスクロール（横） */
scroll-snap-align: start;      /* スナップ位置 */

/* テキスト */
text-overflow: ellipsis;     /* はみ出したテキストを...に */
white-space: nowrap;         /* テキストを改行させない */
word-break: break-all;       /* 単語の途中でも改行 */
line-clamp: 3;               /* 3行で切り捨て */
-webkit-line-clamp: 3;       /* Safari対応 */

/* 表示/非表示 */
visibility: hidden;          /* 非表示だが場所は確保 */
opacity: 0;                  /* 透明だが場所は確保 */
display: none;               /* 完全に非表示 */

/* 位置調整 */
object-fit: cover;           /* 画像をトリミングして埋める */
object-fit: contain;         /* 画像をそのまま収める */
object-position: center;     /* 画像の基準位置 */

/* レイアウト */
aspect-ratio: 16 / 9;        /* アスペクト比を固定 */
place-items: center;         /* Grid/Flexで中央配置 */
gap: 2rem;                   /* Grid/Flexの隙間 */
isolation: isolate;          /* 新しいスタッキングコンテキスト作成 */

/* 境界 */
box-sizing: border-box;      /* パディング込みでサイズ計算 */
outline: none;               /* フォーカス枠を消す */
resize: none;                /* textareaのリサイズ禁止 */

/* 背景 */
background-size: cover;      /* 背景画像を隙間なく埋める */
background-position: center; /* 背景画像の位置 */
background-attachment: fixed; /* 背景を固定（パララックス） */
backdrop-filter: blur(10px); /* 背景をぼかす */

/* アニメーション */
will-change: transform;      /* GPUアクセラレーション有効化 */
transform: translateZ(0);    /* 3D変換を強制してGPU使用 */
backface-visibility: hidden; /* 裏面を非表示（ちらつき防止） */

/* その他 */
cursor: pointer;             /* マウスカーソルを指に */
cursor: not-allowed;         /* 禁止マーク */
appearance: none;            /* デフォルトスタイルを無効化 */
-webkit-appearance: none;    /* Safari対応 */
mix-blend-mode: multiply;    /* ブレンドモード */
filter: grayscale(100%);     /* グレースケール */
clip-path: circle(50%);      /* 円形に切り抜き */
writing-mode: vertical-rl;   /* 縦書き */

/* Flexbox高度 */
flex-shrink: 0;              /* 縮小を禁止 */
flex-grow: 1;                /* 伸縮を許可 */
flex-basis: 0;               /* 初期サイズを0に */
order: -1;                   /* 並び順を変更 */

/* Grid高度 */
grid-auto-flow: dense;       /* 隙間を詰める */
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* レスポンシブグリッド */

/* モバイル対応 */
-webkit-overflow-scrolling: touch;  /* iOSの慣性スクロール */
-webkit-tap-highlight-color: transparent; /* タップ時のハイライト消去 */
touch-action: pan-y;         /* 縦スクロールのみ許可 */

/* パフォーマンス */
contain: layout style paint; /* レンダリング最適化 */
content-visibility: auto;    /* 見えない部分の描画をスキップ */
```


## AIへのコメントの指示：CSSにコメントを書いてもらうとき

ここ、ソースみてHTMLも、直感的にわかりやすいコメントつけたして

小カテゴリを以下のように記載するのもてです。　自由にきめてください。
/* ═══════════════════════════════════════════════════════════════════════
   【親】右サイド固定ヘッダー全体（<header id="side_area">）
   画面右端に固定される白い縦長エリア
   ═══════════════════════════════════════════════════════════════════════ */

## 隣接要素
/* ハンバーガーメニューがオープンしたら背景が白の目次のページを表示する。 */
.hamburger_menu.open + .side_nav_overlay {
  display: block;
}



CSSでは**隣接兄弟セレクタ（`+`）** を使うこと���、特定の要素の**直後にある兄弟要素**のスタイルを変更できます。

このコードの場合：
- `.hamburger_menu.open` の状態が変わると
- その**直後の兄弟要素** `.side_nav_overlay` のスタイルが変わる

ただし、CSSで操作できるのは：
- ✅ 隣接する兄弟要素（`+`）
- ✅ 後続の兄弟要素（`~`）
- ✅ 子孫要素（` `や`>`）

逆に操作できないのは：
- ❌ 親要素
- ❌ 前の兄弟要素

つまり、**CSS単体では「後方・下方向」の要素しか操作できません**。
*/


## 3000万円控除　不動産

不動産	" 最終的に手元に残る金額に対する控除。利益、不動産屋に対する手数料とか、更地も含むのかな？そういった手数料を抜いて、3000万円利益が残った場合、控除がタダになるってこと。 

原則は、家が建っていない「更地」では控除は使えない 。

しかし、以下の三つをみたしていればうれる
・家を取り壊した日から1年以内に、土地の売買契約を結ぶこと 。

・（お母様が）家に住まなくなった日から3年目の年末までに売ること 。

・家を壊してから売買契約の日まで、その土地を駐車場などで貸していないこと（事業に使っていないこと） 。"


## 軽減税率の特例	不動産	

"◉売った家の所有期間が10年を超えている場合 、上記の3,000万円控除を使った後、残った利益（6,000万円以下の部分）にかかる税率が通常より安くなります 。

まず、利益から**「3,000万円特別控除」**を使います 。
そして、控除した後の**「残りの利益」（6,000万円以下の部分）に対して、「軽減税率」**が適用されます 。
その税率は、資料によると10%（ほかに住民税4%）です 。

例）

 4,900万で売れました。更地にするとか不動産手数料がかかり、かかった上で実際入った利益に対しての税に対して3000万円控除が適用されますってことでしょ。さらに3000万円以上の利益にたいしても１０年すんでれば、それを超えるものに対しては軽減税率が適用されるかもしれないってこと？　だから更地、手数料はもちろんかかる



"
## 相続税	不動産

"相続税 → 3,000万＋600万×人数（3人なら4,800万）までは税金なし

家を売るときの3,000万控除 → 売った利益用の別ルール

❗ この2つは「足し算」ではなく、まったく別の税金の仕組み"

## 相続するとき注意したいこと。 不動産 	

相続	もしも自分が相続したら、その年の年末調整の収入が大幅に増えるため、税金が増加する。税金が増加するため、母親名義で売った方がいい。そして、母親名義で売るということは、自宅にいる人が家を売るということであり、3000万円控除も利用できるという理由から、2つの理由から母親が相続人になった方がいい
/* ✨
# 結論：**間違いが多く含まれています**


/* ✨
# 不動産相続の正しい知識

## 基本の誤解を解消
- **相続しても給与所得は増え���い**。相続税と所得税は別物
- 相続財産は年末調整とは無関係

## 居住用不動産の3000万円控除
- **実際に住んでいた人**だけが利用可能
- 母親が住んでいるなら、母親が売却すれば控除を受けられる

## 誰が相続すべきか
- **配偶者控除**（1.6億円まで非課税）は有利だが、母親が亡くなる時の**二次相続**で子供の税負担が重くなる可能性あり
- 一次相続で子も一部相続する方が、トータルの税負担が少ない場合も多い

## 結論
**家族構成・財産額・居住状況で最適解は異なる。必ず税理士に相談を**
*/







## flex-shrink: 0;の説明  html

## 意味
**要素を縮小させない**という指定です。

## 使��道
- Flexboxレイアウトで、親要素の幅が足りなくなった時の動作を制御
- デフォルトは `flex-shrink: 1`（縮小する）
- `0` にすると、**どんなに狭くなっても元のサイズを保つ**

## 具体例
.item {
  flex-shrink: 0;  /* この要素は縮まない */
  width: 200px;    /* 常に200pxを維持 */
}

**使うシーン：**
- アイコンやボタンのサイズを固定したい
- 画像が潰れるのを防ぎたい
- サイドバーの幅を保ちたい
*/



## CSS JUMP ツール

![](images/2026-02-07-12-57-15.png)

拡張機能の説明は、取説参照


![SVG](./その他/SVG一覧/svg_20260207_131003.svg)


## JavaScript が正しく動作しません。新しいライブラリを追加したものの動作しないのはなぜでしょうか。 html

答えは、ライブラリを script タグで囲む必要があったからです。実際に動作するスクリプトとライブラリのスクリプトを、それぞれ別々に囲む必要があります。

```html
<!-- JavaScript -->
<script src="js/shuffle-text.js"></script>
<script>
  const text = new ShuffleText(document.querySelector("#myText"));
  text.start();
</script>
</body>
```


## 📌 パララックス　position: fixed と子要素の関係 html

【結論】
親が fixed で、子は relative や absolute のようなことができるということです。

別に親は relative である必要はなく、fixed があれば relative の代わりになりつつ、本来の fixed としての意味（固定）も持たせられる、といった形になります

- 親が固定されると、子も一緒に固定される
- fixed は relative の代わりになる + 固定機能も持つ


【具体例：固定背景のパララックス】
```html
<div class="particle-bg">       <!-- fixed -->
  <div class="house"></div>      <!-- relative -->
</div>
```

```css
.particle-bg {
  position: fixed;   /* 画面に固定 */
  top: 0; left: 0;
}

.house {
  position: relative; /* 親の中で配置 */
  /* fixed 不要！親と一緒に固定される */
}
```

【補足】
- fixedは親1箇所のみ
- 子に fixed を付けると親を無視して画面全体を基準に固定される
- パララックスは transform: translateY() で実装


## Claudecodeのスキルズへの追加方法 

・～.claude\skills\memo-format\SKILL.md

に追加する。

サンプル-------------------

# 出力先
d:\50_knowledge\01_memo.md に追記

---
name: memo-format
description: 学習メモを指定フォーマットで作成
triggers:
  - メモ作成
  - 学習メモ
  - フォーマットで
---

# 学習メモフォーマット

【結論】
要点を簡潔に

【具体例】
```コード例```

【補足】
- 箇条書き


例）
----------------------------

## 📌 パララックスのシンプルな作り方 html

![](images/2026-02-14-01-55-43.png)

[プレビュー](http://localhost:54321/preview-20260215-035019.html)

★なぜリラティブなのか！？
[プレビュー](http://localhost:54321/preview-20260215-035655.html)


【結論】
固定背景 + スクロール前景の2層構造で視差効果を作る

1. 大きくDivセクションを2つ作る
   (a) 1つは背景画像
   (b) 1つは前面画像
2. 1つ目の背景画像には、position: fixed で固定配置させる
3. 2つ目の前面の方には、あえて position: relative を付けて、z-index で前面に持ってくるようにする

あとはJavaScript(`transform: translateY()` )で調整します。

【具体例】
```html
<!-- ➀背景画像（固定） -->
<div class="particle-bg">
  <div class="house-illustration"></div>
</div>

<!-- ➁前面画像（スクロール） -->
<div class="parallax-container">
  <section class="parallax-section">
    <!-- コンテンツ -->
  </section>
</div>
```



```css
/* ➀背景：画面に固定 */
.particle-bg {
  position: fixed;
  z-index: -1;  /* 背景に配置 */
}

/* ➁前面：z-indexで前面に */
.parallax-container {
  position: relative;  /* z-indexを有効化 */
  z-index: 1;          /* 前面に配置 */
  padding-top: 100vh;  /* 最初は背景だけ表示 */
}
```

----------------------------

## 📌 particles.js の基本構成 ライブラリからスライドなどの実装をする場合（星座のような背景）　html

【結論】
CDN読込 → HTML要素準備 → particlesJS()で初期化の3ステップ


![SVG](./その他/SVG一覧/svg_20260210_000528.svg)

【具体例】
```html
<!-- ➀要素準備 -->
<div id="particles-js"></div>

<!-- ➁CDN読込 -->
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
```

```javascript
/* ➂初期化（script2.js） */
particlesJS("particles-js", {
  particles: {
    number: { value: 80 },           // パーティクル数
    shape: { type: "circle" },       // 形状：円
    size: { value: 3 },              // サイズ：3px
    line_linked: {
      enable: true,                  // 線接続ON
      distance: 150,                 // 接続距離150px
      color: "#ffffff",              // 線色：白
      opacity: 0.4,
      width: 1
    },
    move: {
      enable: true,
      speed: 6                       // 移動速度
    }
  },
  interactivity: {
    events: {
      onhover: { enable: true, mode: "repulse" }  // ホバーで反発
    }
  }
});
```

【補足】
- 第1引数：対象要素のid名（`particles-js`）
- 第2引数：設定オブジェクト
- CDN v2.0.0使用（jsdelivr配信）
- ホバー効果は `repulse`（反発）/ `grab`（つかむ）などが選択可能


## 📌 javaScriptでボタンを追加した際に、ループでそれぞれのボタンを追加した際に、アドイベントリスナーをつけても、該当のボタンがおせない。イベントが発火しない。

ループごとにconstで定義しないと初期化されないため。

変数を宣言していないかった。


## ライブラリのファイルを読み込む時、CDNなどはかならずjsの上に記述する。

```html
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script src="js/particle_setting.js"></script>
```

## ビューポートが小さくなった際、フォントサイズをある程度の大きさで止める。逆に、ビューポートが大きくなった場合も、指定したサイズであまり大きくしすぎないようにする。 html

```css
font-size: clamp(10px, (10 / 1280 * 100vw), 16px);
/* ✨
# clamp()の計算説明

この`clamp()`は**最小値、推奨値、最大値**の3つを指定してい���す。

clamp(10px, (10 / 1280 * 100vw), 16px)

## 各値の意味

1. **最小値: 10px** → これより小さくならない
2. **推奨値: (10 / 1280 * 100vw)** → 画面幅に応じて変動
3. **最大値: 16px** → これより大きくならない

つまり、**画面幅に応じて10px〜16pxの範囲で可変するフォントサイズ**です。
*/

```


## 検証画面のCSS画面への遷移の仕方、計算済みタブ(Computed)画面からギャップなどをクリックする。 html

ソースが表示されるのでクリック
![](images/2026-02-10-00-26-08.png)

スタイルタブからも可能
![](images/2026-02-10-00-28-48.png)



## JavaScriptなどでオープンメニューなどのクラスを追加した際に他のクラスを操作する。　html

`子クラス`（この場合は通常にクラス指定する）
#side_area.open .side_nav_container {


`兄弟セレクタ（~）を使う`(子要素ではない、親が同じ
この場合　 `~ `で兄弟クラスを設定し、さらにそこからの経由で子要素を指定する　`~これで一回親を経由すると考える`) */`
#side_area.open ~ #mainVisual_area .page_container {
  display: none;
}


body（お母さん）
├─ header#side_area（兄）
└─ section#mainVisual_area（弟）
   └─ nav.page_container（弟の子供）

★どのような経由で兄弟、クラスに移動するか！
   [プレビュー](http://localhost:54321/preview-20260215-040633.html)

![](images/2026-02-10-01-29-55.png)
/* ✨
# 回答

**概ね正しいですが、一部表現が不正確です。**

## 正しい点
- `#side_area.open .side_nav_container` は子孫セレクタとして正しい
- `~` は一般兄弟結合子として正しい
- HTML構造の理解は正しい

## 不正確な点

### 「~で一回親を経由する」は**誤り**
- `~` は**親を経由しない**
- **同じ親を持つ後続の兄弟要素**を直接選択する
- `#side_area.open ~ #mainVisual_area` は「openクラスがついたside_areaの**後に続く兄弟**のmainVisual_area」という意味

## 正確な説明
#side_area.open ~ #mainVisual_area .page_container

1. `#side_area.open` を起点に
2. `~` で**後続の兄弟**である `#mainVisual_area` を選択
3. その**子孫要素**の `.page_container` を選択

「親を経由」ではなく「**兄弟関係で横移動**」→「子孫へ降りる」が正確です。
*/


## 📌 ハンバーガーメニュー　兄弟セレクタ（~）でサブメニュー画面表示 html

【結論】
別セクションの要素を消すには兄弟セレクタ（~）を使う。
ハンバーガーメニュークリック時、JSでクラス付与 → CSSで全画面メニュー表示 + 他要素非表示。

【具体例】
```html
<!-- HTML構造 -->
<header id="side_area">         <!-- ここにopenクラス付与 -->
  <div class="side_nav_container"><!-- 通常非表示 → open時に表示 --></div>
</header>
<section id="mainVisual_area">  <!-- 兄弟要素 -->
  <nav class="page_container"><!-- open時に非表示にしたい --></nav>
</section>
```

```css
/* 通常時：サブメニュー非表示 */
.side_nav_container {
  display: none;
}

/* open時：サブメニューを全画面表示 */
#side_area.open .side_nav_container {
  display: flex;
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background-color: white;
  z-index: 999;
}

/* open時：兄弟要素の縦書きメニューを非表示 */
#side_area.open ~ #mainVisual_area .page_container {
  display: none;
}
```

```javascript
// JSでクラス付け外し
hamburgerBtn.addEventListener("click", function () {
  hamburgerBtn.classList.toggle("open");
  document.getElementById("side_area").classList.toggle("open");
});
```

【補足】
- `~` = 兄弟セレクタ（同じ親を持つ後ろの要素を指定）
- セクションが違っても、bodyの直下なら兄弟関係
- position: fixed は1箇所のみ（サブメニュー画面のみ）
- z-index で重なり順を制御


## javaScriptのオブジェクトがはいっているかを調べるには html

console.log(typeof ShuffleText);

はいっていれば「function」はいっていなければ「undefined」がかえってくる


## 動画の入れかた

・以下に動画を配置
C:\Users\guest04\Desktop\高橋研三\03_knowledge\その他\00_サンプルソース

・<video controls width="600">
  <source src="../../images/chrome_TVnJAHhbls.mp4" type="video/mp4">
</video>

動画名を指定する。（なおこれは、サンプルソースからみたパス）



## 📌 アニメーションライブラリ デモ管理（Swiper等）skillsの説明 html

【結論】
- `/animation-library-snippet {ライブラリ} {タイプ日本語}` でデモ一式生成
- `index.html` で全ライブラリのデモを一元管理（クライアント向け説明なし）
- ファイル名: `{ライブラリ英語}_{タイプ日本語}.md` （例: swiper_フェード切替.md）
- 必ず4デモ構成（シンプル版→パターン2つ→多機能版）

【具体例：参照場所】
```
# index.html（デモ一覧管理ページ）
\03_knowledge\images\
index.html

# デモHTML（4ファイル）
\03_knowledge\images\
  {library}_demo1_*_simple.html  ← シンプル版（緑枠）
  {library}_demo2_*.html
  {library}_demo3_*.html
  {library}_demo4_*.html

# MDファイル（スニペット）
C:\Users\guest04\Desktop\高橋研三\03_knowledge\その他\00_サンプルソース\
  ★{library}_{タイプ}.md
```

【具体例：コマンド】
```bash
# 新規ライブラリ追加
/animation-library-snippet swiper フェード切替
/animation-library-snippet gsap スクロール連動
/animation-library-snippet anime パララックス

# 生成されるもの
- ★{library}_{タイプ}.md
- 4つのデモHTML
- index.html に新規カード更新
```

【補足】
- デモHTML内に説明パネル禁止（クライアント向けのため）
- 説明は index.html のカードのみ（開発者向け情報）
- シンプル版は必ず最初（学習効率）
- ファイル名は日本語（わかりやすさ優先）
- MD内リンクは相対パス（会社・自宅でパス異なるため）
- パス自動判定機能を `/snippet` と `/memo-format` にも追加済み


## 📌 検証ツールのフレックスボックスの見方、要素、スタイルなどを駆使してフレックスボックスを理解　特に、親spacebetweenで子がflex1の場合 html





## 📌 Flexboxの使い方で、片方はflex1、片方はflexなしの場合、どのような動きをするか。これは隠しメニューなどに使えるので、理解すること。とりあえず上を確保して、下に値があればその分増えていくけど、なければ上の枠で埋め尽くすというイメージ。 html

クラスとプロパティのイメージ
![](images/2026-02-10-21-11-14.png)


画面イメージ。
![](images/2026-02-10-21-14-27.png)
画面イメージ（検証ツールイメージ）
![](images/2026-02-10-21-15-05.png)


ここが最重要ポイントです！

↓親要素のふたつの子要素（.menu_navi_upperと.menu_navi_lower）
.menu_navi_upper（メニュー部分）に flex: 1 をかける →
余っている空間をすべて自分が占領する という動きをします。

・一番下に何もない（何も flex の指定がない）
.menu_navi_lower
.menu_navi_lower に何も（flex の特別な指定）ないからこそ、
上手くいっています。

・仕組み
親（.menu_navi）が height: 100%（画面いっぱいの高さ）を持っている。
上の子（upper）が flex: 1 で「余ったスペースは全部俺がもらう！」と巨大化する。
その結果、下の子（lower）は、巨大化した upper にグイグイ押し出されて、一番下にくっつく。




## Flexboxを利用するときは、以下でも縦中央に持ってくることができるが、基本は親Flexboxで中央に指定してあげるのがベストプラクティス。 html

.hidden_nav {
  position: absolute; /* 親に対して自由になる */
  top: 50%;           /* 上から50%の位置へ */
  transform: translateY(-50%); /* 自分の高さの半分だけ上に戻る（これでピッタリ中央） */
}

![](images/2026-02-11-07-50-49.png)


★ベストプラクティス
```css
/* 縦へのflex 100%でcenter【flex】 */
.hidden_nav {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}
.hidden_menu {
  「右」に位置したい場合
}
```



## 兄弟要素の関係（セレクタの問題）: ~（一般兄弟結合子）は、同じ親要素を持つ兄弟間でのみ有効です。 html 

#hamburger_btn は <header id="side_area"> の中にあるため、その外にある .mainVisual_area を直接 ~ で指定することはできません。

✨他のセクションは操作できるのか？
できます。

ただし、CSSの`~`セレクタでは直接指定できないため、**JavaScriptを使う**必要があります。

// 例
hamburger_btn.addEventListener('change', function() {
  document.querySelector('.mainVisual_area').classList.toggle('active');
});

または、HTML構造を変更して、チェックボックスをheaderの外（兄弟要素として）に配置すれば、CSSだけで制御可能になります。
*/



## 表示と非表示にはいくつか種類があって、HTMLやCSSには以下のようなプロパティがある html

1. display: block  レイアウトから削除、
2. opacity: 1.0    透明化
3. visibility: visible は領域を保持したまま非表示、★あまり使用頻度は高くない。エラーメッセージなどに使える

`レイアウトから削除と領域保持の違い`

## **レイアウトから削除** (`display: none`)
- 要素が**完全に消えて、スペースも残らない**
- 他の要素が詰めて配置される
- 例：本棚から本を抜き取ると、隣の本が詰まる

## **領域を保持したまま非表示** (`visibility: hidden`)
- 要素は**見えないが、スペースは残る**
- 他の要素の位置は変わらない
- 例：本を透明にしても、本の場所は空いたまま

## 視覚的なイメージ
元の状態: [A][B][C]

display: none で B を消す
→ [A][C]  ← B のスペースも消える

visibility: hidden で B を消す
→ [A][  ][C]  ← B のスペースは残る
*/


## 先生への質問
▢　 --content-width: 129.6rem;
などのCSSでは共通定数を設定することがあると思うのですが、
これは一般的にアンダーラインではなくて、ハイフンを推奨されていると
のことでしたが、これは統一すべきでしょうか

▢　
## 📌 セクション高さは固定しない（height → min-height）

【結論】
コンテンツ増減に対応できるよう、セクションはmin-heightまたはautoを使う

【具体例】
```css
/* ❌ 悪い例：固定 */
.about_area {
  height: 60rem;  /* コンテンツが増えるとはみ出す */
}

/* ✅ 良い例：最低限の高さを確保 */
.about_area {
  min-height: 60rem;  /* 最低60rem、増えれば伸びる */
}

/* ✅ または完全自動 */
.about_area {
  height: auto;  /* コンテンツに合わせる */
}
```

【補足】
- 固定高さ → スマホ・タブレットでレイアウト崩れ
- min-height → デザイン維持 + 柔軟性
- レスポンシブ対応に必須

---

## 📌 CSS変数で繰り返し計算を共通化

【結論】
同じ計算式が複数箇所にある → CSS変数で一元管理

【具体例】
```css
/* ❌ 悪い例：同じ計算を3回 */
.news_area {
  width: calc(100% - var(--space-hor-pc) - var(--space-hor-pc-right) - var(--header-side-width));
}
.access_area {
  width: calc(100% - var(--space-hor-pc) - var(--space-hor-pc-right) - var(--header-side-width));
}
.access_container {
  width: calc(100% - var(--space-hor-pc) - var(--space-hor-pc-right) - var(--header-side-width));
}

/* ✅ 良い例：変数化 */
:root {
  --main-content-width: calc(100% - var(--space-hor-pc) - var(--space-hor-pc-right) - var(--header-side-width));
}

.news_area { width: var(--main-content-width); }
.access_area { width: var(--main-content-width); }
.access_container { width: var(--main-content-width); }
```

【補足】
- メリット1: 修正が1箇所で済む
- メリット2: コード量削減
- メリット3: 可読性向上

---

## 📌 JavaScript関数化で重複コード削減

【結論】
同じパターンの処理 → 関数にまとめて再利用

【具体例】
```javascript
// ❌ 悪い例：同じ処理を繰り返し
if (rect.top <= windowHeight) {
  storeImg.classList.add("animate");
}
if (rectManekiNeko.top <= windowHeight) {
  manekiNekoImg.classList.add("animate");
}

// ✅ 良い例：関数化
function addAnimateOnScroll(element) {
  const rect = element.getBoundingClientRect();
  const windowHeight = window.innerHeight;
  
  if (rect.top <= windowHeight) {
    element.classList.add("animate");
  }
}

// 使用
addAnimateOnScroll(storeImg);
addAnimateOnScroll(manekiNekoImg);
```

【補足】
- 要素追加時に関数呼び出すだけ
- バグ修正が1箇所で済む
- テスト・保守が簡単

---

## 📌 要素取得方法の統一（querySelector推奨） html

【結論】
getElementByIdとquerySelectorを混在させず、querySelectorに統一

【具体例】
```javascript
// ❌ 悪い例：混在
const btn = document.getElementById("btn");
const area = document.querySelector("#area");

// ✅ 良い例：querySelector統一
const btn = document.querySelector("#btn");
const area = document.querySelector("#area");
```

【補足】
- querySelectorはID・クラス・属性全対応
- モダンで柔軟（CSS セレクタ使用可）
- コードの一貫性向上
- チーム開発で混乱を防ぐ


## 📌background-image: url("../img/logo_omodakaya-vrt.png");で画像が取得できない　html

htmlをimgタグではなくてdivタグにする必要あり


## メディアクエリ内で当たり前のように設定しているのに、うまくいかない場合、おおもとのPCを崩している可能性があるのでチェックすること html


## PCのＣＳＳを、left 50rem　などを取り消して　メディアクエリでright 1remとかに修正したい場合、left:autoに設定する html





## 📌 CSS変数とメディアクエリでレスポンシブ余白管理 html

【結論】
- CSS変数を `:root` で定義
- メディアクエリで**上書き**して画面サイズごとの余白を変更
- 各要素は `var()` で参照するだけ


★★★　基本きめておくのは、（必須）
1. 左右余白（--space-hor）
2. 上下余白（--space-vrt）
3. セクション間（--section-top/bottom）← これも必須！
4. サイドバー

【具体例】
```css
/* デフォルト（スマホ: ~767px） */
:root {
  --space-hor: 2rem;
  --space-vrt: 12rem;
}

/* タブレット（768px~1024px）でCSSvariable変数を上書き */
@media screen and (min-width: 76.8rem) {
  :root {
    --space-hor: 4rem;  /* 上書き */
    --space-vrt: 16rem;
  }
}

/* PC（1025px~）でCSSvariable変数を上書き */
@media screen and (min-width: 102.5rem) {
  :root {
    --space-hor: 8rem;  /* さらに上書き */
    --space-vrt: 24rem;
  }
}

/* 使用側（画面サイズで自動変更） */
.about_area {
  margin-left: var(--space-hor);  /* スマホ2rem→タブレット4rem→PC8rem */
}
```

【補足】
- 一箇所変更で全セクションに適用
- 保守性・可読性が高い
- `--space-hor` = 左右余白、`--space-vrt` = 上下余白

## 📌 overflow: hidden と height の関係 CSS

【結論】
`overflow: hidden` を使うには、親要素に `height` の指定が必須。`height`、`width` がないと、親が子のサイズに合わせて自動的に伸びるため、`overflow: hidden` は効果を発揮しない。

【具体例】
```css
/* ❌ 効かない（heightなし） */
.right_container {
  overflow: hidden;  /* 親が伸びるので効果なし */
  display: flex;
  flex-direction: column;
}

/* ✅ 効く（height指定あり） */
.right_container {
  overflow: hidden;  /* はみ出しを切り取る */
  display: flex;
  flex-direction: column;
  height: 100%;     ★ /* ← 親の高さに固定 */
}

/* ✅ calc()で微調整も可能 */
.right_container {
  overflow: hidden;
  height: calc(100% - 5rem); ★右下に調整したいとき /* 演算子の前後にスペース必須 */
}
```

![](images/2026-02-12-13-39-50.png)

【補足】
- `height` なし → 親が子に合わせて伸びる → `overflow: hidden` 無効
- `height` あり → 親が固定される → はみ出し部分を切り取る
- `calc()` の演算子（+, -, *, /）の前後には必ずスペースが必要
- `height: 100%` は親に固定サイズが必要（`min-height` では動作しない）



---

## 🎯 スクロールアニメーション ()

### 📊  の意味

rect.top = 画面の上端（0px）から要素の上端までの距離
 **スクロールするほど `rect.top` は減少**　`つまりスクロールした位置からの要素までの距離`


### 🔍 値の変化

| スクロール量 | rect.top | 状態 |
|--------------|----------|------|
| 0px | 1200px | 画面外 ❌ |
| 400px | 800px | 画面下端 ⚠️ |
| 600px | 600px | 画面内 ✅ |

➡ **スクロールするほど `rect.top` は減少**

### ✅ 判定条件
```javascript
if (rect.top <= windowHeight) {
  element.classList.add('animate');
}
```

### 📌 重要な値

| 変数 | 意味 | 変動 |
|------|------|------|
| `window.innerHeight` | ブラウザの見える範囲の高さ | 固定 |
| `window.scrollY` | スクロールした距離 | 変動 |
| `rect.top` | 画面上端から要素上端までの距離 | 変動 |

### 🎬 動作イメージ
```
スクロール前:
画面上端 ━━━━━━━━━━━━━━━━━ 0px
    ↕ rect.top = 1200px (遠い)
    800px (innerHeight)
    ↕
画面下端 ━━━━━━━━━━━━━━━━━
────────────────────────────
要素上端 📦

スクロール後:
画面上端 ━━━━━━━━━━━━━━━━━ 0px
    ↕
    600px
    ↕
要素上端 📦 rect.top = 600px ✅
    ↕
    800px (innerHeight)
    ↕
画面下端 ━━━━━━━━━━━━━━━━━

➡ 600 <= 800 → true → アニメーション発動！
```

### 💡 デモファイル
- [scroll-demo.html](../02_作業/00_リンクワーク/HTML自動化/過去の課題/67_猫サイト/scroll-demo.html)
- リアルタイムで値を確認可能



## 📌 メディアクエリで margin を消す方法

【結論】
PCからスマホ用のメディアクエリで値を消すには、`0` を設定する

【具体例】
```css
/* PC */
.element {
  margin-right: 20px;
}

/* スマホ */
@media (max-width: 768px) {
  .element {
    margin-right: 0;  /* 0で消す */
  }
}
```

【補足】
- 継承されたプロパティを打ち消すには `0` を設定
- モバイルファーストという方法もあるが、チームの方針に従う


## 📌 CSS Jumper：モバイルCSS自動検知＆HTMLハイライト（2026-02-12追加）

### ✅ 新機能
1. **767px以下で自動モバイルCSS検索**（`@media (max-width: 767px)` 優先）
2. **HTMLファイルの該当行を黄色ハイライト**（3秒間）
3. **3点連携**：CSS（フォーカス）+ HTML（🟡ハイライト）+ ブラウザ（🔴赤枠）

### 🔧 インストール
```bash
cd css-to-html-jumper
code --install-extension css-to-html-jumper-1.10.0.vsix --force
# VS Code: Ctrl+Shift+P → Developer: Reload Window
# Chrome: chrome://extensions/ → CSS Jumper → 🔄
```

### 📋 操作
| 操作 | 結果 |
|------|------|
| ダブルクリック（通常画面） | CSS + HTML🟡 + ブラウザ🔴 |
| Ctrl+ダブルクリック | 📱強制モバイルCSS |
| Flexラベルクリック | モバイル自動検知対応 |
| Alt+クリック | 通常ジャンプ |

**⚠ DevToolsレスポンシブモード中のダブルクリックは動作しない**（Chrome仕様）



## 画面幅一杯にひろげたいときwidth100％でもできないとき html

width: 100vw;
## 📌 CSSの読み込み順とrem単位の挙動

【結論】
CSSは後から読み込まれたファイルが優先される（後勝ち）。
work.cssでfont-size: 62.5%が適用されてremが固定になっていた。
全てremで設定されている場合、absoluteでもfixedでも位置は変わらない。

【具体例】
```html
<!-- index.html -->
<link rel="stylesheet" href="css/reset.css" />
<link rel="stylesheet" href="css/style.css" />
<link rel="stylesheet" href="css/work.css" />  <!-- この順番が重要！後勝ち -->
```

```css
/* style.css */
html {
  font-size: calc(10 / 1280 * 100vw); /* レスポンシブなrem */
}

/* work.css（後に読み込まれるため優先される） */
html {
  font-size: 62.5%; /* 固定rem（1rem = 10px） */
}
```

【補足】
- CSSの読み込み順で同じプロパティは後勝ち
- font-sizeはremの基準値
- 全てremなら absolute/fixed の位置は変わらない（違いはスクロール時の挙動のみ）
- px固定の場合のみ、absoluteで位置がズレる

## 📌 list-style: none が効かない html

【結論】
`ul { list-style: none; }` だけでは黒丸が消えないことがある。
`ul li { list-style: none; }` のように li にも指定する必要がある。

【具体例】
```html
<ul class="page_nav">
  <li><a href="#">リンク</a></li>
</ul>
```

```css
/* ❌ これだけでは消えないことがある */
.page_nav {
  list-style: none;
}

/* ✅ li にも指定（確実） */
.page_nav li {
  list-style: none;
}
```

【補足】
- ulに指定しても継承されないケースがある
- 念のためliにも指定すると確実
- または `ul, li { list-style: none; }` でまとめて指定

## 📌 ホバーで画像拡大エフェクト html

【結論】
マウスを乗せると画像が拡大、離すと元に戻るエフェクトは、`transition` + `:hover` + `transform: scale()` で実装。

【具体例】
```css
/* 通常状態 */
.weekly_cat_img {
  transition: transform 0.3s ease; /* スムーズに変化 */
  cursor: pointer; /* カーソルをポインターに */
}

/* ホバー時 */
.weekly_cat_img:hover {
  transform: scale(1.2); /* 1.2倍に拡大 */
}
```

【補足】
- `transition` で変化速度を指定（0.3s = 0.3秒）
- `scale(1.2)` で1.2倍に拡大（数値変更で調整可能）
- `ease` でスムーズに（`linear`もあり）
- マウスを離すと自動で元に戻る

[プレビュー](http://localhost:54321/preview-20260215-032945.html)

## .共通クラス:nth-child(2) {display: none;}ここを消すと2つのリンクが消えるんだけど、なぜだろう？  共通クラスを複数に作成するとdisplay none ネストで対応する　配列ではなく html



display: contents を使うと、.left_container と .right_container の子がすべて共通の親（.about_area）の直下として扱われます。そのため、nth-child(2) が意図しない複数の要素（それぞれのコンテナ内の2番目の子）にヒットしている可能性が高いです ❌

⇀親要素がはっきりしなくなるため

/* 非表示「今週のひと品　詳しく見るリンク」  同じ`クラスを指定しているため、ネストで対応`*/
  .weekly_area .weekly_container .weekly_info_container .radius_link {
    display: none;
  }

  [プレビュー](http://localhost:54321/preview-20260215-033142.html)

  
## 📌 同じクラスが複数ある場合の対処法 CSS

【結論】
同じクラスが複数箇所で使われている場合、1箇所だけスタイルを変更したいときは**専用クラスを追加**する

【具体例】
```html
<!-- 元のコード（3箇所で使用） -->
<a href="#" class="radius_link">おもだか屋について</a>
<a href="#" class="radius_link weekly_space">くわしく見る</a>
<div class="radius_link">今週のひと品 一覧</div>

<!-- 1箇所だけ変更したい場合 -->
<div class="radius_link item_list_link">今週のひと品 一覧</div>
```

```css
/* モバイル専用のクラスを追加し場所を変更 */
/* 同じクラスを指定しているため、専用クラスで対応 */
@media (max-width: 768px) {
  .item_list_link {
    transform: translateY(180px); /* 見た目だけ移動 */
  }
}
```

【補足】
- **margin-top**: 親要素の高さも広がる（スペースができる）
- **transform**: 見た目だけ移動、親は広がらない（レイアウトに影響なし）
- **rem単位注意**: `300rem` = 約4800px（超巨大！）→ `px` 使用推奨
- モバイル専用は `@media (max-width: 768px)` 内に記述



## jQueryの拡張機能セットアップ

ひな形が欲しい → 拡張機能「jQuery Code Snippets」（donjayamanne.jquerysnippets など）を入れる

ちゃんと補完したい → プロジェクト直下に jsconfig.json を作って

{ "typeAcquisition": { "include": ["jquery"] } }


## jQuery 構文

// Pタグを要素にいれる
$(".inPTag").append("<p class='myClass'>jQuery</p>");
$(".myClass").slideToggle(2000);
/* ✨
「Toggle」は「切り替え」という意味で、**表示/非表示を切り替える動作**を指します。

`slideToggle()`は：
- **非表示の要素** → スライドしながら**表示**
- **表示中の要素** → スライドしながら**非表示**

このように、実行するたびに**表示状態を自動で切り替える（Toggle）**のが特徴です。

つまり「Slide」は**動き方**、「Toggle」は**切り替え機能**を表しています。現在の状態を判断して逆の動作をする点が「Toggle」の意味です。
*/

[プレビュー](http://localhost:54321/preview-20260214-091739.html)


## JavaScriptなど html
・クラスの追加　element.classList.add("aaa"); 
★クラスリストとaddが必要

・選択するたびにクラスをON/Offする　element.classList.toggle("aaa");　
★クラスリストとトグルが必要


・アコーディオンタグと
非表示のタグは、同じ階層

[プレビュー](http://localhost:54321/preview-20260215-033626.html)

## CSSでの構文 html
ボタンがおされた時は
.要素.クラス{

}
★要素とクラスをブランクなしでくっつける

例）#acc-btn-icon.active {}

## アコーディオンメニューの作り方 html

<!-- 親要素を並列で並べる。アコーディオンのボックス -->

★　親要素を並列で並べる（子要素に記載するのではない。）
```html
    <div class="acc">
      <!-- アコーディオン・選択するとメニュー -->
      <div class="acc-btn" type="button">
        <div class="acc-btn-title">Webディレクター</div>
        <div id="acc-btn-icon"></div>
      </div>
      <!-- 表示エリア flex -->
      <div class="acc-panel">
        <div class="acc-panel-title">Webディレクター</div>
        <div class="acc-panel-description">テキストテキスト</div>
      </div>
    </div>

```

```css
/* アコーディオン・選択するとメニュー */
.acc-btn {
  width: 80%;
  padding: 16px;
  /* border: 1px solid #000; */
  background: #ffd86a;

  display: flex;
  justify-content: space-between;

  border: 0.1px solid blue;
}
.acc-btn-title {
  font-size: 16px;
  display: block;
}

★CSSでインラインの文字を変更する際は、疑似要素を利用する！
（おそらく通常のクラスのプロパティではcontent:"文字"がつかえない）
★クラスが追加された際の書き方は「.クラス名.クラス名　」　
空白をいれない！！

#acc-btn-icon.active::before {
  display: block;
  content: "ー";
  font-size: 20px;
}

#acc-btn-icon::before {
  display: block;
  padding-right: 10px;
  cursor: pointer;
  content: "＋";
}

/* 表示エリア flex */
.acc-panel {
  width: 60%;
  padding: 16px;

  display: flex;
  justify-content: space-between;
}


```

```javascript

// HTMLの読み込みが完了してから中の処理を実行する
const accBtnIcon = document.getElementById("acc-btn-icon");


★クラスを`切り替える`ロジックは　element.classList.toggleとかく。クラスリストがつくことの注意！！！

★スライドトグル($(this).next(".acc-panel").slideToggle(200);)スライドの切り替えを表す。

//ドキュメント読み込み完了を待つ関数（した後）
$(function () {
  // ボタンがクリックされたら、（した後）
  $(".acc-btn").on("click", function () {
    $(this).next(".acc-panel").slideToggle(200);
    accBtnIcon.classList.toggle("active");
  });
});


```

## 📌 Claude Code スキル一覧

【結論】
自作スキルは5つ。`/スキル名` で呼び出せる。

【具体例】

### 1. `/snippet` - コードスニペット保存
- コードを `★{名前}.md` 形式で保存する
- 保存先: `D:\50_knowledge\その他\00_サンプルソース\`（自宅）
- 使い方: `/snippet` → 機能名・コードを伝える → ★付きmdで保存
- 例: `★ハンバーガーメニュー全画面表示.md`

### 2. `/memo-format` - 学習メモ作成
- 【結論】【具体例】【補足】フォーマットでメモを追記
- 保存先: `D:\50_knowledge\01_memo.md`（自宅）

### 3. `/animation-library-snippet` - アニメーションライブラリ デモ生成
- Swiper, GSAP, AOS等のアニメーションライブラリの学習用デモを一括生成
- 引数: `<ライブラリ名> <アニメーション種類>`
- 例: `/animation-library-snippet swiper フェード切替`
- 生成物:
  - ★mdファイル（HTML/CSS/JS分離で解説）
  - デモHTML 4つ（①シンプル版 ②③パターン ④多機能版）
  - index.html更新（全ライブラリ統合一覧）
- 保存先: 会社PC `03_knowledge\images\` 配下

### 4. `/class-auto` - クラス名自動付与
- HTMLの `<タグ>` だけ書く → AIが `class="クラス名"` を全タグに付与
- ルール: `[section]_[element]`（2単語）、状態は `_[state]`（3単語MAX）
- 外枠は `_area`（`_container`禁止）、省略禁止（img/nav除く）

### 5. `/section-auto` - セクション名自動提案
- スクショやURLを渡す → 大セクション名を日本語で一括提案
- HTMLコメント + CSS特徴付きコメントを生成
- `/class-auto` と連携可能（セクション確定後 → クラス名付与）

【補足】
- スキル保存先: `C:\Users\sensh\.claude\skills\[スキル名]\`
- 4と5は連携: `/section-auto` → `/class-auto`