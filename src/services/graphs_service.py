import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import services.statistics_service as statistics_service

IMAGES_BASE_DIR = '../images/'

# def graph_population_rate_by_sex(pop_ref_by_sex,show_plot):
#     pop_total = pop_ref_by_sex[pop_ref_by_sex['sex']=='all']['population'].reset_index()

#     pop_homens = pop_ref_by_sex[pop_ref_by_sex['sex']=='male']['population'].reset_index()
#     pop_mulheres = pop_ref_by_sex[pop_ref_by_sex['sex']=='female']['population'].reset_index()

#     r = [0,1,2,3,4,5,6,7,8]
#     g1_bars_bottom = round((pop_homens/pop_total)*100)['population']
#     g1_bars_top = round((pop_mulheres/pop_total)*100)['population']

#     fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
#     p1 = ax1.bar(r, g1_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
#     p2 = ax1.bar(r, g1_bars_top, bottom=g1_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')
#     ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
#     ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
#     ax1.set_ylabel('Proportion', fontweight='bold')
#     ax1.set_title("Population", fontweight='bold')
#     ax1.bar_label(p1, label_type='center', fontweight='bold')
#     ax1.bar_label(p2, label_type='center', fontweight='bold')

#     fig.set_facecolor("#E5F2A5")
#     handles, labels = ax1.get_legend_handles_labels()
#     fig.set_figheight(6)
#     fig.set_figwidth(10)
#     fig.legend(handles, labels, loc = (0.35, 0.01), ncol=2, labelspacing=0.)
#     plt.savefig(IMAGES_BASE_DIR+'population_by_sex.png',dpi=1200)
#     if(show_plot): plt.show()
#     return

