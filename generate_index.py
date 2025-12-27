import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Index of {path}</title>
<style>
body {{ font-family: monospace; }}
a {{ text-decoration: none; }}
</style>
</head>
<body>
<h1>Index of {path}</h1>
<hr>
<pre>
{entries}
</pre>
<hr>
</body>
</html>
"""

def generate_index(dirpath, root):
    rel = os.path.relpath(dirpath, root)
    path = "/" if rel == "." else "/" + rel.replace("\\", "/") + "/"

    entries = []
    if rel != ".":
        entries.append('<a href="../">../</a>')

    for name in sorted(os.listdir(dirpath)):
        if name == "index.html":
            continue
        full = os.path.join(dirpath, name)
        if os.path.isdir(full):
            entries.append(f'<a href="{name}/">{name}/</a>')
        else:
            entries.append(f'<a href="{name}">{name}</a>')

    html = TEMPLATE.format(
        path=path,
        entries="\n".join(entries)
    )

    with open(os.path.join(dirpath, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def walk(root):
    for dirpath, _, _ in os.walk(root):
        generate_index(dirpath, root)

if __name__ == "__main__":
    walk("docs")

