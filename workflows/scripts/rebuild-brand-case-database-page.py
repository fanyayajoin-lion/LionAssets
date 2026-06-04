from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


WORKSPACE = Path.cwd()
CSV_PATH = WORKSPACE / "wiki" / "cases" / "database" / "品牌案例資料庫.csv"
OUT_PATH = WORKSPACE / "wiki" / "cases" / "品牌案例資料庫.md"


def read_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def page_link(path: str) -> str:
    return path.replace("\\", "/").removesuffix(".md")


def main() -> int:
    rows = read_rows()
    source_counts = Counter(row["source_collection"] for row in rows)
    industry_links = sorted({row["industry"] for row in rows})
    source_links = sorted({row["source_collection"] for row in rows})

    lines = [
        "# 品牌案例資料庫",
        "",
        "這是品牌案例批次讀取後的資料庫索引。原檔仍保留在老闆原本資料夾，知識庫只保存抽取摘要、原路徑、補全狀態與後續歸檔卡。",
        "",
        "## 統計",
        "",
        "- 建立日期：2026-06-05",
        f"- 檔案總數：{len(rows)}",
    ]
    for source, count in sorted(source_counts.items()):
        lines.append(f"- {source}：{count} 件")
    lines.extend(
        [
            "",
            "## 欄位邏輯",
            "",
            "- `case_id`：每個來源檔案的穩定識別碼。",
            "- `brand`：由檔名初步清理出的品牌或主題名。",
            "- `industry`：先用檔名關鍵字初分，後續補全時可修正。",
            "- `research_status`：目前為待最新資料補充，代表還要逐案連網查證。",
            "- `original_source_path`：原檔仍在原資料夾，不複製到知識庫。",
            "- `case_card`：待補全案例卡。",
            "",
            "## 案例清單",
            "",
            "| case_id | 品牌/主題 | 初分類 | 來源 | 檔案 | 狀態 |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        link = page_link(row["case_card"])
        brand = row["brand"].replace("|", "／")
        file_name = row["file_name"].replace("|", "／")
        lines.append(f"| [[{link}|{row['case_id']}]] | {brand} | {row['industry']} | {row['source_collection']} | `{file_name}` | {row['research_status']} |")

    lines.extend(
        [
            "",
            "## 雙向連結入口",
            "",
            "- 分類總覽：[[wiki/synthesis/品牌案例庫分類總覽]]",
            "- 補全隊列：[[wiki/cases/品牌案例補全隊列]]",
            "- 補全狀態稽核：[[wiki/cases/品牌案例補全狀態稽核]]",
            "",
            "## 補全狀態提醒",
            "",
            "截至 2026-06-05，目前 107 件皆已完成原檔摘要與資料庫化，但尚未補全最新品牌資料。不可把 `research_status: 待最新資料補充` 視為已補全。",
            "",
            "### 產業索引",
            "",
        ]
    )
    lines.extend([f"- [[wiki/cases/分類/{industry}]]" for industry in industry_links])
    lines.extend(["", "### 來源索引", ""])
    lines.extend([f"- [[wiki/cases/來源/{source}]]" for source in source_links])
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"rebuilt={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
