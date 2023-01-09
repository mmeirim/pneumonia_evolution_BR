import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

file_path = Path(__file__).parents[2] / 'tables/Pneumonia_data_by_age_group.xlsx'

def graph_pneumocom_lethality():
    years = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]

    admissoes_total = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=22,thousands=',')
    admissoes_total = admissoes_total.astype(float)

    admissoes_non_elderly = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=37,thousands=',')
    admissoes_non_elderly = admissoes_non_elderly.astype(float)

    admissoes_elderly = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=40,thousands=',')
    admissoes_elderly = admissoes_elderly.astype(float)

    admissoes_icu = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=23,thousands=',')
    admissoes_icu = admissoes_icu.astype(float)

    admissoes_icu_non_elderly = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=38,thousands=',')
    admissoes_icu_non_elderly = admissoes_icu_non_elderly.astype(float)

    admissoes_icu_elderly = pd.read_excel(file_path,3, header=None, nrows=1, usecols="B:J,P:Q",skiprows=41,thousands=',')
    admissoes_icu_elderly = admissoes_icu_elderly.astype(float)

    letalidade_icu = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=15,thousands=',')
    letalidade_icu = round(letalidade_icu.astype(float)*100,1)
    letalidade_icu = letalidade_icu.T
    letalidade_icu.columns = ["count"]
    letalidade_icu["year"] = years

    letalidade_icu_non_elderly = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=20,thousands=',')
    letalidade_icu_non_elderly = round(letalidade_icu_non_elderly.astype(float)*100,1)
    letalidade_icu_non_elderly = letalidade_icu_non_elderly.T
    letalidade_icu_non_elderly.columns = ["count"]
    letalidade_icu_non_elderly["year"] = years

    letalidade_icu_elderly = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=21,thousands=',')
    letalidade_icu_elderly = round(letalidade_icu_elderly.astype(float)*100,1)
    letalidade_icu_elderly = letalidade_icu_elderly.T
    letalidade_icu_elderly.columns = ["count"]
    letalidade_icu_elderly["year"] = years

    letalidade_non_icu = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=8,thousands=',')
    letalidade_non_icu = round(letalidade_non_icu.astype(float)*100,1)
    letalidade_non_icu = letalidade_non_icu.T
    letalidade_non_icu.columns = ["count"]
    letalidade_non_icu["year"] = years

    letalidade_non_icu_non_elderly = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=13,thousands=',')
    letalidade_non_icu_non_elderly = round(letalidade_non_icu_non_elderly.astype(float)*100,1)
    letalidade_non_icu_non_elderly = letalidade_non_icu_non_elderly.T
    letalidade_non_icu_non_elderly.columns = ["count"]
    letalidade_non_icu_non_elderly["year"] = years

    letalidade_non_icu_elderly = pd.read_excel(file_path,4, header=None, nrows=1, usecols="B:J,P:Q",skiprows=14,thousands=',')
    letalidade_non_icu_elderly = round(letalidade_non_icu_elderly.astype(float)*100,1)
    letalidade_non_icu_elderly = letalidade_non_icu_elderly.T
    letalidade_non_icu_elderly.columns = ["count"]
    letalidade_non_icu_elderly["year"] = years


    total_percent = round((admissoes_icu/admissoes_total)*100,1)

    total_percent_transposed = total_percent.T
    total_percent_transposed.columns = ["percent"]
    total_percent_transposed["non-elderly"] = round((admissoes_icu_non_elderly/admissoes_non_elderly)*100,1).T
    total_percent_transposed["elderly"] = round((admissoes_icu_elderly/admissoes_elderly)*100,1).T
    total_percent_transposed["year"] = years

    fig = make_subplots(rows=1, cols=3, subplot_titles=("All", "Non elderly", "Elderly"), specs=[[{"secondary_y": True},{"secondary_y": True},{"secondary_y": True}]])
    fig.add_trace( 
        go.Bar(x = years,y =total_percent_transposed["percent"],name="ICU occupation (%)",legendgroup="group1",legendgrouptitle_text="First Graph"),
        secondary_y=False,
        row=1, col=1,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_icu["count"],name="ICU Lethality",legendgroup="group1"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_non_icu["count"],name="Non ICU Lethality",legendgroup="group1"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace( 
        go.Bar(x = years,y =total_percent_transposed["non-elderly"],name="ICU occupation (%)",legendgroup="group2",legendgrouptitle_text="Second Graph"),
        secondary_y=False,
        row=1, col=2,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_icu_non_elderly ["count"],name="ICU Lethality",legendgroup="group2"),
        secondary_y=True,
        row=1, col=2,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_non_icu_non_elderly ["count"],name="Non ICU Lethality",legendgroup="group2"),
        secondary_y=True,
        row=1, col=2,
    )

    fig.add_trace( 
        go.Bar(x = years,y =total_percent_transposed["elderly"],name="ICU occupation (%)",legendgroup="group3", legendgrouptitle_text="Third Graph",),
        secondary_y=False,
        row=1, col=3,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_icu_elderly["count"],name="ICU Lethality",legendgroup="group3"),
        secondary_y=True,
        row=1, col=3,
    )

    fig.add_trace(
        go.Line(x = years,y = letalidade_non_icu_elderly["count"],name="Non ICU Lethality",legendgroup="group3"),
        secondary_y=True,
        row=1, col=3,
    )

    fig.update_layout(
        title_text="Pneumonia ICU occupation and lethality by age group",
        template='simple_white',
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 2011,
            dtick = 1
        ),
        # legend = dict(
        #     orientation="v",
        #     yanchor="top",
        #     y=0.9,
        #     xanchor="right",
        #     x=1.12
        # )
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="<b>Pneumonia ICU occupation percentage</b> ", secondary_y=False,)
    fig.update_yaxes(title_text="<b>Pneumonia Lethality rate</b>", secondary_y=True)

    return fig

