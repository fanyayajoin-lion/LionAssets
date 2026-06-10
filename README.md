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
- `wiki/synthesis/`：跨來源蒸餾、決策結晶。
- `workflows/`：每日蒸餾、週報、剪藏、新聞雷達、output 回流等流程。
- `skills/`：可重複調用的能力卡。
- `outputs/`：文章、PPT、圖片提示詞、影片腳本、HTML 復盤看板等產出。
- `assets/`：圖片、附件、PPT、影片素材。
- `archive/`：舊 LionAssets 備份與歷史封存。

## AI 使用方式

1. 先讀 `AGENTS.md` 與 `index.md`。
2. 判斷任務類型，讀取對應 workflow 或 skill。
3. 需要最新資料時連網查證並保留來源。
4. 把原始資料放在 `raw/`，整理成果放在 `wiki/`，對外產出放在 `outputs/`。
5. 任務結束前更新 `index.md`、`hot.md`，並 append `log.md`。

## GitHub

遠端：`https://github.com/fanyayajoin-lion/LionAssets`

覆蓋推送前，先把遠端舊內容備份到 `archive/`。
