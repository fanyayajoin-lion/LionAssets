from __future__ import annotations

import csv
import hashlib
import html
import re
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


WORKSPACE = Path.cwd()
BATCH_DATE = "2026-06-05"

SOURCES = [
    ("其他人品牌", Path(r"C:\Users\Administrator\Desktop\新增資料夾\DFP重新整理\講師_運營\課件\其他人品牌")),
    ("晨訓商模-自己", Path(r"C:\Users\Administrator\Desktop\新增資料夾\DFP重新整理\講師_運營\課件\晨訓商模-自己")),
    ("8點通-自品牌", Path(r"C:\Users\Administrator\Desktop\新增資料夾\DFP重新整理\講師_運營\課件\8點通\自品牌")),
]


@dataclass
class CaseFile:
    case_id: str
    brand: str
    industry: str
    source_collection: str
    source_path: Path
    file_name: str
    extension: str
    size_bytes: int
    last_modified: str
    case_card: str
    slide_count: int | str
    extracted_summary: str


def clean_brand_name(name: str) -> str:
    base = Path(name).stem
    replacements = [
        (r"^OK品牌[-_ ]*", ""),
        (r"^0品牌[-_ ]*", ""),
        (r"^品牌[-_ ]*", ""),
        (r"^\d{3,4}[-_ ]*", ""),
        (r"^\d+[.]\d+", ""),
        (r"（.*?）", ""),
        (r"\(.*?\)", ""),
        (r"-晨訓版更新", ""),
        (r"-晨訓版", ""),
        (r"-晨訓", ""),
        (r"-錄影版.*$", ""),
        (r"-錄影$", ""),
        (r"-錄$", ""),
        (r"晨會版更新", ""),
        (r"_final", ""),
        (r"2[.]0$", ""),
    ]
    for pattern, repl in replacements:
        base = re.sub(pattern, repl, base, flags=re.IGNORECASE)
    base = base.strip(" -_　")
    return base or Path(name).stem


def guess_industry(brand: str, name: str, source: str, ext: str) -> str:
    text = f"{brand} {name}"
    if ext in {".jpg", ".jpeg", ".png", ".mp4"}:
        return "素材輔助"
    if source == "8點通-自品牌":
        return "自品牌案例"
    if re.search(r"辣|雞|鴨|生煎|磨房|買菜|香瓜子|糖水|KFC|海天|茶|沙拉|麵包|好利來|紫燕|衛龍|外婆家|譚鴨血|小菜園|西貝|盼盼|熊大爺|咖啡|肆拾玖坊|十月稻田|溜溜梅|古茗|簡愛|莫小仙|認養一頭牛|虎邦", text, re.I):
        return "食品餐飲品牌"
    if re.search(r"韓都|GAP|HFP|SPANX|Tory|話梅|FANCL|Stitch|lclcle|小仙燉|服裝|美妝", text, re.I):
        return "服飾美妝品牌"
    if re.search(r"抖音|淘寶|蝦皮|Tokopedia|Udaan|山姆|麥德龍|易捷|Thrasio|粉象|電商|零售", text, re.I):
        return "零售平台電商"
    if re.search(r"小熊|熊小夕|蔚來|傳音|任天堂|roblox|快看|Yalla|比心|OYO|自如|Getir|Classpass|Curves|HIPCAMP|SWVL|UO|TOPTOY|周大福|倍輕鬆", text, re.I):
        return "生活科技服務"
    return "需人工確認"


def case_id(source: str, brand: str, name: str) -> str:
    raw = f"{source}-{brand}-{name}".encode("utf-8")
    return f"case-{hashlib.sha1(raw).hexdigest()[:8]}"


def extract_pptx(path: Path) -> tuple[int, list[str]]:
    texts: list[str] = []
    with zipfile.ZipFile(path) as zf:
        slides = []
        for name in zf.namelist():
            match = re.match(r"ppt/slides/slide(\d+)\.xml", name)
            if match:
                slides.append((int(match.group(1)), name))
        for slide_no, slide_name in sorted(slides):
            xml = zf.read(slide_name).decode("utf-8", errors="ignore")
            parts = [html.unescape(t).strip() for t in re.findall(r"<a:t>(.*?)</a:t>", xml)]
            line = " / ".join([p for p in parts if p])
            if line:
                texts.append(f"Slide {slide_no}: {line}")
        return len(slides), texts


def extract_docx(path: Path) -> tuple[str, list[str]]:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
    parts = [html.unescape(t).strip() for t in re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml)]
    text = " ".join([p for p in parts if p])
    return "docx", split_text(text)


def extract_pdf(path: Path) -> tuple[str, list[str]]:
    try:
        from pypdf import PdfReader
    except Exception:
        return "pdf", ["PDF 文字抽取套件不可用，需後續人工或工具補抽。"]
    reader = PdfReader(str(path))
    lines = []
    for idx, page in enumerate(reader.pages[:20], 1):
        text = page.extract_text() or ""
        if text.strip():
            lines.append(f"Page {idx}: {one_line(text)}")
    return str(len(reader.pages)), lines


