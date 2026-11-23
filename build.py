#!/usr/bin/env python3
"""Ghép data/set*.json vào src/template.html -> Odoo18_Mock_Certification.html.

Mỗi file data/setN.json là một đề (danh sách câu hỏi). Chạy: python3 build.py (thêm --check để chỉ kiểm tra, không ghi file)
"""
import collections, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "Odoo18_Mock_Certification.html")


def load():
    qs = []
    files = sorted(glob.glob(os.path.join(ROOT, "data", "set*.json")),
                   key=lambda p: int(re.search(r"set(\d+)", p).group(1)))
    for path in files:
        n = int(re.search(r"set(\d+)", path).group(1))
        for q in json.load(open(path, encoding="utf8")):
            qs.append({"set": n, **q})
    return qs


def check(qs):
    errs = []
    for q in qs:
        tag = f"set{q['set']}: {q['question'][:60]}"
        if len(q["options"]) != 4 or len(set(q["options"])) != 4:
            errs.append(f"cần 4 đáp án khác nhau - {tag}")
        if q["answer"] not in range(4):
            errs.append(f"answer phải là 0..3 - {tag}")
    dup = [k for k, v in collections.Counter(q["question"].strip().lower() for q in qs).items() if v > 1]
    errs += [f"câu hỏi trùng: {d[:80]}" for d in dup]
    return errs


def report(qs):
    by_set = collections.defaultdict(list)
    for q in qs:
        by_set[q["set"]].append(q)
    print("đề  số câu  hình  đúng=dài nhất  đúng=ngắn nhất")
    for n, g in sorted(by_set.items()):
        lens = [[len(o) for o in q["options"]] for q in g]
        longest = sum(1 for q, l in zip(g, lens) if l[q["answer"]] == max(l) and l.count(max(l)) == 1)
        shortest = sum(1 for q, l in zip(g, lens) if l[q["answer"]] == min(l) and l.count(min(l)) == 1)
        imgs = sum(1 for q in g if q.get("image"))
        print(f"{n:>3} {len(g):>7} {imgs:>5} {longest/len(g):>13.0%} {shortest/len(g):>15.0%}")


def main():
    qs = load()
    errs = check(qs)
    report(qs)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    if "--check" in sys.argv:
        return
    data = json.dumps(qs, ensure_ascii=False).replace("</", "<\\/")
    tpl = open(os.path.join(ROOT, "src", "template.html"), encoding="utf8").read()
    open(OUT, "w", encoding="utf8").write(tpl.replace("/*__QBANK__*/[]", data))
    print(f"-> {os.path.basename(OUT)} ({len(qs)} câu)")


if __name__ == "__main__":
    main()
