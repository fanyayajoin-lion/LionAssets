---
title: Claude Code 快捷操作指南
created: 2026-07-01
tags: [tools, claude-code, fable-5, cost-optimization, productivity]
aliases: [CC快捷操作, Claude Code shortcuts]
---

# Claude Code 快捷操作指南

## 一、脈絡管理（最該先會，也最省錢）

你跟 AI 的對話越長，它就越慢、越貴、越容易恍神——這四個是底層心法：

### `/init`
進新專案第一件事。它會掃一遍你的 code，自動生成一份 `CLAUDE.md`（專案說明書），之後不用每次重講背景。

### `/context`
看目前脈絡用了多少（等於油表），快滿了就是該清的訊號。

### `/compact`
把長對話壓縮成摘要、但保留重點。（同一件事做很久時用）

### `/clear`
整碗倒掉、從零開始。（任務已經無關了用）

> **一句話分清楚：**
> - 需要前情提要 → `compact`
> - 不要前情提要 → `clear`

---

## 二、鍵盤快捷（比指令還常用）

| 快捷鍵 | 功能 | 時機 |
|---|---|---|
| `esc` | 喊停（它正在亂跑） | 發現它在亂做時 |
| `esc esc` | 回到上一步重來 | 做壞了的安全網 |
| `@檔名` | 直接 tag 檔案讓它讀 | 不用貼整串路徑 |
| 直接貼圖 | 截圖丟給它看 | debug 介面、讀錯誤畫面 |
| `shift + tab` | 切 Plan 計畫模式 | 大改前必開，它會先給你計畫、不直接動手，你確認方向再放行 |

---

## 三、讓它記住你（這招最多人不知道）

### `#` 開頭
在輸入框用「`#`」開頭打一句，例如：
```
# 這個專案一律用繁體中文寫註解
```
這句不會被執行，而是**存成記憶、寫進 CLAUDE.md**，之後每次自動帶入，不用再講第二次。

> 白話：`#` 開頭 ＝ 把這句記下來，不是叫它做

### `/memory`
打開那份記憶直接編輯、整理規則。

---

## 四、控制它的大腦

### `/model`
簡單任務切小模型（sonnet／haiku）省錢，難的再動用 opus。不用每件事都派最貴的腦。

### `ultrathink`
臨時把腦力開到最大、想得更深，複雜邏輯時用。
> 但只對當下這句有效，下一句就恢復正常。想整場都深思就改用 `/effort high`。

### `/effort high`
整場都開啟深度思考模式。

---

## 五、Fable 5 成本優化策略（2026-07-09 新增）

Fable 5 是最強的模型，但也最貴（$10/$50 per million tokens）。
**不一定要全程開 Fable 5**——有兩種省錢又高效的玩法。

### 方法一：Advisor 模式

```
/model sonnet
/advisor fable
（或 /advisor claude-fable-5）
```

- Sonnet 5 負責 90% 以上的實際執行
- Fable 5 只在關鍵決策、架構設計、卡關時提供建議

> **Fable 思考，Sonnet 執行。**

Anthropic SWE-bench Pro 測試：Sonnet 5 + Fable 5 Advisor ≈ Fable 5 92% 表現，成本只要 63%。

### 方法二：Orchestrator 模式

讓 Fable 5 擔任編排者（Orchestrator）：

- 規劃任務、拆解工作
- 指派給 Worker（Sonnet 5）
- 最後整合結果

大量 Token 由 Sonnet 5 消耗。

Anthropic BrowseComp 測試：Fable 5（Orchestrator）＋ Sonnet 5（Worker）→ 96% Fable 5 效果，成本只要 46%。

> **🧠 Fable 負責想，⚙️ Sonnet 負責做**

### 實踐方式

**方式 A：Custom Command**

建立 `~/.claude/commands/orchestrator.md`，內容讓 Claude 進入 Orchestrator 模式：

- 負責整體規劃與拆解
- 執行工作委派給 Sub-agents / Workers
- 最後負責審核與整合
- 優先使用低成本模型完成細節
- 保持 Context 精簡

使用：`/orchestrator 幫我做登入功能`

**方式 B：寫進 CLAUDE.md 預設**

在專案的 `CLAUDE.md` 加上：

```markdown
## 預設工作模式：Orchestrator
你預設使用 Orchestrator 模式：
- 你負責整體規劃、任務拆解、委派與最終審核
- 把執行細節委派給子代理（worker），優先使用 Sonnet 5 等低成本模型
- 保持上下文精簡，只保留重要決策與總結
- 每個子任務都要明確定義驗收標準
- 盡量平行委派加速
```

### 關聯知識

- [[wiki/concepts/AI蒸餾與分層使用法]] — 強模型做判斷、弱模型做執行
- [[wiki/concepts/AI個人作業系統架構]] — Fable 5 五步驟建構
- [[wiki/concepts/AI一人公司與蒸餾人物Skill]] — 蒸餾人物 Skill 技術

---

## 六、收尾與求救

### `/code-review`
改完讓它幫你抓 bug、可讀性、資安問題——等於免費請一個 reviewer。

### `/help`
忘了就按，列出全部指令。

---

## 七、新手必練四組反射

```
init 開場 → context 看油表 → compact/clear 收尾 → esc esc 當保險
```

**最被低估的兩招：**
- `#` 開頭存記憶
- `shift + tab` 先看計畫

---

## 八、速查表

| 需求 | 指令 |
|---|---|
| 開新專案 | `/init` |
| 看剩多少空間 | `/context` |
| 壓縮對話 | `/compact` |
| 清空重來 | `/clear` |
| 喊停 | `esc` |
| 重做上一步 | `esc esc` |
| 讓它讀檔案 | `@檔名` |
| 看圖 | 貼圖 |
| 先計畫再執行 | `shift + tab` |
| 記下規則 | `#規則內容` |
| 編輯記憶 | `/memory` |
| 省錢切模型 | `/model` |
| 單次深思 | `ultrathink` |
| 整場深思 | `/effort high` |
| 改完檢查 | `/code-review` |
| 忘記指令 | `/help` |
