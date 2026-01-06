
## シンボリックリンク

pullする。

pullする。


* [ ] レイアウト保存ツール


## 拡張機能

* [] ~~*Paste Image*~~ [2026-01-05]
## Paste Image
MDファイルに画像をはりつける。
Ctrl + alt + Vで貼り付けることができる。MDファイルに

※以下の設定で特定のフォルダに保存できる
VS Codeの設定（Ctrl + ,）で「paste image」と検索し、以下の通り書き換えてください。

Paste Image: Base Path
${currentFileDir} に変更
Paste Image: Path
images に変更
上記の必須



* [ ] markdown checkbox


Ctrl + K の後に Ctrl + S を押して、キーボードショートカット設定を開く。
上部の検索バーに 「markdown checkbox」 と入力。
markdown-checkbox.toggle という項目が出てきたら、その左側の鉛筆アイコンをクリック。


## ショートカットキー
keybindings.json

に以下を追加
{
  "key": "ctrl+`",
  "command": "editor.action.insertSnippet",
  "when": "editorTextFocus",
  "args": {
    "snippet": "`${TM_SELECTED_TEXT}$0`"
  }
}

ドラッグして色が変えられる
`あああ`


2. Restore Editors をインストール

VS Code レイアウト復元ショートカット
 Editors をインストール

保存　Restore Editors: Save Editor Layout
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
