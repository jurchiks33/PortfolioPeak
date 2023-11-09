import tkinter as tk  
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#Screen sizing and positioning starts
root = tk.Tk()
root.title("Stock Price App")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = int(screen_width * 0.8)
height = int(screen_height * 0.8)

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f'{width}x{height}+{x}+{y}')
#Screen sizing and positioning ends

def on_entry_click(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focusout(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg='grey')

    
def fetch_stock_price():
    ticker = entry_ticker.get()
    if not ticker:
        messagebox.showinfo("Error", "Please enter a stock ticker symbol")
        return
    
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    if not todays_data.empty:
        price = todays_data['Close'].iloc[-1]  # Get the last close price
        label_price.config(text=f"Current price of {ticker}: ${price}")
    else:
        messagebox.showinfo("Error", "Could not retrieve stock data. Please check the ticker symbol.")
#function to validate and format date
def validate_and_format_date(data_str):
    try:
        date_obj = datetime.strptime(data_str, "%Y-%m-%d")
        formatted_date_str = date_obj.strftime("%Y-%m-%d")
        return formatted_date_str
    except ValueError as e:
        messagebox.showinfo("Error", f"Date format error: {e}")

#function that will fetch and display historical stock data on a graph
def fetch_and_display_stock_data():
    ticker1 = entry_ticker1.get()
    ticker2 = entry_ticker2.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    start_date = validate_and_format_date(start_date)
    end_date = validate_and_format_date(end_date)

    if not (start_date and end_date):
        messagebox.showinfo("Error", "Please enter valid start and end dates")
        return
    
    try:
        stock_data1 = yf.download(ticker1, start=start_date, end=end_date)
        stock_data2 = yf.download(ticker2, start=start_date, end=end_date)

        fig, ax = plt.subplots()
        if not stock_data1.empty:
            stock_data1['Close'].plot(ax=ax, label=f"{ticker1} Closing Price")
        if not stock_data2.empty:
            stock_data2['Close'].plot(ax=ax, label=f"{ticker2} Closing Price")
        
        ax.legend()
        ax.set_title(f"{ticker1} vs {ticker2} Stock Price Comparison")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        plt.close(fig)

    except Exception as e:
        messagebox.showinfo("Error", f"An error occured: (e)")

def setup_enrtry_with_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, placeholder_text))
    entry.bind('<FocusOut>', lambda event: on_focusout(event, entry, placeholder_text))

frame = tk.Frame(root)
frame.pack(pady=20)

entry_ticker1 = tk.Entry(frame)
setup_enrtry_with_placeholder(entry_ticker1, "First Ticker")
entry_ticker1.pack(side=tk.LEFT)

# Entry for the second stock ticker
entry_ticker2 = tk.Entry(frame)
setup_enrtry_with_placeholder(entry_ticker2, "Second Ticker")
entry_ticker2.pack(side=tk.LEFT)

# Button to fetch and plot data
button_fetch_graph = tk.Button(frame, text="Display Graph", command=fetch_and_display_stock_data)
button_fetch_graph.pack(side=tk.LEFT)

entry_ticker = tk.Entry(frame)
entry_ticker.pack(side=tk.LEFT)

# # Button command corrected to 'fetch_stock_price'
# button_fetch = tk.Button(frame, text="Fetch Data", command=fetch_stock_price)
# button_fetch.pack(side=tk.LEFT)

label_price = tk.Label(root, text="Enter a stock ticker symbol and click fetch")
label_price.pack(pady=20)

#Date entry field starting
entry_start_date = tk.Entry(root)
entry_start_date.pack()
entry_start_date.insert(0, "Start Date (YYYY-MM-DD)")
entry_start_date.bind('<FocusIn>', lambda event: on_entry_click(event, entry_start_date, "Start Date (YYYY-MM-DD)"))
entry_start_date.bind('<FocusOut>', lambda event: on_focusout(event, entry_start_date, "Start Date (YYYY-MM-DD)"))

entry_end_date = tk.Entry(root)
entry_end_date.pack()
entry_end_date.insert(0, "End Date (YYYY-MM-DD)")
entry_end_date.bind('<FocusIn>', lambda event: on_entry_click(event, entry_end_date, "End Date (YYYY-MM-DD)"))
entry_end_date.bind('<FocusOut>', lambda event: on_focusout(event, entry_end_date, "End Date (YYYY-MM-DD)"))
#Date entry field ends

button_fetch_graph = tk.Button(root, text="Display Graph", command=fetch_and_display_stock_data)
button_fetch_graph.pack(pady=10)

root.mainloop()
