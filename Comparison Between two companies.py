import yfinance as yf

def compare_companies(tickers, metrics):
    company_data = {}
    for ticker in tickers:
        try:
            data = yf.download(ticker, start="2020-01-01", end="2024-01-01")
            company_data[ticker] = {}
            for metric in metrics:
                company_data[ticker][metric] = data[metric].mean()
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")
    return company_data

def print_comparison(company_data):
    print("Comparison of Companies:")
    for ticker, metrics in company_data.items():
        print(f"\nCompany: {ticker}")
        for metric, value in metrics.items():
            print(f"{metric}: {value}")

# Define the list of tickers and financial metrics to compare
tickers = ["AAPL", "MSFT"]  # Example tickers for Apple and Microsoft
metrics = ["Open", "Close", "Volume"]  # Example metrics

# Compare companies based on the defined tickers and metrics
company_data = compare_companies(tickers, metrics)

# Print the comparison results
print_comparison(company_data)
