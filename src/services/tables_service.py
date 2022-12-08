import services.statistics_service as statistics_service
import pandas as pd

def generate_overview_table(base,begin_year,last_year):

    # VALORES BRUTOS 

    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_20_49 = base[base['classificacao'] == 1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_50_59 = base[base['classificacao'] == 2].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_60_69 = base[base['classificacao'] == 3].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_70_up = base[base['classificacao'] == 4].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_elderly = base[base['classificacao'].isin([1,2])].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_elderly = base[base['classificacao'].isin([3,4])].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    admissoes_uti_total = base[base['uti']==1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_uti_20_49 = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_50_59 = base[(base['uti']==1) & (base['classificacao'] == 2)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_60_69 = base[(base['uti']==1) & (base['classificacao'] == 3)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_70_up = base[(base['uti']==1) & (base['classificacao'] == 4)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_non_elderly = base[(base['uti']==1) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_uti_elderly = base[(base['uti']==1) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    admissoes_non_uti_total = base[base['uti']==0].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_non_uti_20_49 = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_50_59 = base[(base['uti']==0) & (base['classificacao'] == 2)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_60_69 = base[(base['uti']==0) & (base['classificacao'] == 3)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_70_up = base[(base['uti']==0) & (base['classificacao'] == 4)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_non_elderly = base[(base['uti']==0) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_elderly = base[(base['uti']==0) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'}).reset_index()

    mortes_20_49 = base[(base['morte']==1) & (base['classificacao'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_50_59 = base[(base['morte']==1) & (base['classificacao'] == 2)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_60_69 = base[(base['morte']==1) & (base['classificacao'] == 3)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_70_up = base[(base['morte']==1) & (base['classificacao'] == 4)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_non_elderly = base[(base['morte']==1) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_elderly = base[(base['morte']==1) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    lst_dfs = [admissoes_total,
                mortes_total,
                admissoes_uti_total,
                admissoes_non_uti_total,
                admissoes_20_49,
                admissoes_50_59,
                admissoes_60_69,
                admissoes_70_up,
                admissoes_non_elderly,
                admissoes_elderly,
                admissoes_uti_20_49,
                admissoes_uti_50_59,
                admissoes_uti_60_69,
                admissoes_uti_70_up,
                admissoes_uti_non_elderly,
                admissoes_uti_elderly,
                admissoes_non_uti_20_49,
                admissoes_non_uti_50_59,
                admissoes_non_uti_60_69,
                admissoes_non_uti_70_up,
                admissoes_non_uti_non_elderly,
                admissoes_non_uti_elderly,
                mortes_20_49,
                mortes_50_59,
                mortes_60_69,
                mortes_70_up,
                mortes_non_elderly,
                mortes_elderly]

    lst_nomes = ['Admissions',
                'Deaths',
                'Admissions_uti',
                'Admissions_non_uti',
                'Admissions_20_49',
                'Admissions_50_59',
                'Admissions_60_69',
                'Admissions_70_up',
                'Admissions_non_elderly',
                'Admissions_elderly',
                'Admissions_uti_20_49',
                'Admissions_uti_50_59',
                'Admissions_uti_60_69',
                'Admissions_uti_70_up',
                'Admissions_uti_non_elderly',
                'Admissions_uti_elderly',
                'Admissions_non_uti_20_49',
                'Admissions_non_uti_50_59',
                'Admissions_non_uti_60_69',
                'Admissions_non_uti_70_up',
                'Admissions_non_uti_non_elderly',
                'Admissions_non_uti_elderly',
                'Mortes_20_49',
                'Mortes_50_59',
                'Mortes_60_69',
                'Mortes_70_up',
                'Mortes_non_elderly',
                'Mortes_elderly']

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

def generate_100k_rates_table(base,dfWHO,pop_ref,begin_year,last_year):
    # TAXAS POR 100 mil
    admissoes_total_tx = base.groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_total_tx_adjusted = statistics_service.age_adjust(admissoes_total_tx,dfWHO,pop_ref)

    admissoes_uti_total_tx = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_uti_total_tx,dfWHO,pop_ref)

    admissoes_non_uti_total_tx = base[base['uti']==0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_non_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_total_tx,dfWHO,pop_ref)

    admissoes_20_49_tx = base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_20_49_tx,dfWHO,pop_ref)

    admissoes_50_59_tx = base[base['classificacao'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_50_59_tx,dfWHO,pop_ref)

    admissoes_60_69_tx = base[base['classificacao'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_60_69_tx,dfWHO,pop_ref)

    admissoes_70_up_tx = base[base['classificacao'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_70_up_tx,dfWHO,pop_ref)

    admissoes_non_elderly_tx = base[base['classificacao'].isin([1,2])].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_non_elderly_tx,dfWHO,pop_ref)

    admissoes_elderly_tx = base[base['classificacao'].isin([3,4])].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_elderly_tx,dfWHO,pop_ref)

    # ICU ADMISSIONS #
    admissoes_uti_20_49_tx = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_uti_20_49_tx,dfWHO,pop_ref)

    admissoes_uti_50_59_tx = base[(base['uti']==1) & (base['classificacao'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_uti_50_59_tx,dfWHO,pop_ref)

    admissoes_uti_60_69_tx = base[(base['uti']==1) & (base['classificacao'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_uti_60_69_tx,dfWHO,pop_ref)

    admissoes_uti_70_up_tx = base[(base['uti']==1) & (base['classificacao'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_uti_70_up_tx,dfWHO,pop_ref)

    admissoes_uti_non_elderly_tx = base[(base['uti']==1) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_uti_non_elderly_tx,dfWHO,pop_ref)

    admissoes_uti_elderly_tx = base[(base['uti']==1) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_uti_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_uti_elderly_tx,dfWHO,pop_ref)

    # NON ICU ADMISSIONS #
    admissoes_non_uti_20_49_tx = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_20_49_tx,dfWHO,pop_ref)

    admissoes_non_uti_50_59_tx = base[(base['uti']==0) & (base['classificacao'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_50_59_tx,dfWHO,pop_ref)

    admissoes_non_uti_60_69_tx = base[(base['uti']==0) & (base['classificacao'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_60_69_tx,dfWHO,pop_ref)

    admissoes_non_uti_70_up_tx = base[(base['uti']==0) & (base['classificacao'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_70_up_tx,dfWHO,pop_ref)

    admissoes_non_uti_non_elderly_tx = base[(base['uti']==0) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_non_elderly_tx,dfWHO,pop_ref)

    admissoes_non_uti_elderly_tx = base[(base['uti']==0) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_non_uti_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_non_uti_elderly_tx,dfWHO,pop_ref)

    # DEATHS #
    mortes_total_tx = base[(base['morte']==1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_total_tx_adjusted = statistics_service.age_adjust(mortes_total_tx,dfWHO,pop_ref)

    mortes_20_49_tx = base[(base['morte']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_20_49_tx_adjusted = statistics_service.age_adjust(mortes_20_49_tx,dfWHO,pop_ref)

    mortes_50_59_tx = base[(base['morte']==1) & (base['classificacao'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_50_59_tx_adjusted = statistics_service.age_adjust(mortes_50_59_tx,dfWHO,pop_ref)

    mortes_60_69_tx = base[(base['morte']==1) & (base['classificacao'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_60_69_tx_adjusted = statistics_service.age_adjust(mortes_60_69_tx,dfWHO,pop_ref)

    mortes_70_up_tx = base[(base['morte']==1) & (base['classificacao'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_70_up_tx_adjusted = statistics_service.age_adjust(mortes_70_up_tx,dfWHO,pop_ref)

    mortes_non_elderly_tx = base[(base['morte']==1) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_non_elderly_tx_adjusted = statistics_service.age_adjust(mortes_non_elderly_tx,dfWHO,pop_ref)

    mortes_elderly_tx = base[(base['morte']==1) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_elderly_tx_adjusted = statistics_service.age_adjust(mortes_elderly_tx,dfWHO,pop_ref)

    lst_dfs = [admissoes_total_tx_adjusted,
                mortes_total_tx_adjusted,
                admissoes_uti_total_tx_adjusted,
                admissoes_non_uti_total_tx_adjusted,
                admissoes_20_49_tx_adjusted,
                admissoes_50_59_tx_adjusted,
                admissoes_60_69_tx_adjusted,
                admissoes_70_up_tx_adjusted,
                admissoes_non_elderly_tx_adjusted,
                admissoes_elderly_tx_adjusted,
                admissoes_uti_20_49_tx_adjusted,
                admissoes_uti_50_59_tx_adjusted,
                admissoes_uti_60_69_tx_adjusted,
                admissoes_uti_70_up_tx_adjusted,
                admissoes_uti_non_elderly_tx_adjusted,
                admissoes_uti_elderly_tx_adjusted,
                admissoes_non_uti_20_49_tx_adjusted,
                admissoes_non_uti_50_59_tx_adjusted,
                admissoes_non_uti_60_69_tx_adjusted,
                admissoes_non_uti_70_up_tx_adjusted,
                admissoes_non_uti_non_elderly_tx_adjusted,
                admissoes_non_uti_elderly_tx_adjusted,
                mortes_20_49_tx_adjusted,
                mortes_50_59_tx_adjusted,
                mortes_60_69_tx_adjusted,
                mortes_70_up_tx_adjusted,
                mortes_non_elderly_tx_adjusted,
                mortes_elderly_tx_adjusted]

    lst_nomes = ['Admissions_Tx',
                'Mortality_Tx',
                'Admissions_uti_Tx',
                'Admissions_non_uti_Tx',
                'Admissions_20_49_Tx',
                'Admissions_50_59_Tx',
                'Admissions_60_69_Tx',
                'Admissions_70_up_Tx',
                'Admissions_non_elderly_Tx',
                'Admissions_elderly_Tx',
                'Admissions_uti_20_49_Tx',
                'Admissions_uti_50_59_Tx',
                'Admissions_uti_60_69_Tx',
                'Admissions_uti_70_up_Tx',
                'Admissions_uti_non_elderly_Tx',
                'Admissions_uti_elderly_Tx',
                'Admissions_non_uti_20_49_Tx',
                'Admissions_non_uti_50_59_Tx',
                'Admissions_non_uti_60_69_Tx',
                'Admissions_non_uti_70_up_Tx',
                'Admissions_non_uti_non_elderly_Tx',
                'Admissions_non_uti_elderly_Tx',
                'Mortes_20_49_Tx',
                'Mortes_50_59_Tx',
                'Mortes_60_69_Tx',
                'Mortes_70_up_Tx',
                'Mortes_non_elderly_Tx',
                'Mortes_elderly_Tx']

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
    
    letalidade_20_49 = base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_20_49_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_20_49)

    letalidade_50_59 = base[base['classificacao'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_50_59_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_50_59)

    letalidade_60_69 = base[base['classificacao'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_60_69_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_60_69)

    letalidade_70_up = base[base['classificacao'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_70_up_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_70_up)

    letalidade_non_elderly = base[base['classificacao'].isin([1,2])].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_elderly)

    letalidade_elderly = base[base['classificacao'].isin([3,4])].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_elderly)

    # ICU LETHALITY #
    letalidade_uti = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti)

    letalidade_uti_20_49 = base[(base['uti']==1) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_20_49_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_20_49)

    letalidade_uti_50_59 = base[(base['uti']==1) & (base['classificacao'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_50_59_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_50_59)

    letalidade_uti_60_69 = base[(base['uti']==1) & (base['classificacao'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_60_69_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_60_69)

    letalidade_uti_70_up = base[(base['uti']==1) & (base['classificacao'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_70_up_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_70_up)

    letalidade_uti_non_elderly = base[(base['uti']==1) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_non_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_non_elderly)

    letalidade_uti_elderly = base[(base['uti']==1) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_uti_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_uti_elderly)

    # NON ICU LETHALITY #
    letalidade_non_uti = base[base['uti']==0].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti)

    letalidade_non_uti_20_49 = base[(base['uti']==0) & (base['classificacao'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_20_49_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_20_49)

    letalidade_non_uti_50_59 = base[(base['uti']==0) & (base['classificacao'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_50_59_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_50_59)

    letalidade_non_uti_60_69 = base[(base['uti']==0) & (base['classificacao'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_60_69_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_60_69)

    letalidade_non_uti_70_up = base[(base['uti']==0) & (base['classificacao'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_70_up_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_70_up)

    letalidade_non_uti_non_elderly = base[(base['uti']==0) & (base['classificacao'].isin([1,2]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_non_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_non_elderly)

    letalidade_non_uti_elderly = base[(base['uti']==0) & (base['classificacao'].isin([3,4]))].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    letalidade_non_uti_elderly_tx_adjusted = statistics_service.age_adjust_lethality(dfWHO,letalidade_non_uti_elderly)

    lst_dfs = [letalidade_total_tx_adjusted,
                letalidade_uti_tx_adjusted,
                letalidade_non_uti_tx_adjusted,
                letalidade_20_49_tx_adjusted,
                letalidade_50_59_tx_adjusted,
                letalidade_60_69_tx_adjusted,
                letalidade_70_up_tx_adjusted,
                letalidade_non_elderly_tx_adjusted,
                letalidade_elderly_tx_adjusted,
                letalidade_uti_20_49_tx_adjusted,
                letalidade_uti_50_59_tx_adjusted,
                letalidade_uti_60_69_tx_adjusted,
                letalidade_uti_70_up_tx_adjusted,
                letalidade_uti_non_elderly_tx_adjusted,
                letalidade_uti_elderly_tx_adjusted,
                letalidade_non_uti_20_49_tx_adjusted,
                letalidade_non_uti_50_59_tx_adjusted,
                letalidade_non_uti_60_69_tx_adjusted,
                letalidade_non_uti_70_up_tx_adjusted,
                letalidade_non_uti_non_elderly_tx_adjusted,
                letalidade_non_uti_elderly_tx_adjusted,]

    lst_nomes = ['Lethality_tx',
                'Lethality_uti_tx',
                'Lethality_non_uti_Tx',
                'Lethality_20_49_tx',
                'Lethality_50_59_tx',
                'Lethality_60_69_tx',
                'Lethality_70_up_tx',
                'Lethality_non_elderly_tx',
                'Lethality_elderly_tx',
                'Lethality_uti_20_49_tx',
                'Lethality_uti_50_59_tx',
                'Lethality_uti_60_69_tx',
                'Lethality_uti_70_up_tx',
                'Lethality_uti_non_elderly_tx',
                'Lethality_uti_elderly_tx',
                'Lethality_non_uti_20_49_tx',
                'Lethality_non_uti_50_59_tx',
                'Lethality_non_uti_60_69_tx',
                'Lethality_non_uti_70_up_tx',
                'Lethality_non_uti_non_elderly_tx',
                'Lethality_non_uti_elderly_tx',
                ]

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

def generate_ICU_los_table(base,begin_year,last_year):
    los_uti_total =  base[base['uti']==1].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()

    los_uti_20_49 =  base[(base['classificacao'] == 1)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    los_uti_50_59 =  base[(base['classificacao'] == 2)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    los_uti_60_69 =  base[(base['classificacao'] == 3)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    los_uti_70_up =  base[(base['classificacao'] == 4)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()

    lst_dfs = [los_uti_total,
                los_uti_20_49,
                los_uti_50_59,
                los_uti_60_69,
                los_uti_70_up]

    lst_nomes = ['los_uti_total',
                'los_uti_20_49',
                'los_uti_50_59',
                'los_uti_60_69',
                'los_uti_70_up']

    table_aapc = statistics_service.aapc(lst_dfs[0],"""los_uti ~ ano_inter""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]
        
        expr = """los_uti ~ ano_inter"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc(df,expr,nome)])
    
    table_los_uti = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'ano_inter',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_los_uti)
    table_los_uti.to_excel('../tables/table_los_uti_'+str(begin_year)+'_'+str(last_year)+'.xlsx')
    return

def generate_CID_ranking(base,begin_year,last_year):
    print(sorted(base['diag_princ_trim_upper'].unique()))
    print((base['diag_princ_trim_upper'].nunique()))

    cids_ranking = base.groupby(['ano_inter','diag_princ_trim_upper']).agg({'id':'count'}).reset_index()
    cids_ranking.sort_values(by=['ano_inter','id'], ascending = [True, False],inplace=True)
    cids_ranking['percent'] = cids_ranking['id']/cids_ranking.groupby('ano_inter')['id'].transform('sum')
    cids_ranking.to_excel('../tables/cids_ranking_'+str(begin_year)+'_'+str(last_year)+'.xlsx')    
    return

def generate_general_admissions_table(base,begin_year,last_year):
    admissoes_gerais_uti_total =  base.groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()

    admissoes_gerais_uti_20_49 =  base[base['classificacao'] == 1].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_50_59 =  base[base['classificacao'] == 2].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_60_69 =  base[base['classificacao'] == 3].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_70_up =  base[base['classificacao'] == 4].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_non_elderly = base[base['classificacao'].isin([1,2])].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_elderly = base[base['classificacao'].isin([3,4])].groupby(['ano_inter']).agg({'utilizacao_uti':'sum'}).reset_index()


    admissoes_gerais_non_uti_total =  base.groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()

    admissoes_gerais_non_uti_20_49 =  base[base['classificacao'] == 1].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_50_59 =  base[base['classificacao'] == 2].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_60_69 =  base[base['classificacao'] == 3].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_70_up =  base[base['classificacao'] == 4].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_non_elderly = base[base['classificacao'].isin([1,2])].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_elderly = base[base['classificacao'].isin([3,4])].groupby(['ano_inter']).agg({'admissoes_nao_uti':'sum'}).reset_index()

    admissoes_gerais_total =  base.groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()

    admissoes_gerais_20_49 =  base[base['classificacao'] == 1].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_50_59 =  base[base['classificacao'] == 2].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_60_69 =  base[base['classificacao'] == 3].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_70_up =  base[base['classificacao'] == 4].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_non_elderly = base[base['classificacao'].isin([1,2])].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_elderly = base[base['classificacao'].isin([3,4])].groupby(['ano_inter']).agg({'admissoes':'sum'}).reset_index()

    lst_dfs = [admissoes_gerais_total,
                admissoes_gerais_uti_total,
                admissoes_gerais_non_uti_total,
                admissoes_gerais_20_49,
                admissoes_gerais_uti_20_49,
                admissoes_gerais_non_uti_20_49,
                admissoes_gerais_50_59,
                admissoes_gerais_uti_50_59,
                admissoes_gerais_non_uti_50_59,
                admissoes_gerais_60_69,
                admissoes_gerais_uti_60_69,
                admissoes_gerais_non_uti_60_69,
                admissoes_gerais_70_up,
                admissoes_gerais_uti_70_up,
                admissoes_gerais_non_uti_70_up,
                admissoes_gerais_non_elderly,
                admissoes_gerais_uti_non_elderly,
                admissoes_gerais_non_uti_non_elderly,
                admissoes_gerais_elderly,
                admissoes_gerais_uti_elderly,
                admissoes_gerais_non_uti_elderly]

    lst_nomes = ['admissoes_gerais_total',
                'admissoes_gerais_uti_total',
                'admissoes_gerais_non_uti_total',
                'admissoes_gerais_20_49',
                'admissoes_gerais_uti_20_49',
                'admissoes_gerais_non_uti_20_49',
                'admissoes_gerais_50_59',
                'admissoes_gerais_uti_50_59',
                'admissoes_gerais_non_uti_50_59',
                'admissoes_gerais_60_69',
                'admissoes_gerais_uti_60_69',
                'admissoes_gerais_non_uti_60_69',
                'admissoes_gerais_70_up',
                'admissoes_gerais_uti_70_up',
                'admissoes_gerais_non_uti_70_up',
                'admissoes_gerais_non_elderly',
                'admissoes_gerais_uti_non_elderly',
                'admissoes_gerais_non_uti_non_elderly',
                'admissoes_gerais_elderly',
                'admissoes_gerais_uti_elderly',
                'admissoes_gerais_non_uti_elderly']

    table_aapc = statistics_service.aapc(lst_dfs[0],"""admissoes ~ ano_inter""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]

        if nome in ['admissoes_gerais_uti_total','admissoes_gerais_uti_20_49','admissoes_gerais_uti_50_59','admissoes_gerais_uti_60_69','admissoes_gerais_uti_70_up','admissoes_gerais_uti_non_elderly','admissoes_gerais_uti_elderly']:
            expr = """utilizacao_uti ~ ano_inter"""
        elif nome in ['admissoes_gerais_non_uti_total','admissoes_gerais_non_uti_20_49','admissoes_gerais_non_uti_50_59','admissoes_gerais_non_uti_60_69','admissoes_gerais_non_uti_70_up','admissoes_gerais_non_uti_non_elderly','admissoes_gerais_non_uti_elderly']:
            expr = """admissoes_nao_uti ~ ano_inter"""
        else:
            expr = """admissoes ~ ano_inter"""
                
        table_aapc = pd.concat([table_aapc,statistics_service.aapc(df,expr,nome)])
    
    table_admissoes_gerais = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'ano_inter',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_admissoes_gerais)
    table_admissoes_gerais.to_excel('../tables/table_general_admissions_'+str(begin_year)+'_'+str(last_year)+'.xlsx')
    return

def generate_general_admissions_100k_rates_table(base,dfWHO,pop_ref,begin_year,last_year):
    admissoes_gerais_uti_total_tx =  base.groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_total_tx,dfWHO,pop_ref)

    admissoes_gerais_uti_20_49_tx =  base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_20_49_tx,dfWHO,pop_ref)

    admissoes_gerais_uti_50_59_tx =  base[base['classificacao'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_50_59_tx,dfWHO,pop_ref)

    admissoes_gerais_uti_60_69_tx =  base[base['classificacao'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_60_69_tx,dfWHO,pop_ref)
    
    admissoes_gerais_uti_70_up_tx =  base[base['classificacao'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_70_up_tx,dfWHO,pop_ref)

    admissoes_gerais_uti_non_elderly_tx =  base[base['classificacao'].isin([1,2])].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_non_elderly_tx,dfWHO,pop_ref)

    admissoes_gerais_uti_elderly_tx =  base[base['classificacao'].isin([3,4])].groupby(['ano_inter','idade_grupo_who']).agg({'utilizacao_uti':'sum'}).reset_index()
    admissoes_gerais_uti_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_uti_elderly_tx,dfWHO,pop_ref)

    #NON ICU#
    admissoes_gerais_non_uti_total_tx =  base.groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_total_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_total_tx,dfWHO,pop_ref)

    admissoes_gerais_non_uti_20_49_tx =  base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_20_49_tx,dfWHO,pop_ref)

    admissoes_gerais_non_uti_50_59_tx =  base[base['classificacao'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_50_59_tx,dfWHO,pop_ref)

    admissoes_gerais_non_uti_60_69_tx =  base[base['classificacao'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_60_69_tx,dfWHO,pop_ref)
    
    admissoes_gerais_non_uti_70_up_tx =  base[base['classificacao'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_70_up_tx,dfWHO,pop_ref)

    admissoes_gerais_non_uti_non_elderly_tx =  base[base['classificacao'].isin([1,2])].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_non_elderly_tx,dfWHO,pop_ref)

    admissoes_gerais_non_uti_elderly_tx =  base[base['classificacao'].isin([3,4])].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes_nao_uti':'sum'}).reset_index()
    admissoes_gerais_non_uti_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_uti_elderly_tx,dfWHO,pop_ref)

    #ALL#

    admissoes_gerais_total_tx =  base.groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_total_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_total_tx,dfWHO,pop_ref)

    admissoes_gerais_20_49_tx =  base[base['classificacao'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_20_49_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_20_49_tx,dfWHO,pop_ref)

    admissoes_gerais_50_59_tx =  base[base['classificacao'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_50_59_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_50_59_tx,dfWHO,pop_ref)

    admissoes_gerais_60_69_tx =  base[base['classificacao'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_60_69_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_60_69_tx,dfWHO,pop_ref)
    
    admissoes_gerais_70_up_tx =  base[base['classificacao'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_70_up_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_70_up_tx,dfWHO,pop_ref)

    admissoes_gerais_non_elderly_tx =  base[base['classificacao'].isin([1,2])].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_non_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_non_elderly_tx,dfWHO,pop_ref)

    admissoes_gerais_elderly_tx =  base[base['classificacao'].isin([3,4])].groupby(['ano_inter','idade_grupo_who']).agg({'admissoes':'sum'}).reset_index()
    admissoes_gerais_elderly_tx_adjusted = statistics_service.age_adjust(admissoes_gerais_elderly_tx,dfWHO,pop_ref)

    lst_dfs = [admissoes_gerais_total_tx_adjusted,
                admissoes_gerais_uti_total_tx_adjusted,
                admissoes_gerais_non_uti_total_tx_adjusted,
                admissoes_gerais_20_49_tx_adjusted,
                admissoes_gerais_uti_20_49_tx_adjusted,
                admissoes_gerais_non_uti_20_49_tx_adjusted,
                admissoes_gerais_50_59_tx_adjusted,
                admissoes_gerais_uti_50_59_tx_adjusted,
                admissoes_gerais_non_uti_50_59_tx_adjusted,
                admissoes_gerais_60_69_tx_adjusted,
                admissoes_gerais_uti_60_69_tx_adjusted,
                admissoes_gerais_non_uti_60_69_tx_adjusted,
                admissoes_gerais_70_up_tx_adjusted,
                admissoes_gerais_uti_70_up_tx_adjusted,
                admissoes_gerais_non_uti_70_up_tx_adjusted,
                admissoes_gerais_non_elderly_tx_adjusted,
                admissoes_gerais_uti_non_elderly_tx_adjusted,
                admissoes_gerais_non_uti_non_elderly_tx_adjusted,
                admissoes_gerais_elderly_tx_adjusted,
                admissoes_gerais_uti_elderly_tx_adjusted,
                admissoes_gerais_non_uti_elderly_tx_adjusted,]

    lst_nomes = ['admissoes_gerais_total_tx_adjusted',
                'admissoes_gerais_uti_total_tx_adjusted',
                'admissoes_gerais_non_uti_total_tx_adjusted',
                'admissoes_gerais_20_49_tx_adjusted',
                'admissoes_gerais_uti_20_49_tx_adjusted',
                'admissoes_gerais_non_uti_20_49_tx_adjusted',
                'admissoes_gerais_50_59_tx_adjusted',
                'admissoes_gerais_uti_50_59_tx_adjusted',
                'admissoes_gerais_non_uti_50_59_tx_adjusted',
                'admissoes_gerais_60_69_tx_adjusted',
                'admissoes_gerais_uti_60_69_tx_adjusted',
                'admissoes_gerais_non_uti_60_69_tx_adjusted',
                'admissoes_gerais_70_up_tx_adjusted',
                'admissoes_gerais_uti_70_up_tx_adjusted',
                'admissoes_gerais_non_uti_70_up_tx_adjusted',
                'admissoes_gerais_non_elderly_tx_adjusted',
                'admissoes_gerais_uti_non_elderly_tx_adjusted',
                'admissoes_gerais_non_uti_non_elderly_tx_adjusted',
                'admissoes_gerais_elderly_tx_adjusted',
                'admissoes_gerais_uti_elderly_tx_adjusted',
                'admissoes_gerais_non_uti_elderly_tx_adjusted']

    table_aapc = statistics_service.aapc_offset(lst_dfs[0],"""taxa_ajd_qnt_Y ~ year""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]

        expr = """taxa_ajd_qnt_Y ~ year"""
                
        table_aapc = pd.concat([table_aapc,statistics_service.aapc_offset(df,expr,nome)])
    
    table_admissoes_gerais = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'year',begin_year,last_year),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_admissoes_gerais)
    table_admissoes_gerais.to_excel('../tables/table_general_100k_rates_'+str(begin_year)+'_'+str(last_year)+'.xlsx')
    return



