import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    return pd.read.csv('data/processed/bikes_completed.csv')
df=load_data()
st.dataframe(df)
if__name__=='__main__':
    main()