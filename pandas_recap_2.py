import pandas as pd 
import numpy as np  

art = pd.read_csv("/Users/John Demetriades/Desktop/artworks.csv")
happiness2015 = pd.read_csv("/Users/John Demetriades/Desktop/World_Happiness_2015.csv")
happiness2016 = pd.read_csv("/Users/John Demetriades/Desktop/World_Happiness_2016.csv")
happiness2017 = pd.read_csv("/Users/John Demetriades/Desktop/World_Happiness_2017.csv")
'''
Concatenate pandas objects - Combining pandas objects
concat
To understand see the "axis" works, go to: https://app.dataquest.io/m/344/combining-data-with-pandas/3/combining-dataframes-with-the-concat-function-continued 
'''
column_zero = art.iloc[:,0]
column_three = art.iloc[:,2]
combined_columns = pd.concat([column_zero,column_three],axis = 1) #combine columns/ combine allong index
print(combined_columns.shape)
print(combined_columns)
combined_index = pd.concat([column_zero,column_three],axis = 0) #combines indexs/ combines allong columns
print(combined_index)
print(combined_index.shape) 
rows_top = art[["Artist","BeginDate","EndDate"]].head()
rows_bottom = art[["Artist","EndDate"]].tail()
rows = pd.concat([rows_top,rows_bottom],ignore_index = True) #here the index of the new Dataframe is reset/ from 0 to n-1
rows_not_ignore = pd.concat([rows_top,rows_bottom],ignore_index = False) #here the index of the Dataframe corresponds to the actual index of the values
print(rows)
print(rows_not_ignore)
'''
merge, to combine Dataframes on a key
the output is only on the values that are common (ie in this case only for Norway, as it is included in both Dataframes)
'''
happiness2015["Year"] = 2015
happiness2016["Year"] = 2016
happiness2017["Year"] = 2017 #adding a new column at the end with the Year = 2017

three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]

merged = pd.merge(left = three_2015, right = three_2016, on = "Country")
print(merged)
merged = pd.merge(left = three_2015, right = three_2016,how = "left",on = "Country", suffixes = ("_2015","_2016")) #merging based on  left - three_2015 (values not in three_2016 will appear as NaN)
                                                                                                                   #suffixes, replace _x with the corresponding value
print(merged)
merged = pd.merge(left = three_2015, right = three_2016, suffixes = ("_2015","_2016"), left_index = True, right_index = True) #all countries are include/ there is no "on" parameter
print(merged)
#see the differences between, pd.concat() and pd.merge() at: https://app.dataquest.io/m/344/combining-data-with-pandas/9/challenge-combine-data-and-create-a-visualization
three_2015 = three_2015.rename({"Country":"country"},axis = 1)
print(pd.merge(left = three_2015,right = three_2016,left_on = "country",right_on = "Country")) #left_on and right_on go together, in the case I need to specify the columns and they dont have the same name

'''
Rename index/column
'''
mapping = {"Country" : "country","Region":"region","Happiness Rank":"Rank","Happiness Score":"Score","Economy (GDP per Capita)": "Economy","Health (Life Expectancy)":"Health","Trust (Government Corruption)":"Trust"}
happiness2015 = happiness2015.rename(mapping, axis = 1) #change columns name (axis = 0 for index, axis = 1 for columns)
print(happiness2015.head())

'''
Series.map
Works only on series

apply
works on Dataframe and Series
works series-wise
for Dataframe, only functions like np.sum and other that invoke the whole Series of the Dtaframe can be used

applymap
works on Dataframe only 
works element-wise
'''
def hl(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'

print(happiness2015["Economy"].map(hl)) #use function

def label(element, x):
    if element > x:
        return 'High'
    else:
        return 'Low'

print(happiness2015["Economy"].apply(label,x =0.8)) #this cannot be done on map

factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
print(happiness2015[factors].applymap(hl)) #wont work using apply, as it is element wise

def value(element):
    return element.sum()
print(happiness2015[factors].apply(value)) #function, invokes a function Series-wise


H_L = happiness2015[factors].applymap(hl)
print(H_L)
def v_counts(col):
    '''
    counts how many Highs and Lows exist in each Series
    divide by size fo each Series to get proportion of Highs and Lows
    '''
    num = col.value_counts() #inique values per Series
    den = col.size 
    return num/den

v_counts_pct = H_L[factors].apply(v_counts)
print(v_counts_pct)
    
'''
melt -> id_vars = identifier variables, value_vars = meausred variavles
id_vars, are included in the new DataFrame
value_vars, are in the variable column and there is an extra column "value" which shows the corrsesponding value
'''
main_cols = ['country', 'region', 'Rank', 'Score'] #columns
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust'] #variables
melt = pd.melt(happiness2015, id_vars = main_cols, value_vars = factors) 
melt['Percentage'] = round(melt['value']/melt['Score'] * 100, 2) #create new column
print(melt)