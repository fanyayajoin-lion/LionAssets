# 群獅靈感知識庫 Claude Code 規則

請先讀 `AGENTS.md`，並完全遵守其中的通用 AI 工作規則。本檔只補充 Claude Code 使用時的提醒。

## 必做

- 稱呼使用者為老闆。
- 任務前先讀 `index.md`。
- 依任務類型讀取相關 `workflows/` 與 `skills/`。
- 需要提示詞參考時，查 `prompts/` 目錄。
- `raw/` 不修改、不刪除、不覆蓋。
- 產出內容後必須回流到 `wiki/notes/` 或 `wiki/synthesis/`。
- 任務後更新需要的 `index.md`、`hot.md`，並 append `log.md`。
- 同一類工作出現 3 次以上，必須提名 skill candidate，等老闆確認後再寫入 `skills/`。

## 不做

- 不把 API Key、密碼、token 寫進檔案。
- 不為了分類新增過深資料夾。
- 不只摘要資料；要補上商業判斷、可複用框架與下一步。
- 不把 `outputs/` 當終點，輸出必須回流。

## Hermes / Discord / Obsidian 分工

- Hermes 是知識庫前門，負責收件、預處理、狀態回報。
- Discord 是顯示層，只顯示收件、整理、待補資料、入庫與輸出狀態，不當正式知識庫。
- Obsidian markdown 是正式知識庫，搜尋與判斷以 `index.md`、`hot.md`、`wiki/synthesis/`、`wiki/concepts/`、`wiki/notes/` 為主。
- `inbox/raw/` 完全不分類，只放 Hermes 收到但尚未整理的資料。
- `inbox/processed/` 放 AI 閱讀員整理出的老闆理解版。
- `inbox/needs-review/` 放讀不到、抓不到、OCR 失敗、需要補充的資料。
- 搜尋順序固定為：`index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed`。
- 不要先搜 `raw/`，除非需要回查原始來源。

## 其他 AI 如何往知識庫丟資料

如果你是用 Hermes Agent、OpenClaw、Codex 或其他 AI 工具，要往本知識庫丟資料，請遵守以下規則：

### 你要丟到哪？

| 你做的事情 | 丟到哪裡 | 說明 |
|-----------|---------|------|
| 收到網址、文章、YT 影片 | `inbox/raw/` | 建立 Markdown 中繼資料檔 |
| 收到截圖、圖片 | `inbox/raw/` + `assets/` | 中繼資料放 raw，圖檔放 assets |
| 收到文件（PDF、DOC） | `inbox/raw/` + `assets/` | 同上 |
| 收到社群貼文（Threads、IG、FB） | `inbox/raw/` | 貼文內容 + 原始連結 |
| 收到零散想法 | `inbox/raw/` | 用碎片接收格式 |
| 整理後的摘要、分類 | **不要寫** | 這是管理獅的職責 |
| 更新 wiki 頁面 | **不要寫** | 這是管理獅的職責 |

### 原始檔命名規則

```
inbox/raw/YYYYMMDD-HHMMSS-<短識別>.md
```

範例：
```
inbox/raw/20260706-143000-hermes-agent.md
```

### Markdown 中繼資料格式

每筆來源必須包含 YAML frontmatter：

```yaml
---
source_id: "YYYYMMDD-HHMMSS-<short-id>"
source_type: "web|social|image|document|video|note"
source_url: "原始網址"
captured_at: "ISO-8601 時間"
sha256: "檔案 SHA-256（如有附件）"
status: "received"
title: "標題"
excerpt: "一段話摘要（≤200字）"
---

## 原始內容

這裡放截取的正文、貼文內容、或附件引用說明。
```

### 附件處理

- 圖片、PDF 等附件放在 `assets/` 目錄
- 附件命名規則：`assets/YYYYMMDD-HHMMSS-<short-id>-<描述>.<副檔名>`
- 中繼資料檔中用 `attachment` 欄位引用附件路徑

### 絕對不要做的事

- ❌ 不要修改 `inbox/raw/` 裡的原始檔
- ❌ 不要直接寫入 `wiki/` 目錄
- ❌ 不要更新 `index.md`、`log.md`
- ❌ 不要執行 Git 操作
- ❌ 不要刪除任何檔案

### 簡單來說

> **你的任務：把資料原封不動丟進 `inbox/raw/`**
> **管理獅的任務：讀取、摘要、分類、寫入 wiki、更新索引**

你不需要判斷資料有沒有價值、要不要分類、怎麼連結。那些都是管理獅的工作。你只需要確保：
1. 資料完整（原文不修改）
2. 來源可追溯（網址、時間、作者）
3. 命名符合規則

### 更多資訊

詳細規則請見 `README.md` 的「其他 AI 如何補充資料進知識庫」章節。
