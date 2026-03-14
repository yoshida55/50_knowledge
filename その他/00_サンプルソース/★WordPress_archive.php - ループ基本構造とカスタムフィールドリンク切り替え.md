# WordPress archive.php - ループ基本構造とカスタムフィールドリンク切り替え

archive.phpの基本ループ構造と、カスタムフィールドのIDを使って一覧のリンク先を別の投稿タイプに切り替える実装。

★カスタムフィールド `related_test_id` にリンク先のポストIDを入れておくだけで、クリック先を切り替えられる

## ★重要ポイント

【★ポイント: カスタムフィールドでリンク先を切り替え】
```php
<?php
$related_id = get_post_meta(get_the_ID(), 'related_test_id', true);
$url = $related_id ? get_permalink($related_id) : get_permalink();
?>
<a href="<?php echo $url; ?>" class="news_item">
```
- `get_post_meta(get_the_ID(), 'フィールド名', true)` でカスタムフィールドの値を取得
- 値があればそのIDのURL、なければ自分自身のURLを使う
- カスタムフィールドに値がない投稿は通常通り動く（安全）

---

## PHP（archive.php フルソース）

```php
<?php echo '【テンプレート】' . basename(__FILE__); ?>
<?php get_header(); ?>

<main>
    <h1 class="page_title">お知らせ</h1>
    <section class="news_section">

        <?php while (have_posts()) : the_post(); ?>

        <?php
        $related_id = get_post_meta(get_the_ID(), 'related_test_id', true);
        $url = $related_id ? get_permalink($related_id) : get_permalink();
        ?>

        <a href="<?php echo $url; ?>" class="news_item">

            <?php if (has_post_thumbnail()) { ?>
                <?php the_post_thumbnail('thumbnail', ['class' => 'news_img']); ?>
            <?php } else { ?>
                <img src="<?php echo get_template_directory_uri(); ?>/img/news.jpg" alt="" class="news_img">
            <?php } ?>

            <div class="news_info">
                <div class="news_meta">
                    <time class="news_date"><?php the_time('Y.m.d'); ?></time>
                    <p class="author"><?php the_author(); ?></p>
                </div>
                <h3 class="news_title"><?php the_title(); ?></h3>
            </div>

        </a>

        <?php endwhile; ?>

        <?php the_posts_pagination(); ?>

    </section>
</main>

<?php get_footer(); ?>
```

## カスタムフィールドの設定方法

1. 管理画面 → 投稿の編集画面 → 下部「カスタムフィールド」
2. 名前：`related_test_id`
3. 値：リンクしたい投稿のID（URLの `post=◯◯` で確認）
4. 「カスタムフィールドを追加」→ 保存

## 動作フロー

1. お知らせ一覧（archive.php）でループ
2. 各投稿の `related_test_id` を取得
3. 値があれば → その投稿のURL（例: テスト投稿の詳細）
4. 値がなければ → その投稿自身のURL
5. クリックで該当ページへ遷移
