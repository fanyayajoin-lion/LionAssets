---
title: Meta Ads 投放自動化架構
created: 2026-07-09
updated: 2026-07-09
type: concept
tags: [工具/Meta, 工具/Claude Code, 自動化, 廣告投放, MCP]
sources: [inbox/raw/20260709-002000-MetaAds自動化架構.md]
aliases: [Meta Ads 自動化, 廣告投放自動化, Meta Ads MCP]
---

# Meta Ads 投放自動化架構

## 核心概念

用 Claude Code 串 Meta Ads 的 MCP（Model Context Protocol），打造從數據分析到廣告上架的全自動化流程。

## 五步自動化流程

### ① 看帳號狀況

AI 透過 MCP 拉 insights、帳戶活動，自動整理：

- 哪支廣告在燒錢
- 哪支該加碼
- 不用手動開一堆報表

### ② 找落地連結

AI 直接爬整個網站：

- 自動找到對應的產品頁
- 確認要導的 CTA
- 打包成短網址

> **實作註記：** 老闆有自己的短網址 hub，但加速上線階段可用有 API 的 LiHi。

### ③ 本地選圖

- 素材放本地
- 人工 + AI 共同判圖
- 第一關標準：有沒有把主打賣點呈現出來
- 原生素材多，流程中也要自動優化選圖裁圖技巧

### ④ GCS 掛圖床

- 選好的圖上傳 Google Cloud Storage（GCS bucket）
- 自動生出公開 URL
- 有穩定的圖片網址，後面才能全程走 API

### ⑤ 回丟 Meta 建素材

- 拿 GCS 的 URL 建 creative、上廣告
- 整條龍不用手動搬圖

## 自動化邊界設定

在 AI 對談過程中，順便把決策規則寫成 MD 文件：

- 什麼時間點關廣告
- 什麼時候加預算
- 什麼時候換素材

每天快速掃一次，漸次 update MD，一兩周就可以達到非常穩定的狀態。

## 進階：Marketing API

當發現 MCP 有侷限時，把 Marketing API 放進來一起協作。

## 關鍵技術堆疊

| 元件 | 用途 |
|---|---|
| Claude Code | 流程編排 + AI 決策 |
| Meta Ads MCP | 串接 Meta 廣告數據 |
| GCS Bucket | 圖床，自動生成公開 URL |
| 短網址 API | 自有 hub 或 LiHi |
| MD 決策文件 | 自動化邊界設定 |

## 關聯知識

- [[wiki/tools/claude-code-shortcuts]] — Claude Code 快捷操作 + Fable 5 成本優化
- [[wiki/concepts/AI蒸餾與分層使用法]] — 強模型做判斷、弱模型做執行
- [[wiki/concepts/AI一人公司與蒸餾人物Skill]] — 蒸餾人物 Skill 技術
- [[wiki/concepts/AI工具分層使用法]] — GPT vs Codex 分工策略
