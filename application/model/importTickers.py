import pandas as pd

def getTickers():
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    #read in html from url above
    tables = pd.read_html(sp500_url)
    #print('Tables found:', len(tables))
    #get table with tickers from S&P 500 and save into pandas dataframe
    df1 = tables[0]
    tickers = df1['Symbol']
    tickers = tickers.sort_values(ascending=True)
    return tickers