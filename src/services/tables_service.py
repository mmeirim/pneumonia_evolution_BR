import services.statistics_service as statistics_service
import pandas as pd

def generate_overview_table(base,begin_year,last_year):

    # VALORES BRUTOS 

    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_eld = base[base['classificacao'] == 1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_eld = base[base['classificacao'] == 0].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    admissoes_uti_total = base[base['uti']==1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_uti_eld = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_non_eld = base[(base['uti']==1) & (base['classificacao'] == 0)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_non_uti_total = base[base['uti']==0].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_non_uti_eld = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_non_eld = base[(base['uti']==0) & (base['classificacao'] == 0)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'}).reset_index()

    mortes_eld = base[(base['morte']==1) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_non_eld = base[(base['morte']==1) & (base['classificacao'] == 0)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    lst_dfs = [admissoes_total,mortes_total,
                admissoes_uti_total,
                admissoes_non_uti_total,
                admissoes_eld,admissoes_non_eld,
                admissoes_uti_eld,
                admissoes_uti_non_eld,
                admissoes_non_uti_eld,
                admissoes_non_uti_non_eld,
                mortes_eld,
                mortes_non_eld]

    lst_nomes = ['Admissions',
                'Deaths',
                'Admissions_uti',
                'Admissions_non_uti',
                'Admissions_eld',
                'Admissions_non_eld',
                'Admissions_uti_eld',
                'Admissions_uti_non_eld',
                'Admissions_non_uti_eld',
                'Admissions_non_uti_non_eld',
                'Deaths_eld',
                'Deaths_non_eld']

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

    admissoes_eld_tx = base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_eld_tx_adjusted = statistics_service.age_adjust(admissoes_eld_tx,dfWHO,pop_ref)

    admissoes_non_eld_tx = base[base['classificacao'] == 0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_eld_tx_adjusted = statistics_service.age_adjust(admissoes_non_eld_tx,dfWHO,pop_ref)

    admissoes_uti_eld_tx = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_eld_tx_adjusted = statistics_service.age_adjust(admissoes_uti_eld_tx,dfWHO,pop_ref)

    admissoes_uti_non_eld_tx = base[(base['uti']==1) & (base['classificacao'] == 0)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_non_eld_tx_adjusted = statistics_service.age_adjust(admissoes_uti_non_eld_tx,dfWHO,pop_ref)

    admissoes_non_uti_eld_tx = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_eld_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_eld_tx,dfWHO,pop_ref)

    admissoes_non_uti_non_eld_tx = base[(base['uti']==0) & (base['classificacao'] == 0)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_non_eld_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_non_eld_tx,dfWHO,pop_ref)

    mortes_total_tx = base[(base['morte']==1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_total_tx_adjusted = statistics_service.age_adjust(mortes_total_tx,dfWHO,pop_ref)

    mortes_eld_tx = base[(base['morte']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_eld_tx_adjusted = statistics_service.age_adjust(mortes_eld_tx,dfWHO,pop_ref)

    mortes_non_eld_tx = base[(base['morte']==1) & (base['classificacao'] == 0)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_non_eld_tx_adjusted = statistics_service.age_adjust(mortes_non_eld_tx,dfWHO,pop_ref)

    lst_dfs = [admissoes_total_tx_adjusted,
                mortes_total_tx_adjusted,
                admissoes_uti_total_tx_adjusted,
                admissoes_non_uti_total_tx_adjusted,
                admissoes_eld_tx_adjusted,
                admissoes_non_eld_tx_adjusted,
                admissoes_uti_eld_tx_adjusted,
                admissoes_uti_non_eld_tx_adjusted,
                admissoes_non_uti_eld_tx_adjusted,
                admissoes_non_uti_non_eld_tx_adjusted,
                mortes_eld_tx_adjusted,
                mortes_non_eld_tx_adjusted]

    lst_nomes = ['Admissions_Tx',
                'Mortality_Tx',
                'Admissions_uti_Tx',
                'Admissions_non_uti_Tx',
                'Admissions_eld_Tx',
                'Admissions_non_eld_Tx',
                'Admissions_uti_eld_Tx',
                'Admissions_uti_non_eld_Tx',
                'Admissions_non_uti_eld_Tx',
                'Admissions_non_uti_non_eld_Tx',
                'Mortality_eld_Tx',
                'Mortality_non_eld_Tx']

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
    
    letalidade_eld = base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_eld)
    
    letalidade_non_eld = base[base['classificacao'] == 0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_eld)

    letalidade_uti = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti)

    letalidade_uti_eld = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_eld)
    
    letalidade_uti_non_eld = base[(base['uti']==1) & (base['classificacao'] == 0)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_non_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_non_eld)

    letalidade_non_uti = base[base['uti']==0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti)

    letalidade_non_uti_eld = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_eld)
    
    letalidade_non_uti_non_eld = base[(base['uti']==0) & (base['classificacao'] == 0)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_non_eld_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_non_eld)


    lst_dfs = [letalidade_total_tx_adjusted,
                letalidade_uti_tx_adjusted,
                letalidade_non_uti_tx_adjusted,
                letalidade_eld_tx_adjusted,
                letalidade_non_eld_tx_adjusted,
                letalidade_uti_eld_tx_adjusted,
                letalidade_uti_non_eld_tx_adjusted,
                letalidade_non_uti_eld_tx_adjusted,
                letalidade_non_uti_non_eld_tx_adjusted]

    lst_nomes = ['Lethality_tx',
                'Lethality_uti_tx',
                'Lethality_non_uti_Tx',
                'Lethality_eld_tx',
                'Lethality_non_eld_tx',
                'Lethality_uti_eld_tx',
                'Lethality_uti_non_eld_tx',
                'Lethality_non_uti_eld_tx',
                'Lethality_non_uti_non_eld_tx']

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