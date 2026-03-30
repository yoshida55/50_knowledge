## 2026-03-30

- `get_categories()` → 全カテゴリを取得
- `get_the_category()` → ループ内で使う・今の記事についた全カテゴリを取得

- `esc_html()` → テキストを表示するとき（カテゴリ名・タイトル・著者名など）
- `esc_url()` → URLを表示するとき（hrefの中など）
- `esc_attr()` → HTML属性の値を表示するとき（class・id・valueの中など）

- PHPでHTMLタグを書くとき → `'` で囲む（外が `'` なら中に `"` を書ける）
- `href=""` の `"` が使えるのも外を `'` で囲んでいるから

[プレビュー](http://localhost:54321/preview-20260330-114258.svg)

- echoのコード分解：


　【以下の構文の解析】
 echo '<li><a href="' . esc_url( get_category_link($cate) ) . '">' .esc_html($cate->name) . '</a></li>' ;
　
  - `'<li><a href="'`         → HTMLタグは ' で囲む→　　なお。"　が必要なのは、通常のHTMLもa hrefのあとに、　""をかくから。最初に
  ""タグの文字列の内部にいれる

  - `esc_url( get_category_link($cate) )` → URLを取得（hrefの中）　→<a href="' . esc_url( get_category_link($cate) ) . '">ここはサイドの"" でかこまれているる
  
  - `'">'`                    → " を閉じてタグを閉じる
  - `esc_html($cate->name)`   → テキストは "" 不要（タグの外のテキスト）
  - `'</a></li>'`             → 閉じタグ



- `get_queried_object_id()` → 今のページのID（数字） / `get_the_category()` → 記事のカテゴリ配列
基本的にどちらも画面に表示されているカテゴリであるのはかわれない。IDか、配列あの違い。　なので表示でなければ、get_queried_object_idをつかう