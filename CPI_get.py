import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

def get_cpi_from_fred(fred_key, start, end):
    fred = Fred(api_key=fred_key)
    cpi = fred.get_series('CPIAUCNS', start_date=start, end_date=end)
    return pd.DataFrame(cpi, columns=['CPI_All'])

# 設定
start_date = '1985-01-01'
end_date   = '2025-12-31'
fred_key   = 'e1770dedd6505e4e160107f54ba52556'

# 抓資料
df_cpi = get_cpi_from_fred(fred_key, start_date, end_date)

# 視覺化
df_cpi.plot(title='CPI All Urban Consumers (1985–2025)', figsize=(12,6))
plt.ylabel('CPI')
plt.grid(True)
plt.tight_layout()
plt.show()

# 輸出
df_cpi.to_csv('/Users/wanlun/python/勞動部爬蟲資料/CPI_1985_2025.csv')
