# Financial Fundamental Data Crawler 📊

這是一個自動抓取經濟基本面資料的 Python 專案，透過 API 整合多個資料來源，包括 CPI、黃金、原油與非農就業數據（NFP），可供後續財經分析與機器學習模型使用。

---

## 📌 功能特色

目前已支援以下數據抓取：

| 指標 | 資料來源 | 技術方法 |
|------|----------|-----------|
| CPI（消費者物價指數） | [FRED](https://fred.stlouisfed.org/) | 使用 FRED API（Key: `e1770dedd6505e4e160107f54ba52556`） |
| Gold（黃金價格） | [Yahoo Finance](https://finance.yahoo.com) | 使用 `yfinance` 套件抓取歷史黃金價格 |
| Oil（原油價格） | [FRED](https://fred.stlouisfed.org/) | 使用 FRED API 抓取原油現貨價格 |
| NFP（非農就業） | [FRED](https://fred.stlouisfed.org/) | 使用 FRED API 抓取月度非農數據 |

---

## 🔮 擴充規劃

- [ ] 支援即時金價（Live Gold Price）
- [ ] 抓取市場預期的 NFP 數據（如 Investing.com / ForexFactory）
- [ ] 圖形化資料展示（使用 matplotlib / plotly）
- [ ] 與機器學習模型結合，預測指標走勢

---

## 🚀 執行方式

1. 安裝必要套件（建議使用虛擬環境）：

```bash
pip install -r requirements.txt
```
2. 執行主程式

```bash
python main.py
```
3.專案結構

```bash
project/
│
├── main.py                  # 主控制流程
├── fetch_cpi.py             # 抓取 CPI 的模組
├── fetch_gold.py            # 抓取黃金價格的模組（使用 yfinance）
├── fetch_oil.py             # 抓取油價資料模組
├── fetch_nfp.py             # 抓取 NFP（非農就業）模組
├── data/                    # 儲存下載資料的資料夾
├── utils/                   # 工具函式（API 呼叫、日期處理等）
├── requirements.txt         # 需要安裝的 Python 套件列表
└── README.md                # 專案說明文件（本檔案）
```
本專案僅供學術與學習用途。請勿用於商業用途。如需合作或授權，請與作者聯繫。