def graph_pneumocom_admissions():
    years = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]

    admissoes_total = pd.read_excel(file_path,2, header=None, nrows=1, usecols="B:J,P:Q",skiprows=8,thousands=',')
    admissoes_total = admissoes_total.astype(float)
    admissoes_total = admissoes_total.T
    admissoes_total.columns = ["count"]
    admissoes_total["year"] = years

    admissoes_non_elderly = pd.read_excel(file_path,2, header=None, nrows=1, usecols="B:J,P:Q",skiprows=13,thousands=',')
    admissoes_non_elderly = admissoes_non_elderly.astype(float)
    admissoes_non_elderly = admissoes_non_elderly.T
    admissoes_non_elderly.columns = ["count"]
    admissoes_non_elderly["year"] = years

    admissoes_elderly = pd.read_excel(file_path,2, header=None, nrows=1, usecols="B:J,P:Q",skiprows=14,thousands=',')
    admissoes_elderly = admissoes_elderly.astype(float)
    admissoes_elderly = admissoes_elderly.T
    admissoes_elderly.columns = ["count"]
    admissoes_elderly["year"] = years


    fig = make_subplots()

    fig.add_trace(
        go.Line(x = years,y = admissoes_total["count"],name="All"),
    )

    fig.add_trace(
        go.Line(x = years,y = admissoes_non_elderly["count"],name="Non Elderly"),
    )

    fig.add_trace(
        go.Line(x = years,y = admissoes_elderly["count"],name="Elderly"),
    )

    fig.add_vline(x=8, line_width=1, line_dash="dash", line_color="black")


    fig.update_layout(
        title_text="Pneumonia Age-adjusted admissions",
        template='simple_white',
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 2011,
            dtick = 1
        ),
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="<b>Age-adjusted Pneumonia admissions rate</b> ")

    return fig

