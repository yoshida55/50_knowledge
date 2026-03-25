"""
01_memo.md の ## 見出しに WordPress / HTML タグを一括付与するスクリプト
- WordPress/PHP関連 → 末尾に "WordPress" を追加
- それ以外          → 末尾に "HTML" を追加
- 既存の html/css/jquery/js などのタグは正規化する
"""
import re

MEMO_PATH = r"D:\50_knowledge\01_memo.md"

# ── WordPress/PHP と判定するキーワード（見出し文字列にマッチするか確認）──
WP_PATTERNS = [
    r'WordPress', r'\bPHP\b', r'wp_', r'the_post', r'the_title',
    r'the_permalink', r'the_content', r'the_date', r'the_author',
    r'the_thumbnail', r'the_posts_pagination', r'get_the_',
    r'get_post_meta', r'get_template', r'get_categories', r'get_header',
    r'wp_enqueue', r'wp_footer', r'wp_head', r'wp_query',
    r'functions\.php', r'archive\.php', r'single\.php', r'page\.php',
    r'category\.php', r'header\.php', r'footer\.php',
    r'esc_url', r'esc_html', r'esc_attr',
    r'add_theme_support', r'add_action', r'add_filter',
    r'カスタムフィールド', r'カスタム投稿',
    r'テーマ作成', r'テーマ開発', r'テーマ化',
    r'パーマリンク', r'permalink',
    r'have_posts', r'setup_postdata', r'wp_reset_postdata',
    r'paginate_links',
    r'bloginfo', r'home_url',
    r'get_template_directory_uri', r'get_theme_file_uri',
    r'single_cat_title', r'get_queried_object',
    r'アイキャッチ',
    r'アーカイブページ',
    r'固定ページ',
    r'WordPressテーマ', r'WordPressのテーマ',
    r'WordPressで', r'WordPressの',
    r'Local.*WordPress', r'WordPress.*Local',
    r'endwhile', r'endforeach',
    r'ページネーション',
]

# 既存の末尾タグ（正規化対象）
EXISTING_TAG_RE = re.compile(
    r'\s+(html|css|js|jquery|javascript|php)\s*$',
    re.IGNORECASE
)

def is_wordpress(text):
    for pat in WP_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False

with open(MEMO_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

changed = 0
new_lines = []

for line in lines:
    # ## または ### で始まる見出しのみ処理
    if re.match(r'^#{2,3} ', line):
        stripped = line.rstrip('\n').rstrip()

        # 既存の旧タグを除去
        clean = EXISTING_TAG_RE.sub('', stripped)

        # 末尾にすでに WordPress / HTML が付いていたらスキップ
        if re.search(r'\s+(WordPress|HTML)\s*$', clean):
            new_lines.append(line)
            continue

        if is_wordpress(clean):
            new_line = clean + ' WordPress\n'
        else:
            new_line = clean + ' HTML\n'

        if new_line.rstrip('\n') != line.rstrip('\n'):
            changed += 1
        new_lines.append(new_line)
    else:
        new_lines.append(line)

print(f"変更件数: {changed} 件")

with open(MEMO_PATH, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("完了！")
