import pandas as pd

# Load the historical stock data from the Excel file
stock_data = pd.read_excel('stock_data.xlsx')


def search_stock_data(query):
    # Search for the query in the stock data
    results = stock_data[stock_data['Date'].str.contains(query, case=False)]
    return results


def search_stock_data(query):
    # Convert the 'Date' column to string format
    stock_data['Date'] = stock_data['Date'].astype(str)

    # Search for the query in the stock data
    results = stock_data[stock_data['Date'].str.contains(query, case=False)]
    return results

# Main function to interact with the user
def main():
    while True:
        # Get user input for the search query
        query = input("Enter a date(e.g.,'2020-01-01'): ")

        # Check if the user wants to exit
        if query.lower() == 'exit':
            print("Exiting the search engine.")
            break

        # Search for the query in the stock data
        search_results = search_stock_data(query)

        # Display the search results
        if not search_results.empty:
            print("Search results:")
            print(search_results)
        else:
            print("No matching results found.")


# Run the search engine
if __name__ == "__main__":
    main()
