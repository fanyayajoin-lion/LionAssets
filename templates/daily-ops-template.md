---
playbook_type: daily_operations
version: 1.0.0
author: 業萱
created: 2026-07-09
updated: 2026-07-09
---
# 每日營運 SOP 模板

## Purpose
標準化每日營運流程，確保知識庫持續更新、碎片持續流入。

## Daily Checklist
- [ ] 檢查 inbox/raw/ 是否有新碎片
- [ ] 執行碎片接收流程（playbooks/碎片接收與入庫）
- [ ] 執行每日蒸餾（playbooks/每日蒸餾）
- [ ] 更新 index.md 和 hot.md
- [ ] append log.md
- [ ] 檢查系統健康狀態（Gateway、備份、cron）

## Weekly Checklist
- [ ] 執行每週內容工廠（playbooks/每週內容工廠）
- [ ] 執行每週復盤（wiki/workflows/每週復盤）
- [ ] 檢查 3 個月未更新的頁面
- [ ] 同步 Notion（若啟用）

## Monthly Checklist
- [ ] 執行每月整理（wiki/workflows/每月整理）
- [ ] 清理 inbox/archive/
- [ ] 備份知識庫
- [ ] 更新 skills/ 和 templates/

## Quality Standard
- 每日碎片必須在 24 小時內處理
- 每週至少產出 3 篇社群內容
- 每月至少更新 5 個知識原子

## Common Mistakes
- 碎片積壓超過一週
- 忘記更新 index.md
- 知識原子寫太長（超過 1500 字）

## Related Knowledge
- [[playbooks/碎片接收與入庫]]
- [[playbooks/每日蒸餾]]
- [[playbooks/每週內容工廠]]
