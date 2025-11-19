import streamlit as st
import pandas as pd

def app ():
    st.title('Загрузка Вашего CSV файла')
    uploaded_file = st.file_uploader("Выберите и загрузите CSV файл", type="csv")
    if uploaded_file is not None:
        st.subheader("Загруженный файл:")
        try:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
            st.success("Файл успешно загружен и отображен")
        except Exception as e:
            st.error(f"Произошла ошибка при чтении файла: {e}")
        else:
            st.info("Пожалуйста, загрузите CSV файл через кнопку выше.")