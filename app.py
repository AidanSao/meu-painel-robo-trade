import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Painel Robô de Trade", layout="wide")
st.title("Painel Robô de Trade com Médias Móveis")

st.sidebar.header("Configurações")
ticker = st.sidebar.text_input("Código da Ação", value="AAPL")
ma_curta = st.sidebar.slider("Média Móvel Curta", 3, 50, 5)
ma_longa = st.sidebar.slider("Média Móvel Longa", 10, 200, 30)

@st.cache_data
def carregar_dados(ticker):
    dados = yf.download(ticker, period="6mo")
    dados.dropna(inplace=True)
    return dados

dados = carregar_dados(ticker)

if dados.empty:
    st.error("Erro ao carregar dados. Verifique o código da ação.")
else:
    dados['MA_Curta'] = dados['Close'].rolling(window=ma_curta).mean()
    dados['MA_Longa'] = dados['Close'].rolling(window=ma_longa).mean()

    colunas_para_grafico = [c for c in ['Close', 'MA_Curta', 'MA_Longa'] if c in dados.columns]
    st.line_chart(dados[colunas_para_grafico])
    st.dataframe(dados.tail(30))
  adicional painel app.py
