import yfinance as yf
import pandas as pd

# 抓黃金期貨代碼 "GC=F"
data = yf.download(
    'GC=F',
    start='1985-01-01',
    end='2025-12-31'
)

# 檢查有沒有成功
if data.empty:
    print("⚠️ 沒有抓到任何資料！")
else:
    # 只保留收盤價
    df_gold = data[['Close']].rename(columns={'Close': 'Gold_Price'})

    # 印出前幾筆
    print(df_gold.head())

    # 存成CSV
    df_gold.to_csv('gold_price_1985_2025.csv')
    print("✅ 已經把黃金價格存到 gold_price_1985_2025.csv")
