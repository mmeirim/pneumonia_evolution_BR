import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install','statsmodels'], stdout=subprocess.DEVNULL)
import math

import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices


def aapc(df,expr,name):
    y_train, X_train = dmatrices(expr, df, return_type='dataframe')
    poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()
    aapc_value = (math.exp(poisson_training_results.params["ano_inter"]) - 1)*100
    aapc_inf = (math.exp(poisson_training_results.conf_int().loc['ano_inter',0]) - 1)*100
    aapc_sup = (math.exp(poisson_training_results.conf_int().loc['ano_inter',1]) - 1)*100

    data = {'Analise': [name],
        'AAPC': [aapc_value],
        'IC_Inf': [aapc_inf],
        'IC_Sup': [aapc_sup]}
    df_results = pd.DataFrame(data)
    return df_results

def age_adjust_ML(df,dfWHO,pop_ref):
    
    df.columns = ['ano_inter','idade_grupo_who','num']
    df_merged = pd.merge(pop_ref, df,  how='left', left_on=['year','idade_grupo_who'], right_on=['ano_inter','idade_grupo_who']) # junta a quantidade por ano por faixa etária com a população de referencia
    df_merged['taxa'] = df_merged['num']/df_merged['population'] # calcula a taxa
    result = pd.merge(df_merged, dfWHO,  how='left', left_on=['idade_grupo_who'], right_on=['age_group']) # junta o dataframe com a proporção do WHO
    result['obitos_esp'] = result['taxa']*result['world_avg_dec'] # calcula a proporção da quantidade esperados
    df_result = result.groupby(['year']).agg({'num':'sum','obitos_esp':'sum','population':'sum','world_avg_dec':'sum'}).reset_index() # agrupa por ANO
    # tx = obts esp / pop
    #somar as faixas etarias do ano e dividir pela pop de ref total
    df_result['taxa_ajustada'] = df_result['obitos_esp']/df_result['world_avg_dec']
    df_result['taxa_ajustada_100mil'] = (df_result['taxa_ajustada']*100000).apply(np.ceil)
    df_result['taxa_bruta_100mil'] = (df_result['num']/df_result['population'])*100000
    df_result['taxa_ajd_qnt'] = df_result['obitos_esp']*df_result['population'] # calcula a quantidade para a populacao de referencia
    df_result['taxa_ajd_qnt_Y'] = df_result['taxa_ajd_qnt'].apply(np.ceil) # arredonda para ter um numero inteiro (count data)
    #df_result = result.groupby(['year']).agg({'taxa_ajd_qnt_Y':'sum','population':'sum'}).reset_index() # agrupa por ANO
    df_result_final = df_result[['year','population','taxa_ajd_qnt_Y','taxa_ajustada','taxa_ajustada_100mil','taxa_bruta_100mil']]
    return df_result_final


def age_adjust(df,dfWHO,pop_ref):

    df.columns = ['ano_inter','idade_grupo_who','num']
    df_merged = pd.merge(df,pop_ref,  how='left', left_on=['ano_inter','idade_grupo_who'], right_on=['year','idade_grupo_who']) # junta a quantidade por ano por faixa etária com a população de referencia
    df_merged['taxa'] = df_merged['num']/df_merged['population'] # calcula a taxa
    result = pd.merge(df_merged, dfWHO,  how='left', left_on=['idade_grupo_who'], right_on=['age_group']) # junta o dataframe com a proporção do WHO
    result['obitos_esp'] = result['taxa']*result['world_avg_dec'] # calcula a proporção da quantidade esperados
    df_result = result.groupby(['year']).agg({'num':'sum','obitos_esp':'sum','population':'sum','world_avg_dec':'sum'}).reset_index() # agrupa por ANO
    #    # tx = obts esp / pop
    #    #somar as faixas etarias do ano e dividir pela pop de ref total
    df_result['taxa_ajustada'] = df_result['obitos_esp']/df_result['world_avg_dec']
    df_result['taxa_ajustada_100mil'] = (df_result['taxa_ajustada']*100000).apply(np.ceil)
    df_result['taxa_bruta_100mil'] = (df_result['num']/df_result['population'])*100000
    df_result['taxa_ajd_qnt'] = df_result['obitos_esp']*df_result['population'] # calcula a quantidade para a populacao de referencia
    df_result['taxa_ajd_qnt_Y'] = df_result['taxa_ajd_qnt'].apply(np.ceil) # arredonda para ter um numero inteiro (count data)
    # #df_result = result.groupby(['year']).agg({'taxa_ajd_qnt_Y':'sum','population':'sum'}).reset_index() # agrupa por ANO
    df_result_final = df_result[['year','population','taxa_ajd_qnt_Y','taxa_ajustada_100mil']]
    return df_result_final

def aapc_offset(df,expr,name):
    y_train, X_train = dmatrices(expr, df, return_type='dataframe')
    poisson_training_results = sm.GLM(y_train, X_train, offset=np.log(df['population']), family=sm.families.Poisson()).fit()
    #print(poisson_training_results.summary())
    aapc_value = (math.exp(poisson_training_results.params["year"]) - 1)*100
    aapc_inf = (math.exp(poisson_training_results.conf_int().loc['year',0]) - 1)*100
    aapc_sup = (math.exp(poisson_training_results.conf_int().loc['year',1]) - 1)*100

    data = {'Analise': [name],
        'AAPC': [aapc_value],
        'IC_Inf': [aapc_inf],
        'IC_Sup': [aapc_sup]}
    df_results = pd.DataFrame(data)
    return df_results


def registros_ano(lst_dfs,lst_nomes,col_ano):

    df_first = lst_dfs[0].copy()
    nome = lst_nomes[0]

    if col_ano == 'year':
        df_first.drop('population',axis=1,inplace=True)
        df_first.drop('taxa_ajd_qnt_Y',axis=1,inplace=True)


    df_first = df_first.set_index(col_ano).T
    df_first['Analise'] = nome
    df_first['delta'] = ((df_first[2019] - df_first[2011])/df_first[2011])*100

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i].copy()
        nome = lst_nomes[i]

        if col_ano == 'year':
            df.drop('population',axis=1,inplace=True)
            df.drop('taxa_ajd_qnt_Y',axis=1,inplace=True)

        df = df.set_index(col_ano).T
        df['Analise'] = nome
        df['delta'] = ((df[2019] - df[2011])/df[2011])*100
    
        df_first = pd.concat([df_first,df])
    
    #df_first.drop(col_ano,axis=1,inplace=True)
    
    return df_first