def graph_pneumocom_percent_of_general_admissions():
    years = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]
    admissoes_total = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=16,thousands=',')
    admissoes_total = admissoes_total.astype(float)

    admissoes_non_elderly = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=26,thousands=',')
    admissoes_non_elderly = admissoes_non_elderly.astype(float)

    admissoes_elderly = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=28,thousands=',')
    admissoes_elderly = admissoes_elderly.astype(float)

    admissoes_gerais_total_tx = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=15,thousands=',')
    admissoes_gerais_total_tx = admissoes_gerais_total_tx.astype(float)

    admissoes_gerais_non_elderly = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=25,thousands=',')
    admissoes_gerais_non_elderly = admissoes_gerais_non_elderly.astype(float)

    admissoes_gerais_elderly = pd.read_excel(file_path,0, header=None, nrows=1, usecols="B:J,P:Q",skiprows=27,thousands=',')
    admissoes_gerais_elderly = admissoes_gerais_elderly.astype(float)

    pneumonia_percent_total_tx = round((admissoes_total/admissoes_gerais_total_tx)*100,1)

    pneumonia_percent_total_transposed = pneumonia_percent_total_tx.T
    pneumonia_percent_total_transposed.columns = ["percent"]
    pneumonia_percent_total_transposed["non-elderly"] = round((admissoes_non_elderly/admissoes_gerais_non_elderly)*100,1).T
    pneumonia_percent_total_transposed["elderly"] = round((admissoes_elderly/admissoes_gerais_elderly)*100,1).T
    pneumonia_percent_total_transposed["year"] = years

    admissoes_total = admissoes_total.T
    admissoes_total.columns = ["count"]
    admissoes_total["year"] = years

    admissoes_non_elderly = admissoes_non_elderly.T
    admissoes_non_elderly.columns = ["count"]
    admissoes_non_elderly["year"] = years

    admissoes_elderly = admissoes_elderly.T
    admissoes_elderly.columns = ["count"]
    admissoes_elderly["year"] = years
    
    fig = make_subplots(rows=1, cols=3, subplot_titles=("All", "Non elderly", "Elderly"), specs=[[{"secondary_y": True},{"secondary_y": True},{"secondary_y": True}]])    
    fig.add_trace( 
        go.Bar(x = years,y =admissoes_total["count"],name="Pneumonia Admissions",legendgroup="group1",legendgrouptitle_text="First Graph"),
        secondary_y=False,
        row=1, col=1,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["percent"],name="Pneumonia Admissions (%)",legendgroup="group1"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace( 
        go.Bar(x = years,y =admissoes_non_elderly["count"],name="Pneumonia Admissions",legendgroup="group2",legendgrouptitle_text="Second Graph"),
        secondary_y=False,
        row=1, col=2,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["non-elderly"],name="Pneumonia Admissions (%)",legendgroup="group2"),
        secondary_y=True,
        row=1, col=2,
    )

    fig.add_trace( 
        go.Bar(x = years,y =admissoes_elderly["count"],name="Pneumonia Admissions",legendgroup="group3", legendgrouptitle_text="Third Graph",),
        secondary_y=False,
        row=1, col=3,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["elderly"],name="Pneumonia Admissions (%)",legendgroup="group3"),
        secondary_y=True,
        row=1, col=3,
    )

    fig.update_layout(
        title_text="Pneumonia Age-adjusted admissions and percentage of general admissions",
        template='simple_white',
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 2011,
            dtick = 1
        ),
        # legend = dict(
        #     orientation="v",
        #     yanchor="top",
        #     y=0.8,
        #     xanchor="right",
        #     x=1.12
        # )
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="<b>Age-adjusted admissions rate</b> ", secondary_y=False,)
    fig.update_yaxes(title_text="<b>Percentage cases</b>", secondary_y=True)

    return fig


