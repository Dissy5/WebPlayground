from pathlib import Path

root = Path(r"d:\Cursor\Learning\HTMLCSSJS\SamWorks")

replacements = (
    ('id="lesson-header"', 'class="lesson-header"'),
    ('id="lesson-content"', 'class="lesson-content"'),
    ('<main id="content">', '<main class="main-content">'),
)


def skip(path: Path) -> bool:
    return "projects" in path.parts


for html_file in root.rglob("*.html"):
    if skip(html_file):
        continue

    content = html_file.read_text(encoding="utf-8")
    original = content

    for old, new in replacements:
        content = content.replace(old, new)

    if '<div id="content">' in content:
        content = content.replace('<div id="content">', '<main class="main-content">', 1)
        body_idx = content.rfind("</body>")
        div_idx = content.rfind("</div>", 0, body_idx if body_idx != -1 else None)
        if div_idx != -1:
            content = content[:div_idx] + "</main>" + content[div_idx + 6 :]

    if content != original:
        html_file.write_text(content, encoding="utf-8")
        print(f"Updated {html_file.relative_to(root)}")
