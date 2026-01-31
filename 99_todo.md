




## 拡張機能

▢　修正したファイルを置き換える。
▢　会社でコメント一覧がでないことをつたえて、確認する。

html {
  font-size: 62.5%; /* 1rem = 10px */
}

/* ┌──────────────────────────────────────────────────────────────────────┐
   │ 共通                                         │
   │ コンテンツ幅、右の固定メニューのサイズ                          │
   │ レスポンシブ対応: スマホ→タブレット(76.8rem〜)→PC(102.5rem〜)           │
   └──────────────────────────────────────────────────────────────────────┘ */
:root {
  --content-width: 129.6rem;
  --header-side-width: 20rem;
  --space-hor: 2.4rem;

  /* 最大コンテンツ幅：*/
  --view: 129.6rem;

  /* 上下の余白：*/
  --space-vrt: 12rem; /* sm(スマホ)サイズ */
  /* 左右の余白：*/
  --space-hor: 2rem; /* sm(スマホ)サイズ */
}

/* debug  あとでどこで使われているかチェック*/
:root {
  /* font */
  --f-serif: "Noto Serif JP", serif;
  --f-sans: "dnp-shuei-gothic-gin-std", sans-serif;
  --f-en: "Manrope", "dnp-shuei-gothic-gin-std", sans-serif;
  --f-en2: "garamond-premier-pro-caption", "Noto Serif JP", serif;
}

/* 各セクションに共通の上下余白をつける */
/* 76.8rem（tab）以上の切り替え：*/
@media screen and (min-width: 76.8rem) {
  :root {
    --space-vrt: 16rem; /* md の値 */
    --space-hor: 4rem; /* md の値 */
  }
}

/* 102.5rem（pc）以上の切り替え：*/
@media screen and (min-width: 102.5rem) {
  :root {
    --space-vrt: 24rem; /* lg の値  「お知らせ」等のセクションのコンテナマージン*/
    --space-hor: 8rem; /* lg の値 */
  }
}
/* ┌─────────────────────────────────────────┐
   │ メモ　　　　　　　                        │
   └─────────────────────────────────────────┘ */

.main-content {
  /* 通常コンテンツ */
  z-index: 1;
}
.fixed-header {
  /* 固定ヘッダー */
  z-index: 100;
}
.overlay {
  /* オーバーレイ（黒マスク） */
  z-index: 800;
}
.modal {
  /* モーダル */
  z-index: 900;
}
/* ハンバーガーメニュー */
.hamburger-menu {
  z-index: 1000;
}

/* ┌──────────────────────────────────────────────────────────────────────┐
   │ ヘッダー                                                             │
   │ PC: 右側に固定表示 / スマホ: 上部に配置                              │
   │ ロゴ・ナビゲーション・SNSリンクを含む                                │
   └──────────────────────────────────────────────────────────────────────┘ */

/* 右サイドに固定のメニューを表示する  */
#side_area {
  position: fixed;
  top: 0;
  right: 0;
  width: var(--header-side-width);
  height: 100vh;
  background-color: #fff;
  z-index: 100;
  padding: 10rem 1.5rem;
  border: 0.5rem solid red;
}

