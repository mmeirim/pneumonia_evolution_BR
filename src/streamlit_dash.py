import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

import services.plotly_graphs_service as plotly_graphs_service

st.set_page_config(layout="wide")

# logo = Image.open(Path(__file__).parents[1] / 'images/puc-rio_logo.png')
# st.sidebar.image(logo,use_column_width=True)
st.sidebar.title("Pneumonia Dashboard")
make_choice = st.sidebar.multiselect('Select years to display on tables:',[2012,2013,2014,2015,2016,2017,2018])
filter = ["Data Information",2011,2019,'%∆*','AAPC [95% CI]',2020,2021,'%∆*.1','AAPC [95% CI].1']
for element in make_choice:
    for i in range(len(filter)-1):
        if isinstance(filter[i], int) and isinstance(filter[i+1], int):
            if element > filter[i] and element < filter[i+1]:
                filter.insert(i+1,element)

make_choice2 = st.sidebar.multiselect('Select age groups to display on tables:',['\t\t\t\t\t\t\t\t\t\t\t\t20-49','\t\t\t\t\t\t\t\t\t\t\t\t50-59','\t\t\t\t\t\t\t\t\t\t\t\t60-69','\t\t\t\t\t\t\t\t\t\t\t\t70+'])
filter2 = ["Admissions","\t\t\t\t\t\t\t\t\t\t\t\tNon-Elderly","\t\t\t\t\t\t\t\t\t\t\t\tElderly","Age-adjusted Admissions rate ᵃ","Deaths","Age-adjusted In-hospital\nMortality rate ᵃ",
            "Age-adjusted In-hospital\nLethality rate","Age-adjusted Non ICU\nLethality rate","Age-adjusted ICU\nLethality rate", "Age-adjusted ICU Admissions \nRate ᵃ"]
for element in make_choice2:
    filter2.insert(1,element)

def highlight_rows(s):
    return ['background-color: green']*len(s) if s.index % 2 == 0 else ['background-color: white']*len(s)

file_path = Path(__file__).parents[1] / 'tables/Pneumonia_data_by_age_group_08.11.xlsx'

tab_list = ['20-49','50-59','60-69','70+','Non-Elderly','Elderly']
double_tab_list = ['ICU Admissions','Non ICU Admissions','Pneumonia Admissions','Pneumonia Admissions (ICU)']

st.title("Pneumonia Dashboard") 

###########################################################################################################################
col1, col2, col3 = st.columns([2,0.01,2])
col1.header('Study population')
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

st.markdown('---')
col1, col2, col3 = st.columns([2,0.01,2])
col1.header('Materials and Methods')
col1.markdown('### Outcomes and Variables')
col1.markdown('##### - Age-adjusted hospitalization rate per 100,000 population')
col1.markdown('##### - Age-adjusted in-hospital mortality rate per 100,000 population')
col1.markdown('##### - Age-adjusted in-hospital lethality rate')
col1.markdown('##### - Age-adjusted in-hospital Pneumonia occupation rate')
col1.markdown('##### - Crude number of hospital admissions')
col1.markdown('##### - Crude number of in-hospital deaths')

col3.header('')
col3.markdown('')
col3.markdown('')
col3.markdown('### Statistical Analysis')
col3.markdown('##### - Annual Average Percent Change (AAPC) and its respective 95% confidence interval (95% CI)')
col3.markdown('##### - For count data: AAPC obtained using log-linear Poisson regression with the year as the preditor')
col3.markdown('##### - For age-standardized rates: AAPC obtained using log-linear Poisson regression with the year as the preditor and adding the age-adjusted denominator as an offset variable to the previous Poisson model')

st.markdown('---')
###########################################################################################################################
st.header('Pneumonia Admissions and Mortality by age group')

st.plotly_chart(plotly_graphs_service.graph_pneumocom_admissions(),use_container_width=True)

st.subheader('Pneumonia Admissions and Mortality by age group (Table)')

age_groups = pd.read_excel(file_path,2,nrows=28, usecols="A:L,P:S",thousands=',')

for i in range(len(age_groups)):
    element = age_groups.loc[i].at["Data Information"]
    if element in tab_list:
        age_groups.loc[i,"Data Information"] = "\t\t\t\t\t\t\t\t\t\t\t\t" + element
    if element in double_tab_list:
        age_groups.loc[i,"Data Information"] = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + element

with st.expander("See Table"):
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

