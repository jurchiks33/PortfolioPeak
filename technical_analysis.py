import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()

def calculate_rsi(data, window):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, short_window=12, long_window=26, signal=9):
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calculate_bollinger_bands(data, window):
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    upper_band = sma + (std * 2)
    lower_band = sma - (std * 2)
    return upper_band, lower_band

def calculate_stochastic_oscillator(data, window):
    low_min = data['Low'].rolling(window=window).min()
    high_max = data['High'].rolling(window=window).max()
    stoch = ((data['Close'] - low_min) / (high_max - low_min)) * 100
    return stoch

def calculate_macd_histogram(data, short_window=12, long_window=26, signal=9):
    macd, signal_line = calculate_macd(data, short_window, long_window, signal)
    histogram = macd - signal_line
    return histogram

def calculate_atr(data, window):
    high_low = data['High'] - data['Low']
    high_close = np.abs(data['High'] - data['Close'].shift())
    low_close = np.abs(data['Low'] - data['Close'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    atr = true_range.rolling(window=window).mean()
    return atr

def calculate_vwap(data):
    vwap = (data['Volume'] * (data['High'] + data['Low'] + data['Close']) / 3).cumsum() / data['Volume'].cumsum()
    return vwap

def calculate_parabolic_sar(data):
    # This is a simplified version and might not cover all aspects of the Parabolic SAR calculation
    sar = data['Close'].rolling(window=2).apply(lambda x: x[1] if x[1] > x[0] else x[0], raw=True)
    return sar

def calculate_cci(data, window):
    tp = (data['High'] + data['Low'] + data['Close']) / 3
    cci = (tp - tp.rolling(window=window).mean()) / (0.015 * tp.rolling(window=window).std())
    return cci

def calculate_ichimoku_cloud(data):
    high_9 = data['High'].rolling(window=9).max()
    low_9 = data['Low'].rolling(window=9).min()
    tenkan_sen = (high_9 + low_9) / 2

    high_26 = data['High'].rolling(window=26).max()
    low_26 = data['Low'].rolling(window=26).min()
    kijun_sen = (high_26 + low_26) / 2

    senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(26)

    high_52 = data['High'].rolling(window=52).max()
    low_52 = data['Low'].rolling(window=52).min()
    senkou_span_b = ((high_52 + low_52) / 2).shift(26)

    chikou_span = data['Close'].shift(-26)

    return tenkan_sen, kijun_sen, senkou_span_a, senkou_span_b, chikou_span

def calculate_williams_r(data, window):
    high_max = data['High'].rolling(window=window).max()
    low_min = data['Low'].rolling(window=window).min()
    williams_r = -100 * ((high_max - data['Close']) / (high_max - low_min))
    return williams_r