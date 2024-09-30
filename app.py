#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri
data = {
    'Name': ['Hotel A', 'Hotel B', 'Hotel C'],
    'ID': [123, 456, 789],
    'Booking': [True, False, True],
    'Expedia': [False, True, True],
    'Agoda': [True, True, False]
}

# DataFrame oluştur
df = pd.DataFrame(data)

# Check ve cross işaretlerini ekleyelim
df['Booking'] = df['Booking'].apply(lambda x: "✔️" if x else "❌")
df['Expedia'] = df['Expedia'].apply(lambda x: "✔️" if x else "❌")
df['Agoda'] = df['Agoda'].apply(lambda x: "✔️" if x else "❌")

# Streamlit tablosunu oluştur
st.title("Price Existence")
st.write(df)





