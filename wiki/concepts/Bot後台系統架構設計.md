---
title: "Bot後台系統架構設計 — 多Profile管理 + CRM + 客戶培育"
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [Bot後台, 多Profile管理, CRM, 客戶培育, LINE-OA, Telegram-Bot]
sources:
  - "黑獅每日萃取 — 20260710 Telegram 對話"
lion_score:
  變現價值: 5
  可複製性: 4
  長期價值: 4
  顧問可用性: 4
  內容延展性: 4
---

# Bot 後台系統架構設計 — 多 Profile 管理 + CRM + 客戶培育

## 摘要

業萱在 Telegram 上討論了一個 Bot 後台系統的設計，目標是用來管理多個 Hermes Profile（命理 Bot、AI 課 Bot、香料大叔 Bot），每個 Bot 有不同的 SOUL.md 人格、模型、Skills、群組綁定。

## 核心需求

| 項目 | 說明 |
|------|------|
| 多 Profile 管理 | 一個後台管理所有 Bot |
| 人格設定 | 每個 Bot 有獨立 SOUL.md |
| 模型切換 | 可選不同 LLM |
| Skills 管理 | 可裝卸技能模組 |
| 群組綁定 | 知道自己在哪個 LINE/TG 群組 |
| 管理員權限 | 只有管理員能改設定 |
| 回應模式 | 隨時回 / @才回 |
| 互動遊戲 | 抽牌、問答、抽獎等模組 |
| CRM | 客戶資料 + 標籤 + 購買意向 |
| 內容排程 | 定時推送知識分享/課程試讀 |

## 開發階段

| 階段 | 功能 | 難度 |
|------|------|------|
| MVP | Bot 列表 + SOUL.md 編輯 + 模型切換 | ⭐⭐ |
| v2 | 群組綁定 + 管理員權限 + 回應模式 | ⭐⭐⭐ |
| v3 | Skills 管理 + 互動遊戲模組 | ⭐⭐⭐ |
| v4 | CRM 客戶管理 + 內容排程 | ⭐⭐⭐⭐ |

## 技術實現要點

- 利用現有的 `~/.hermes/dashboard/api_server.py`（port 8765）擴充
- Bot Profile 資料讀寫 `~/.hermes/profiles/` 目錄
- SOUL.md 編輯器用網頁端直接編輯
- 群組綁定透過 Hermes Adapter 的 webhook 配置實現

## 決策記錄

- 老闆要的是「潛在客戶培育群」Bot，不是銷售 Bot
- 人格定位：AI 課助教 / 知識分享者
- 模式：混合（知識分享 + 答疑 + 課程試讀 + 互動）

## 關鍵洞察

這個架構的核心價值在於**多品牌矩陣的自動化客戶培育**。每個 Bot 代表一個品牌/產品線，但共用同一套後台管理。CRM 模組讓老闆可以看到跨品牌的客戶旅程（例如：命理 Bot 的客戶可能也是 AI 課的潛在客戶）。

## 關聯

- [[hermes-agent-overview]] — Hermes Agent 架構解析，Bot 後台建立在之上
- [[AI工具分層使用法]] — 不同 Bot 可以用不同模型（強模型做判斷、弱模型做執行）
- [[Meta Ads投放自動化架構]] — CRM 資料可反哺 Meta Ads 受眾包
- [[引流]] — Bot 後台是私域引流的重要節點

## 來源

- 對話 session: 20260710_001631_051c69de (Telegram)
- 時間: 2026-07-10 凌晨