/* └ おもだか屋の猫のロゴ・説明のコンテナ 【flex】 */
.omodakaya_container {
  position: absolute;

  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.omodakaya_logo {
  width: 7.5rem;
  height: auto; /* 固定値をやめて auto にする */
  margin-bottom: 1rem;
}

.omodakaya_description {
  writing-mode: vertical-lr;
  font-family: var(--f-serif);
  font-size: 1.4rem;
  color: black;
}

/* └ SNSアイコンのコンテナ 【flex】 */
.side_sns_container {
  position: absolute;

  bottom: 10rem;
  left: 50%;
  transform: translateX(-50%);

  width: 15rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  text-align: center;
}

/* └ └ インスタグラムのコンテナ【flex】 */
.sns_container {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  gap: 0.3rem;
}

.sns_img {
  width: 2.4rem;
  height: 2.4rem;
  margin-left: 0.5rem;
}

.sns_name {
  font-family: var(--f-en2);
  font-size: 1.6rem;
  color: black;
}

/* └ └ オンラインストアのコンテナ【flex】  */
.onlinestore_container {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

/* ハンバーガーメニュー */
.hamburger_menu {
  position: absolute;

  right: 50%;
  transform: translateX(50%);
  width: 4.5rem;
  height: 4.5rem;
  cursor: pointer;
  z-index: 1000; /* メニューが他の要素より前に表示されるようにする */
  background-color: white;
}

/* ハンバーガーメニューのバー */
.bar {
  position: absolute;
  transition: 0.3s;
  left: 0;
  height: 0.4rem;
  width: 100%;
  background: black;
}

.bar:nth-child(1) {
  top: 0.8rem;
}
.bar:nth-child(2) {
  top: 2.2rem;
}
.bar:nth-child(3) {
  top: 3.6rem;
}

/* ┌──────────────────────────────────────────────────────────────────────┐
   │ キービジュアル / ページタイトル                                      │
   │ トップ: スライド表示・縦書きキャッチコピー                           │
   │ 下層: .kv-second でシンプルなタイトル表示                            │
   └──────────────────────────────────────────────────────────────────────┘ */

▢　キーフレームの仕組みについて聞く



##　長期的

作成・チェック時のルールをさらにブラッシュアップしていく


ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

































## 覚えておくべき共通ルール

`【チェック＆作成時の注意事項】`
・命名規則チェック　接続部分が_になっているか？
・英単語の間違いがあれば修正
・共通化できるところがあれば、共通化する
・px表記があればremに統一する。
　10px 1remとする。
・HTMLはとくにコメントがお客様にみえるところなので正確な文章にする。
例）とりあえず～　暫定的等　NG
・debugの文字がないか
・固定で設定する必要性がなければ（例）画像サイズなどは基本固定、しかし説明などは、基本指定しない。してもwidthだけとか。widthは省略する。
とりあえず、その場合ユーザー(自分に)に確認してください。

・サイズなどが不明な場所は、
以下のフォーマットでコメントを残す(コードの横ではなく必ず上に記載すること)

```css
/* 【要確認！】推定値。必ず確認すること！ */
width:8rem;
```
・セマンティックな構成になっているか
・メニューはUL,LIでつくられているか。　navが必要な場合も確認
ユーザーに
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

・コンテンツ幅がある場合、
その設定がされているか？
ある場合、定数で共通化させる
```css
/* 定数を定義 */
:root {
  --contents_padding: 3rem;
  --contents_main_width: 80rem;
}

・あとAI風に記載しているコメントなども全削除
```








▢CSS　JUMP　インストール手順

必要なもの
css-jumper フォルダ一式

STEP 1️⃣ フォルダを配置
C:\tools\css-jumper\   ← 日本語パスは避ける

STEP 2️⃣ Chrome拡張をインストール
chrome://extensions/ を開く
右上 「デベロッパーモード」ON
「パッケージ化されていない拡張機能を読み込む」
css-jumper フォルダを選択
表示された 拡張機能ID をメモ（例: hoplahamgadnacgmihmaceglgeopkfeg）

STEP 3️⃣ setup.bat を実行
setup.bat をダブルクリック → ID入力 → Enter
自動で行われること:

処理	内容
JSONファイル更新	native-host/com.cssjumper.open_vscode.json にexeパス設定
レジストリ登録	HKCU\Software\Google\Chrome\NativeMessagingHosts\...
vscode://登録	HKCU\Software\Classes\vscode\shell\open\command

STEP 4️⃣ Chrome再起動
完全に閉じて再起動（タスクトレイも確認）

STEP 5️⃣ 動作確認
拡張機能アイコン → プロジェクトパス設定
Live ServerでHTML開く
Alt+クリック → VS Codeで該当CSS行が開けばOK

⚠ トラブルシューティング
症状	対処
Native Messaging失敗	setup.bat再実行 → Chrome再起動
VS Code開かない	start vscode://file/C:/test.txt:1 をコマンドプロンプトで確認
拡張機能動かない	chrome://extensions で再読み込み + ページリロード













ーーーーーーーーーーーーーーーーーーーーーーー
完了/あとで他の端末でセットアップできるように拡張機能のセット手順などを記載





▢サンプルソースは以下　エクセルをみながらする。
⇀D:\02_作業\00_リンクワーク\HTML自動化\過去の課題\55_css_jump_pikaso_zyou_短い版_練習用




▢　環境整理　Googleドライブにある。
SVG表示保存CS+S.ahk　
で使用。　これがあることによって、保存先が以下となる。
★同じツールを家と会社で使い回すための改修
【ポイント　環境変数で環境ごとに以下を設定する】
・KNOWLEDGE_ROOT・・・SVGを保存する先を設定する
★環境変数KNOWLEDGE_ROOTに、ナレッジのフォルダをセットする

ここで取得したフォルダを同じ階層の各プロジェクト用資料などに移動したりする。




〇vccodeからブラウザ表示.ahk
Ctrl+P → ファイル名入力 → Enter → Alt+B → ブラウザ表示
これで奥深いフォルダのSVGもサクッと確認できるね。



◯会社のcss-to-html-jumper-1.0.0.vsixをインストール

VS Codeの「定義へ移動」機能を使っています。デフォルトでは Ctrl+Click ですが、VS Codeの設定で Alt+Click に変更できます：

VS Code設定を開く（Ctrl+,）
editor.multiCursorModifier を検索
ctrlCmd に変更



VS Code設定（Ctrl+,）を開く
CSS to HTML Jumper で検索
Target Files を変更
設定例
設定値	説明
**/index.html	index.htmlのみ（デフォルト）
**/*.html	全HTMLファイル
**/index.html, **/about.html	複数指定


この .vsix ファイルを会社に持っていく
会社のVS Codeを開く
拡張機能パネル（左側の四角いアイコン）の右上にある「…」（三点リーダー）をクリック
「VSIXからのインストール...」 を選択し、ファイルを選ぶ

CTRL　：　セクション一覧表示





▢　Googleドライブにある、vsixをインストールする
css-to-html-jumper-1.2.0.vsix
・CSS⇀HTML
・コメント（セクションの一覧を表示）CTRL　SHIft L



▢
loop-visualizer-1.0.17.vsix　　
・解説
・ループビジュアライズ
 ┌─────────────────────────────┬──────────────────────────┬──────────────┐
  │           設定名            │           用途           │    検索語    │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.apiKey       │ Claude API Key（図解用） │ loop api     │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.geminiApiKey │ Gemini API Key（解説用） │ loop gemini  │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.geminiModel  │ Geminiモデル選択         │ loop model   │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.model        │ Claudeモデル選択         │ loop model   │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.outputDir    │ HTML出力先               │ loop output  │
  ├─────────────────────────────┼──────────────────────────┼──────────────┤
  │ loopVisualizer.timeout      │ タイムアウト             │ loop timeout │
  └─────────────────────────────┴──────────────────────────┴──────────────
