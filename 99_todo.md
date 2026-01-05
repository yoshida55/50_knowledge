
## シンボリックリンク

pullする。

pullする。


* [ ] レイアウト保存ツール


## 拡張機能

* [X] ~~*Paste Image*~~ [2026-01-05]
- MDファイルに画像をはりつける。
    Ctrl + alt + Vで貼り付けることができる。MDファイルに

- [ ] 設定が必要
    VS Codeの設定（Ctrl + ,）で：
    json"pasteImage.path": "${currentFileDir}/images"
    これで今後貼り付けた画像は `images` フォルダに入る。
    
    
* [ ] Markdown Preview Enhanced 


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


## GitHub Copilotへの指示



