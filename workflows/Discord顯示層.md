# Discord 顯示層 Workflow

## 使用時機

Hermes 收件、AI 閱讀、知識入庫、每週輸出或系統錯誤時，用 Discord 顯示狀態。

## 核心原則

- Discord 是顯示層，不是正式知識庫。
- Discord 不做分類決策。
- Discord 讓老闆看得到系統處理到哪。

## 頻道

- `#inbox-log`：今天 Hermes 收到什麼。
- `#daily-digest`：晚上 AI 閱讀員整理結果。
- `#needs-review`：讀不到、抓不到、需要補資料。
- `#knowledge-updates`：今天新增到 Obsidian 的 note / concept / synthesis。
- `#weekly-output`：每週產出的 Threads、FB、IG 輪播草稿。
- `#hermes-errors`：系統錯誤、API 失敗、排程失敗。

## 顯示格式

### inbox-log

```text
已收到：網頁文章
標題：...
來源：Telegram
狀態：待晚上整理
```

### daily-digest

```text
今日整理完成：7 筆
高價值：3 筆
需人工確認：1 筆
已寫入 Obsidian：2 筆
```

### needs-review

```text
YouTube transcript 抓不到
來源：...
建議：請補文字摘要或換一個連結
```

## 不做

- 不把 Discord 當 raw 資料庫。
- 不把 Discord 當 Obsidian 替代品。
- 不在 Discord 裡建立正式分類。
