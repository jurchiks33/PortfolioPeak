import tkinter as tk  
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Define the function to fetch stock price
def fetch_stock_price():
    ticker = entry_ticker.get()
    if not ticker:
        messagebox.showinfo("Error", "Please enter a stock ticker symbol")
        return

    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        if price:
            label_price.config(text=f"Current price of {ticker}: ${price.text}")
        else:
            messagebox.showinfo("Error", "Price element not found.")
    else:
        messagebox.showinfo("Error", f"Failed to fetch page with status code: {response.status_code}")

#function that will fetch and display historical stock data on a graph
def fetch_and_display_stock_data():
    ticker = entry_ticker.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    if not ticker:
        messagebox.showinfo("Error", "Please enter stock ticker symbol")
        return
    
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)

        fig, ax = plt.subplots()
        stock_data['Close'].plot (ax=ax, title=f"{ticker} Stock Price")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        plt.close(fig)
    
    except Exception as e:
        messagebox.showinfo("Error", f"An error occured: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Stock Price App")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_ticker = tk.Entry(frame)
entry_ticker.pack(side=tk.LEFT)

# Button command corrected to 'fetch_stock_price'
button_fetch = tk.Button(frame, text="Fetch Data", command=fetch_stock_price)
button_fetch.pack(side=tk.LEFT)

label_price = tk.Label(root, text="Enter a stock ticker symbol and click fetch")
label_price.pack(pady=20)

entry_start_date = tk.Entry(root)
entry_start_date.pack()
entry_start_date.insert(0, "Start Date (YYYY-MM-DD)")

entry_end_date = tk.Entry(root)
entry_end_date.pack()
entry_end_date.insert(0, "End Date (YYYY-MM-DD)")

root.mainloop()
