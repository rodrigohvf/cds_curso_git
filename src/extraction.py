import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def load_data():
    return pd.read.csv('data/processed/bikes_completed.csv')
df_raw=load_data()
st.dataframe(df_raw)
if__name__=='__main__':
    main()