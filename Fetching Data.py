import yfinance as yf

# Step 1: Data Collection
ticker_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-01-01'
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the fetched data to an Excel file
stock_data.to_excel('stock_data.xlsx')