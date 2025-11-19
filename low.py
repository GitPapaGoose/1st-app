import streamlit as st
import yfinance as yf
import plotly.express as px
def app ():
    st.title('Минимальная цена сделки за день')
    ticker_symbol = 'AAPL'
    data = yf.Ticker(ticker_symbol)
    hist = data.history(period="5y")
    st.subheader("Последние 5 дней")
    st.write(hist['Low'].tail())
    st.subheader("Последние 5 лет")
    fig = px.line(hist, y='Low', title="Минимальная цена котировки Apple (AAPL)")
    st.plotly_chart(fig)
    csv_data = hist.to_csv(index=True).encode('utf-8')
    st.download_button(
    label="Скачать данные графика (CSV)", # Текст на кнопке
    data=csv_data, # Данные для загрузки
    file_name='apple_quotes_low.csv', # Имя файла, которое будет у скачанного файла
    mime='text/csv')