# 壞掉時怎麼查

## 一句話理解
Hermes 很少壞掉，但如果遇到問題，先用這三個指令就能解決 90% 的問題。

## 這是什麼
這篇列出**最常見的 5 個問題**和**對應的解法**。

## 為什麼需要
遇到問題時不要慌，先查這篇。大部分問題都是**設定錯誤**或**網路問題**，不是真的壞掉。

## 生活比喻
想像你的**手機當機**：
1. 先重啟（最有效）
2. 再檢查網路
3. 最後才想是不是要送修

Hermes 也是一樣。

## 最常見的 5 個問題

### 問題 1：Hermes 不回我了

**症狀**：輸入訊息，沒有回應

**解法**：
1. 先重啟：
   ```bash
   hermes
   ```
   關掉再重新打開
   
2. 如果還不行，檢查 AI 模型是否正常：
   ```bash
   hermes model
   ```
   確認 API Key 沒過期
   
3. 還是壞掉？用診斷工具：
   ```bash
   hermes doctor
   ```

### 問題 2：Hermes 記不住我了

**症狀**：每次重新打開都像是第一次見面

**解法**：
1. 檢查記憶功能是否開啟：
   ```bash
   hermes memory status
   ```
   
2. 如果沒開啟，開啟它：
   ```bash
   hermes memory setup
   ```
   
3. 如果是設定檔壞了，重新設定：
   ```bash
   hermes setup
   ```

### 問題 3：Hermes 回覆很慢

**症狀**：輸入訊息後要等很久才有回應

**解法**：
1. 檢查 AI 模型是否正常：
   ```bash
   hermes model
   ```
   換一個比較快的模型（比如 GPT-4o → Claude Haiku）
   
2. 檢查網路是否穩定
   
3. 如果同時用太多工具，關閉不必要的：
   ```bash
   hermes tools
   ```

### 問題 4：手機收不到 Hermes 的訊息

**症狀**：電腦上的 Hermes 正常，但手機 Telegram 收不到

**解法**：
1. 檢查 Gateway 是否正常：
   ```bash
   hermes gateway status
   ```
   
2. 重啟 Gateway：
   ```bash
   hermes gateway restart
   ```
   
3. 檢查 Telegram Bot 是否被停用：
   回到 @BotFather 確認 Bot 狀態

### 問題 5：不知道問題出在哪

**症狀**：什麼都不知道，就是不正常

**解法**：
1. 用診斷工具：
   ```bash
   hermes doctor
   ```
   
2. 如果還不知道，用完整診斷：
   ```bash
   hermes dump
   ```
   這會產生一份完整的狀態報告，可以貼到技術支援群組。

## 進階：重裝 Hermes

如果以上都不行，最後的手段是**重裝**：

1. 先備份你的資料：
   ```bash
   cp -r ~/.hermes ~/.hermes-backup
   ```
   
2. 重新安裝：
   ```bash
   curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
   ```
   
3. 恢復備份：
   ```bash
   cp -r ~/.hermes-backup/* ~/.hermes/
   ```

## 常見錯誤

### 錯誤 1：一壞掉就慌張
大部分問題都是**設定錯誤**，不是真的壞掉。先查這篇。

### 錯誤 2：不檢查就重裝
重裝是最後手段。先試過上面的解法再說。

### 錯誤 3：不備份就重裝
重裝前一定要備份，不然記憶和技能都會消失。

## 壞掉會怎樣
- **Hermes 壞了**：你的 AI 模型（ChatGPT、Claude）還是正常的
- **記憶丟了**：可以重新介紹
- **技能丟了**：可以重新教
- **最重要的是**：資料不會真正消失，只要備份過 `~/.hermes/` 目錄

## 技術補充
- 日誌位置：`~/.hermes/logs/`
- 診斷工具：`hermes doctor`、`hermes dump`
- 重啟指令：`hermes`（關掉重開）
- 備份指令：`cp -r ~/.hermes ~/.hermes-backup`
