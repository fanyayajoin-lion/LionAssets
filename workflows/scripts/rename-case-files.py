from __future__ import annotations

import csv
import re
from pathlib import Path


WORKSPACE = Path.cwd()
CSV_PATH = WORKSPACE / "wiki" / "cases" / "database" / "品牌案例資料庫.csv"


def safe_filename(value: str) -> str:
    value = value.strip().replace("/", "／").replace("\\", "／").replace(":", "：")
    value = re.sub(r'[<>:"/\\|?*]', "＿", value)
    value = re.sub(r"\s+", "", value)
    value = value.strip(". ")
    return value or "未命名"


def read_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_rows(rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def replace_in_markdown(replacements: dict[str, str]) -> None:
    for path in WORKSPACE.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements.items():
            old_no_ext = old.removesuffix(".md")
            new_no_ext = new.removesuffix(".md")
            new_text = new_text.replace(old, new)
            new_text = new_text.replace(old_no_ext, new_no_ext)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")


def main() -> int:
    rows = read_rows()
    used: dict[str, int] = {}
    replacements: dict[str, str] = {}

    for row in rows:
        industry = safe_filename(row["industry"])
        brand = safe_filename(row["brand"])
        stem = f"{industry}-{brand}"
        count = used.get(stem, 0) + 1
        used[stem] = count
        filename = f"{stem}.md" if count == 1 else f"{stem}-{count}.md"
        new_rel = f"wiki/cases/案例庫/{filename}"
        old_rel = row["case_card"].replace("\\", "/")
        old_path = WORKSPACE / old_rel
        new_path = WORKSPACE / new_rel
        if old_path.exists() and old_path.resolve() != new_path.resolve():
            if new_path.exists():
                raise FileExistsError(f"target exists: {new_path}")
            old_path.rename(new_path)
        row["case_card"] = new_rel
        replacements[old_rel] = new_rel

    write_rows(rows)
    replace_in_markdown(replacements)
    print(f"renamed={len(rows)} unique_names={len(used)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
