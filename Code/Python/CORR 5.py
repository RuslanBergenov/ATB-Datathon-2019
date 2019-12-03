import time
start = time.time()

# =============================================================================
# SET DIRECTORY
# =============================================================================
path = "my_path/data"
import os
os.chdir(path)
del(path)



# =============================================================================
# IMPORT PACKAGES
# =============================================================================
import pandas as pd
#import numpy as np

# =============================================================================
# READ IN CSV
# =============================================================================
v_Census_AgroLoc = pd.read_csv('v_Census (AgroLoc).csv', low_memory=False)



# =============================================================================
# DEAL WITH BLANK VALUES
# =============================================================================
v_Census_AgroLoc.isna().sum()
v_Census_AgroLoc["Unit of measure"] = v_Census_AgroLoc["Unit of measure"].fillna("NA")
v_Census_AgroLoc.isna().sum()


# =============================================================================
# PREVIEW
# =============================================================================
v_Census_AgroLoc_test_subset = v_Census_AgroLoc.head(10000) # select top N obs

print(v_Census_AgroLoc.columns.values) # print column names

v_Census_AgroLoc['GEO Level'].unique() # look at unique column names



#df = v_Census_AgroLoc.loc[(v_Census_AgroLoc['Census Year'] == 2016)]

#list = ('Country')

#test_check = v_Census_AgroLoc.loc[(v_Census_AgroLoc['GEO Level'] == 'Country') & (v_Census_AgroLoc['Indicator'] == 'Area from which crop residue was baled')]



# =============================================================================
# DATASET OF INTEREST
# =============================================================================

#farms by farm type
    #32100403
#Farms reporting technologies used on the operation in the year prior to the census
    #32100446

#To select rows whose column value is in list
list = (32100403, 32100446)

df  = v_Census_AgroLoc.loc[v_Census_AgroLoc['Dataset'].isin(list)]


df  = v_Census_AgroLoc.loc[v_Census_AgroLoc['Census Year']==2016]

df  = v_Census_AgroLoc.loc[(v_Census_AgroLoc['Dataset'].isin(list))& (v_Census_AgroLoc['Census Year']==2016)]


Type  = v_Census_AgroLoc.loc[(v_Census_AgroLoc['Dataset']==32100403)& (v_Census_AgroLoc['Census Year']==2016) & (v_Census_AgroLoc['GEO Level']=='Region') ]


Tech  = v_Census_AgroLoc.loc[(v_Census_AgroLoc['Dataset']==32100446)& (v_Census_AgroLoc['Census Year']==2016) & (v_Census_AgroLoc['GEO Level']=='Region') ]


#df = v_Census_AgroLoc



# =============================================================================
# CALCULATED VARIABLE
# =============================================================================
#
df['new'] = df.index


#df["Parameter"] = (df["Indicator"] + " - " + df["Indicator Level"] )

df["Parameter"] = (df["Indicator"] + " - " + df["Indicator Level"] + " - "+  df["Unit of measure"]) #add column


df["Parameter"] = (df["Indicator"] + " - " + df["Indicator Level"]) #add column

di_check = pd.DataFrame(df["Parameter"].unique())
df_test_subset = df.head(10000) # select top N obs


# =============================================================================
# PIVOT DATA FOR ANALYSIS
# =============================================================================
# =============================================================================
# # PIVOT DATA
# =============================================================================

#test_check = df.loc[(v_Census_AgroLoc['GEO Level'] == 'Country') & (df['Indicator'] == 'Area from which crop residue was baled')]


Kirill_Pivot_Table = pd.pivot_table(df, values='Value', index=['new', 'GEO Name'], columns='Parameter')
#
#Kirill_Pivot_Table = pd.pivot_table(df, values='Value', columns='Parameter')

# =============================================================================
# # SUBSET DATA BASED ON GEO TYPE
# =============================================================================


Country = df.loc[df['GEO Level'] == 'Country']
Region = df.loc[df['GEO Level'] == 'Region']
Province = df.loc[df['GEO Level'] == 'Province']
Division = df.loc[df['GEO Level'] == 'Division']
ConsSubdivision = df.loc[df['GEO Level'] == 'ConsSubdivision']



#df.to_csv('df_test.csv')



# function
def MY_PIVOT(table) :
    """ Pivot a subset of census data, so we can create a correlogram later """
    new_table = pd.pivot_table(table, values='Value', index='GEO Name', columns='Parameter', aggfunc='mean')

    return new_table



Pvt_Province= MY_PIVOT(Province)
Pvt_Region = MY_PIVOT(Region)
Pvt_Division = MY_PIVOT(Division)
Pvt_ConsSubdivision = MY_PIVOT(ConsSubdivision)
Pvt_All = MY_PIVOT(df)

Pvt_Region_Power_BI =  pd.pivot_table(Region, values='Value', index='GEO Name', columns='Parameter', aggfunc='mean')



# =============================================================================
# CORRELATIONS
# =============================================================================


# create corr matrices via function
def MY_CORR(pivot_table):
    """ create a correlation matrix from a pivoted dataframe """
    corr_matrix = pivot_table.corr()
    return corr_matrix


Corr_Province = MY_CORR(Pvt_Province)
Corr_Region = MY_CORR(Pvt_Region)
Corr_Division = MY_CORR(Pvt_Division)
Corr_ConsSubdivision = MY_CORR(Pvt_ConsSubdivision)
Corr_All = MY_CORR(df)





# =============================================================================
# FUNCTION CORRELOGRAM
# =============================================================================
def MY_CORRELOGRAM(pivot_table, exportfilename='File'):
    """ create a correlogram from a pivot table """
    #from string import ascii_letters
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(style="white")


    # Compute the correlation matrix
    corr = pivot_table.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(20, 30))

    # Generate a custom diverging colormap
    #cmap = sns.diverging_palette(220, 10, sep=20, as_cmap=True)
    #cmap = sns.diverging_palette(220, 10, sep=20, as_cmap=True)

    plt.title(('Correlations Part ' + exportfilename), fontsize=25)




    cmap = sns.diverging_palette(250, 10, sep=200, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    ax.figure.savefig((exportfilename + '.jpeg'),  bbox_inches='tight')




print("Pvt_Province_Territory")
MY_CORRELOGRAM(Pvt_Province, exportfilename='1 - Provinces & Territories')

print("Pvt_CensusAgriculturalRegion")
MY_CORRELOGRAM(Pvt_Region, exportfilename='2 - Census Agricultural Regions')

print("Pvt_CensusDivision")
MY_CORRELOGRAM(Pvt_Division, exportfilename='3 - Census Divisions')

print("Pvt_CensusConsolidatedSubdivision")
MY_CORRELOGRAM(Pvt_ConsSubdivision, exportfilename='4 - Census Consolidated Subdivisions')



end = time.time()
Time_Code_Ran_Seconds = end - start
Time_Code_Ran_Minutes_Decimal = Time_Code_Ran_Seconds / 60

print('Time the code ran in seconds is: ' + str(Time_Code_Ran_Seconds))
print('Time the code ran in minutes (decimal): ' + str(Time_Code_Ran_Minutes_Decimal))


# =============================================================================
# play a sound when done running the code
# on a GOA machine it's super quiet
# =============================================================================
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)


# =============================================================================
# EXPORT CSV
# =============================================================================
df.to_csv('df.csv')
Pvt_Region.to_csv('Pvt_Region.csv')
Corr_Region.to_csv('Corr_Region.csv')


Type.to_csv('Type.csv')
Tech.to_csv('Tech.csv')
