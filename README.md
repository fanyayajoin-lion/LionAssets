# 群獅靈感知識庫

這是群獅的 Codex + Obsidian 通用自生長知識庫，不綁單一 LLM。Codex、Claude Code 或其他 AI 只要讀到 `AGENTS.md` / `CLAUDE.md`，就能理解規則並接手。

核心流程：

```text
靈感收集 -> 原始保存 -> AI 補全 -> 知識整理 -> 商業蒸餾 -> Lion Score 評分 -> 輸出 -> 回流 -> 沉澱成 Skill / Asset / Memory
```

## 資料夾

- `raw/`：原始資料，不修改、不刪除。
- `wiki/`：AI 整理後的知識層。
- `wiki/concepts/`：框架、方法論、商業洞察。
- `wiki/entities/`：人、品牌、工具、客戶、平台。
- `wiki/notes/`：單篇資料摘要。
- `wiki/cases/`：品牌案例與商業模式拆解。
- `wiki/synthesis/`：跨來源蒸餾、決策結晶。
- `workflows/`：每日蒸餾、剪藏、新聞雷達、品牌案例補全等流程。
- `skills/`：可重複調用的能力。
- `outputs/`：文章、PPT、圖片提示詞、影片腳本等產出。
- `assets/`：圖片、附件、PPT、影片素材。
- `archive/`：舊資料與歷史備份。

## AI 使用方式

1. 任務前先讀 `index.md`。
2. 需要處理品牌案例時，依 `workflows/品牌案例補全歸檔.md`。
3. 任務後更新 `index.md`、`hot.md`，並 append `log.md`。
4. 同一主題重複出現三次以上，必須判斷是否升級為 Skill、Asset 或 Memory。

