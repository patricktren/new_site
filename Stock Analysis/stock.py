import yfinance as yf
import pandas as pd
import matplotlib as plt
import seaborn as sns



# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Set the ticker
ticker = 'AMZN'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
print(data.tail())

