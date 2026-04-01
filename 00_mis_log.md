## 2026-03-30

- `get_categories()` → 全カテゴリを取得
- `get_the_category()` → ループ内で使う・その特定記事につけた全カテゴリを取得



- `wp_title('|', true, 'right')` → ページごとのタイトル表示・`bloginfo('name')` と組み合わせて「ページ名 | サイト名」になる

- wp_head()にCSSが自動で出るのを不思議に思ったが（つまりCSSの一覧がWEB出力時に設定される） → functions.phpのwp_enqueue_style()で登録したものがwp_head()から出てくる2段階の仕組み

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



- `get_queried_object_id()` → 今のページのID（数字） / `get_the_category()` → 記事のカテゴリ配列（これはカテゴリだけではない。今いるページによって取得するＩＤがかわってくる。　記事ページ(single.php)ならば記事ＩＤ）

・ `get_queried_object_id()` ようするにID取得するか配列か。シンプルにIDを利用すると、比較しやすい。　
カテゴリを表示するときなどは、配列からカテゴリ名を取り出す必要がある。　なので、IDで比較して、表示するときは、配列からカテゴリ名を取り出すのがベスト。


例）その投稿に対して、全カテゴリを回して一致したものの色を変える（class）そのときでは、配列で比較すると大変なので、get_queried_object_id()でカテゴリのＩＤを
取得し、比較をすると便利。


- タグごと出力する関数（この3つだけ覚える）：
  - `the_post_thumbnail()` → `<img>` ごと出る
  - `the_category()` → `<ul><li><a>` ごと出る
  - `wp_list_categories()` → `<ul><li><a>` ごと出る
  - それ以外の `the_` 系 → テキストだけ（自分でタグを書く）
基本的にどちらも画面に表示されているカテゴリであるのはかわれない。IDか、配列あの違い。　なので表示でなければ、get_queried_object_idをつかう

- justify-content: space-between → 子要素が3つのとき、2つめが自動的に中央にくる（1つめ=左端 / 3つめ=右端）

- クラス名のハイフン（`-`）禁止 → アンダースコア（`_`）に統一（例: `global-nav` → `header_nav`）
- `font-size: calc(10 / 1400 * 100vw)` → 横幅が狭いとremが小さくなり全体が縮む（1400px幅で正常サイズ）


- 「項目名＋内容」（会社情報とか）の組み合わせ → `dl dt dd` + `display:flex` + `flex-wrap:wrap` がベスト
- `table` → 比較・集計データ用 / `ul` → 順序なしリスト用 / `div` → 意味なし
- `dt { width: 20% }` + `dd { width: 80% }` → 合計100%で自動折り返し

会社情報サンプル
![](images/2026-03-30-22-12-55.png)

## 2026-03-31



- get_template_directory_uri() はURLを返す（物理パスではない）→ src="" や href="" に使う★画像やＵＲＬにつかう。　
- get_template_directory() は物理パスを返す → require / include に使う（_uri なし）

- wp_footer() は </body> 直前に必ず書く（WordPressのお決まり）
- wp_head() は </head> 直前に書く（wp_footer() は </body> 直前・セットで覚える）

- ローカルHTMLのWordPress化 → ①style.css ②header/footer.php ③index.php ④functions.phpの4ステップ

- wp_enqueue_styleのハンドル名が重複すると2つ目が無視される → それぞれ別名にする

- HTML属性の中（datetime=""など）→ get_the_date() + echo / タグの外の表示 → the_date()　つまりなぜ、<time datetime= get_the_date> the_date</time>
→これはよくわからないのでそういうものだとおもっておく！
- the_category()はaタグを自動出力 → 親のCSSのcolor:whiteが効かない。なぜなら、<li>タグであればそのなかに<a>タグがつくられるので、

.news_category a { color: white; } で上書きが必要
（  - `the_post_thumbnail()` → `<img>` ごと出る
  - `the_category()` → `<ul><li><a>タグででる` ごと出る
  - `wp_list_categories()` → `<ul><li><a>` ごと出る　要注意）
## 2026-04-01

- <ul>直下に<a>を置いてしまった → 正しくは<li>の中に<a>を入れる
- href=""を空のままにした → href="<?php the_permalink(); ?>"を入れる
- target="blank" と書いてしまった → 正しくは target="_blank"（アンダースコアが必要）
- カテゴリーURLの取得：get_category_link(get_cat_ID('カテゴリー名')) をセットで使う
- position: absolute は横並び・SPで調整大変 → 横並びは flexbox を使う
- SP切り替え時に新変数を作らない → @media内で既存の --side-width の値を上書きする