def graph_pneumocom_percent_of_general_admissions_icu():
    years = ["2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021"]
    admissoes_total = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=16,thousands=',')
    admissoes_total = admissoes_total.astype(float)

    admissoes_non_elderly = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=26,thousands=',')
    admissoes_non_elderly = admissoes_non_elderly.astype(float)

    admissoes_elderly = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=28,thousands=',')
    admissoes_elderly = admissoes_elderly.astype(float)

    admissoes_gerais_total_tx = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=15,thousands=',')
    admissoes_gerais_total_tx = admissoes_gerais_total_tx.astype(float)

    admissoes_gerais_non_elderly = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=25,thousands=',')
    admissoes_gerais_non_elderly = admissoes_gerais_non_elderly.astype(float)

    admissoes_gerais_elderly = pd.read_excel(file_path,1, header=None, nrows=1, usecols="B:J,P:Q",skiprows=27,thousands=',')
    admissoes_gerais_elderly = admissoes_gerais_elderly.astype(float)

    pneumonia_percent_total_tx = round((admissoes_total/admissoes_gerais_total_tx)*100,1)

    pneumonia_percent_total_transposed = pneumonia_percent_total_tx.T
    pneumonia_percent_total_transposed.columns = ["percent"]
    pneumonia_percent_total_transposed["non-elderly"] = round((admissoes_non_elderly/admissoes_gerais_non_elderly)*100,1).T
    pneumonia_percent_total_transposed["elderly"] = round((admissoes_elderly/admissoes_gerais_elderly)*100,1).T
    pneumonia_percent_total_transposed["year"] = years

    admissoes_total = admissoes_total.T
    admissoes_total.columns = ["count"]
    admissoes_total["year"] = years

    admissoes_non_elderly = admissoes_non_elderly.T
    admissoes_non_elderly.columns = ["count"]
    admissoes_non_elderly["year"] = years

    admissoes_elderly = admissoes_elderly.T
    admissoes_elderly.columns = ["count"]
    admissoes_elderly["year"] = years
    
    fig = make_subplots(rows=1, cols=3, subplot_titles=("All", "Non elderly", "Elderly"), specs=[[{"secondary_y": True},{"secondary_y": True},{"secondary_y": True}]])    
    fig.add_trace( 
        go.Bar(x = years,y =admissoes_total["count"],name="ICU Pneumonia Admissions",legendgroup="group1",legendgrouptitle_text="First Graph"),
        secondary_y=False,
        row=1, col=1,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["percent"],name="ICU Pneumonia Admissions (%)",legendgroup="group1"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace( 
        go.Bar(x = years,y =admissoes_non_elderly["count"],name="ICU Pneumonia Admissions",legendgroup="group2",legendgrouptitle_text="Second Graph"),
        secondary_y=False,
        row=1, col=2,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["non-elderly"],name="ICU Pneumonia Admissions (%)",legendgroup="group2"),
        secondary_y=True,
        row=1, col=2,
    )

    fig.add_trace( 
        go.Bar(x = years,y =admissoes_elderly["count"],name="ICU Pneumonia Admissions",legendgroup="group3", legendgrouptitle_text="Third Graph",),
        secondary_y=False,
        row=1, col=3,
    )

    fig.add_trace(
        go.Line(x = years,y = pneumonia_percent_total_transposed["elderly"],name="ICU Pneumonia Admissions (%)",legendgroup="group3"),
        secondary_y=True,
        row=1, col=3,
    )

    fig.update_layout(
        title_text="Pneumonia Age-adjusted admissions and percentage of general admissions",
        template='simple_white',
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 2011,
            dtick = 1
        ),
        # legend = dict(
        #     orientation="v",
        #     yanchor="top",
        #     y=0.8,
        #     xanchor="right",
        #     x=1.12
        # )
    )

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="<b>Age-adjusted admissions rate</b> ", secondary_y=False,)
    fig.update_yaxes(title_text="<b>Percentage cases</b>", secondary_y=True)

    return fig