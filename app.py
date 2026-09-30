import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


final_df = pd.read_csv('/Users/shivamkumar/Documents/DSMP/Week 9 - Data Visualization/india.csv')

st.sidebar.title('India ka Data Visualization')

selected_state = st.sidebar.selectbox('Select a State', final_df['State'].unique().insert(0,'Overall India'))

primary_param = st.sidebar.selectbox('Select Primary Parameter', sorted(final_df.columns[5:]))
secondary_param = st.sidebar.selectbox('Select Secondary Parameter', sorted(final_df.columns[5:]))

button = st.sidebar.button('Plot Graph')

if button:
    st.text('Size Represents: ' + primary_param)
    st.text('Color Represents: ' + secondary_param)
    if selected_state == 'Overall India':
        # Plotting for india
        fig = px.scatter_map(final_df,
                             lat='Latitude',
                             lon='Longitude',
                             zoom=3,height=500,
                             size=primary_param,color=secondary_param,
                             size_max=30,width=1200,hover_name='State')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = final_df[final_df['State'] == selected_state]
        # Plotting for state
        fig = px.scatter_map(state_df,
                             lat='Latitude',
                             lon='Longitude',
                             zoom=5,height=500,
                             size=primary_param,color=secondary_param,
                             size_max=30,width=1200,hover_name='State')
        st.plotly_chart(fig,use_container_width=True)        