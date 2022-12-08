import streamlit as st
import pandas as pd

import services.plotly_graphs_service as plotly_graphs_service

BEGIN_YEAR = 2011
LAST_YEAR = 2019
STOP_YEAR = 2020

def highlight_rows(x):
    df = x.copy()
    df.iloc[10:, 0] = 'background-color: yellow'
    return df

st.set_page_config(layout="wide")
st.title("Pneumocom Dashboard") 

st.header('Pneumocom and General Admissions by age group')
st.plotly_chart(plotly_graphs_service.graph_pneumocom_percent_of_general_admissions(),use_container_width=True)

data = pd.read_excel('../tables/Pneumonia_data_by_age_group_08.11.xlsx',0,nrows=20, usecols="A:L,P:S",thousands=',')

years_choice = [2011,2012]
# make_choice = st.radio('Select at least 2 years:',[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])
make_choice = st.sidebar.multiselect('Select years to display on tables:',[2012,2013,2014,2015,2016,2017,2018])
filter = ["Data Information",2011,2019,'%∆*','AAPC [95% CI]',2020,2021,'%∆*.1','AAPC [95% CI].1']
for element in make_choice:
    for i in range(len(filter)-1):
        if isinstance(filter[i], int) and isinstance(filter[i+1], int):
            if element > filter[i] and element < filter[i+1]:
                filter.insert(i+1,element)

st.dataframe(data[filter].style.format({
    2011: '{:,.0f}'.format,
    2012: '{:,.0f}'.format,
    2013: '{:,.0f}'.format,
    2014: '{:,.0f}'.format,
    2015: '{:,.0f}'.format,
    2016: '{:,.0f}'.format,
    2017: '{:,.0f}'.format,
    2018: '{:,.0f}'.format,
    2019: '{:,.0f}'.format,
    2020: '{:,.0f}'.format,
    2021: '{:,.0f}'.format,
    '%∆*' : '{:,.2f}'.format,
    '%∆*.1' : '{:,.2f}'.format
}),use_container_width=True)
st.write("AAPC - Annual Average Percent Change (estimated from Poisson regression model")
st.write("ᵃ Rates per 100,000 population, adjusted to the WHO standard population")
st.write("*Percentage change between 2011-2019 and 2019-2021, respectively")

