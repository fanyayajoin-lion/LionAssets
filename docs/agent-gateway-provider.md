# Agent / Gateway / Provider — 大白話解釋

## 一句話理解
這三個詞聽起來很技術，其實就是：**大腦（Provider）+ 管家（Agent）+ 電話線（Gateway）**。

## 這是什麼

### Provider = AI 大腦
就是你的「思考引擎」。Hermes 自己不會思考，他需要請一個 AI 來幫忙想事情。

- **GPT-4o** = 什麼都知道的通才
- **Claude** = 寫文案很強的作家
- **Gemini** = 便宜好用的學生

你隨時可以換 Provider，就像換顧問一樣。

### Agent = 管家本人
就是 Hermes 本身。他負責：
- 記住你的喜好
- 安排哪位 Provider 來幫你
- 幫你讀檔案、跑程式、查資料
- 24 小時等你吩咐

### Gateway = 電話線
就是你怎麼找到 Hermes 的管道。

- **手機 App（Telegram）** → 最常用，隨時隨地找 Hermes
- **電腦終端機** → 在家裡用電腦時
- **網頁介面** → 用瀏覽器管理

Gateway 只是「聯絡方式」，Hermes 本人還是在你家電腦或雲端跑。

## 為什麼需要懂
因為當你遇到問題時，你知道問題出在哪：
- **Provider 問題** = AI 回答很奇怪（換一個就好）
- **Agent 問題** = Hermes 不記住你了（重啟就好）
- **Gateway 問題** = 手機收不到訊息（檢查網路就好）

## 生活比喻
想像你在開一家**診所**：

| 術語 | 診所比喻 | 作用 |
|------|---------|------|
| **Provider** | 醫師 | 負責診斷、開藥（思考） |
| **Agent** | 診所管理員 | 記住病人喜好、安排醫師（管家） |
| **Gateway** | 掛號窗口 | 病人透過窗口找到診所（聯絡方式） |

- 醫師累了？換一位 Provider（GPT → Claude）
- 管理員當機？重啟 Agent（hermes restart）
- 掛號窗口不通？檢查 Gateway（Telegram Bot）

## 實際使用場景

### 場景 1：你想換 AI 模型
輸入：
```bash
hermes model
```
選一個新的 Provider。管理員（Agent）會自動安排新醫師。

### 場景 2：你想用手機跟 Hermes 說話
設定 Gateway → Telegram Bot。以後你的手機就是掛號窗口。

### 場景 3：Hermes 不記住你了
可能是 Agent 當機。輸入：
```bash
hermes restart
```
重新啟動管理員就好。

## 常見錯誤

### 錯誤 1：以為 Provider 越貴越好
不一定。不同 Provider 擅長不同事：
- 寫文案 → Claude 比較強
- 分析資料 → GPT-4o 比較強
- 預算有限 → Gemini 或 DeepSeek 就好

### 錯誤 2：以為 Gateway 越多越好
不用。一個 Gateway 就夠了（推薦 Telegram），多了反而容易搞混。

### 錯誤 3：以為 Agent 會自己壞掉
不會。除非你關掉電腦或網路斷線，Agent 一直在跑。

## 壞掉會怎樣
- **Provider 壞了** → 換另一個 Provider，Hermes 還在
- **Agent 壞了** → 重啟就好
- **Gateway 壞了** → 換另一個 Gateway（電腦還是能找到 Hermes）

## 技術補充
- Provider 設定：`hermes model`
- Agent 路徑：`~/.hermes/`
- Gateway 設定：`hermes gateway setup`
- 查看所有 Gateway：`hermes gateway status`
