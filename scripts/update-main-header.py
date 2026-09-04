from pathlib import Path
import re

root = Path(r"d:\Cursor\Learning\HTMLCSSJS\SamWorks")
header_inner = (root / "boilerplates" / "main-header.html").read_text(encoding="utf-8").strip()

pattern = re.compile(
    r'(<header id="main-header">).*?(</header>)',
    re.DOTALL,  # let . match newlines
)

def skip(path: Path) -> bool:
    return "projects" in path.parts

for html_file in root.rglob("*.html"):
    if skip(html_file):
            continue
        
    if "boilerplates" in html_file.parts:
        continue

    content = html_file.read_text(encoding="utf-8")
    updated, count = pattern.subn(
        rf"\1\n      {header_inner}\n    \2",
        content,
        count=1,
    )

    if count:
        html_file.write_text(updated, encoding="utf-8")
        print(f"Updated {html_file.relative_to(root)}")