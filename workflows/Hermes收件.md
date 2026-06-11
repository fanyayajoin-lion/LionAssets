# Hermes 收件 Workflow

## 使用時機

老闆從 Telegram / Hermes Inbox 丟網址、YouTube、截圖、圖片、文章、Threads、IG、小紅書或臨時想法時使用。

## 核心原則

- Telegram / Hermes 是入口，不是正式知識庫。
- Hermes 收件後先進 `inbox/raw/`，全部不分類。
- Hermes 只回短訊息，不在 Telegram 長篇摘要。
- Discord `#inbox-log` 顯示收件狀態。

## Hermes 分流

- 問問題：Assistant Mode。
- 丟網址 / YT / 圖片 / 截圖：Inbox Mode。
- `/save`：強制存入知識庫。
- `/ask`：強制助理回答。
- `/digest`：查今日整理結果。
- `/find 關鍵字`：搜尋 Obsidian 知識庫。
- `/draft 主題`：從知識庫產內容草稿。

## 收件格式

每筆 raw item 至少保留：

```yaml
id:
received_at:
source_platform:
content_type:
source_url:
raw_text:
asset_path:
status: received
```

## 收件後回覆

Telegram 只回：

```text
已收到，已進 Inbox。今晚 23:00 會整理。
```

若明顯讀不到，回：

```text
已收到，但可能需要補資料。已放到 needs-review。
```

## 寫入位置

- 未整理資料：`inbox/raw/`
- 附件與圖片：`assets/`
- 需要補資料：`inbox/needs-review/`
