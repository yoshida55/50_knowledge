import re

MEMO_PATH = r"D:\50_knowledge\01_memo.md"

WP_KEYWORDS = [
    "wordpress", "wp_", "php", "the_", "get_the_", "get_post", "get_posts",
    "functions.php", "archive.php", "single.php", "page.php", "header.php",
    "footer.php", "index.php", "esc_url", "esc_html", "esc_attr",
    "wp_enqueue", "wp_query", "have_posts", "the_post", "the_title",
    "the_content", "the_permalink", "the_date", "the_author",
    "bloginfo", "カスタムフィールド", "テーマ", "パーマリンク",
    "アイキャッチ", "テンプレート階層", "テンプレートファイル",
    "投稿タイプ", "固定ページ", "category.php",
]

ALREADY_TAGGED = re.compile(r'\b(WordPress|HTML)\s*$', re.IGNORECASE)

def classify(title_lower):
    for kw in WP_KEYWORDS:
        if kw.lower() in title_lower:
            return "WordPress"
    return "HTML"

with open(MEMO_PATH, encoding="utf-8") as f:
    lines = f.readlines()

changed = 0
wp_count = 0
html_count = 0
result = []
for line in lines:
    if re.match(r'^#{2,3}\s+', line):
        stripped = line.rstrip('\n').rstrip()
        if ALREADY_TAGGED.search(stripped):
            result.append(line)
            continue
        tag = classify(stripped.lower())
        new_line = stripped + "  " + tag + "\n"
        result.append(new_line)
        changed += 1
        if tag == "WordPress":
            wp_count += 1
        else:
            html_count += 1
    else:
        result.append(line)

with open(MEMO_PATH, "w", encoding="utf-8") as f:
    f.writelines(result)

print(f"完了: {changed}件タグ追加 （WordPress: {wp_count}件 / HTML: {html_count}件）")
