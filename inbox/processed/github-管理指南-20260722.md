---
title: "GitHub 完整管理指南"
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [github, workflow, best-practices, ci-cd, automation]
sources: [hermes-agent-skill-review, web-research-2026-07-22]
---

# GitHub 完整管理指南

## 結論先行

GitHub 對專業開發者不是「雲端硬碟」，而是**「專案操作系統」**。大神管理 GitHub 的核心就 5 件事：**結構標準化、分支策略清晰、自動化取代手動、文件即程式碼、安全控管**。

---

## 一、GitHub 功能地圖（白話版）

| 功能 | 用途 | 大神怎麼用 |
|------|------|-----------|
| **Repositories** | 專案倉庫 | 一專案一 repo，命名統一，private/public 分明 |
| **Issues** | 任務/問題追蹤 | 當看板 + 工單系統，標記 priority、type、status |
| **Projects** | 專案管理 | 類似 Trello，拖曳式看 milestone、排期、進度 |
| **Actions** | 自動化工作流 | CI/CD、自動測試、自動發版、自動備份、自動通知 |
| **Wiki** | 官方文件 | 放架構圖、API 文件、部署 SOP、決策記錄 |
| **Discussions** | 社群/提問 | 客戶或合作者交流區，不污染 code history |
| **Copilot** | AI 輔助 | 自動補碼、寫測試、解釋程式碼、提 PR 建議 |
| **Secrets** | 金鑰管理 | 放 API Key、Token，永不外洩到程式碼裡 |

---

## 二、大神管理 GitHub 的 5 個黃金法則

### 法則 1：結構標準化（不靠記憶，靠慣例）

根目錄固定放這些，任何人接手 30 秒看懂：

```
├── README.md          ← 一頁看懂：是什麼、怎麼裝、怎麼用
├── .gitignore         ← 不上傳的檔案清單
├── LICENSE            ← 授權條款
├── CHANGELOG.md       ← 版本更新紀錄
├── CONTRIBUTING.md    ← 怎麼貢獻/提交問題
├── docs/              ← 詳細文件
├── src/               ← 原始碼
├── tests/             ← 測試
└── scripts/           ← 部署/備份/工具腳本
```

### 法則 2：分支策略（小團隊選最簡單的）

