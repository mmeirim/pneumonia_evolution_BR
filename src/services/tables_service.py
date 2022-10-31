import services.statistics_service as statistics_service
import pandas as pd

def generate_overview_table(base,begin_year,last_year):

    # VALORES BRUTOS 

    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_S = base[base['regiao'] == 'S'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_N = base[base['regiao'] == 'N'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_NE = base[base['regiao'] == 'NE'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_SE = base[base['regiao'] == 'SE'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_CO = base[base['regiao'] == 'CO'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_uti_total = base[base['uti']==1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_uti_S = base[(base['uti']==1) & (base['regiao'] == 'S')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_N = base[(base['uti']==1) & (base['regiao'] == 'N')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_NE = base[(base['uti']==1) & (base['regiao'] == 'NE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_SE = base[(base['uti']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_CO = base[(base['uti']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_non_uti_total = base[base['uti']==0].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_non_uti_S = base[(base['uti']==0) & (base['regiao'] == 'S')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_N = base[(base['uti']==0) & (base['regiao'] == 'N')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_NE = base[(base['uti']==0) & (base['regiao'] == 'NE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_SE = base[(base['uti']==0) & (base['regiao'] == 'SE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_CO = base[(base['uti']==0) & (base['regiao'] == 'CO')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'}).reset_index()

    mortes_S = base[(base['morte']==1) & (base['regiao'] == 'S')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_N = base[(base['morte']==1) & (base['regiao'] == 'N')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_NE = base[(base['morte']==1) & (base['regiao'] == 'NE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_SE = base[(base['morte']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_CO = base[(base['morte']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    lst_dfs = [admissoes_total,admissoes_S,admissoes_N,admissoes_NE,admissoes_SE,admissoes_CO,mortes_total,mortes_S,mortes_N,mortes_NE,mortes_SE,
                mortes_CO,admissoes_uti_total,admissoes_uti_S,admissoes_uti_N,admissoes_uti_NE,admissoes_uti_SE,admissoes_uti_CO,
                admissoes_non_uti_total,admissoes_non_uti_S,admissoes_non_uti_N,admissoes_non_uti_NE,admissoes_non_uti_SE,admissoes_non_uti_CO]

    lst_nomes = ['Admissions','Admissions_S','Admissions_N','Admissions_NE','Admissions_SE','Admissions_CO','Deaths','Deaths_S','Deaths_N',
                    'Deaths_NE','Deaths_SE','Deaths_CO','Admissions_uti','Admissions_uti_S', 'Admissions_uti_N','Admissions_uti_NE',
                    'Admissions_uti_SE','Admissions_uti_CO','Admissions_non_uti','Admissions_non_uti_S','Admissions_non_uti_N',
                    'Admissions_non_uti_NE','Admissions_non_uti_SE','Admissions_non_uti_CO']

    table_aapc = statistics_service.aapc(lst_dfs[0],"""id ~ ano_inter""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]

        if nome in ['Deaths']:
            expr = """morte ~ ano_inter"""
        else:
            expr = """id ~ ano_inter"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc(df,expr,nome)])
    
    table_overview = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'ano_inter',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_overview)
    table_overview.to_excel('../tables/table_overview_'+str(begin_year)+'_'+str(last_year)+'.xlsx')
    return

def generate_100k_rates_table(base,dfWHO,pop_ref,pop_ref_by_sex,pop_ref_by_region,begin_year,last_year):
    # TAXAS POR 100 mil
    admissoes_total_tx = base.groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_total_tx_adjusted = statistics_service.age_adjust(admissoes_total_tx,dfWHO,pop_ref)

    admissoes_uti_total_tx = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_uti_total_tx,dfWHO,pop_ref)

    admissoes_non_uti_total_tx = base[base['uti']==0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_non_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_total_tx,dfWHO,pop_ref)

    admissoes_S_tx = base[base['regiao'] == 'S'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_S_tx_adjusted = statistics_service.age_adjust(admissoes_S_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='S'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_N_tx = base[base['regiao'] == 'N'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_N_tx_adjusted = statistics_service.age_adjust(admissoes_N_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='N'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_NE_tx = base[base['regiao'] == 'NE'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_NE_tx_adjusted = statistics_service.age_adjust(admissoes_NE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='NE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_SE_tx = base[base['regiao'] == 'SE'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_SE_tx_adjusted = statistics_service.age_adjust(admissoes_SE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='SE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_CO_tx = base[base['regiao'] == 'CO'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_CO_tx_adjusted = statistics_service.age_adjust(admissoes_CO_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='CW'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_uti_S_tx = base[(base['uti']==1) & (base['regiao'] == 'S')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_S_tx_adjusted = statistics_service.age_adjust(admissoes_uti_S_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='S'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_uti_N_tx = base[(base['uti']==1) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_N_tx_adjusted = statistics_service.age_adjust(admissoes_uti_N_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='N'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_uti_NE_tx = base[(base['uti']==1) & (base['regiao'] == 'NE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_NE_tx_adjusted = statistics_service.age_adjust(admissoes_uti_NE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='NE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_uti_SE_tx = base[(base['uti']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_SE_tx_adjusted = statistics_service.age_adjust(admissoes_uti_SE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='SE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_uti_CO_tx = base[(base['uti']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_CO_tx_adjusted = statistics_service.age_adjust(admissoes_uti_CO_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='CW'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_non_uti_S_tx = base[(base['uti']==0) & (base['regiao'] == 'S')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_S_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_S_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='S'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_non_uti_N_tx = base[(base['uti']==0) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_N_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_N_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='N'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_non_uti_NE_tx = base[(base['uti']==0) & (base['regiao'] == 'NE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_NE_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_NE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='NE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_non_uti_SE_tx = base[(base['uti']==0) & (base['regiao'] == 'SE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_SE_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_SE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='SE'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_non_uti_CO_tx = base[(base['uti']==0) & (base['regiao'] == 'CO')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_CO_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_CO_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='CW'].reset_index()[['year','idade_grupo_who','population']])
    
    mortes_total_tx = base[(base['morte']==1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_total_tx_adjusted = statistics_service.age_adjust(mortes_total_tx,dfWHO,pop_ref)

    mortes_S_tx = base[(base['morte']==1) & (base['regiao'] == 'S')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_S_tx_adjusted = statistics_service.age_adjust(mortes_S_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='S'].reset_index()[['year','idade_grupo_who','population']])

    mortes_N_tx = base[(base['morte']==1) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_N_tx_adjusted = statistics_service.age_adjust(mortes_N_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='N'].reset_index()[['year','idade_grupo_who','population']])

    mortes_NE_tx = base[(base['morte']==1) & (base['regiao'] == 'NE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_NE_tx_adjusted = statistics_service.age_adjust(mortes_NE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='NE'].reset_index()[['year','idade_grupo_who','population']])

    mortes_SE_tx = base[(base['morte']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_SE_tx_adjusted = statistics_service.age_adjust(mortes_SE_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='SE'].reset_index()[['year','idade_grupo_who','population']])

    mortes_CO_tx = base[(base['morte']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_CO_tx_adjusted = statistics_service.age_adjust(mortes_CO_tx,dfWHO,pop_ref_by_region[pop_ref_by_region['uf']=='CW'].reset_index()[['year','idade_grupo_who','population']])

    lst_dfs = [admissoes_total_tx_adjusted,admissoes_S_tx_adjusted,admissoes_N_tx_adjusted,admissoes_NE_tx_adjusted,admissoes_SE_tx_adjusted,
                admissoes_CO_tx_adjusted,mortes_total_tx_adjusted,mortes_S_tx_adjusted,mortes_N_tx_adjusted,mortes_NE_tx_adjusted,
                mortes_SE_tx_adjusted,mortes_CO_tx_adjusted,admissoes_uti_total_tx_adjusted,admissoes_uti_S_tx_adjusted,
                admissoes_uti_N_tx_adjusted,admissoes_uti_NE_tx_adjusted,admissoes_uti_SE_tx_adjusted,admissoes_uti_CO_tx_adjusted,
                admissoes_non_uti_total_tx_adjusted,admissoes_non_uti_S_tx_adjusted,admissoes_non_uti_N_tx_adjusted,
                admissoes_non_uti_NE_tx_adjusted,admissoes_non_uti_SE_tx_adjusted,admissoes_non_uti_CO_tx_adjusted]
    lst_nomes = ['Admissions_Tx','Admissions_S_Tx','Admissions_N_Tx','Admissions_NE_Tx','Admissions_SE_Tx','Admissions_CO_Tx','Mortality_Tx',
                    'Mortality_S_Tx','Mortality_N_Tx','Mortality_NE_Tx','Mortality_SE_Tx','Mortality_CO_Tx','Admissions_uti_Tx',
                    'Admissions_uti_S_Tx','Admissions_uti_N_Tx','Admissions_uti_NE_Tx','Admissions_uti_SE_Tx','Admissions_uti_CO_Tx',
                    'Admissions_non_uti_Tx','Admissions_non_uti_S_Tx','Admissions_non_uti_N_Tx','Admissions_non_uti_NE_Tx',
                    'Admissions_non_uti_SE_Tx','Admissions_non_uti_CO_Tx']

    table_aapc = statistics_service.aapc_offset(lst_dfs[0],"""taxa_ajd_qnt_Y ~ year""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]
        print(nome)
        expr = """taxa_ajd_qnt_Y ~ year"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc_offset(df,expr,nome)])
    
    table_100k_rates = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'year',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_100k_rates)
    table_100k_rates.to_excel('../tables/table_100k_rates_'+str(begin_year)+'_'+str(last_year)+'.xlsx')

    return

def generate_lethality_table(base,dfWHO,begin_year,last_year):
    letalidade_total = base.groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_total_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO, letalidade_total)

    letalidade_S = base[base['regiao'] == 'S'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_S_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_S)

    letalidade_N = base[base['regiao'] == 'N'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_N_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_N)

    letalidade_NE = base[base['regiao'] == 'N'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_NE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_NE)

    letalidade_SE = base[base['regiao'] == 'SE'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_SE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_SE)

    letalidade_CO = base[base['regiao'] == 'CO'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_CO_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_CO)

    letalidade_uti = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti)

    letalidade_uti_S = base[(base['uti']==1) & (base['regiao'] == 'S')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_S_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_S)

    letalidade_uti_N = base[(base['uti']==1) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_N_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_N)

    letalidade_uti_NE = base[(base['uti']==1) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_NE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_NE)

    letalidade_uti_SE = base[(base['uti']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_SE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_SE)

    letalidade_uti_CO = base[(base['uti']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_CO_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_CO)

    letalidade_non_uti = base[base['uti']==0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti)

    letalidade_non_uti_S = base[(base['uti']==0) & (base['regiao'] == 'S')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_S_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_S)

    letalidade_non_uti_N = base[(base['uti']==0) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_N_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_N)

    letalidade_non_uti_NE = base[(base['uti']==0) & (base['regiao'] == 'N')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_NE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_NE)

    letalidade_non_uti_SE = base[(base['uti']==0) & (base['regiao'] == 'SE')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_SE_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_SE)

    letalidade_non_uti_CO = base[(base['uti']==0) & (base['regiao'] == 'CO')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_CO_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_CO)


    lst_dfs = [letalidade_total_tx_adjusted,letalidade_S_tx_adjusted,letalidade_N_tx_adjusted,letalidade_NE_tx_adjusted,letalidade_SE_tx_adjusted,
                letalidade_CO_tx_adjusted,letalidade_uti_tx_adjusted,letalidade_uti_S_tx_adjusted,letalidade_uti_N_tx_adjusted,
                letalidade_uti_NE_tx_adjusted,letalidade_uti_SE_tx_adjusted,letalidade_uti_CO_tx_adjusted,letalidade_non_uti_tx_adjusted,
                letalidade_non_uti_S_tx_adjusted,letalidade_non_uti_N_tx_adjusted,letalidade_non_uti_NE_tx_adjusted,
                letalidade_non_uti_SE_tx_adjusted,letalidade_non_uti_CO_tx_adjusted]
    lst_nomes = ['Lethality_tx','Lethality_S_Tx','Lethality_N_Tx','Lethality_NE_Tx','Lethality_SE_Tx','Lethality_CO_Tx','Lethality_uti_tx',
                'Lethality_uti_S_Tx','Lethality_uti_N_Tx','Lethality_uti_NE_Tx','Lethality_uti_SE_Tx','Lethality_uti_CO_Tx','Lethality_non_uti_Tx',
                'Lethality_non_uti_S_Tx','Lethality_non_uti_N_Tx','Lethality_non_uti_NE_Tx','Lethality_non_uti_SE_Tx','Lethality_non_uti_CO_Tx']

    table_aapc = statistics_service.aapc_offset(lst_dfs[0],"""taxa_ajd_qnt_Y ~ year""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]
        print(nome)
        expr = """taxa_ajd_qnt_Y ~ year"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc_offset(df,expr,nome)])
    
    table_lethality_rates = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'year',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_lethality_rates)
    table_lethality_rates.to_excel('../tables/table_lethality_rates_'+str(begin_year)+'_'+str(last_year)+'.xlsx')


    return