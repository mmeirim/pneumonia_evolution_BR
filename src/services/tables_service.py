import services.statistics_service as statistics_service
import pandas as pd

def generate_overview_table(base):

    # VALORES BRUTOS 

    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_homens = base[base['sexo'] == 1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_mulheres = base[base['sexo'] == 3].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_brancos = base[base['raca_cor'] == 1].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_pretos = base[base['raca_cor'] == 2].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_pardos = base[base['raca_cor'] == 3].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_amarelos = base[base['raca_cor'] == 4].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_indigenas = base[base['raca_cor'] == 5].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_seminfo = base[base['raca_cor'] == 99].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_S = base[base['regiao'] == 'S'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_N = base[base['regiao'] == 'N'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_NE = base[base['regiao'] == 'NE'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_SE = base[base['regiao'] == 'SE'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_CO = base[base['regiao'] == 'CO'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    admissoes_hosppublico = base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_hosppart = base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    admissoes_hospong = base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'}).reset_index()

    mortes_homens =  base[(base['morte']==1) & (base['sexo'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_mulheres =  base[(base['morte']==1) & (base['sexo'] == 3)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_brancos = base[(base['morte']==1) & (base['raca_cor'] == 1)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_pretos = base[(base['morte']==1) & (base['raca_cor'] == 2)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_pardos = base[(base['morte']==1) & (base['raca_cor'] == 3)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_amarelos = base[(base['morte']==1) & (base['raca_cor'] == 4)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_indigenas = base[(base['morte']==1) & (base['raca_cor'] == 5)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_seminfo = base[(base['morte']==1) & (base['raca_cor'] == 99)].groupby(['ano_inter']).agg({'id':'count'}).reset_index()

    mortes_S = base[(base['morte']==1) & (base['regiao'] == 'S')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_N = base[(base['morte']==1) & (base['regiao'] == 'N')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_NE = base[(base['morte']==1) & (base['regiao'] == 'NE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_SE = base[(base['morte']==1) & (base['regiao'] == 'SE')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_CO = base[(base['morte']==1) & (base['regiao'] == 'CO')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    
    mortes_hosppublico =  base[(base['morte']==1) & (base['nat_jur'] == 'Administração Pública')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_hosppart =  base[(base['morte']==1) & (base['nat_jur'] == 'Entidades Empresariais')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()
    mortes_hospong =  base[(base['morte']==1) & (base['nat_jur'] == 'Entidades sem Fins Lucrativos')].groupby(['ano_inter']).agg({'id':'count'}).reset_index()


    lst_dfs = [admissoes_total,admissoes_homens,admissoes_mulheres,admissoes_brancos,admissoes_pretos,admissoes_pardos,
                admissoes_amarelos,admissoes_indigenas,admissoes_seminfo,admissoes_S,admissoes_N,admissoes_NE,admissoes_SE,admissoes_CO,
                admissoes_hosppublico,admissoes_hosppart,admissoes_hospong,mortes_total,mortes_homens,mortes_mulheres,mortes_brancos,
                mortes_pretos,mortes_pardos,mortes_amarelos,mortes_indigenas,mortes_seminfo,mortes_S,mortes_N,mortes_NE,mortes_SE,
                mortes_CO,mortes_hosppublico,mortes_hosppart,mortes_hospong]
    lst_nomes = ['Admissions','Admissions_Male','Admissions_Female','Admissions_White','Admissions_Black','Admissions_Brown','Admissions_Yellow',
                    'Admissions_Indigenous','Admissions_NoInfo','Admissions_S','Admissions_N','Admissions_NE','Admissions_SE','Admissions_CO',
                    'Admissions_Public','Admissions_Private','Admissions_ONG','Deaths','Deaths_Male','Deaths_Female','Deaths_White','Deaths_Black',
                    'Deaths_Brown','Deaths_Yellow','Deaths_Indigenous','Deaths_NoInfo','Deaths_S','Deaths_N','Deaths_NE','Deaths_SE','Deaths_CO',
                    'Deaths_Public','Deaths_Private','Deaths_ONG']

    table_aapc = statistics_service.aapc(lst_dfs[0],"""id ~ ano_inter""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]

        if nome in ['Deaths']:
            expr = """morte ~ ano_inter"""
        else:
            expr = """id ~ ano_inter"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc(df,expr,nome)])
    
    table_overview = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'ano_inter'),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_overview)
    table_overview.to_excel('../tables/table_overview.xlsx')
    return

def generate_100k_rates_table(base,dfWHO,pop_ref,pop_ref_by_sex,pop_ref_by_region):
    # TAXAS POR 100 mil
    admissoes_total_tx = base.groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_total_tx_adjusted = statistics_service.age_adjust(admissoes_total_tx,dfWHO,pop_ref)

    admissoes_homens_tx = base[base['sexo'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_homens_tx_adjusted = statistics_service.age_adjust(admissoes_homens_tx,dfWHO,pop_ref_by_sex[pop_ref_by_sex['sex']=='male'].reset_index()[['year','idade_grupo_who','population']])
    
    admissoes_mulheres_tx = base[base['sexo'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index() # conta a quantidade de internacoes por ano por faixa etária
    admissoes_mulheres_tx_adjusted = statistics_service.age_adjust(admissoes_mulheres_tx,dfWHO,pop_ref_by_sex[pop_ref_by_sex['sex']=='female'].reset_index()[['year','idade_grupo_who','population']])

    admissoes_brancos_tx = base[base['raca_cor'] == 1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_brancos_tx_adjusted = statistics_service.age_adjust(admissoes_brancos_tx,dfWHO,pop_ref)

    admissoes_pretos_tx = base[base['raca_cor'] == 2].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_pretos_tx_adjusted = statistics_service.age_adjust(admissoes_pretos_tx,dfWHO,pop_ref)

    admissoes_pardos_tx = base[base['raca_cor'] == 3].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_pardos_tx_adjusted = statistics_service.age_adjust(admissoes_pardos_tx,dfWHO,pop_ref)

    admissoes_amarelos_tx = base[base['raca_cor'] == 4].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_amerelos_tx_adjusted = statistics_service.age_adjust(admissoes_amarelos_tx,dfWHO,pop_ref)

    admissoes_indigenas_tx = base[base['raca_cor'] == 5].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_indigenas_tx_adjusted = statistics_service.age_adjust(admissoes_indigenas_tx,dfWHO,pop_ref)

    admissoes_seminfo_tx = base[base['raca_cor'] == 99].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_seminfo_tx_adjusted = statistics_service.age_adjust(admissoes_seminfo_tx,dfWHO,pop_ref)

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

    admissoes_hosppublico_tx = base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_hosppublico_tx_adjusted = statistics_service.age_adjust(admissoes_hosppublico_tx,dfWHO,pop_ref)

    admissoes_hosppart_tx = base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_hosppart_tx_adjusted = statistics_service.age_adjust(admissoes_hosppart_tx,dfWHO,pop_ref)

    admissoes_hospong_tx = base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    admissoes_hospong_tx_adjusted = statistics_service.age_adjust(admissoes_hospong_tx,dfWHO,pop_ref)

    mortes_total_tx = base[(base['morte']==1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_total_tx_adjusted = statistics_service.age_adjust(mortes_total_tx,dfWHO,pop_ref)

    mortes_homens_tx =  base[(base['morte']==1) & (base['sexo'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_homens_tx_adjusted = statistics_service.age_adjust(mortes_homens_tx,dfWHO,pop_ref_by_sex[pop_ref_by_sex['sex']=='male'].reset_index()[['year','idade_grupo_who','population']])

    mortes_mulheres_tx =  base[(base['morte']==1) & (base['sexo'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_mulheres_tx_adjusted = statistics_service.age_adjust(mortes_mulheres_tx,dfWHO,pop_ref_by_sex[pop_ref_by_sex['sex']=='female'].reset_index()[['year','idade_grupo_who','population']])

    mortes_brancos_tx = base[(base['morte']==1) & (base['raca_cor'] == 1)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_brancos_tx_adjusted = statistics_service.age_adjust(mortes_brancos_tx,dfWHO,pop_ref)

    mortes_pretos_tx = base[(base['morte']==1) & (base['raca_cor'] == 2)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_pretos_tx_adjusted = statistics_service.age_adjust(mortes_pretos_tx,dfWHO,pop_ref)

    mortes_pardos_tx = base[(base['morte']==1) & (base['raca_cor'] == 3)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_pardos_tx_adjusted = statistics_service.age_adjust(mortes_pardos_tx,dfWHO,pop_ref)

    mortes_amarelos_tx = base[(base['morte']==1) & (base['raca_cor'] == 4)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_amarelos_tx_adjusted = statistics_service.age_adjust(mortes_amarelos_tx,dfWHO,pop_ref)

    mortes_indigenas_tx = base[(base['morte']==1) & (base['raca_cor'] == 5)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_indigenas_tx_adjusted = statistics_service.age_adjust(mortes_indigenas_tx,dfWHO,pop_ref)

    mortes_seminfo_tx = base[(base['morte']==1) & (base['raca_cor'] == 99)].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_seminfo_tx_adjusted = statistics_service.age_adjust(mortes_seminfo_tx,dfWHO,pop_ref)

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

    mortes_hosppublico_tx =  base[(base['morte']==1) & (base['nat_jur'] == 'Administração Pública')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_hosppublico_tx_adjusted = statistics_service.age_adjust(mortes_hosppublico_tx,dfWHO,pop_ref)

    mortes_hosppart_tx =  base[(base['morte']==1) & (base['nat_jur'] == 'Entidades Empresariais')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_hosppart_tx_adjusted = statistics_service.age_adjust(mortes_hosppart_tx,dfWHO,pop_ref)

    mortes_hospong_tx =  base[(base['morte']==1) & (base['nat_jur'] == 'Entidades sem Fins Lucrativos')].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count'}).reset_index()
    mortes_hospong_tx_adjusted = statistics_service.age_adjust(mortes_hospong_tx,dfWHO,pop_ref)

    lst_dfs = [admissoes_total_tx_adjusted,admissoes_homens_tx_adjusted,admissoes_mulheres_tx_adjusted,admissoes_brancos_tx_adjusted,
                admissoes_pretos_tx_adjusted,admissoes_pardos_tx_adjusted,admissoes_amerelos_tx_adjusted,admissoes_indigenas_tx_adjusted,
                admissoes_seminfo_tx_adjusted,admissoes_S_tx_adjusted,admissoes_N_tx_adjusted,admissoes_NE_tx_adjusted,admissoes_SE_tx_adjusted,
                admissoes_CO_tx_adjusted,admissoes_hosppublico_tx_adjusted,admissoes_hosppart_tx_adjusted,admissoes_hospong_tx_adjusted,
                mortes_total_tx_adjusted,mortes_homens_tx_adjusted,mortes_mulheres_tx_adjusted,mortes_brancos_tx_adjusted,mortes_pretos_tx_adjusted,
                mortes_pardos_tx_adjusted,mortes_amarelos_tx_adjusted,mortes_indigenas_tx_adjusted,mortes_seminfo_tx_adjusted,mortes_S_tx_adjusted,
                mortes_N_tx_adjusted,mortes_NE_tx_adjusted,mortes_SE_tx_adjusted,mortes_CO_tx_adjusted,mortes_hosppublico_tx_adjusted,
                mortes_hosppart_tx_adjusted,mortes_hospong_tx_adjusted]
    lst_nomes = ['Admissions_Tx','Admissions_Male_Tx','Admissions_Female_Tx','Admissions_White_Tx','Admissions_Black_Tx','Admissions_Brown_Tx',
                    'Admissions_Yellow_Tx','Admissions_Indigenous_Tx','Admissions_NoInfo_Tx','Admissions_S_Tx','Admissions_N_Tx','Admissions_NE_Tx',
                    'Admissions_SE_Tx','Admissions_CO_Tx','Admissions_Public_Tx','Admissions_Private_Tx','Admissions_ONG_Tx','Mortality_Tx',
                    'Mortality_Male_Tx','Mortality_Female_Tx','Mortality_White_Tx','Mortality_Black_Tx','Mortality_Brown_Tx','Mortality_Yellow_Tx',
                    'Mortality_Indigenous_Tx','Mortality_NoInfo_Tx','Mortality_S_Tx','Mortality_N_Tx','Mortality_NE_Tx','Mortality_SE_Tx',
                    'Mortality_CO_Tx','Mortality_Public_Tx','Mortality_Private_Tx','Mortality_ONG_Tx']

    table_aapc = statistics_service.aapc_offset(lst_dfs[0],"""taxa_ajd_qnt_Y ~ year""",lst_nomes[0])

    for i in range(1,len(lst_dfs)):
        df = lst_dfs[i]
        nome = lst_nomes[i]
        print(nome)
        expr = """taxa_ajd_qnt_Y ~ year"""
        
        table_aapc = pd.concat([table_aapc,statistics_service.aapc_offset(df,expr,nome)])
    
    table_100k_rates = pd.merge(table_aapc,statistics_service.registros_ano(lst_dfs,lst_nomes,'year'),how='left',left_on='Analise',right_on='Analise')
    
    # print(table_100k_rates)
    table_100k_rates.to_excel('../tables/table_100k_rates.xlsx')

    return

