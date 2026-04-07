## 2026-03-30

- `get_categories()` → 全カテゴリを取得
- `get_the_category()` → ループ内で使う・その特定記事につけた全カテゴリを取得



- `wp_title('|', true, 'right')` → ページごとのタイトル表示・`bloginfo('name')` と組み合わせて「ページ名 | サイト名」になる
/* ✨ポイント✨ */
`wp_title('|', true, 'right')`**: 現在表示しているページの名前（例：会社概要）を取得し、後ろに「|」を付けます。
`bloginfo('name')`**: 設定で決めた「サイト名（例：〇〇株式会社）」を取得します。

これらを組み合わせることで、**「会社概要 | 〇〇株式会社」**という形式で、ページごとに正しいタイトルが自動的に表示される仕組みです。



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


- わき余白は padding、要素間の隙間は margin（marginをwidth:100%と組み合わせると横スクロールの原因）

- pタグは細かく分けすぎない → 話題が変わらなければ1つの<p>にまとめる


- セクション余白：上・サイドはpadding、下だけmargin-bottom → モバイルで修正しやすい
- <ul>直下に<a>を置いてしまった → 正しくは<li>の中に<a>を入れる
- href=""を空のままにした → href="<?php the_permalink(); ?>"を入れる
- target="blank" と書いてしまった → 正しくは target="_blank"（アンダースコアが必要）
- カテゴリーURLの取得：get_category_link(get_cat_ID('カテゴリー名')) をセットで使う
- position: absolute は横並び・SPで調整大変 → 横並びは flexbox を使う
- SP切り替え時に新変数を作らない → @media内で既存の --side-width の値を上書きする
- position: absolute する要素は親の子にしない → 兄弟要素にするとSP切り替えで static に戻すだけで縦並びになる(子要素にするとあとでSPのとき、分けて処理できないのでやっかい。)


- position: fixed に margin-left: auto は効かない → left プロパティで位置指定する
- サイドバーありパララックス: left: var(--left-side-width) + width: calc(100% - サイドバー幅) + z-index管理（背景1・セクション10・ヘッダー100）
z-index サイドバーは200
z-index トップ画像は10
z-index contentsは100（margin-top 100vh）

こうすることで、背景を固定したまま、セクションとヘッダーはスクロールに合わせて動くようになる。　サイドバーは常に最前面に表示される。

-   background-image: url("../img/project1.jpg");(3点セット)は,DIVタグに記載する


## 2026-04-04
・専門用語
- セクションラベル

- outline = paddingの外側に線（レイアウトに影響しない） / border = レイアウトに影響する
- 幅を文字+paddingに自動で合わせる → width: fit-content

- 角を完全に丸くする（カプセル型）→ border-radius: 100px
- border-radius: 50% = 完全な丸（縦横が同じ正方形のときだけ丸。長方形だと楕円になる）

- margin: 0 auto はインライン要素（span）に効かない → display: block を追加する


- clip-path で切り取られた部分は描画ごと消える → 別要素を margin-top マイナスで潜り込ませる

![](images/2026-04-05-06-13-17.png)


- overflow: hidden 削除後に position: absolute; right: マイナス値の要素がはみ出す → overflow-x: hidden を body に追加

- タブボタンの余白は gap でなく padding → gap だと tab_line（position: absolute の下線）がズレるリスクあり
- box-sizing: border-box → paddingかけてもコンテンツ幅はひろがらない。でもpaddingの合計がwidthをこえるとひろがってしまう
- CSSの継承は子（下方向）にしか流れない → 兄弟・親には継承されない
- 継承される: color / font-size / font-family など / されない: width / padding / margin など

- JavaScript概要 → HTML/CSSだけでは動かせない「動き・操作・タイミング制御」を担当する言語。スクロール検知・クラスの付け外し・値の書き換えなどをする
- CSSアニメーションの使い分け → 単純な動きはCSS / スクロールや操作が絡むときはJS / 複雑な連続アニメはライブラリ（GSAP等）
- transition → 値が変わるときになめらかに動かす。transition: プロパティ名 時間 イージング の形
- ease → ゆっくり始まって速くなってゆっくり終わる（自然な動き）/ linear → 一定速度

## 2026-04-05

- tab_line に span を使うのは装飾用だから → flex から外れているのは position: absolute のおかげ（spanかどうかは関係ない）
```html
<div class="tab_list"> <!-- flex & position:relative -->
  <button class="tab_btn is-active" data-tab="news">軽　作　業</button>
  <button class="tab_btn" data-tab="press">ＩＴ作業</button>
  <span class="tab_line"></span> <!-- position:absolute 下線-->
</div>

- タブUIは flex（横並び）+ position:absolute（下線の自由配置）+ JS（クリックで動かす）の3役割分担

- CSS transition → 値が変わるときになめらかにする / JS → 実際に値を書き換える役割　
transition: プロパティ名 時間 イージング の形で書く。　

- ブラウザはデフォルトで body に margin: 8px が付く → リセットCSSで * { margin: 0; padding: 0; box-sizing: border-box; } を先頭に書く

- セクションwidthの選択基準：背景を全幅に伸ばしたい → width:100% + padding / コンテンツだけ中央に収めたい → width:70% + margin:0 auto。背景も考慮して選ぶ

- flexで段差レイアウトにするには align-items: flex-start が必要（ないとflex が全カードを同じ高さに揃えてしまい margin-top が効かない）

## 2026-04-07

- 疑似要素の縦位置を fixed 値（rem/px）で合わせると、フォントサイズ変更でズレる → vertical-align: middle か top:50- 疑似要素の縦位置を固定値（rem/px）で合わせると、フォントサイズ変更でズレる → vertical-align: middle か top:50%+translateY(-50%) を使う

## 2026-04-07

- border-radiusは特定の角だけ指定できる → border-radius: 左上 右上 右下 左下（時計回り）
- margin-bottomが効かないときはDevToolsで取り消し線チェック → 上書き・親のoverflow・flexが原因
- :nth-last-child は () と数字が必須 → 最後の要素だけなら :last-child がシンプル
- border shorthand は border-bottom を上書きする → 書く順番に注意
