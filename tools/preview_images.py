#!/usr/bin/env python3
"""Chụp ảnh xem trước các câu hỏi có hình trong một file JSON.

Dùng: python3 tools/preview_images.py data/set7.json out.png [chỉ_số_bắt_đầu] [số_câu]
Cần google-chrome. Ảnh ghép các hình theo thứ tự, mỗi hình có số thứ tự câu trong file.
"""
import html, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, out = sys.argv[1], os.path.abspath(sys.argv[2])
start = int(sys.argv[3]) if len(sys.argv) > 3 else 0
count = int(sys.argv[4]) if len(sys.argv) > 4 else 6
tpl = open(os.path.join(ROOT, "src", "template.html"), encoding="utf8").read()
css = "\n".join(re.findall(r"<style>(.*?)</style>", tpl, re.S))
qs = [(i, q) for i, q in enumerate(json.load(open(src, encoding="utf8"))) if q.get("image")][start:start + count]
body = "".join(
    f'<section><p><b>#{i}</b> {html.escape(q["question"])}</p>'
    f'<figure class="shot"><div class="shot-in">{q["image"]}</div></figure></section>'
    for i, q in qs)
page = (f'<html><head><meta charset="utf8"><style>{css}</style></head>'
        f'<body style="padding:16px;width:900px;display:flex;flex-direction:column;gap:20px">{body}</body></html>')
with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, "p.html")
    open(f, "w", encoding="utf8").write(page)
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", f"--user-data-dir={d}/prof",
                    "--window-size=940,%d" % (40 + 520 * max(1, len(qs))), f"--screenshot={out}", "file://" + f],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
print(f"{len(qs)} hình -> {out}")
