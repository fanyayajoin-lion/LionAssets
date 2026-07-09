# knowledge/ — 知識原子庫

## 定位
給 LLM 讀的知識原子。每個文件只講一件事，可獨立理解、可被 Skill 引用。

## 與 wiki/ 的區別
- **wiki/**：給人類閱讀的完整知識庫，包含案例、實體、筆記
- **knowledge/**：給 AI 閱讀的知識原子，萃取核心框架和方法論

## 文件結構
每個知識原子包含：
- `title`：知識原子名稱
- `type`：knowledge_atom
- `domain`：領域分類（strategy/framework/tactics）
- `source`：來源文件連結
- `tags`：標籤
- 核心命題：一句話總結
- 模型/框架：結構化的知識內容
- 關聯：與其他知識原子的連結

## 當前知識原子清單

### 策略類（strategy）
- [[knowledge/ai-five-stages]] — AI 五階段演進模型
- [[knowledge/ai-talent-replication]] — AI 人才複製框架
- [[knowledge/manufacturing-digital-path]] — 傳產數位轉型路徑
- [[knowledge/ameba-core]] — 阿米巴經營核心
- [[knowledge/consulting-productization]] — 顧問服務產品化框架

### 框架類（framework）
- [[knowledge/case-deconstruction-framework]] — 品牌案例拆解框架
- [[knowledge/content-strategy-framework]] — 社群內容策略框架

## 使用方式
LLM 在執行任務時，根據需求讀取相關的知識原子，而不是讀取整個 wiki/。
這樣可以提高資訊密度，減少上下文浪費。
