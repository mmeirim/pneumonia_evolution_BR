import pandas as pd

def get_reference_population_by_age_group_and_year(reference_population,pneumoCom_dataset,begin_year,stop_year):
    pop_ref_by_age_group_and_year = reference_population[(reference_population['age']!='TOTAL') & (reference_population['uf']=='BR') & (reference_population['sex']=='all') & (reference_population['year'].isin(range(begin_year,stop_year)))]
    pop_ref_by_age_group_and_year['age'] = pop_ref_by_age_group_and_year['age'].astype(int)

    idadeWHO = pneumoCom_dataset.groupby(['idade_grupo_who','idade_real_anos']).agg({'id':'count'}).reset_index()
    idadeWHO.drop('id',axis=1,inplace=True)

    pop_ref_by_age_group_and_year = pd.merge(pop_ref_by_age_group_and_year,idadeWHO, how='left', left_on='age',right_on='idade_real_anos')
    pop_ref_by_age_group_and_year = pop_ref_by_age_group_and_year.groupby(['year','idade_grupo_who']).agg({'population':'sum'}).reset_index()
    
    return pop_ref_by_age_group_and_year

def get_reference_population_by_sex_and_year(reference_population,pneumoCom_dataset,begin_year,stop_year):
    pop_ref_by_sex = reference_population[(reference_population['age']!='TOTAL') & (reference_population['uf']=='BR') & (reference_population['sex']!='all') & (reference_population['year'].isin(range(begin_year,stop_year)))]
    pop_ref_by_sex['age'] = pop_ref_by_sex['age'].astype(int)

    idadeWHO = pneumoCom_dataset.groupby(['idade_grupo_who','idade_real_anos']).agg({'id':'count'}).reset_index()
    idadeWHO.drop('id',axis=1,inplace=True)

    pop_ref_by_sex = pd.merge(pop_ref_by_sex,idadeWHO, how='left', left_on='age',right_on='idade_real_anos')
    pop_ref_by_sex = pop_ref_by_sex.groupby(['year','sex','idade_grupo_who']).agg({'population':'sum'}).reset_index()
        
    return pop_ref_by_sex

def get_reference_population_by_age_group_region_and_year(reference_population,pneumoCom_dataset,begin_year,stop_year):
    pop_ref_by_region = reference_population[(reference_population['age']!='TOTAL') & (reference_population['region'].isin(['North','Northeast','South','Southeast','Central-West'])) & (reference_population['sex']=='all') & (reference_population['year'].isin(range(begin_year,stop_year)))]
    pop_ref_by_region['age'] = pop_ref_by_region['age'].astype(int)

    idadeWHO = pneumoCom_dataset.groupby(['idade_grupo_who','idade_real_anos']).agg({'id':'count'}).reset_index()
    idadeWHO.drop('id',axis=1,inplace=True)

    pop_ref_by_region = pd.merge(pop_ref_by_region,idadeWHO, how='left', left_on='age',right_on='idade_real_anos')
    pop_ref_by_region = pop_ref_by_region.groupby(['year','uf','idade_grupo_who']).agg({'population':'sum'}).reset_index()
    
    return pop_ref_by_region

def get_cnes_clean(cnes,cnes_prof):
    cnes_pf = cnes_prof.groupby('CNES').agg({'NOME':'count'}).reset_index() 
    cnes_pf.columns = ['cnes','qnt_prof']

    cnes_clean = pd.merge(cnes,cnes_pf,how='left',left_on='CO_CNES',right_on='cnes')

    return cnes_clean

