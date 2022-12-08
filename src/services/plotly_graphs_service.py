import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def graph_pneumocom_percent_of_general_admissions():
    years = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]
    admissoes_total = pd.read_excel('../tables/Pneumonia_data_by_age_group_08.11.xlsx',0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=12,thousands=',')
    admissoes_total = admissoes_total.astype(float)
    admissoes_total = admissoes_total.T
    admissoes_total.columns = ["count"]
    admissoes_total["year"] = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]

    admissoes_total_tx = pd.read_excel('../tables/Pneumonia_data_by_age_group_08.11.xlsx',0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=12,thousands=',')
    admissoes_total_tx = admissoes_total_tx.astype(float)

    admissoes_gerais_total_tx = pd.read_excel('../tables/Pneumonia_data_by_age_group_08.11.xlsx',0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=11,thousands=',')
    admissoes_gerais_total_tx = admissoes_gerais_total_tx.astype(float)

    pneumonia_percent_total_tx = round((admissoes_total_tx/admissoes_gerais_total_tx)*100,1)

    pneumonia_percent_total_transposed = pneumonia_percent_total_tx.T
    pneumonia_percent_total_transposed.columns = ["percent"]
    pneumonia_percent_total_transposed["year"] = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace( 
        go.Bar(x = years,y =admissoes_total["count"],name="Admissions",),
        secondary_y=False,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["percent"],name="Admissions_Percent"),
        secondary_y=True,
    )

    fig.update_layout(
        title_text="Pneumonia Age-adjusted admissions and percentage of general admissions",
        template='simple_white',
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 2011,
            dtick = 1
        ),
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="<b>Age-adjusted Pneumonia admissions rate</b> ", secondary_y=False)
    fig.update_yaxes(title_text="<b>Percentage of Pneumonia cases</b>", secondary_y=True)

    return fig