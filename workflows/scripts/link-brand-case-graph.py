from __future__ import annotations

import csv
from collections import defaultdict
from datetime import date
from pathlib import Path


WORKSPACE = Path.cwd()
CSV_PATH = WORKSPACE / "wiki" / "cases" / "database" / "品牌案例資料庫.csv"
CASE_DB = "wiki/cases/品牌案例資料庫"
SYNTHESIS = "wiki/synthesis/品牌案例庫分類總覽"
QUEUE = "wiki/cases/品牌案例補全隊列"
TODAY = "2026-06-05"


def safe_page_name(value: str) -> str:
    return value.replace("/", "／").replace("\\", "／").strip() or "未分類"


def read_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def append_once(path: Path, marker: str, content: str) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in current:
        path.write_text(current.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8")


def card_link(card_path: str) -> str:
    return card_path.removesuffix(".md").replace("\\", "/")


def update_case_card(row: dict[str, str]) -> None:
    path = WORKSPACE / row["case_card"]
    industry = safe_page_name(row["industry"])
    source = safe_page_name(row["source_collection"])
    brand = row["brand"]
    marker = "## 知識圖譜連結"
    content = f"""
## 知識圖譜連結

- 資料庫入口：[[{CASE_DB}]]
- 分類總覽：[[{SYNTHESIS}]]
- 補全隊列：[[{QUEUE}]]
- 產業索引：[[wiki/cases/分類/{industry}]]
- 來源索引：[[wiki/cases/來源/{source}]]
- 品牌條目候選：[[wiki/entities/{brand}]]

## 回流要求

補完最新資料後，必須回寫到：

- [[{CASE_DB}]]
- [[{SYNTHESIS}]]
- [[wiki/cases/分類/{industry}]]
- [[wiki/entities/{brand}]]
"""
    append_once(path, marker, content)


def write_industry_pages(rows: list[dict[str, str]]) -> None:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[safe_page_name(row["industry"])].append(row)

    root = WORKSPACE / "wiki" / "cases" / "分類"
    root.mkdir(parents=True, exist_ok=True)

    for industry, items in sorted(groups.items()):
        lines = [
            f"# {industry}",
            "",
            "## 這頁怎麼用",
            "",
            "這是品牌案例庫的產業索引頁，用來避免案例卡變成孤島。每個案例補全後，要把可複製打法回流到本頁與分類總覽。",
            "",
            "## 上層連結",
            "",
            f"- [[{CASE_DB}]]",
            f"- [[{SYNTHESIS}]]",
            f"- [[{QUEUE}]]",
            "",
            "## 案例",
            "",
        ]
        for row in sorted(items, key=lambda r: (r["brand"], r["file_name"])):
            lines.append(f"- [[{card_link(row['case_card'])}|{row['brand']}]]：`{row['file_name']}`，來源 `{row['source_collection']}`，狀態 `{row['research_status']}`")
        lines.extend(
            [
                "",
                "## 待蒸餾問題",
                "",
                "- 這類案例共同的變現邏輯是什麼？",
                "- 哪些打法能轉成顧問診斷題？",
                "- 哪些打法能轉成課程模組或自媒體內容？",
                "- 哪些流程重複三次以上，應升級為 Skill / Asset / Memory？",
            ]
        )
        (root / f"{industry}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_source_pages(rows: list[dict[str, str]]) -> None:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[safe_page_name(row["source_collection"])].append(row)

    root = WORKSPACE / "wiki" / "cases" / "來源"
    root.mkdir(parents=True, exist_ok=True)

    for source, items in sorted(groups.items()):
        lines = [
            f"# {source}",
            "",
            "## 上層連結",
            "",
            f"- [[{CASE_DB}]]",
            f"- [[{SYNTHESIS}]]",
            f"- [[{QUEUE}]]",
            "",
            "## 檔案與案例卡",
            "",
        ]
        for row in sorted(items, key=lambda r: (r["industry"], r["brand"], r["file_name"])):
            lines.append(f"- [[{card_link(row['case_card'])}|{row['brand']}]]：{row['industry']}，`{row['file_name']}`")
        (root / f"{source}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_queue(rows: list[dict[str, str]]) -> None:
    by_industry: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_industry[safe_page_name(row["industry"])].append(row)

    lines = [
        "# 品牌案例補全隊列",
        "",
        "這頁是 AI 補最新資料與正式歸檔的工作入口。原始檔不複製，依案例卡中的 `original_source_path` 讀取。",
        "",
        "## 上層連結",
        "",
        f"- [[{CASE_DB}]]",
        f"- [[{SYNTHESIS}]]",
        "",
        "## 補全規則",
        "",
        "- 先讀案例卡的原檔摘要。",
        "- 連網查證品牌最新現況，不可硬補。",
        "- 保留「原 PPT 觀點」與「最新補充」兩層。",
        "- 完成後建立正式案例頁與品牌 entity，並回寫本隊列。",
        "",
    ]
    for industry, items in sorted(by_industry.items()):
        lines.append(f"## {industry}")
        lines.append("")
        lines.append(f"- 產業索引：[[wiki/cases/分類/{industry}]]")
        for row in sorted(items, key=lambda r: (r["brand"], r["file_name"])):
            lines.append(f"- [ ] [[{card_link(row['case_card'])}|{row['brand']}]]：`{row['file_name']}`")
        lines.append("")
    (WORKSPACE / "wiki" / "cases" / "品牌案例補全隊列.md").write_text("\n".join(lines), encoding="utf-8")


def update_database_page(rows: list[dict[str, str]]) -> None:
    path = WORKSPACE / "wiki" / "cases" / "品牌案例資料庫.md"
    industry_links = sorted({safe_page_name(row["industry"]) for row in rows})
    source_links = sorted({safe_page_name(row["source_collection"]) for row in rows})
    content = [
        "## 雙向連結入口",
        "",
        f"- 分類總覽：[[{SYNTHESIS}]]",
        f"- 補全隊列：[[{QUEUE}]]",
        "",
        "### 產業索引",
        "",
    ]
    content.extend([f"- [[wiki/cases/分類/{industry}]]" for industry in industry_links])
    content.extend(["", "### 來源索引", ""])
    content.extend([f"- [[wiki/cases/來源/{source}]]" for source in source_links])
    append_once(path, "## 雙向連結入口", "\n".join(content))


def update_synthesis_page(rows: list[dict[str, str]]) -> None:
    path = WORKSPACE / "wiki" / "synthesis" / "品牌案例庫分類總覽.md"
    industries = sorted({safe_page_name(row["industry"]) for row in rows})
    content = [
        "## 雙向索引",
        "",
        f"- 品牌案例資料庫：[[{CASE_DB}]]",
        f"- 補全隊列：[[{QUEUE}]]",
        "",
        "### 產業索引",
        "",
    ]
    content.extend([f"- [[wiki/cases/分類/{industry}]]" for industry in industries])
    append_once(path, "## 雙向索引", "\n".join(content))


def update_index_and_logs(rows: list[dict[str, str]]) -> None:
    index_content = f"""
## 品牌案例知識圖譜

- [[{CASE_DB}]]
- [[{QUEUE}]]
- [[{SYNTHESIS}]]
- 產業索引：`wiki/cases/分類/`
- 來源索引：`wiki/cases/來源/`
"""
    append_once(WORKSPACE / "index.md", "## 品牌案例知識圖譜", index_content)

    hot_content = f"""
## 品牌案例連結修復

- 107 張案例卡已補上資料庫、分類總覽、補全隊列、產業索引、來源索引與品牌 entity 候選連結。
- 下一步：依 [[{QUEUE}]] 分批連網補最新資料。
"""
    append_once(WORKSPACE / "hot.md", "## 品牌案例連結修復", hot_content)

    log_content = f"""
## {TODAY} 品牌案例雙向連結修復

- 替 {len(rows)} 張 `wiki/cases/案例庫/` 案例卡補上知識圖譜連結。
- 建立 `wiki/cases/分類/` 產業索引頁。
- 建立 `wiki/cases/來源/` 來源索引頁。
- 建立 `wiki/cases/品牌案例補全隊列.md`。
- 更新 `wiki/cases/品牌案例資料庫.md`、`wiki/synthesis/品牌案例庫分類總覽.md`、`index.md`、`hot.md`。
"""
    append_once(WORKSPACE / "log.md", f"## {TODAY} 品牌案例雙向連結修復", log_content)


def main() -> int:
    rows = read_rows()
    for row in rows:
        update_case_card(row)
    write_industry_pages(rows)
    write_source_pages(rows)
    write_queue(rows)
    update_database_page(rows)
    update_synthesis_page(rows)
    update_index_and_logs(rows)
    print(f"linked={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
