# 標籤索引（Tag Index）

> 每個標籤都是一個可點擊的連結，指向對應的 wiki 頁面。
> 新標籤出現時，先檢查是否已有對應頁面；沒有則建立。

## 工具與平台

- [[標籤/GPT]] — OpenAI GPT 系列模型使用心得、比較、技巧
- [[標籤/Codex]] — OpenAI Codex CLI 使用心得、與 GPT 的差異
- [[標籤/Anthropic/Claude]] — Anthropic Claude 系列模型使用心得
- [[標籤/Hermes]] — Hermes Agent 框架
- [[標籤/Obsidian]] — Obsidian 知識庫工具
- [[標籤/Antigravity]] — Antigravity AI Agent 工具
- [[標籤/WordPress]] — WordPress 網站建置與外掛
- [[標籤/Telegram]] — Telegram 社群與機器人
- [[標籤/Coze]] — 扣子 Coze 無代碼 AI 平台
- [[標籤/Dify]] — Dify AI 應用平台
- [[標籤/FastGPT]] — FastGPT 無代碼 AI 平台

## 商業模式

- [[標籤/引流]] — 引流策略與案例
- [[標籤/截流]] — 截流策略與案例
- [[標籤/回流]] — 回流策略與案例
- [[標籤/裂變]] — 裂變策略與案例
- [[標籤/私域]] — 私域流量經營
- [[標籤/會員制]] — 會員制模式
- [[標籤/一人公司]] — OPC 一人公司
- [[標籤/品牌案例]] — 品牌案例拆解

## 技術概念

- [[標籤/Agent]] — AI Agent 相關
- [[標籤/蒸餾]] — AI 蒸餾技術（模型壓縮、知識萃取）
- [[標籤/Skill]] — AI Skill 架構與沉澱
- [[標籤/提示詞]] — Prompt Engineering
- [[標籤/LLM]] — 大型語言模型
- [[標籤/知識圖譜]] — Knowledge Graph
- [[標籤/自動化]] — 工作流程自動化

## 人物與品牌

- [[標籤/電腦王阿達]] — koc.com.tw 科技媒體
- [[標籤/陳修平]] — 蒸餾對象
- [[標籤/Harry]] — 《我媽叫我不要創業》執行長
- [[標籤/Zoe]] — 《每日一錠》創辦人
- [[標籤/香料大叔]] — 堉華生技食品品牌

## 內容與教學

- [[標籤/課程]] — 課程開發與架構
- [[標籤/自媒體]] — 自媒體經營
- [[標籤/Threads]] — Threads 平台
- [[標籤/YouTube]] — YouTube 內容經營

## 分類規則

1. **標籤格式：** `[[標籤/標籤名稱]]`
2. **標籤頁面位置：** `wiki/標籤/` 目錄
3. **標籤頁面內容：** 不寫長文，只放：
   - 標籤定義（1-2 行）
   - 關聯頁面列表（auto-generated 或手動更新）
   - 最近相關文章
4. **新標籤出現時：**
   - 先搜尋是否已有對應頁面
   - 沒有則在 `wiki/標籤/` 建立標籤頁
   - 在本文的標籤索引中新增連結
5. **標籤頁面本身也要有 frontmatter：**
   ```yaml
   ---
   title: 標籤名稱
   type: tag
   related: [相關頁面列表]
   articles: [相關文章列表]
   ---
   ```