def one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_text(text: str) -> list[str]:
    compact = one_line(text)
    if not compact:
        return []
    return [compact[i : i + 500] for i in range(0, min(len(compact), 3000), 500)]


def extract_summary(path: Path) -> tuple[int | str, str]:
    ext = path.suffix.lower()
    try:
        if ext == ".pptx":
            count, lines = extract_pptx(path)
        elif ext == ".docx":
            count, lines = extract_docx(path)
        elif ext == ".pdf":
            count, lines = extract_pdf(path)
        else:
            return "素材", "此檔案是圖片、影片或非文字素材，需作為品牌案例輔助素材連回相關 output。"
    except Exception as exc:
        return "需重抽", f"文字抽取失敗：{exc}"

    useful = []
    for line in lines:
        compact = one_line(line)
        if compact and compact not in useful:
            useful.append(compact)
        if len(useful) >= 12:
            break
    return count, "\n".join(f"- {line[:700]}" for line in useful) or "未抽取到可用文字，需人工或 OCR 補充。"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_case_card(row: CaseFile) -> None:
    path = WORKSPACE / row.case_card
    path.parent.mkdir(parents=True, exist_ok=True)
    body = f"""---
type: brand_case_intake
case_id: {row.case_id}
brand: {yaml_quote(row.brand)}
industry: {yaml_quote(row.industry)}
source_collection: {yaml_quote(row.source_collection)}
source_file: {yaml_quote(row.file_name)}
original_source_path: {yaml_quote(str(row.source_path))}
original_case_year: 待判定
last_updated: 2026-06-05
research_status: 待最新資料補充
archive_status: 原檔保留在原路徑，未複製進知識庫
lion_score:
  變現價值:
  可複製性:
  長期價值:
  顧問可用性:
  內容延展性:
---

# {row.brand}

## 資料庫狀態

- 案例 ID：`{row.case_id}`
- 原始檔案路徑：`{row.source_path}`
- 來源批次：{row.source_collection}
- 檔案類型：`{row.extension}`
- 頁數/素材狀態：{row.slide_count}
- 狀態：已抽取原檔重點，待連網補最新資料後歸檔

## 原檔重點摘要

{row.extracted_summary}

## 最新資料補充

待連網查證後補上。必須補品牌現況、營收/融資/IPO/門市/會員/通路、產品線、私域/自媒體/直播/電商策略、AI 或數位化應用，以及可查證來源。

## 商業模式拆解

- 引流：待補充
- 截流：待補充
- 回流：待補充
- 裂變：待補充

## 可延伸商業應用

- 顧問應用：待補充
- 課程應用：待補充
- 自媒體內容：待補充
- AI 系統建置：待補充

## 待辦

- [ ] 補品牌最新狀態與來源
- [ ] 建立或更新 `wiki/entities/品牌名.md`
- [ ] 歸檔到正式產業分類
- [ ] 蒸餾到 `wiki/synthesis/`
- [ ] 更新 `hot.md` 與 `log.md`
"""
    path.write_text(body, encoding="utf-8")


