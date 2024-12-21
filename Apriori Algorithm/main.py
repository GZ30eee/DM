import tkinter as tk
from tkinter import ttk
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import yfinance as yf
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

# Function for Apriori Algorithm
def apriori_analysis():
    transactions = [
        ['milk', 'bread', 'butter'],
        ['bread', 'butter', 'jam'],
        ['milk', 'bread'],
        ['bread', 'butter'],
        ['milk', 'bread', 'butter', 'jam'],
        ['bread', 'butter'],
        ['milk', 'bread', 'butter', 'jam'],
    ]
    df = pd.DataFrame(transactions)
    df = df.stack().str.get_dummies().groupby(level=0).sum()
    df = df.astype(bool)
    frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7, num_itemsets=2)
    output = f"Frequent Itemsets:\n{frequent_itemsets}\n\nAssociation Rules:\n{rules}"
    return output

def finance_analysis():
    stock_symbol = "AAPL"  # Apple stock as an example
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    # Fetch stock data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Check if the data is empty
    if stock_data.empty:
        print("No data fetched. Please check the stock symbol and date range.")
        return

    # Calculate Moving Averages (50-day and 200-day)
    stock_data['50_day_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200_day_MA'] = stock_data['Close'].rolling(window=200).mean()

    # Plot the data
    plt.figure(figsize=(14, 8))

    # Plotting the closing price
    plt.plot(stock_data['Close'], label="Stock Price", color='blue', alpha=0.6)

    # Plotting the 50-day moving average
    plt.plot(stock_data['50_day_MA'], label="50-Day Moving Average", color='red', alpha=0.8)

    # Plotting the 200-day moving average
    plt.plot(stock_data['200_day_MA'], label="200-Day Moving Average", color='green', alpha=0.8)

    # Add title and labels
    plt.title(f"Stock Price Trend Analysis for {stock_symbol}", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Price (USD)", fontsize=14)

    # Show legend
    plt.legend(loc='upper left')

    # Show the plot
    plt.grid(True)
    plt.show()

    # Get the latest stock price using iloc
    latest_price = stock_data.iloc[-1]['Close']
    latest_50_day_MA = stock_data.iloc[-1]['50_day_MA']
    latest_200_day_MA = stock_data.iloc[-1]['200_day_MA']

    print(f"Latest Stock Price: {latest_price}")
    print(f"Latest 50-Day Moving Average: {latest_50_day_MA}")
    print(f"Latest 200-Day Moving Average: {latest_200_day_MA}")

    # Basic trend indication
    if latest_price > latest_50_day_MA:
        print("The stock is in an upward trend relative to the 50-day moving average.")
    else:
        print("The stock is in a downward trend relative to the 50-day moving average.")

    if latest_50_day_MA > latest_200_day_MA:
        print("The stock is in a short-term uptrend compared to the long-term trend.")
    else:
        print("The stock is in a short-term downtrend compared to the long-term trend.")

# Call the function
finance_analysis()


# Function for Sentiment Analysis
def sentiment_analysis():
    data = pd.read_csv("cleaned_data.csv")  # Example path
    def clean_text(text):
        if isinstance(text, str):
            text = re.sub(r"http\S+", "", text)
            text = re.sub(r"@\w+", "", text)
            text = re.sub(r"#\w+", "", text)
            text = re.sub(r"[^\w\s]", "", text)
            return text.strip().lower()
        return ""
    
    data['cleaned_text'] = data['text'].apply(clean_text)
    data = data[data['cleaned_text'] != ""]
    
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
    
    data['Sentiment'] = data['cleaned_text'].apply(analyze_sentiment)
    sentiment_counts = data['Sentiment'].value_counts()
    
    output = f"Sentiment Distribution:\n{sentiment_counts}"
    return output

# Function to update the output in the UI
def update_output(tab, output_text):
    tab.config(state=tk.NORMAL)
    tab.delete('1.0', tk.END)
    tab.insert(tk.END, output_text)
    tab.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Python Script UI")

# Create Tab Control
tabControl = ttk.Notebook(root)

# Apriori Tab
apriori_tab = ttk.Frame(tabControl)
tabControl.add(apriori_tab, text='Apriori Algorithm')

# Finance Tab
finance_tab = ttk.Frame(tabControl)
tabControl.add(finance_tab, text='Finance Analysis')

# Sentiment Tab
sentiment_tab = ttk.Frame(tabControl)
tabControl.add(sentiment_tab, text='Sentiment Analysis')

tabControl.pack(expand=1, fill="both")

# Create output areas in each tab
apriori_output = tk.Text(apriori_tab, wrap=tk.WORD, width=80, height=20)
apriori_output.pack(padx=10, pady=10)
apriori_output.config(state=tk.DISABLED)

finance_output = tk.Text(finance_tab, wrap=tk.WORD, width=80, height=20)
finance_output.pack(padx=10, pady=10)
finance_output.config(state=tk.DISABLED)

sentiment_output = tk.Text(sentiment_tab, wrap=tk.WORD, width=80, height=20)
sentiment_output.pack(padx=10, pady=10)
sentiment_output.config(state=tk.DISABLED)

# Run analysis and update UI with results
apriori_result = apriori_analysis()
update_output(apriori_output, apriori_result)

finance_result = finance_analysis()
update_output(finance_output, finance_result)

sentiment_result = sentiment_analysis()
update_output(sentiment_output, sentiment_result)

# Start the GUI loop
root.mainloop()
