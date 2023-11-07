import tkinter as tk  # Import statement added here
from tkinter import messagebox
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

# Run the application
root.mainloop()
