---
title: "Jarvis Pocket Pet AI 寵物規格書 — API 策略決策"
date: 2026-07-24
source: "黑獅每日萃取 — CLI 對話"
tags: [daily-extract, 黑獅, Pocket-Pet, API策略, OmniRoute]
---

# Jarvis Pocket Pet AI 寵物規格書 — API 策略決策

## 摘要

2026-07-24 在 Jarvis Pocket Pet（口袋寵物 AI）專案規格書撰寫過程中，針對 AI API 策略做出重要決策：放棄直接呼叫 Gemini/OpenAI API，改為「Agnes AI（Hermes Gateway）主力 + OmniRoute 備用」的雙層架構。

## 關鍵決策記錄

### DEC_004：API 策略調整

| 項目 | 內容 |
|------|------|
| **決策編號** | DEC_004 |
| **日期** | 2026-07-24 |
| **主題** | Pocket Pet AI 的 API 路由策略 |
| **結論** | Agnes AI（Hermes Gateway）為主力，OmniRoute 為備用 |

### 決策理由

1. **Agnes AI 已內建在 Hermes Agent 環境** — 不需要額外申請 API Key，穩定、快速、中文支援良好
2. **OmniRoute 免費層可當故障轉移** — VPS 部署 OmniRoute（localhost:20128），自動切換免費層級模型（Gemini/GPT-5/Qwen）
3. **成本結構優化** — Phase 1 先用 Agnes（$0），Phase 2 再上 OmniRoute 備援（$0 免費層）

### 技術架構變更

**改前：**
- 日常對話 → Gemini 1.5 Flash（免費）
- 複雜問題 → GPT-4o / Claude
- 需要額外申請 API Key

**改後：**
- 日常對話 → Agnes AI（Hermes Gateway），主力，已內建
- 備用回應 → OmniRoute 免費層，故障轉移
- 複雜問題 → GPT-4o / Claude（不變）

## 可複製性評估

**適用場景：** 任何需要低成本的 AI App 開發
- 適合一人公司或 MVP 階段
- 適合已有 Hermes Agent 基礎設施的團隊
- 適合需要中文支援的應用

**不適用場景：**
- 需要高併發量（OmniRoute 免費層有速率限制）
- 需要特定模型的專屬功能

## 相關檔案

- `inbox/raw/2026-07-24-jarvis-pocket-pet-spec.md` — Pocket Pet 規格書（已更新）
- GitHub：https://github.com/fanyayajoin-lion/LionAssets/commit/521f2fa

## 來源

- 來源：CLI 對話（session 20260721_192942_77eb4f）
- 查證日期：2026-07-24
- 可信度：A（直接決策記錄）
