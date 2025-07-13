import yfinance as yf
import matplotlib.pyplot as plt

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

    # 畫圖
    plt.figure(figsize=(12,6))
    plt.plot(df_gold.index, df_gold["Gold_Price"], color="gold")
    plt.title("Gold Price Over Time (1985–2025)")
    plt.xlabel("Date")
    plt.ylabel("USD per ounce")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 存成CSV
    df_gold.to_csv('gold_price_1985_2025.csv')
    print("✅ 已經把黃金價格存到 gold_price_1985_2025.csv")