def build_database(rows: list[CaseFile]) -> None:
    db_dir = WORKSPACE / "wiki" / "cases" / "database"
    db_dir.mkdir(parents=True, exist_ok=True)
    csv_path = db_dir / "品牌案例資料庫.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "case_id",
                "brand",
                "industry",
                "source_collection",
                "file_name",
                "extension",
                "size_bytes",
                "last_modified",
                "original_source_path",
                "case_card",
                "research_status",
                "archive_status",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "case_id": row.case_id,
                    "brand": row.brand,
                    "industry": row.industry,
                    "source_collection": row.source_collection,
                    "file_name": row.file_name,
                    "extension": row.extension,
                    "size_bytes": row.size_bytes,
                    "last_modified": row.last_modified,
                    "original_source_path": str(row.source_path),
                    "case_card": row.case_card,
                    "research_status": "待最新資料補充",
                    "archive_status": "原檔未複製",
                }
            )

    lines = [
        "# 品牌案例資料庫",
        "",
        "這是品牌案例批次讀取後的資料庫索引。原檔仍保留在老闆原本資料夾，知識庫只保存抽取摘要、原路徑、補全狀態與後續歸檔卡。",
        "",
        "## 統計",
        "",
        f"- 建立日期：{BATCH_DATE}",
        f"- 檔案總數：{len(rows)}",
    ]
    for source in sorted(set(row.source_collection for row in rows)):
        count = sum(1 for row in rows if row.source_collection == source)
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
            "- `case_card`：案例卡。",
            "",
            "## 案例清單",
            "",
            "| case_id | 品牌/主題 | 初分類 | 來源 | 檔案 | 狀態 |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        link = row.case_card.removesuffix(".md")
        brand = row.brand.replace("|", "/")
        file_name = row.file_name.replace("|", "/")
        lines.append(f"| [[{link}|{row.case_id}]] | {brand} | {row.industry} | {row.source_collection} | `{file_name}` | 待最新資料補充 |")
    (WORKSPACE / "wiki" / "cases" / "品牌案例資料庫.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_synthesis(rows: list[CaseFile]) -> None:
    lines = [
        "# 品牌案例庫分類總覽",
        "",
        "## 目前資料庫邏輯",
        "",
        "這批資料採用「原路徑引用 + 原檔摘要 + 案例卡 + 資料庫索引」四層管理：",
        "",
        "1. 原檔保留在老闆原本資料夾，不複製進知識庫。",
        "2. 每個檔案都有一張 `wiki/cases/案例庫/` 案例卡。",
        "3. `wiki/cases/品牌案例資料庫.md` 作為 Obsidian 查詢入口。",
        "4. `wiki/cases/database/品牌案例資料庫.csv` 作為表格資料庫。",
        "",
        "## 初始分類統計",
        "",
    ]
    for industry in sorted(set(row.industry for row in rows)):
        count = sum(1 for row in rows if row.industry == industry)
        lines.append(f"- {industry}：{count} 件")
    lines.extend(
        [
            "",
            "## 後續補全順序建議",
            "",
            "1. 先補老闆已經常用、可直接變現的餐飲食品案例。",
            "2. 再補可做傳產轉型對照的零售平台與生活服務案例。",
            "3. 最後補國際品牌與素材輔助檔。",
            "",
            "## 商業使用方向",
            "",
            "- 顧問案：用案例對照老闆的引流、截流、回流、裂變缺口。",
            "- 課程：把同類案例蒸餾成模組，例如會員制、私域、單品爆款、多品牌矩陣。",
            "- 自媒體：從高 Lion Score 案例產出文章與短影音題目。",
            "- AI 系統：把重複拆解流程沉澱成品牌案例補全 Skill。",
        ]
    )
    (WORKSPACE / "wiki" / "synthesis" / "品牌案例庫分類總覽.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_once(path: Path, marker: str, content: str) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in current:
        with path.open("a", encoding="utf-8") as f:
            f.write(content)


def main() -> int:
    rows: list[CaseFile] = []
    (WORKSPACE / "wiki" / "cases" / "案例庫").mkdir(parents=True, exist_ok=True)

    for source, root in SOURCES:
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            stat = path.stat()
            brand = clean_brand_name(path.name)
            ext = path.suffix.lower()
            industry = guess_industry(brand, path.name, source, ext)
            cid = case_id(source, brand, path.name)
            slide_count, summary = extract_summary(path)
            card = f"wiki/cases/案例庫/{cid}.md"
            row = CaseFile(
                case_id=cid,
                brand=brand,
                industry=industry,
                source_collection=source,
                source_path=path,
                file_name=path.name,
                extension=ext,
                size_bytes=stat.st_size,
                last_modified=datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                case_card=card,
                slide_count=slide_count,
                extracted_summary=summary,
            )
            rows.append(row)
            write_case_card(row)

    rows.sort(key=lambda row: (row.source_collection, row.industry, row.brand, row.file_name))
    build_database(rows)
    write_synthesis(rows)

    append_once(
        WORKSPACE / "index.md",
        "## 品牌案例資料庫",
        """

## 品牌案例資料庫

- [[wiki/cases/品牌案例資料庫]]
- [[wiki/synthesis/品牌案例庫分類總覽]]
- CSV 資料庫：`wiki/cases/database/品牌案例資料庫.csv`
- 案例卡：`wiki/cases/案例庫/`
- 原檔策略：保留原路徑，不複製進知識庫。
""",
    )
    append_once(
        WORKSPACE / "hot.md",
        "## 品牌案例批次整理",
        """

## 品牌案例批次整理

- 2026-06-05 已讀取 107 個品牌案例相關檔案，未複製原檔。
- 優先補全：食品餐飲品牌、自品牌案例、可直接轉顧問工具的案例。
- 待回流：補全後要更新 `wiki/synthesis/品牌案例庫分類總覽.md`。
""",
    )
    append_once(
        WORKSPACE / "log.md",
        "## 2026-06-05 品牌案例批次整理",
        """

## 2026-06-05 品牌案例批次整理

- 從三個來源資料夾讀取 107 個檔案，未複製原始檔。
- 建立 `wiki/cases/品牌案例資料庫.md` 與 `wiki/cases/database/品牌案例資料庫.csv`。
- 為每個來源檔案建立 `wiki/cases/案例庫/` 案例卡，內含原檔抽取摘要與原始路徑。
- 建立 `wiki/synthesis/品牌案例庫分類總覽.md`。
- 本輪已完成資料庫化與原檔摘要；最新資料補充需逐案連網查證。
""",
    )
    print(f"indexed={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