def get_pneumoCom_dataset_clean(cid10_dataset,cnes_dataset_clean, pneumoCom_dataset_raw,begin_year,stop_year):
    pneumoCom_dataset_clean = pneumoCom_dataset_raw[pneumoCom_dataset_raw['ano_inter'].isin(range(begin_year,stop_year))]

    pneumoCom_dataset_clean = pd.merge(pneumoCom_dataset_clean,cid10_dataset,how='left',left_on='diag_princ_trim_upper',right_on='icd10_br')

    pneumoCom_dataset_clean = pd.merge(pneumoCom_dataset_clean,cnes_dataset_clean,how='left',left_on='cnes',right_on='CO_CNES')

    pneumoCom_dataset_clean['classificacao'] = pneumoCom_dataset_clean['idade_grupo_who'].apply(age_group_classification)

    pneumoCom_dataset_clean['nat_jur'] = pneumoCom_dataset_clean['CO_NATUREZA_JUR'].apply(lambda x: 'Administração Pública' if x in range(1000,2000) else ('Entidades Empresariais' if x in range(2000,3000) else ('Entidades sem Fins Lucrativos' if x in range(3000,4000) else ('Pessoas Físicas' if x in range(4000,5000) else 'Organizações Internacionais e Outras Instituições Extraterritoriais'))))
    
    pneumoCom_dataset_clean.drop(['NU_CNPJ_MANTENEDORA','CO_NATUREZA_ORGANIZACAO','DS_NATUREZA_ORGANIZACAO','DS_NATUREZA_ORGANIZACAO','CO_NIVEL_HIERARQUIA','DS_NIVEL_HIERARQUIA','CO_ESFERA_ADMINISTRATIVA','DS_ESFERA_ADMINISTRATIVA','NU_TELEFONE','NU_LATITUDE','NU_LONGITUDE','NU_CNPJ','NO_EMAIL','CO_MOTIVO_DESAB','cnes_y','qnt_prof'],axis=1,inplace=True)

    return pneumoCom_dataset_clean

def filter_cids(base):
    base['remover'] = base['diag_princ_trim_upper'].apply(lambda x: 0 if x.startswith('J10') else (0 if x.startswith('J12') else (0 if x.startswith('J13') else (0 if x.startswith('J14') else (0 if x.startswith('J15') else (0 if x.startswith('J16') else (0 if x.startswith('J17') else (0 if x.startswith('J18') else 1 ) ) ) ) ) ) ) )

    base[base['remover'] == 0]['diag_princ_trim_upper'].head()

    filtered_base = base[base['remover'] == 0]
    return filtered_base

def get_elderly_dataset(pneumoCom_dataset):
    base_eld = pneumoCom_dataset[pneumoCom_dataset['classificacao'] == 1]
    return base_eld

def get_non_elderly_dataset(pneumoCom_dataset):
    base_noneld = pneumoCom_dataset[pneumoCom_dataset['classificacao'] == 0]
    return base_noneld

def get_who_age_group_dataset():
    dfWHO = {'age_group': ['0-4', '5-9', '10-14', '15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85+'],
        'world_avg': [8.86, 8.69, 8.60, 8.47, 8.22, 7.93, 7.61, 7.15, 6.59, 6.04, 5.37, 4.55, 3.72, 2.96, 2.21, 1.52, 0.91, 0.60]}
    dfWHO = pd.DataFrame(dfWHO)
    dfWHO['world_avg_dec'] = dfWHO['world_avg']/100
    return dfWHO

def get_pneumoCom_mortality_dataset(base):
    base_mortalidade = base[['estado','regiao','sexo','raca_cor','idade_real_anos','los_hosp','los_uti','uti','diag_princ_trim_upper','nat_jur','morte']]
    # base_mortalidade.to_csv('../data/base_mortalidade.csv')
    return base_mortalidade

def get_pneumoCom_LOS_UTI_dataset(base):
    base_losuti = base[base['uti']==1][['estado','regiao','sexo','raca_cor','idade_real_anos','diag_princ_trim_upper','nat_jur','los_uti']]
    # base_losuti.to_csv('../data/base_losuti.csv')
    return base_losuti

def age_group_classification(x):
    if x in ['20-24','25-29','30-34','35-39','40-44','45-49']:
        return 1
    elif x in ['50-54','55-59']:
        return 2
    elif x in ['60-64','65-69']:
        return 3
    else:
        return 4