#!/usr/bin/env python3
"""Build preview/index.html: the README run sheet plus links to every demo file. Made up data only.
Maintainer step, not part of the live run."""
import glob, html, os, re
import markdown
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
md = open("README.md", encoding="utf-8").read()
body = markdown.markdown(md, extensions=["fenced_code"])
# link each demo folder path to its file list below
for d in sorted(os.path.dirname(p) for p in glob.glob("day*/*/prompt.md")):
    slug = d.replace("/", "-")
    body = body.replace(f"<code>{d}/</code>", f'<a href="#{slug}"><code>{d}/</code></a>')
files = []
for d in sorted(os.path.dirname(p) for p in glob.glob("day*/*/prompt.md")):
    slug = d.replace("/", "-")
    fl = sorted(f for f in glob.glob(f"{d}/**/*", recursive=True) if os.path.isfile(f))
    lis = "".join(f'<li><a href="../{html.escape(f)}">{html.escape(f[len(d)+1:])}</a></li>' for f in fl)
    files.append(f'<section id="{slug}"><h3><code>{d}/</code></h3><ul>{lis}</ul></section>')
extra = "".join(f'<li><a href="../{f}">{f}</a></li>' for f in ("README.md", "CLAUDE.md", "demos/INVENTORY.md", "tools/seed.py", "tools/verify.py"))
page = f"""<!doctype html>
<!-- Made up data only. Preview of the GovTech instructor demos run sheet. -->
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GovTech instructor demos · run sheet (made up data)</title>
<style>
body{{font-family:system-ui,Helvetica,Arial,sans-serif;max-width:920px;margin:0 auto;padding:40px 24px 80px;color:#111;line-height:1.55}}
h1{{font-size:34px;letter-spacing:-.02em}} h2{{margin-top:44px;border-top:1px solid #ddd;padding-top:20px}} h3{{margin-top:28px}}
pre{{background:#f4f5f8;border:1px solid #e3e5ea;padding:12px 14px;white-space:pre-wrap;font-size:13.5px}}
code{{font-family:ui-monospace,SFMono-Regular,monospace;font-size:.88em}} a{{color:#2b54e8}}
.badge{{display:inline-block;font:600 11px ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;background:#fff4d6;color:#7a4b00;padding:4px 8px;border-radius:4px}}
section{{border:1px solid #e3e5ea;padding:4px 16px 8px;margin:12px 0}}
</style></head><body>
<p><span class="badge">Made up data</span></p>
{body}
<h2>Demo files</h2>
<ul>{extra}</ul>
{''.join(files)}
</body></html>
"""
os.makedirs("preview", exist_ok=True)
open("preview/index.html", "w", encoding="utf-8").write(page)
print("preview/index.html written")
