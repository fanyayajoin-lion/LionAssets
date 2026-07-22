---
title: "OmniRoute 開源免費 AI 閘道研究"
date: 2026-07-21
source: "黑獅每日萃取 — Telegram 即時對話"
tags: [daily-extract, 黑獅, 工具研究, AI-Gateway, OmniRoute, API成本]
---

# OmniRoute 開源免費 AI 閘道研究

## 來源
- 抖音/TikTok 影片（帳號 l.l.e.o.e.e，驗證帳號）
- GitHub: `diegosouzapw/OmniRoute`
- 老闆於 2026-07-21 19:30 透過 Telegram 分享截圖並要求搜尋

## 快速摘要

**一個 endpoint 串接 250+ AI 供應商**的開源免費 AI 閘道。

## 核心功能

### 供應商與成本
- **90+ 免費層級**供應商
- **11 個永久 $0 供應商**：Kiro、Qoder、LongCat、Pollinations、Qwen、Cloudflare、Groq、NVIDIA、Scaleway、Cerebras 等
- Token 壓縮可省 15-95%

### 路由策略（18 種）
- 優先權路由
- 輪詢路由
- 成本優化路由
- 自動智能路由
- 延遲最低路由
- 成功率最高路由
- 混合策略路由
- ...等共 18 種

### 相容性
- 支援 Claude Code、Codex、Cursor、OpenClaw 等 14+ CLI 工具
- 內建 MCP 伺服器（25 種工具）
- 支援 A2A 協議

## 對群獅的價值評估

### 直接應用 ✅
1. **省 API 成本**：如果我們的多個 Agent（蝦趴獅、管理獅、彩綺）都用不同供應商，OmniRoute 可以統一路由、自動選最便宜/最快的
2. **免費層級足夠日常使用**：Groq、Qwen、Cloudflare 都有免費額度
3. **Token 壓縮**：長對話場景可顯著降低成本

### 間接應用 ⚠️
1. **客戶方案選項**：顧問服務中可以推薦給客戶作為成本控制方案
2. **課程素材**：AI 成本優化是一個實戰話題，適合放在實體課中

### 風險 / 待確認
- [ ] 需要實際部署測試，確認穩定性
- [ ] 250+ 供應商的真實可用性待驗證（有些可能是轉調其他免費層級）
- [ ] 與現有 Hermes Agent 的整合方式需研究
- [ ] 安全考量：API Key 集中管理，一旦 OmniRoute 出問題會影響所有供應商

## 行動建議

**優先級：中**

理由：對我們有實際省錢價值，但不急。建議先在小規模場景（如儀表板 API 呼叫）試用，確認穩定後再考慮全面接入。
