

## シンボリックリンク

pullする。




## 拡張機能




▢　CSSjump を更新。Googleドライブから


▢　会社のcss-to-html-jumper-1.0.0.vsixをインストール

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
ーーーーーーーーーーーーーーーーーーーーーーーーーーーー



覚えておくべき共通ルール


・英単語の間違いがあれば修正
・共通化できるところがあれば、共通化する
・px表記があればremに統一する。
・HTMLはとくにコメントがお客様にみえるところなので正確な文章にする。

例）とりあえず～　暫定的等　NG

・固定で表示の必要性がなければ、widthは省略する。
とりあえず、その場合ユーザーに確認してください。

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





















ーーーーーーーーーーーーーーーーーーーーーーー
完了


## 今後のTODO

▢レイアウト２層の背景画像を透過させるHPを作成
（復習）

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