import yfinance as yf
import streamlit as st
import pandas as pd

from datetime import date

tday = date.today().isoformat()

st.write("""
	# Aplicativo Simples de Preço de Ações

	Shown are the stock **closing price** and ***volume*** of AAPL (Apple), AMZN (Amazon), GOOGL/GOOG (Google) e MSFT (Microsoft).

	 Period: The time period was set from 1/1/2016 until the date of access to the App. 
	
	""")

# Tickers
tickerSymbol = 'GOOGL GOOG AMZN MSFT AAPL'

tickerData = yf.Tickers(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2016-1-01', end=tday)


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)