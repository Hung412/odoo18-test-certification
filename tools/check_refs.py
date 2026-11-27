#!/usr/bin/env python3
"""Kiểm tra link "ref" trong data/set*.json có trỏ tới trang có thật trong tài liệu Odoo 18.0.

Cần bản sao repo tài liệu (nhánh 18.0):
    git clone --depth 1 --branch 18.0 https://github.com/odoo/documentation.git <docs>
Dùng: python3 tools/check_refs.py <docs> [data/set10.json ...]
"""
import glob, json, os, re, sys

docs = sys.argv[1]
files = sys.argv[2:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "data", "set*.json")))
PREFIX = "https://www.odoo.com/documentation/18.0/"
bad = total = 0
for f in files:
    for i, q in enumerate(json.load(open(f, encoding="utf8"))):
        ref = q.get("ref")
        if not ref:
            continue
        total += 1
        path = re.sub(r"[#?].*$", "", ref)
        ok = path.startswith(PREFIX) and path.endswith(".html")
        if ok:
            rel = path[len(PREFIX):-len(".html")]
            ok = any(os.path.exists(os.path.join(docs, "content", rel + ext)) for ext in (".rst", "/index.rst"))
        if not ok:
            bad += 1
            print(f"{os.path.basename(f)} #{i}: {ref}")
print(f"{total - bad}/{total} link hợp lệ")
sys.exit(1 if bad else 0)
