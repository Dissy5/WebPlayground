from pathlib import Path
import re

root = Path(r"d:\Cursor\Learning\HTMLCSSJS\SamWorks\lessons")
pattern = re.compile(
    r'<div id="lesson-header">\s*<h1>(.*?)</h1>\s*'
    r'<div id="lesson-nav-button-container">\s*'
    r"<button>Previous Lesson</button>\s*"
    r"<button>Next Lesson</button>\s*"
    r"</div>\s*</div>",
    re.DOTALL,
)
replacement = (
    '<header id="lesson-header">\n'
    "        <h1>\\1</h1>\n"
    '        <nav class="lesson-nav">\n'
    '          <a href="#">Previous Lesson</a>\n'
    '          <a href="#">Next Lesson</a>\n'
    "        </nav>\n"
    "      </header>"
)

for html_file in root.rglob("*.html"):
    content = html_file.read_text(encoding="utf-8")
    updated, count = pattern.subn(replacement, content, count=1)
    if count:
        html_file.write_text(updated, encoding="utf-8")
        print(f"Updated {html_file.relative_to(root)}")
    else:
        print(f"Skipped {html_file.relative_to(root)}")
