import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
	# Aplicativo simples de preço de ações


	Shown are the stock **closing price** and ***volume*** of Google (GOOGL)
	
	""")

tickerSymbol = 'GOOG'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2011-1-31', end='2021-1-31')


# def select_org(org):
# 	tickerSymbol = str(org)
#	tickerData = yf.Ticker(tickerSymbol)
#	tickerDf = tickerData.history(period='id', start='2011-1-31', end='2021-1-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)