import sys
import subprocess
import pkg_resources

if {'pandas'} not in {pkg.key for pkg in pkg_resources.working_set}:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pandas'], stdout=subprocess.DEVNULL)

if {'numpy'} not in {pkg.key for pkg in pkg_resources.working_set}:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','numpy'], stdout=subprocess.DEVNULL)

if {'matplotlib'} not in {pkg.key for pkg in pkg_resources.working_set}:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','matplotlib'], stdout=subprocess.DEVNULL)

if {'seaborn'} not in {pkg.key for pkg in pkg_resources.working_set}:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','seaborn'], stdout=subprocess.DEVNULL)

if {'openpyxl'} not in {pkg.key for pkg in pkg_resources.working_set}:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','openpyxl'], stdout=subprocess.DEVNULL)

import matplotlib.pyplot as plt 
import os
import pickle
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import services.datasets_service as datasets_service
import services.statistics_service as statistics_service
import services.graphs_service as graphs_service

plt.style.use('seaborn-darkgrid')
pd.set_option('display.max_columns', None)
SHOW_PLOTS = False

# ### Base PneuCom
print("############# READING DATASETS #################")
pneumoCom_dataset_raw = pd.read_csv('../data/sih_aih_env_2011_2020_pneucom.csv',sep=',')
reference_population_raw = pd.read_csv('https://raw.githubusercontent.com/lslbastos/ibge_population_projection/main/output/data_pop_ibge_proj_2010-2016.csv',sep=',')
cnes_dataset_raw = pd.read_csv('../data/cnes_estabelecimentos.csv',sep=';',encoding='unicode_escape')
cnes_prof_dataset_raw = pd.read_csv('../data/profissionais-330000.csv',sep=';')
# sim2020_dataset_raw = pd.read_csv('../data/Mortalidade_Geral_2020.csv',sep=';')

cid10_dataset = pd.read_excel('../data/cids_diag_ahrq_css_br_v5.xlsx')
who_age_group_rate_dataset = datasets_service.get_who_age_group_dataset()
reference_population_by_age_group = datasets_service.get_reference_population_by_age_group_and_year(reference_population_raw,pneumoCom_dataset_raw)
reference_population_by_sex = datasets_service.get_reference_population_by_sex_and_year(reference_population_raw)
cnes_dataset_clean = datasets_service.get_cnes_clean(cnes_dataset_raw,cnes_prof_dataset_raw)
pneumoCom_dataset_clean = datasets_service.get_pneumoCom_dataset_clean(cid10_dataset,cnes_dataset_clean,pneumoCom_dataset_raw)
pneumoCom_mortality_dataset = datasets_service.get_pneumoCom_mortality_dataset(pneumoCom_dataset_clean)
pneumoCom_LOS_UTI_dataset = datasets_service.get_pneumoCom_LOS_UTI_dataset(pneumoCom_dataset_clean)
print("############# READ DATASETS FINISHED #################")

print("############# GENERATING GRAPHS #################")

graphs_service.graph_population_rate_by_sex(reference_population_by_sex,SHOW_PLOTS)
graphs_service.graph_admissions_by_sex(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_deaths_by_sex(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_admissions_by_race(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_deaths_by_race(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_mortality_and_lethality(pneumoCom_dataset_clean,who_age_group_rate_dataset,reference_population_by_age_group,SHOW_PLOTS)
graphs_service.graph_admissions_by_hospital_category(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_deaths_by_hospital_category(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_admissions_by_region(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_deaths_by_region(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_LOS_UTI_by_sex(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_LOS_UTI_by_hospital_category(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_LOS_UTI_by_region(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_UTI_utilization_by_hospital_category(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_UTI_utilization_by_age(pneumoCom_dataset_clean,SHOW_PLOTS)
graphs_service.graph_UTI_lethality(pneumoCom_dataset_clean,who_age_group_rate_dataset,SHOW_PLOTS)

print("############# GENERATE GRAPHS FINISHED #################")
