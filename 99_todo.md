

## シンボリックリンク

pullする。




## 拡張機能




▢　
▢　環境整理　Googleドライブにある。
SVG表示保存CS+S.ahk　
で使用。　これがあることによって、保存先が以下となる。
★同じツールを家と会社で使い回すための改修
【ポイント　環境変数で環境ごとに以下を設定する】
・KNOWLEDGE_ROOT・・・SVGを保存する先を設定する

ここで取得したフォルダを同じ階層の各プロジェクト用資料などに移動したりする。


▢　C:\Users\XXXXX\.claude\CLAUDE.md

を以下に修正する。

# 🔥 最優先ルール（絶対厳守）

## 📖 回答時の確認事項
**毎回の回答末尾に必ず記載**: 「📖 CLAUDE.md確認済」

## 💬 出力スタイル（--ucモード常時ON）
- **文章量**: 通常の50%
- **記号多用**: ✅❌🎯➡💡⚠🔍📋
- **構造**: 箇条書き・表のみ（長文禁止）
- **結論ファースト**: 前置き禁止
- **継続表示**: 会話冒頭に「--uc対応中」と表示

### 記号の使い方
- ✅ 完了 / ❌ 失敗 / ➡ 進行中
- 🎯 目標 / 💡 アイデア / ⚠ 注意
- 📋 リスト / 🔍 調査

### 略語例
- cfg=config / impl=implementation
- req=requirements / perf=performance

---

## 🎨 HTML/CSS設計ルール（絶対厳守）
- **position: fixed は親1箇所のみ**、子は absolute
- **不要な wrapper div 禁止**
- **ユーザーのクラス名で説明**（見本コード参照禁止）

---

## 🐍 Python開発ルール
- **venv必須**: 仮想環境で開発
- **プロトタイプ優先**: ログ大量→問題解決後に整理
- **動的実装**: ハードコーディング禁止
- **バッチ処理**: 時間短縮を常に意識
- **継続表示**: 会話冒頭に「--プロトタイプログ多めに実装！」

---

# SuperClaude Entry Point

This file serves as the entry point for the SuperClaude framework.
You can add your own custom instructions and configurations here.

The SuperClaude framework components will be automatically imported below.

# ═══════════════════════════════════════════════════
# SuperClaude Framework Components
# ═══════════════════════════════════════════════════

# Core Framework
@BUSINESS_PANEL_EXAMPLES.md
@BUSINESS_SYMBOLS.md
@FLAGS.md
@PRINCIPLES.md
@RULES.md

# Behavioral Modes
@MODE_Brainstorming.md
@MODE_Business_Panel.md
@MODE_Introspection.md
@MODE_Orchestration.md
@MODE_Task_Management.md
@MODE_Token_Efficiency.md

# MCP Documentation
@MCP_Context7.md
@MCP_Magic.md
@MCP_Morphllm.md
@MCP_Playwright.md
@MCP_Serena.md

---

## 🔧 トラブルシューティング記録ルール

### エラー発生時の記録
**場所**: `問題解決メモ_Troubleshooting/トラブルシューティング.md`

**フォーマット**:
```markdown
## 🧠 カテゴリ名
### 症状
具体的な症状
### 原因
根本原因
### 対処
1. 手順1
2. 手順2
```

### 運用フロー
- 新問題 → トラブルシューティング.md追記
- 10件超 → 月別アーカイブ移動
- 次回 → まずTOP 10確認





---

## 🔒 セキュリティルール（API Key管理）
- ❌ ログにAPI Key出力禁止
- ✅ `.env` + `.gitignore` 必須
- ✅ 最小権限のみ付与
- ✅ HTTPS通信（URLパラメータ禁止）
- ✅ 不要なKey削除

---

## 📁 ファイル操作ルール（トークン節約）

### ❌ 禁止操作
- ソース全体読み込み
- ディレクトリ全探索（`Glob("**/*")`）
- 推測でのファイルオープン

### ✅ 推奨操作
1. **Troubleshooting/README.md の TOP10 確認**
2. **Grep でピンポイント検索**
3. **該当ファイルのみ読込**

### 🚫 全探索禁止ディレクトリ
```
venv/ node_modules/ __pycache__/
bkup/ uploads/ .git/ *.log
Troubleshooting/ (TOP10→grep→該当ファイルのみ)
```

---

## 🎓 理解確認
**ファイル読込後、必ず回答冒頭に記載**: 「★理解しました！」
 


ーーーーーーーーーーーーーーーーーーーーーーー
## 今後のTODO

▢レイアウト２層の背景画像を透過させるHPを作成
（復習）

▢サンプルソースは以下　エクセルをみながらする。
⇀D:\02_作業\00_リンクワーク\HTML自動化\過去の課題\55_css_jump_pikaso_zyou_短い版_練習用