def graph_admissions_by_sex(pneumoCom_dataset_clean,show_plot):
    admissoes_total = pneumoCom_dataset_clean.groupby(['ano_inter']).agg({'id':'count'})

    admissoes_homens = pneumoCom_dataset_clean[pneumoCom_dataset_clean['sexo'] == 1].groupby(['ano_inter']).agg({'id':'count'}) 
    admissoes_mulheres = pneumoCom_dataset_clean[pneumoCom_dataset_clean['sexo'] == 3].groupby(['ano_inter']).agg({'id':'count'})

    r = [0,1,2,3,4,5,6,7,8]
    g1_bars_bottom = round((admissoes_homens/admissoes_total)*100)['id']
    g1_bars_top = round((admissoes_mulheres/admissoes_total)*100)['id']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax1.bar(r, g1_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
    p2 = ax1.bar(r, g1_bars_top, bottom=g1_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')
    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Proportion', fontweight='bold')
    ax1.set_title("Admissions", fontweight='bold')
    ax1.bar_label(p1, label_type='center', fontweight='bold')
    ax1.bar_label(p2, label_type='center', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.35, 0.01), ncol=2, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'admissions_by_sex.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_deaths_by_sex(base,show_plot):
    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'})

    mortes_homens =  base[base['sexo'] == 1].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_mulheres =  base[base['sexo'] == 3].groupby(['ano_inter']).agg({'morte':'sum'})

    r = [0,1,2,3,4,5,6,7,8]
    g3_bars_bottom = round((mortes_homens/mortes_total)*100)['morte']
    g3_bars_top = round((mortes_mulheres/mortes_total)*100)['morte']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax1.bar(r, g3_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
    p2 = ax1.bar(r, g3_bars_top, bottom=g3_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')
    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Proportion', fontweight='bold')
    ax1.set_title("Deaths", fontweight='bold')
    ax1.bar_label(p1, label_type='center', fontweight='bold')
    ax1.bar_label(p2, label_type='center', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.35, 0.01), ncol=2, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'deaths_by_sex.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_admissions_by_race(base,show_plot):
    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'})

    admissoes_brancos = base[base['raca_cor'] == 1].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_pretos = base[base['raca_cor'] == 2].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_pardos = base[base['raca_cor'] == 3].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_amarelos = base[base['raca_cor'] == 4].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_indigenas = base[base['raca_cor'] == 5].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_seminfo = base[base['raca_cor'] == 99].groupby(['ano_inter']).agg({'id':'count'})

    r = [0,1,2,3,4,5,6,7,8]
    g2_bars_bottom = np.nan_to_num(round((admissoes_brancos/admissoes_total)*100000)['id'])
    g2_bars_bottom2 = np.nan_to_num(round((admissoes_pardos/admissoes_total)*100000)['id'])
    g2_bars_bottom3 = np.nan_to_num(round((admissoes_pretos/admissoes_total)*100000)['id'])
    g2_bars_bottom4 = np.nan_to_num(round((admissoes_amarelos/admissoes_total)*100000)['id'])
    g2_bars_bottom5 = np.nan_to_num(round((admissoes_indigenas/admissoes_total)*100000)['id'])
    g2_bars_top = np.nan_to_num(round((admissoes_seminfo/admissoes_total)*100000)['id'])


    fig, ax2 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax2.bar(r, g2_bars_bottom, edgecolor='white', color = '#EB6C50' , label='White')
    p2 = ax2.bar(r, g2_bars_bottom2, bottom=g2_bars_bottom, edgecolor='white', color = '#BB53F5', label='Brown (Mixed-race)')
    p3 = ax2.bar(r, g2_bars_bottom3, bottom=g2_bars_bottom+g2_bars_bottom2, edgecolor='white', color = '#57A5DE', label='Black')
    p4 = ax2.bar(r, g2_bars_bottom4, bottom=g2_bars_bottom+g2_bars_bottom2+g2_bars_bottom3, color = '#53F56C', label='Yellow (Asian)')
    p5 = ax2.bar(r, g2_bars_bottom5, bottom=g2_bars_bottom+g2_bars_bottom2+g2_bars_bottom3+g2_bars_bottom4, edgecolor='white', color = '#EBD222', label='Indigenous')
    p6 = ax2.bar(r, g2_bars_top, bottom=g2_bars_bottom+g2_bars_bottom2+g2_bars_bottom3+g2_bars_bottom4+g2_bars_bottom5, edgecolor='white', color = '#DC143C', label='No Information')
    ax2.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax2.set_yticks([0,25000,50000,75000,100000],['0','25,000','50,000','75,000','100,000'])
    ax2.set_ylabel('Admissions by Race/Ethnicity (per 100,000 persons)', fontweight='bold')
    ax2.set_xlabel('Years', fontweight='bold')
    ax2.bar_label(p1, label_type='center', fontweight='bold')
    ax2.bar_label(p2, label_type='center', fontweight='bold')
    ax2.bar_label(p3, label_type='center', fontweight='bold')
    # ax2.bar_label(p4, label_type='center', fontweight='bold')
    # ax2.bar_label(p5, label_type='center', fontweight='bold')
    ax2.bar_label(p6, label_type='center', fontweight='bold')
    # ax2.set_facecolor("#E5F2A5")
    fig.set_facecolor("#E5F2A5")
    handles, labels = ax2.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.28, 0.001), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'admissions_by_color.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_deaths_by_race(base,show_plot):
    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'})

    mortes_brancos = base[base['raca_cor'] == 1].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_pretos = base[base['raca_cor'] == 2].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_pardos = base[base['raca_cor'] == 3].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_amarelos = base[base['raca_cor'] == 4].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_indigenas = base[base['raca_cor'] == 5].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_seminfo = base[base['raca_cor'] == 99].groupby(['ano_inter']).agg({'morte':'sum'})


    r = [0,1,2,3,4,5,6,7,8]
    g4_bars_bottom = np.nan_to_num(round((mortes_brancos/mortes_total)*100)['morte'])
    g4_bars_bottom2 = np.nan_to_num(round((mortes_pardos/mortes_total)*100)['morte'])
    g4_bars_bottom3 = np.nan_to_num(round((mortes_pretos/mortes_total)*100)['morte'])
    g4_bars_bottom4 = np.nan_to_num(round((mortes_amarelos/mortes_total)*100)['morte'])
    g4_bars_bottom5 = np.nan_to_num(round((mortes_indigenas/mortes_total)*100)['morte'])
    g4_bars_top = np.nan_to_num(round((mortes_seminfo/mortes_total)*100)['morte'])


    fig, ax2 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax2.bar(r, g4_bars_bottom, edgecolor='white', color = '#EB6C50' , label='Brancos')
    p2 = ax2.bar(r, g4_bars_bottom2, bottom=g4_bars_bottom, edgecolor='white', color = '#BB53F5', label='Pardos')
    p3 = ax2.bar(r, g4_bars_bottom3, bottom=g4_bars_bottom+g4_bars_bottom2, edgecolor='white', color = '#57A5DE', label='Pretos')
    p4 = ax2.bar(r, g4_bars_bottom4, bottom=g4_bars_bottom+g4_bars_bottom2+g4_bars_bottom3, color = '#53F56C', label='Amarelos')
    p5 = ax2.bar(r, g4_bars_bottom5, bottom=g4_bars_bottom+g4_bars_bottom2+g4_bars_bottom3+g4_bars_bottom4, edgecolor='white', color = '#EBD222', label='Indígenas')
    p6 = ax2.bar(r, g4_bars_top, bottom=g4_bars_bottom+g4_bars_bottom2+g4_bars_bottom3+g4_bars_bottom4+g4_bars_bottom5, edgecolor='white', color = '#DC143C', label='Sem Informação')
    ax2.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax2.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax2.set_ylabel('Proportion', fontweight='bold')
    ax2.set_title("Deaths", fontweight='bold')
    ax2.bar_label(p1, label_type='center', fontweight='bold')
    ax2.bar_label(p2, label_type='center', fontweight='bold')
    ax2.bar_label(p3, label_type='center', fontweight='bold')
    # ax2.bar_label(p4, label_type='center', fontweight='bold')
    # ax2.bar_label(p5, label_type='center', fontweight='bold')
    ax2.bar_label(p6, label_type='center', fontweight='bold')
    # ax2.set_facecolor("#E5F2A5")
    fig.set_facecolor("#E5F2A5")
    handles, labels = ax2.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.25, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'deaths_by_color.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_mortality_and_lethality(base,dfWHO,pop_ref,show_plot):
    dfmortes = base.groupby(['ano_inter','idade_grupo_who']).agg({'morte':'sum'}).reset_index()
    dfmortalidade = statistics_service.age_adjust_ML(dfmortes,dfWHO,pop_ref)
    dfmortalidade


    dflet = base.groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    dflet.columns = ['ano_inter','idade_grupo_who','admissoes','num']
    #df_merged = pd.merge(pop_ref, df,  how='left', left_on=['year','idade_grupo_who'], right_on=['ano_inter','idade_grupo_who']) # junta a quantidade por ano por faixa etária com a população de referencia
    dflet['taxa'] = dflet['num']/dflet['admissoes'] # calcula a taxa
    dfletalidade = pd.merge(dflet, dfWHO,  how='left', left_on=['idade_grupo_who'], right_on=['age_group']) # junta o dataframe com a proporção do WHO
    dfletalidade['obitos_esp'] = dfletalidade['taxa']*dfletalidade['world_avg_dec'] # calcula a proporção da quantidade esperados
    dfletalidade = dfletalidade.groupby(['ano_inter']).agg({'num':'sum','obitos_esp':'sum','admissoes':'sum','world_avg_dec':'sum'}).reset_index() # agrupa por ANO
    # tx = obts esp / pop
    #somar as faixas etarias do ano e dividir pela pop de ref total
    dfletalidade['taxa_ajustada'] = dfletalidade['obitos_esp']/dfletalidade['world_avg_dec']
    dfletalidade['taxa_ajustada_100mil'] = (dfletalidade['taxa_ajustada']*100000).apply(np.ceil)
    dfletalidade['taxa_bruta_100mil'] = (dfletalidade['num']/dfletalidade['admissoes'])*100000
    dfletalidade


    tx_mort = round(dfmortalidade['taxa_ajustada_100mil'],1)
    tx_let = round(dfletalidade['taxa_ajustada']*100,1)

    r = [0,1,2,3,4,5,6,7,8]

    fig, (ax1,ax2) = plt.subplots(1,2,sharex=True,)
    p1 = ax1.plot(r, tx_mort, marker='o', markerfacecolor='#380282', markersize=4, color = '#380282' , label='Mortality rate')
    p2 = ax2.plot(r, tx_let, marker='o', markerfacecolor='#380282', markersize=4, color = '#DC143C' , label='Lethality rate')

    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax1.set_yticks([0,20,40,60,80,100],['0','20','40','60','80','100'])
    ax1.set_ylabel('Age-adjusted Mortality rate', fontweight='bold')
    ax1.set_title("Mortality", fontweight='bold')

    ax2.set_yticks([0,2000,4000,6000,8000,10000],['0','2,000','4,000','6,000','8,000','10,000'])
    ax2.set_ylabel('Age-adjusted Lethality rate', fontweight='bold')
    ax2.set_title("Lethality",fontweight='bold')

    for i in range(len(tx_mort)):
        ax1.text(r[i], tx_mort[i]+1, "%.1f" %tx_mort[i], ha="center", fontweight='bold')
        ax2.text(r[i], tx_let[i]+100, "%.1f" %tx_let[i], ha="center", fontweight='bold')
        
    fig.set_facecolor("#E5F2A5")

    fig.set_figheight(6)
    fig.set_figwidth(12)
    plt.savefig(IMAGES_BASE_DIR+'mortality_ratio.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_missing_values(base,show_plot):
    na=(base.shape[0]-base[base.columns].count()).to_frame().reset_index().rename(columns={'index':'COLUNA',0:'NAs'})

    fig, ax = plt.subplots(figsize=(10,15))
    sns.barplot(y='COLUNA',x='NAs',data=na,ax=ax).set_title('VALORES NULOS', fontsize=15)
    #fig.savefig("imagens2\\nulos.png", dpi=None, facecolor='w', edgecolor='w',
    #        orientation='portrait', papertype=None, format=None,
    #        transparent=False, bbox_inches=None, pad_inches=0.1,
    #        frameon=None, metadata=None)
    return

def graph_admissions_by_hospital_category(base,show_plot):
    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'})

    admissoes_hosppublico = base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter']).agg({'id':'count'}) 
    admissoes_hosppart = base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_hospong = base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter']).agg({'id':'count'})


    r = [0,1,2,3,4,5,6,7,8]
    g1_bars_bottom = round((admissoes_hosppublico/admissoes_total)*100)['id']
    g1_bars_mid = round((admissoes_hospong/admissoes_total)*100)['id']
    g1_bars_top = round((admissoes_hosppart/admissoes_total)*100)['id']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax1.bar(r, g1_bars_bottom, edgecolor='white', color = 'darkgreen' , label='Hospital Público')
    p2 = ax1.bar(r, g1_bars_mid, bottom=g1_bars_bottom, edgecolor='white', color = 'orange' , label='Hospital sem Fins Lucrativos')
    p3 = ax1.bar(r, g1_bars_top, bottom=g1_bars_bottom+g1_bars_mid, edgecolor='white', color = 'navy', label='Hospital Privado')
    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Proportion', fontweight='bold')
    ax1.set_title("Admissions", fontweight='bold')
    ax1.bar_label(p1, label_type='center', fontweight='bold')
    ax1.bar_label(p2, label_type='center', fontweight='bold')
    ax1.bar_label(p3, label_type='center', fontweight='bold',color='white')


    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.2, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'admissions_by_hospital.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_deaths_by_hospital_category(base,show_plot):
    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'})

    mortes_hosppublico =  base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_hosppart =  base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_hospong =  base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter']).agg({'morte':'sum'})

    r = [0,1,2,3,4,5,6,7,8]
    g3_bars_bottom = round((mortes_hosppublico/mortes_total)*100)['morte']
    g3_bars_mid = round((mortes_hospong/mortes_total)*100)['morte']
    g3_bars_top = round((mortes_hosppart/mortes_total)*100)['morte']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax1.bar(r, g3_bars_bottom, edgecolor='white', color = 'darkgreen' , label='Hospital Público')
    p2 = ax1.bar(r, g3_bars_mid, bottom=g3_bars_bottom, edgecolor='white', color = 'orange', label='Hospital Sem Fins Lucrativos')
    p3 = ax1.bar(r, g3_bars_top, bottom=g3_bars_bottom+g3_bars_mid, edgecolor='white', color = 'navy', label='Hospital Privado')
    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Proportion', fontweight='bold')
    ax1.set_title("Deaths", fontweight='bold')
    ax1.bar_label(p1, label_type='center', fontweight='bold')
    ax1.bar_label(p2, label_type='center', fontweight='bold')
    ax1.bar_label(p3, label_type='center', fontweight='bold',color='white')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.2, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'deaths_by_hospital.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_admissions_by_region(base,show_plot):
    admissoes_total = base.groupby(['ano_inter']).agg({'id':'count'})

    admissoes_S = base[base['regiao'] == 'S'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_N = base[base['regiao'] == 'N'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_NE = base[base['regiao'] == 'NE'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_SE = base[base['regiao'] == 'SE'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_CO = base[base['regiao'] == 'CO'].groupby(['ano_inter']).agg({'id':'count'})


    r = [0,1,2,3,4,5,6,7,8]
    g2_bars_bottom = np.nan_to_num(round((admissoes_S/admissoes_total)*100)['id'])
    g2_bars_bottom2 = np.nan_to_num(round((admissoes_N/admissoes_total)*100)['id'])
    g2_bars_bottom3 = np.nan_to_num(round((admissoes_NE/admissoes_total)*100)['id'])
    g2_bars_bottom4 = np.nan_to_num(round((admissoes_SE/admissoes_total)*100)['id'])
    g2_bars_bottom5 = np.nan_to_num(round((admissoes_CO/admissoes_total)*100)['id'])


    fig, ax2 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax2.bar(r, g2_bars_bottom, edgecolor='white', color = '#442288' , label='Sul')
    p2 = ax2.bar(r, g2_bars_bottom2, bottom=g2_bars_bottom, edgecolor='white', color = '#6CA2EA', label='Norte')
    p3 = ax2.bar(r, g2_bars_bottom3, bottom=g2_bars_bottom+g2_bars_bottom2, edgecolor='white', color = '#FED23F', label='Nordeste')
    p4 = ax2.bar(r, g2_bars_bottom4, bottom=g2_bars_bottom+g2_bars_bottom2+g2_bars_bottom3, color = '#B5D33D', label='Sudeste')
    p5 = ax2.bar(r, g2_bars_bottom5, bottom=g2_bars_bottom+g2_bars_bottom2+g2_bars_bottom3+g2_bars_bottom4, edgecolor='white', color = '#EB7D5B', label='Centro Oeste')
    ax2.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax2.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax2.set_ylabel('Proportion', fontweight='bold')
    ax2.set_title("Admissions", fontweight='bold')
    ax2.bar_label(p1, label_type='center', fontweight='bold')
    ax2.bar_label(p2, label_type='center', fontweight='bold')
    ax2.bar_label(p3, label_type='center', fontweight='bold')
    ax2.bar_label(p4, label_type='center', fontweight='bold')
    ax2.bar_label(p5, label_type='center', fontweight='bold')
    # ax2.set_facecolor("#E5F2A5")
    fig.set_facecolor("#E5F2A5")
    handles, labels = ax2.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.25, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'admissions_by_REGION.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_deaths_by_region(base,show_plot):
    mortes_total = base.groupby(['ano_inter']).agg({'morte':'sum'})

    mortes_S = base[base['regiao'] == 'S'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_N = base[base['regiao'] == 'N'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_NE = base[base['regiao'] == 'NE'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_SE = base[base['regiao'] == 'SE'].groupby(['ano_inter']).agg({'morte':'sum'})
    mortes_CO = base[base['regiao'] == 'CO'].groupby(['ano_inter']).agg({'morte':'sum'})


    r = [0,1,2,3,4,5,6,7,8]
    g4_bars_bottom = np.nan_to_num(round((mortes_S/mortes_total)*100)['morte'])
    g4_bars_bottom2 = np.nan_to_num(round((mortes_N/mortes_total)*100)['morte'])
    g4_bars_bottom3 = np.nan_to_num(round((mortes_NE/mortes_total)*100)['morte'])
    g4_bars_bottom4 = np.nan_to_num(round((mortes_SE/mortes_total)*100)['morte'])
    g4_bars_bottom5 = np.nan_to_num(round((mortes_CO/mortes_total)*100)['morte'])


    fig, ax2 = plt.subplots(1,1,sharex=True,sharey=True,)
    p1 = ax2.bar(r, g4_bars_bottom, edgecolor='white', color = '#442288' , label='Sul')
    p2 = ax2.bar(r, g4_bars_bottom2, bottom=g4_bars_bottom, edgecolor='white', color = '#6CA2EA', label='Norte')
    p3 = ax2.bar(r, g4_bars_bottom3, bottom=g4_bars_bottom+g4_bars_bottom2, edgecolor='white', color = '#FED23F', label='Nordeste')
    p4 = ax2.bar(r, g4_bars_bottom4, bottom=g4_bars_bottom+g4_bars_bottom2+g4_bars_bottom3, color = '#B5D33D', label='Sudeste')
    p5 = ax2.bar(r, g4_bars_bottom5, bottom=g4_bars_bottom+g4_bars_bottom2+g4_bars_bottom3+g4_bars_bottom4, edgecolor='white', color = '#EB7D5B', label='Centro Oeste')
    ax2.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    ax2.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax2.set_ylabel('Proportion', fontweight='bold')
    ax2.set_title("Deaths", fontweight='bold')
    ax2.bar_label(p1, label_type='center', fontweight='bold')
    ax2.bar_label(p2, label_type='center', fontweight='bold')
    ax2.bar_label(p3, label_type='center', fontweight='bold')
    ax2.bar_label(p4, label_type='center', fontweight='bold')
    ax2.bar_label(p5, label_type='center', fontweight='bold')
    # ax2.set_facecolor("#E5F2A5")
    fig.set_facecolor("#E5F2A5")
    handles, labels = ax2.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.25, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'deaths_by_region.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_LOS_UTI_by_sex(base,show_plot):
    losuti_total = base[base['uti']==1].groupby(['ano_inter','sexo']).agg({'los_uti':'mean'}).reset_index()
    losuti_total['Sexo'] = losuti_total['sexo'].apply(lambda x: 'Homem' if x == 1 else "Mulher")


    losuti_homens =  base[(base['sexo'] == 1)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_mulheres =  base[(base['sexo'] == 3)&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()

    r = [0,2,4,6,8,10,12,14,16]
    r2 = [x+0.6 for x in r]
    #g3_bars_bottom = round((losuti_homens/losuti_total)*100)['los_uti']
    #g3_bars_top = round((losuti_mulheres/losuti_total)*100)['los_uti']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    #p1 = ax1.bar(r, g3_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
    #p2 = ax1.bar(r, g3_bars_top, bottom=g3_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')

    p1 = ax1.bar(r, round(losuti_homens['los_uti'],1), color = '#380282', width = 0.4, label='Homens')
    p2 = ax1.bar(r2, round(losuti_mulheres['los_uti'],1), color = '#DC143C',width = 0.4, label='Mulheres')
    #ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)

    #p1 = sns.barplot(data=losuti_total, x='ano_inter',y='los_uti',hue='Sexo')

    #p2 = sns.barplot(data=losuti_mulheres, x='ano_inter',y='los_uti',color = '#DC143C' , label='Homens')

    ax1.set_xticks([x+0.3 for x in r], ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    #ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Days', fontweight='bold')
    ax1.set_xlabel('Years', fontweight='bold')

    ax1.set_title("Average LOS Uti", fontweight='bold')
    ax1.bar_label(p1, label_type='edge', fontweight='bold')
    ax1.bar_label(p2, label_type='edge', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.35, 0.01), ncol=2, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'los_by_sex.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_LOS_UTI_by_hospital_category(base,show_plot):
    losuti_publico =  base[(base['nat_jur'] == 'Administração Pública')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_priv =  base[(base['nat_jur'] == 'Entidades Empresariais')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_ong =  base[(base['nat_jur'] == 'Entidades sem Fins Lucrativos')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()

    r = [0,2,4,6,8,10,12,14,16]
    r2 = [x+0.5 for x in r]
    r3 = [x+1 for x in r]
    #g3_bars_bottom = round((losuti_homens/losuti_total)*100)['los_uti']
    #g3_bars_top = round((losuti_mulheres/losuti_total)*100)['los_uti']

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)
    #p1 = ax1.bar(r, g3_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
    #p2 = ax1.bar(r, g3_bars_top, bottom=g3_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')

    p1 = ax1.bar(r, round(losuti_publico['los_uti'],1), color = 'darkgreen', width = 0.4, label='Hospital Público')
    p2 = ax1.bar(r2, round(losuti_priv['los_uti'],1), color = 'navy',width = 0.4, label='Hospital Privado')
    p3 = ax1.bar(r3, round(losuti_ong['los_uti'],1), color = 'orange',width = 0.4, label='Hospital sem Fins Lucrativos')
    #ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)

    #p1 = sns.barplot(data=losuti_total, x='ano_inter',y='los_uti',hue='Sexo')

    #p2 = sns.barplot(data=losuti_mulheres, x='ano_inter',y='los_uti',color = '#DC143C' , label='Homens')

    ax1.set_xticks(r2, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    #ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Days', fontweight='bold')
    ax1.set_xlabel('Years', fontweight='bold')

    ax1.set_title("Average LOS Uti", fontweight='bold')
    ax1.bar_label(p1, label_type='edge', fontweight='bold')
    ax1.bar_label(p2, label_type='edge', fontweight='bold')
    ax1.bar_label(p3, label_type='edge', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.2, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'los_by_hospital.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_LOS_UTI_by_region(base,show_plot):
    losuti_S =  base[(base['regiao'] == 'S')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_N =  base[(base['regiao'] == 'N')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_NE =  base[(base['regiao'] == 'NE')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_SE =  base[(base['regiao'] == 'SE')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()
    losuti_CO =  base[(base['regiao'] == 'CO')&(base['uti']==1)].groupby(['ano_inter']).agg({'los_uti':'mean'}).reset_index()

    r = [0,6,12,18,24,30,36,42,48]
    r2 = np.array(r) + 1
    r3 = np.array(r2) + 1
    r4 = np.array(r3) + 1
    r5 = np.array(r4) + 1
    #r2 = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
    #g3_bars_bottom = round((losuti_homens/losuti_total)*100)['los_uti']
    #g3_bars_top = round((losuti_mulheres/losuti_total)*100)['los_uti']

    fig, ax = plt.subplots(1,1,sharex=True,sharey=True,)
    #p1 = ax1.bar(r, g3_bars_bottom, edgecolor='white', color = '#380282' , label='Homens')
    #p2 = ax1.bar(r, g3_bars_top, bottom=g3_bars_bottom, edgecolor='white', color = '#DC143C', label='Mulheres')

    p1 = ax.bar(r, round(losuti_S['los_uti'],1), color = '#442288', width = 0.9, label='Sul')
    p2 = ax.bar(r2, round(losuti_N['los_uti'],1), color = '#6CA2EA',width = 0.9, label='Norte')
    p3 = ax.bar(r3, round(losuti_NE['los_uti'],1), color = '#FED23F',width = 0.9, label='Nordeste')
    p4 = ax.bar(r4, round(losuti_SE['los_uti'],1), color = '#B5D33D',width = 0.9, label='Sudeste')
    p5 = ax.bar(r5, round(losuti_CO['los_uti'],1), color = '#EB7D5B',width = 0.9, label='Centro Oeste')

    ax.set_xticks(r3, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    #ax1.set_yticks([0,25,50,75,100],['0%','25%','50%','75%','100%'])
    ax.set_ylabel('Days', fontweight='bold')
    ax.set_xlabel('Years', fontweight='bold')
    ax.set_title("Average LOS Uti", fontweight='bold')
    ax.bar_label(p1, label_type='edge', fontweight='bold')
    ax.bar_label(p2, label_type='edge', fontweight='bold')
    ax.bar_label(p3, label_type='edge', fontweight='bold')
    ax.bar_label(p4, label_type='edge', fontweight='bold')
    ax.bar_label(p5, label_type='edge', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax.get_legend_handles_labels()
    fig.set_figheight(8)
    fig.set_figwidth(20)
    fig.legend(handles, labels, loc = (0.45, 0.01), ncol=2, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'los_by_region.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_UTI_utilization_by_hospital_category(base,show_plot):
    admissoes_hosppublico = base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter']).agg({'id':'count'}) 
    admissoes_hosppart = base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter']).agg({'id':'count'})
    admissoes_hospong = base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter']).agg({'id':'count'})

    uti_hosppublico = base[base['nat_jur'] == 'Administração Pública'].groupby(['ano_inter']).agg({'uti':'sum'}).reset_index()
    uti_hosppart = base[base['nat_jur'] == 'Entidades Empresariais'].groupby(['ano_inter']).agg({'uti':'sum'}).reset_index()
    uti_hospong = base[base['nat_jur'] == 'Entidades sem Fins Lucrativos'].groupby(['ano_inter']).agg({'uti':'sum'}).reset_index()

    r = [0,2,4,6,8,10,12,14,16]
    r2 = [x+0.5 for x in r]
    r3 = [x+1 for x in r]

    fig, ax1 = plt.subplots(1,1,sharex=True,sharey=True,)

    p1 = ax1.bar(r, round((uti_hosppublico["uti"]/admissoes_hosppublico.reset_index()["id"])*100,1), color = 'darkgreen', width = 0.4, label='Hospital Público')
    p2 = ax1.bar(r2, round((uti_hosppart["uti"]/admissoes_hosppart.reset_index()["id"])*100,1), color = 'navy',width = 0.4, label='Hospital Privado')
    p3 = ax1.bar(r3, round((uti_hospong["uti"]/admissoes_hospong.reset_index()["id"])*100,1), color = 'orange',width = 0.4, label='Hospital sem Fins Lucrativos')

    ax1.set_xticks(r2, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    # ax1.set_yticks([0,5,10,5,100],['0%','25%','50%','75%','100%'])
    ax1.set_ylabel('Proportion', fontweight='bold')
    ax1.set_xlabel('Years', fontweight='bold')

    ax1.set_title("Proportion of ICU", fontweight='bold')
    ax1.bar_label(p1, label_type='edge', fontweight='bold')
    ax1.bar_label(p2, label_type='edge', fontweight='bold')
    ax1.bar_label(p3, label_type='edge', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    handles, labels = ax1.get_legend_handles_labels()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    fig.legend(handles, labels, loc = (0.2, 0.01), ncol=3, labelspacing=0.)
    plt.savefig(IMAGES_BASE_DIR+'uti_by_hospital.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_UTI_utilization_by_age(base,show_plot):
    uti_idade = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'uti':'sum'}).reset_index()

    r = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    r2 = [x+0.5 for x in r]
    r3 = [x+1 for x in r]
    # print(uti_idade[uti_idade["ano_inter"]==2011])

    fig, (ax1,ax2,ax3) = plt.subplots(3,1,sharey=True,)

    p1 = ax1.bar(r,uti_idade[uti_idade["ano_inter"]==2011]["uti"], width =1, edgecolor="black", color = 'darkgreen', label="2011")
    p2 = ax2.bar(r, uti_idade[uti_idade["ano_inter"]==2015]["uti"], width =1, edgecolor="black", color = 'navy',label="2015")
    p3 = ax3.bar(r, uti_idade[uti_idade["ano_inter"]==2019]["uti"], width =1, edgecolor="black", color = 'orange',label="2019")

    ax1.set_xticks(r,uti_idade[uti_idade["ano_inter"]==2011]["idade_grupo_who"])
    ax2.set_xticks(r,uti_idade[uti_idade["ano_inter"]==2015]["idade_grupo_who"])
    ax3.set_xticks(r,uti_idade[uti_idade["ano_inter"]==2019]["idade_grupo_who"])

    ax1.set_ylabel('Use of ICU in 2011', fontweight='bold')
    ax1.set_xlabel('idade_grupo_who', fontweight='bold')

    ax2.set_ylabel('Use of ICU in 2015', fontweight='bold')
    ax2.set_xlabel('idade_grupo_who', fontweight='bold')

    ax3.set_ylabel('Use of ICU in 2019', fontweight='bold')
    ax3.set_xlabel('idade_grupo_who', fontweight='bold')


    ax1.set_title("Use of ICU by age", fontweight='bold')
    ax1.bar_label(p1, label_type='edge', fontweight='bold')
    ax2.bar_label(p2, label_type='edge', fontweight='bold')
    ax3.bar_label(p3, label_type='edge', fontweight='bold')

    fig.set_facecolor("#E5F2A5")
    fig.set_figheight(15)
    fig.set_figwidth(10)
    plt.savefig(IMAGES_BASE_DIR+'use_of_uti_by_age.png',dpi=1200)
    if(show_plot): plt.show()
    return

def graph_UTI_lethality(base,dfWHO,show_plot):
    dflet_uti = base[base['uti']==1].groupby(['ano_inter','idade_grupo_who']).agg({'id':'count','morte':'sum'}).reset_index()
    dflet_uti.columns = ['ano_inter','idade_grupo_who','admissoes','num']
    #df_merged = pd.merge(pop_ref, df,  how='left', left_on=['year','idade_grupo_who'], right_on=['ano_inter','idade_grupo_who']) # junta a quantidade por ano por faixa etária com a população de referencia
    dflet_uti['taxa'] = dflet_uti['num']/dflet_uti['admissoes'] # calcula a taxa
    dfletalidade_uti = pd.merge(dflet_uti, dfWHO,  how='left', left_on=['idade_grupo_who'], right_on=['age_group']) # junta o dataframe com a proporção do WHO
    dfletalidade_uti['obitos_esp'] = dfletalidade_uti['taxa']*dfletalidade_uti['world_avg_dec'] # calcula a proporção da quantidade esperados
    dfletalidade_uti = dfletalidade_uti.groupby(['ano_inter']).agg({'num':'sum','obitos_esp':'sum','admissoes':'sum','world_avg_dec':'sum'}).reset_index() # agrupa por ANO
    # tx = obts esp / pop
    #somar as faixas etarias do ano e dividir pela pop de ref total
    dfletalidade_uti['taxa_ajustada'] = dfletalidade_uti['obitos_esp']/dfletalidade_uti['world_avg_dec']
    dfletalidade_uti['taxa_ajustada_100mil'] = (dfletalidade_uti['taxa_ajustada']*100000).apply(np.ceil)
    dfletalidade_uti['taxa_bruta_100mil'] = (dfletalidade_uti['num']/dfletalidade_uti['admissoes'])*100000

    tx_let_uti = round((dfletalidade_uti['taxa_ajustada_100mil']),1)

    r = [0,1,2,3,4,5,6,7,8]

    fig, ax1 = plt.subplots(1,1,sharex=True,)
    p1 = ax1.plot(r, tx_let_uti, marker='o', markerfacecolor='#380282', markersize=4, color = '#380282' , label='Mortality rate')

    ax1.set_xticks(r, ["2011","2012","2013","2014","2015","2016","2017","2018","2019"])
    # ax1.set_yticks([0,10,20,30,40,50,60],['0%','10%','20%','30%','40%','50%','60%'])
    ax1.set_ylabel('Age-adjusted Lethality rate', fontweight='bold')
    ax1.set_title("Lethality when using UTI",fontweight='bold')

    for i in range(len(tx_let_uti)):
        ax1.text(r[i], tx_let_uti[i]+100, "%d" %tx_let_uti[i], ha="center", fontweight='bold')
        
    fig.set_facecolor("#E5F2A5")

    fig.set_figheight(6)
    fig.set_figwidth(12)
    plt.savefig(IMAGES_BASE_DIR+'letality_ratio_uti.png',dpi=1200)
    if(show_plot): plt.show()
    return









