import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image
import qrcode

import services.plotly_graphs_service as plotly_graphs_service

st.set_page_config(layout="wide")

# logo = Image.open(Path(__file__).parents[1] / 'images/puc-rio_logo.png')
# st.sidebar.image(logo,use_column_width=True)
st.sidebar.title("Pneumocom Dashboard")
make_choice = st.sidebar.multiselect('Select years to display on tables:',[2012,2013,2014,2015,2016,2017,2018])
filter = ["Data Information",2011,2019,'%∆*','AAPC [95% CI]',2020,2021,'%∆*.1','AAPC [95% CI].1']
for element in make_choice:
    for i in range(len(filter)-1):
        if isinstance(filter[i], int) and isinstance(filter[i+1], int):
            if element > filter[i] and element < filter[i+1]:
                filter.insert(i+1,element)

make_choice2 = st.sidebar.multiselect('Select age groups to display on tables:',['20-49','50-59','60-69','70+'])
filter2 = ["Admissions","Non-Elderly","Elderly","Age-adjusted Admissions rate ᵃ","Deaths","Age-adjusted In-hospital\nMortality rate ᵃ",
            "Age-adjusted In-hospital\nLethality rate","Age-adjusted Non ICU\nLethality rate","Age-adjusted ICU\nLethality rate"]
for element in make_choice2:
    for i in range(len(filter2)-1):
        try:
            el = int(element[:2])
            first = int(filter2[i][:2])
            second = int(filter2[i+1][:2])
            if isinstance(first, int) and isinstance(second, int):
                if el > first and el < second:
                    filter2.insert(i+1,element)
            if isinstance(first, int):
                if el > first:
                    filter2.insert(i+1,element)
        except:
            filter2.insert(1,element)

file_path = Path(__file__).parents[1] / 'tables/Pneumonia_data_by_age_group_08.11.xlsx'


st.title("Pneumocom Dashboard") 

###########################################################################################################################
col1, col2, col3 = st.columns([2,0.1,2])
col1.header('Pneumonia Study')
image = Image.open(Path(__file__).parents[1] / 'images/studypopulation_pneumonia.png')
col1.image(image)

col3.header('Objectives')
col3.markdown('#####  Present the evolution of community-acquired pneumonia admissions and deaths , as well as the effects on the Brazilian Unified Health System (SUS) from 2011 to 2021.')
col3.markdown('---')

col3.header('Data Source')
col3.markdown('###  AIH/SIH')
col3.markdown('#### - Brazil')
col3.markdown('#### - 2011-2021')
col3.markdown('#### - Filtering by age (≥20 years)')

###########################################################################################################################
st.header('Pneumonia Admissions by age group')

st.plotly_chart(plotly_graphs_service.graph_pneumocom_admissions(),use_container_width=True)

age_groups = pd.read_excel(file_path,2,nrows=28, usecols="A:L,P:S",thousands=',')
st.dataframe(age_groups[age_groups["Data Information"].isin(filter2)][filter].style.format({
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

###########################################################################################################################

st.header('Pneumonia Lethality and ICU occupation by age group')

st.plotly_chart(plotly_graphs_service.graph_pneumocom_lethality(),use_container_width=True)

st.subheader('Pneumonia Lethality by age group')

lethality = pd.read_excel(file_path,4,nrows=22, usecols="A:L,P:S",thousands=',')
st.dataframe(lethality[lethality["Data Information"].isin(filter2)][filter].style.format({
    2011: '{:.2%}'.format,
    2012: '{:.2%}'.format,
    2013: '{:.2%}'.format,
    2014: '{:.2%}'.format,
    2015: '{:.2%}'.format,
    2016: '{:.2%}'.format,
    2017: '{:.2%}'.format,
    2018: '{:.2%}'.format,
    2019: '{:.2%}'.format,
    2020: '{:.2%}'.format,
    2021: '{:.2%}'.format,
    '%∆*' : '{:,.2f}'.format,
    '%∆*.1' : '{:,.2f}'.format
}),use_container_width=True)
st.write("AAPC - Annual Average Percent Change (estimated from Poisson regression model")
st.write("*Percentage change between 2011-2019 and 2019-2021, respectively")

st.subheader('Pneumonia ICU occupation by age group')

age_groups_icu = pd.read_excel(file_path,3,nrows=42, usecols="A:L,P:S",thousands=',')
st.dataframe(age_groups_icu[filter].style.format({
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

###########################################################################################################################

st.header('Pneumocom vs General Admissions by age group')
st.plotly_chart(plotly_graphs_service.graph_pneumocom_percent_of_general_admissions(),use_container_width=True)

data = pd.read_excel(file_path,0,nrows=28, usecols="A:L,P:S",thousands=',')

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

###########################################################################################################################
# col1, col2, col3 = st.columns([2,0.1,2])
st.header('Pneumonia ICD-10 Ranking')
image_cid = Image.open(Path(__file__).parents[1] / 'images/icd-10_ranking.png')
st.image(image_cid,use_column_width=True, caption='Top 10 ICD-10 Pneumonia Admissons')

###########################################################################################################################
qr_code = Image.open(Path(__file__).parents[1] / 'images/qr_code.png')

st.sidebar.markdown('#### Open This App on your smartphone')
st.sidebar.image(qr_code, use_column_width=True)