st.markdown('---')
###########################################################################################################################

st.header('Pneumonia Lethality and ICU occupation by age group')

st.plotly_chart(plotly_graphs_service.graph_pneumocom_lethality(),use_container_width=True)

st.subheader('Pneumonia Lethality by age group (Table)')

lethality = pd.read_excel(file_path,4,nrows=22, usecols="A:L,P:S",thousands=',')

for i in range(len(lethality)):
    element = lethality.loc[i].at["Data Information"]
    if element in tab_list:
        lethality.loc[i,"Data Information"] = "\t\t\t\t\t\t\t\t\t\t\t\t" + element
    if element in double_tab_list:
        lethality.loc[i,"Data Information"] = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + element

with st.expander("See Table"):
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

st.subheader('Pneumonia ICU occupation by age group (Table)')

age_groups_icu = pd.read_excel(file_path,3,nrows=42, usecols="A:L,P:S",thousands=',')

for i in range(len(age_groups_icu)):
    element = age_groups_icu.loc[i].at["Data Information"]
    if element in tab_list:
        age_groups_icu.loc[i,"Data Information"] = "\t\t\t\t\t\t\t\t\t\t\t\t" + element
    if element in double_tab_list:
        age_groups_icu.loc[i,"Data Information"] = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + element

idx_list = age_groups_icu.index[age_groups_icu["Data Information"].isin(filter2)].tolist()
idx_list1 = [x+1 for x in idx_list]
idx_list2 = [x+2 for x in idx_list]
idx_list = idx_list + idx_list1

with st.expander("See Table"):
    st.dataframe(age_groups_icu[age_groups_icu.index.isin(idx_list)][filter].style.format({
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

st.markdown('---')
###########################################################################################################################

st.header('Pneumonia and General Admissions by age group')
st.plotly_chart(plotly_graphs_service.graph_pneumocom_percent_of_general_admissions(),use_container_width=True)

st.subheader('Pneumonia and General admissions by age group (Table)')

data = pd.read_excel(file_path,0,nrows=28, usecols="A:L,P:S",thousands=',')

for i in range(len(data)):
    element = data.loc[i].at["Data Information"]
    if element in tab_list:
        data.loc[i,"Data Information"] = "\t\t\t\t\t\t\t\t\t\t\t\t" + element
    if element in double_tab_list:
        data.loc[i,"Data Information"] = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + element

data_idx_list = data.index[data["Data Information"].isin(filter2)].tolist()
data_idx_list1 = [x+1 for x in data_idx_list]
data_idx_list = data_idx_list + data_idx_list1
with st.expander("See Table"):
    st.dataframe(data[data.index.isin(data_idx_list)][filter].style.format({
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

st.markdown('---')
###########################################################################################################################

st.header('Pneumonia and General ICU Admissions by age group')
st.plotly_chart(plotly_graphs_service.graph_pneumocom_percent_of_general_admissions_icu(),use_container_width=True)

st.subheader('Pneumonia and General ICU admissions by age group (Table')

data_icu = pd.read_excel(file_path,1,nrows=28, usecols="A:L,P:S",thousands=',')

for i in range(len(data_icu)):
    element = data_icu.loc[i].at["Data Information"]
    if element in tab_list:
        data_icu.loc[i,"Data Information"] = "\t\t\t\t\t\t\t\t\t\t\t\t" + element
    if element in double_tab_list:
        data_icu.loc[i,"Data Information"] = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + element

filter2.append("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tICU Admissions")
data_icu_idx_list = data_icu.index[data_icu["Data Information"].isin(filter2)].tolist()
data_icu_idx_list1 = [x+1 for x in data_icu_idx_list]
data_icu_idx_list = data_icu_idx_list + data_icu_idx_list1
with st.expander("See Table"):
    st.dataframe(data_icu[data_icu.index.isin(data_icu_idx_list)][filter].style.format({
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

st.markdown('---')
###########################################################################################################################
st.header('Pneumonia ICD-10 Ranking')
image_cid = Image.open(Path(__file__).parents[1] / 'images/icd-10_ranking.png')
st.image(image_cid,use_column_width=True, caption='Top 10 ICD-10 Pneumonia Admissons')

###########################################################################################################################
qr_code = Image.open(Path(__file__).parents[1] / 'images/qr_code.png')

st.sidebar.markdown('#### Open This App on your smartphone')
st.sidebar.image(qr_code, use_column_width=True)
