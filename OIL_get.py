import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

def get_oil_data(fred_key, start, end):
    fred = Fred(api_key=fred_key)
    oil = fred.get_series('DCOILWTICO', start_date=start, end_date=end)
    return pd.DataFrame(oil, columns=['WTI_Oil_Price'])

# 設定
start_date = '1985-01-01'
end_date   = '2025-12-31'
fred_key   = 'e1770dedd6505e4e160107f54ba52556'

# 抓資料
df_oil = get_oil_data(fred_key, start_date, end_date)

# 視覺化
df_oil.plot(title='WTI Crude Oil Price (1985–2025)', figsize=(12,6), color='orange')
plt.ylabel('USD per Barrel')
plt.grid(True)
plt.tight_layout()
plt.show()

# 輸出
df_oil.to_csv('/Users/wanlun/python/勞動部爬蟲資料/OIL_1985_2025.csv')
