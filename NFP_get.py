import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

def get_nfp_from_fred(fred_key, start, end):
    fred = Fred(api_key=fred_key)
    nfp = fred.get_series('PAYEMS', start_date=start, end_date=end)
    return pd.DataFrame(nfp, columns=['NFP_Actual'])

# 設定
start_date = '1985-01-01'
end_date   = '2025-12-31'
fred_key   = 'e1770dedd6505e4e160107f54ba52556'

# 抓資料
df_nfp = get_nfp_from_fred(fred_key, start_date, end_date)

# 視覺化
df_nfp.plot(title='Non-Farm Payrolls (NFP) (1985–2025)', figsize=(12,6), color='black')
plt.ylabel('Thousands')
plt.grid(True)
plt.tight_layout()
plt.show()

# 輸出
df_nfp.to_csv('/Users/wanlun/python/勞動部爬蟲資料/NFP_1985_2025.csv')
