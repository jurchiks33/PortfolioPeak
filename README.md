# PortfolioPeak
# Stock Price Application

## Overview
The Stock Price Application is a Python-based GUI tool built with Tkinter that allows users to view and compare the current stock prices and historical stock data of companies listed on stock exchanges.
The application uses the `yfinance` library to fetch stock data and `matplotlib` to plot stock price graphs.

## Features
- **Current Stock Price**: Fetch and display the current stock price of a single company.
- **Historical Stock Data**: Visualize the historical closing prices of up to two companies over a specified date range on a single graph.

## Installation
To run the Stock Price Application, you will need Python installed on your system. Additionally, the following Python libraries are required:
- `tkinter` - For the GUI (usually comes with Python).
- `matplotlib` - For plotting graphs.
- `yfinance` - For fetching stock data.
- `requests` and `BeautifulSoup` - For parsing HTML if needed (currently not used in the main functionality).

You can install the required external libraries using pip:

## Usage
To start the application, run the `stock_price_app.py` script from your terminal or command prompt:


Once the application is running:
1. Enter the stock ticker symbol in the input field labeled "First Ticker" for the stock you want to check.
2. Optionally, enter a second stock ticker symbol in the input field labeled "Second Ticker" for comparison.
3. Enter the start and end dates for the historical data you wish to retrieve.
4. Click on "Display Graph" to fetch the data and display the graph.

## Contributing
Contributions to the Stock Price Application are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is open source and available under the [MIT License](LICENSE.md).

## Disclaimer
This application is for educational purposes only. Stock market investing involves risk, and this tool does not provide any investment advice.

## Contact
For any feedback or issues, please contact jurchiks33.