| 策略 | 適用場景 | 優點 | 缺點 |
|------|---------|------|------|
| **GitHub Flow** ⭐推薦 | 一人公司、顧問、小專案 | 只有 main + feature/*，改完直接合併，靠自動化驗證 | 不適合嚴謹版本發布 |
| **GitFlow** | 產品型團隊、頻繁發版 | main/develop/release/hotfix 五層，流程嚴謹 | 分支太多，容易混亂 |
| **Trunk-Based** | 大型敏捷團隊 | 全員直接推 main，靠短分支+自動化 | 需要高度自動化支援 |

**你的情況：用 GitHub Flow 最合適。** main 永遠穩定，新功能開 `feature/xxx`，測試沒問題就合併刪除。

```bash
# 大神標準起手式
git checkout main && git pull origin main
git checkout -b feat/功能描述        # 命名規範：type/description
git push -u origin HEAD
gh pr create --title "feat: 功能描述" --body "..."
```

分支命名規範：

| 類型 | 範例 | 用途 |
|------|------|------|
| `feat/...` | `feat/add-login` | 新功能 |
| `fix/...` | `fix/login-redirect` | Bug 修復 |
| `refactor/...` | `refactor/auth-module` | 重構 |
| `docs/...` | `docs/update-readme` | 文件更新 |
| `ci/...` | `ci/add-testing` | CI/CD 變更 |

### 法則 3：自動化取代手動（大神絕不重複造輪子）

用 GitHub Actions（免費）自動做這些：

- ✅ 每次 push 自動跑 lint / 測試
- ✅ 每天定時備份到其他 repo 或 cloud storage
- ✅ 合併到 main 自動發 Telegram/Discord 通知
- ✅ 自動更新 CHANGELOG、打 Tag
- ✅ 依賴包漏洞自動開 PR（Dependabot）

**必開自動化工具：**

| 工具 | 用途 | 設定位置 |
|------|------|---------|
| **Dependabot** | 自動檢查依賴漏洞 | Settings → Code security → Dependabot alerts |
| **GitHub Actions** | 自動化備份/通知/部署 | `.github/workflows/` |
| **Projects (Beta)** | 專案看板 + 進度追蹤 | Projects → New project |
| **Pages** | 自動部署靜態網站 | Settings → Pages → Source: main/docs |

**GitHub Actions 常見自動化場景：**

| Action | 用途 |
|--------|------|
| `actions/checkout` | 取得程式碼（幾乎每個 workflow 的第一步） |
| `actions/cache` | 快取依賴，加快建置速度 |
| `github/codeql-action` | 安全漏洞掃描 |
| `docker/build-push-action` | 自動建置 Docker 映像 |
| `TimonVS/pr-labeler-action` | 根據 branch 名稱自動加標籤 |
| `probot/stale` | 自動關閉無回應的 Issues |

**CI/CD 範例：**

```yaml
# .github/workflows/ci.yml
name: CI
on:
  pull_request:
    branches: [main]
    paths: ['src/**', '.github/**']

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Cache dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
      - run: pip install -r requirements.txt
      - run: pytest --cov=src/

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ruff check .

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
      - uses: github/codeql-action/analyze@v3
```

### 法則 4：文件即程式碼（README 是操作手冊，不是名片）

大神寫的 README 一定包含：

| 段落 | 內容 |
|------|------|
| **What** | 這專案在做什麼？解決什麼問題？ |
| **Why** | 為什麼需要它？商業價值？ |
| **How to start** | 3 步內跑起來 |
| **Architecture** | 簡易架構圖或流程圖 |
| **Deployment** | 怎麼部署？環境變數？ |
| **Troubleshooting** | 常見錯誤與解法 |

**標準 README 結構（複製即用）：**

```markdown
# 專案名稱
一句話說明這專案在做什麼。

## 為什麼需要它
商業價值 / 解決什麼痛點

## 快速開始
1. 克隆 repo
2. 安裝依賴
3. 設定環境變數
4. 啟動

## 架構
[簡易圖或流程說明]

## 部署
[VPS / Firebase / 其他]

## 常見問題
[卡關解法]

## 授權
MIT
```

### 法則 5：安全與權限控管

| 措施 | 做法 |
|------|------|
| 🔑 **金鑰不外洩** | 絕不傳 Key 到 repo，用 GitHub Secrets 或 `.env`（加在 `.gitignore`） |
| 🛡️ **Dependabot** | 自動檢查套件漏洞並開 PR |
| 🔒 **Private Repo** | 商業邏輯、客戶資料一律 private |
| 👥 **Branch Protection** | main 禁止直接 push，必須經 PR |
| 📜 **Audit Log** | 所有操作留痕，方便追溯 |

```bash
# Branch Protection 設定
curl -s -X PUT \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/branches/main/protection \
  -d '{
    "required_status_checks": { "strict": true, "contexts": ["ci/test", "ci/lint"] },
    "enforce_admins": false,
    "required_pull_request_reviews": { "required_approving_review_count": 1 }
  }'
```

---

## 三、實戰操作速查表

### Commit 訊息規範（Conventional Commits）

```
type(scope): 簡短描述

較長的說明文字（可選），每行不超過 72 字
```

| type | 用途 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat(auth): add JWT login` |
| `fix` | Bug 修復 | `fix: correct redirect URL` |
| `refactor` | 重構 | `refactor(api): simplify routes` |
| `docs` | 文件 | `docs(readme): update setup guide` |
| `test` | 測試 | `test(auth): add unit tests` |
| `ci` | CI/CD | `ci: add codeql scanning` |
| `chore` | 雜項 | `chore: update dependencies` |
| `perf` | 效能 | `perf(query): add index on users` |

### PR Review 檢查清單

| 類別 | 檢查項目 |
|------|---------|
| **正確性** | 是否達成目的？邊界 case 處理了嗎？錯誤路徑有處理嗎？ |
| **安全性** | 沒有硬編密碼/API Key？使用者輸入有驗證？沒有 SQL injection/XSS？ |
| **程式品質** | 命名清楚？沒有過度抽象？DRY（不重複）？單一職責？ |
| **測試** | 新程式碼有測試嗎？Happy path 和 error case 都有？ |
| **效能** | 沒有 N+1 查詢？適當快取？沒有 blocking 操作？ |
| **文件** | Public API 有文件嗎？非直覺邏輯有註解嗎？README 要更新嗎？ |

### 倉庫管理

| 動作 | gh 命令 |
|------|---------|
| 建立公開 repo | `gh repo create my-project --public --clone` |
| 建立私有 repo | `gh repo create my-project --private --description "..." --license MIT --clone` |
| Fork | `gh repo fork owner/repo-name --clone` |
| 同步 fork | `gh repo sync $GH_USER/repo-name` |
| 編輯設定 | `gh repo edit --enable-auto-merge --enable-issues=true` |
| 查看資訊 | `gh repo view OWNER/REPO` |

### Issue 管理

| 動作 | gh 命令 |
|------|---------|
| 列出開放 issue | `gh issue list --state open --label "bug"` |
| 我的 issue | `gh issue list --assignee @me` |
| 搜尋 issue | `gh issue list --search "authentication error" --state all` |
| 建立 issue | `gh issue create --title "標題" --body "內容" --label "bug,priority:high"` |
| 加標籤 | `gh issue edit 42 --add-label "priority:high,backend"` |
| 指派 | `gh issue edit 42 --add-assignee username` |
| 留言 | `gh issue comment 42 --body "已確認，正在處理"` |
| 關閉 | `gh issue close 42` |

### Pull Request 流程

| 動作 | gh 命令 |
|------|---------|
| 建立 PR | `gh pr create --title "feat: xxx" --body "..." --reviewer user1,user2` |
| 查看 PR | `gh pr view 123` |
| 查看差異 | `gh pr diff 123` |
| 簽出 PR | `gh pr checkout 123` |
| CI 狀態 | `gh pr checks` / `gh pr checks --watch` |
| 留言 | `gh pr comment 123 --body "..."` |
| 審查 | `gh pr review 123 --approve --body "LGTM!"` |
| 要求修改 | `gh pr review 123 --request-changes --body "..."` |
| 合併 | `gh pr merge --squash --delete-branch` |
| 自動合併 | `gh pr merge --auto --squash --delete-branch` |

### Release 管理

| 動作 | gh 命令 |
|------|---------|
| 自動產生 Changelog | `gh release create v1.0.0 --generate-notes` |
| 預覽版 | `gh release create v2.0.0-rc1 --draft --prerelease` |
| 附帶檔案 | `gh release create v1.0.0 ./dist/binary --title "v1.0.0"` |
| 列出 releases | `gh release list` |

### CI/CD 管理

| 動作 | gh 命令 |
|------|---------|
| 列出 workflows | `gh workflow list` |
| 列出最近 runs | `gh run list --limit 10` |
| 查看 run | `gh run view <RUN_ID>` |
| 失敗日誌 | `gh run view <RUN_ID> --log-failed` |
| 重新執行 | `gh run rerun <RUN_ID> --failed` |

### Secrets 管理

| 動作 | gh 命令 |
|------|---------|
| 設定 secret | `gh secret set API_KEY --body "your-value"` |
| 列出 secrets | `gh secret list` |
| 刪除 secret | `gh secret delete API_KEY` |

---

## 四、大神 vs 一般用戶差異

| 維度 | 一般用戶 | 大神 |
|------|---------|------|
| **分支** | 直接在 main 改 | 每個改動獨立分支 |
| **Commit** | "update"、"fix" | Conventional Commits |
| **PR** | 幾百行大改、沒說明 | 小 PR、完整說明、關聯 Issue |
| **CI** | 沒有或手動跑 | 每個 PR 自動測試+審視 |
| **Issue** | 只寫一行描述 | 標準化模板、標籤分類 |
| **自動化** | 手動部署、手動建 PR | GitHub Actions 全自動化 |
| **安全** | Token 寫在程式碼 | GitHub Secrets |
| **文檔** | 沒有 README | README + CONTRIBUTING + CHANGELOG |

---

## 五、專案管理建議

### 命名規範

```
[領域]-[專案名]

lionbot-hermes        ← AI 課 LINE Bot
lionassets            ← 知識庫
tarot-web             ← 塔羅前端
crm-staging           ← CRM 預備版
```

### 分支策略（GitHub Flow）

```
main          ← 永遠可部署的穩定版
feature/xxx   ← 新功能/修復（合併後刪除）
```

---

## 六、下一步建議

| 選項 | 內容 | 耗時 |
|------|------|------|
| **A. 統一 README** | 把你現有 repo 全部換成標準結構 | 10 分鐘 |
| **B. 開 Dependabot** | 自動監控套件漏洞，省未來維修成本 | 2 分鐘 |
| **C. 設 GitHub Actions** | 每天自動備份 + Telegram 通知 | 15 分鐘 |
| **D. 建 Projects 看板** | 跨 repo 追蹤所有專案進度 | 5 分鐘 |
