import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def app ():
    st.title('Неожиданный график чаевых в каком-то рестике')

    path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    tips = pd.read_csv(path)

    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2023-01-31')
    days_diff = (end_date - start_date).days
    random_days = np.random.randint(0, days_diff, len(tips))
    tips['time_order'] = start_date + pd.to_timedelta(random_days, unit='D')
    tips['time_order'] = pd.to_datetime(tips['time_order'])

    daily_avg_tips = tips.groupby('time_order')['tip'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(
        data=daily_avg_tips,
        x='time_order',
        y='tip',
        marker='o',
        ax=ax
    )

    ax.set_title('Динамика чаевых по дням')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Средняя сумма чаевых')
    ax.grid(True)

    st.pyplot(fig)