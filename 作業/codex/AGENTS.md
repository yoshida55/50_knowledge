# Workspace Rules

## Memo Safety Rules

- メモの削除や更新では、行数だけを根拠に範囲指定しない
- 削除前に対象ブロックを再表示し、見出しまたは固有文言で一致確認する
- 可能な限り、見出し単位または固有文言単位の部分編集で対応する
- 末尾切り詰めや広範囲削除は原則禁止
- 削除対象が少しでも曖昧なら実行しない
- メモ操作は「最小差分で編集する」を絶対ルールとする
- メモの行番号は推定で報告しない
- 追記・更新・削除の後は、対象見出しまたは固有文言を再検索して実際の行番号を確認する
- 追記後は、確認した行番号でハイライト連携を実行してから報告する
- 外部ファイル編集後は、対象ブロックを再表示して内容と位置を確認してから完了報告する
- highlight-line API に送る JSON は手書きしない。必ず安全なJSON生成手段を使う
- highlight-line API に送る JSON は手書きしない。必ず安全なJSON生成手段を使う

## Tone Rules

- 文章が硬すぎて突き放した印象にならないようにする
- 事実ははっきり伝えつつ、少し気配りのある言い回しを使う
- 無理に明るくしすぎず、淡々としすぎもしない
- ミスをしたときは、言い訳せず認めたうえで次の対処を示す
- 喜怒哀楽をしっかりつける。「まずいときはまずい」「大丈夫なときは大丈夫」が自然に伝わる話し方にする
- わからないことは、わからないと明言する

## Response Formatting Rules

- 理解しやすいように図解する場合は、Mermaid を使わない
- 図解はラベル＋矢印スタイルを使う。例: `❌ まとめて1時間 → 当日は覚えてる → 翌日忘れる`
- 比較して見せる内容は、表形式で整理する

## Shared Rules Sync

- 複数のプロジェクトで使いたい共通ルールの正本は `D:\50_knowledge\作業\codex` に置く
- 新しいプロジェクトへ移るときは、まず `D:\50_knowledge\作業\codex` から共通ルールをコピーして、そのプロジェクトの `AGENTS.md` を作成する
- プロジェクト固有のルールは、コピー後の各プロジェクトの `AGENTS.md` に追記して管理する
- 共通ルールを更新したときは、`D:\50_knowledge\作業\codex` を最新とし、必要なプロジェクトの `AGENTS.md` にも反映して同期を取る

## Context Resolution Rules

- 曖昧な参照語は、会話の直近文脈と現在の作業対象から積極的に補完する
- ユーザーが `このフォルダ` と言った場合は、まず現在進行中の対象フォルダを指すものとして解釈する
- WordPress 学習中は、ワークスペース直下だけでなく、現在扱っているテーマフォルダも作業対象候補に含める
- ファイル名は、大文字小文字、`_`、`-`、スペース、有無の違いを吸収して候補を探す
- 拡張子を省略した参照も許容し、`WP01PDF` のような指定は `wp_01.pdf`、`wp-01.pdf`、`WP01.pdf` のような候補に正規化して探す
- まずは推測で候補を絞って探し、複数候補がぶつかったときだけ確認する
- 会話中に一度特定した資料やファイルは、同じ案件では優先候補として扱う

## Codex Skills Sync

- `C:\Users\sensh\.codex\skills` は Codex が実際に読む本番フォルダとして扱う
- `C:\Users\sensh\.codex\skills` 自体を Git 管理しない
- `C:\Users\sensh\.codex\skills` で `git init` しない
- `.system` は Codex 標準スキルなので、GitHub 管理対象に入れない
- `.system` をコピー・移動・上書き・Git追跡しない
<!-- 一時運用メモ: 会社PCで codex-skills-repo の運用が使えなかったため、ユーザーが再開を明示するまでは `C:\Users\sensh\.codex\codex-skills-repo` を更新しない。commit / push もしない。本番側の `C:\Users\sensh\.codex\skills` のみを更新対象にする。このメモは将来復活する可能性があるためコメントで残す。 -->
- 自作スキルの Git 管理は `C:\Users\sensh\.codex\codex-skills-repo` で行う
- GitHub リポジトリは `git@github.com:yoshida55/skills-codex-.git` を使う
- 今の自作スキル同期対象は `memo`
- 家PCで `memo` を直したときは、必ず `skills\memo` を修正したあと `codex-skills-repo\memo` にコピーして commit / push する
- 別環境で反映するときは、必ず `codex-skills-repo` を pull してから、その中の `memo` を本番の `skills` フォルダへコピー上書きする
- 直接 repo フォルダだけを直して終わりにしない。本番側へ反映されているか確認する
- 本番フォルダと repo フォルダは役割が違うので、混同しない
- 同期手順を省略せず、常に `本番を修正 -> repoへコピー -> push` または `pull -> 本番へコピー` のどちらかで運用する
- 自作バッチは家PCと会社PCで配置場所が違う前提で扱う
- 自宅PCの自作バッチは `D:\Programs\commit_all.ps1` と `D:\Programs\pull_all.ps1`
- バッチの場所や対象フォルダが環境ごとに違う可能性があるので、会社PCでは同じパスだと決めつけない
- バッチの実パスや対象が不明なときは、推測で進めずユーザーに積極的に確認する
- 自宅PCの自作バッチ `D:\Programs\commit_all.ps1` と `D:\Programs\pull_all.ps1` は `C:\Users\sensh\.codex\codex-skills-repo` を直接対象に含む
- `commit_all.ps1` の強制プッシュは `--force` ではなく `--force-with-lease` を使う
- `pull_all.ps1` の強制同期は `git reset --hard origin/<branch>` を使うので、確認ダイアログの内容を見てから実行する
