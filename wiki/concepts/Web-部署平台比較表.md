---
title: Web 部署平台比較表
created: 2026-07-17
updated: 2026-07-17
type: concept
tags: [web-deployment, platform-comparison, cloudflare, github-pages, netlify, vercel, supabase, zeabur]
sources:
  - telegram-image-2026-07-17
lion_score:
  變現價值: 3
  可複製性: 5
  長期價值: 4
  顧問可用性: 4
  內容延展性: 4
---

# Web 部署平台比較表

> 一張表看懂差異：把幾個常見選項放在一起比較。

## 總覽

| 平台 | 最適合 | 不適合 | 白話判斷 |
|------|--------|--------|----------|
| **Cloudflare Pages / Workers** | 靜態站、Edge Function、小型 API、全球快取 | 傳統長時間後端、完整資料庫堆疊、複雜服務編排 | 便宜又強，但你要接受 Cloudflare 的開發模型 |
| **GitHub Pages** | 文件站、作品集、開源專案頁 | 後端、私有商業工具、需要資料庫的產品 | 最像免費公告欄，不能期待它變雲端主機 |
| **Netlify** | 靜態站、Jamstack、Deploy Preview、表單、前端團隊協作 | 常駐後端、Bot、自架資料庫、多服務編排 | 比 GitHub Pages 完整，比 Zeabur 更偏前端與靜態部署 |
| **Vercel** | 前端產品、Serverless API、Preview Deploy、前端團隊協作 | 長時間常駐服務、Bot、自己管理多個資料庫服務 | 前端部署體驗天花板，但後端持久化通常要搭別人 |
| **Supabase** | Postgres、Auth、Storage、Realtime、Edge Functions | 跑任意 Docker app、n8n、Ghost、常駐 Bot、多服務編排 | 它是很好的資料庫後端，不是萬用部署平台 |
| **Zeabur** | 多服務專案、資料庫、Bot、n8n、Ghost、私有工具、多語言 | 純靜態站、極大規模、需要精細 Kubernetes / Cloudflare Workers 編排 | 不是最便宜的 VPS，是把 VPS 和部署管理做得很方便 |

## 分類歸納

### 靜態站 / 前端部署型
- GitHub Pages：最基礎免費方案，適合文件與作品集
- Netlify：功能較完整，支援表單、Deploy Preview
- Vercel：前端體驗最佳，Serverless API 整合好
- Cloudflare Pages：全球 CDN + Edge Functions，便宜且快

### 後端 / BaaS 型
- Supabase：Postgres 為核心，附帶 Auth、Storage、Realtime

### 全功能 / 多服務部署型
- Zeabur：類似 VPS 但部署管理更方便，支援 Docker、資料庫、Bot

## 決策參考

- **純靜態站** → GitHub Pages（最簡單）或 Netlify/Vercel（功能更多）
- **需要 Serverless API** → Vercel 或 Cloudflare Workers
- **需要資料庫 + Auth** → Supabase
- **多服務 / Docker 部署** → Zeabur
- **全球低延遲 + 低成本** → Cloudflare

## 關聯

- [[AI 工具鏈與基礎設施]] — 老闆的工具鏈全景
- [[好用的工具型網站推薦]] — 其他工具推薦
