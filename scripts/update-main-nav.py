from pathlib import Path
import re

root = Path(r"d:\Cursor\Learning\HTMLCSSJS\WebPlayground")
nav_inner = (root / "boilerplates" / "main-nav.html").read_text(encoding="utf-8").strip()

pattern = re.compile(
    r'(<nav id="main-nav">).*?(</nav>)',
    re.DOTALL,  # let . match newlines
)

for html_file in root.rglob("*.html"):
    if "boilerplates" in html_file.parts:
        continue

    content = html_file.read_text(encoding="utf-8")
    updated, count = pattern.subn(
        rf"\1\n      {nav_inner}\n    \2",
        content,
        count=1,
    )

    if count:
        html_file.write_text(updated, encoding="utf-8")
        print(f"Updated {html_file.relative_to(root)}")