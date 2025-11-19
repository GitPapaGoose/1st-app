import yfinance as yf
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import close, high, low, open, volume, user_csv, tips

st.set_page_config(
    page_title='Котировки компании Apple',
)

class MultiApp:

    def ___init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Котировки Apple:',
                options=['Open', 'High', 'Low', 'Close', 'Volume', 'Your CSV', 'Tips'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    'container':{'padding': '5!important', 'background-color': 'black'},
                    'nav-link':{'color':'white', 'font-size': '20px', 'text-align':'left'}
                }
           )
        if app == 'Open':
            open.app()
        if app == 'High':
            high.app()
        if app == 'Low':
            low.app()
        if app == 'Close':
            close.app()
        if app == 'Volume':
            volume.app()
        if app == 'Your CSV':
            user_csv.app()
        if app == 'Tips':
            tips.app()
    run()
