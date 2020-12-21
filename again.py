import pandas as pd
import numpy as np

art = pd.read_csv("/Users/John Demetriades/Desktop/artworks.csv")
print(art.shape) #prints shape
print(type(art)) #prints type -> Dataframe, collection of series
print(art.info) # prints some rows which are numbered and shape at bottom
print(art.head(2)) #prints 2 top rows
print(art.tail(2)) # prints 2 last rows

'''
loc vs iloc
loc, it's for label based selection
iloc, it's for integer position pased selection 
'''

#Indexing-Using loc in Dataframe
#labes are numbers for index and cell-names for columns
print(art.loc[1:3,["Title", "Artist"]]) #loc requires exact names
print(art[["Title","Artist"]]) # result same as the previous/prints columns
print(art.loc[1:3,[True,True,False,False,False,False,False,False]]) #prints the same as before as it can take a list of "0s and 1s"
print(art.loc[:,"Title":"Nationality"]) #prints a certain Dataframe
print(art.loc[0][0]) #print first row's first column
print(art.loc[1]) #print second row
'''
If loc is not used, then dt[li] prints the columns that are in the list li
To print rows only, use dt.loc[li], which li is a list of row names
'''

#Indexing-Using iloc in Dataframe ()
art_2 = pd.read_csv("/Users/John Demetriades/Desktop/artworks.csv", header = 2) #uses row 3 as the column names

'''
print(art_2.loc[2,"Duplicate of plate from folio 11 verso (supplementary suite, plate 4) from ARDICIA"])
run the code to see an example
remember that here the column labels are the values of the 3rd row of the csv file (ie (Spanish) is a column value)
'''

print(art_2.head(2))
print("iloc:")
print(art_2.iloc[2]) #prints second row
print(art_2.iloc[2,3]) #only use integers, labels will lead to error
print(art_2.iloc[[1,2,3],[1,2,3]])
test = art_2["-2007"].isnull() #see later, creates a Series of booleans (ie True when it is null) -> -2007 corresponds ro EndDate
print(art_2[test])


#Indexing-Using loc in Series
sr = art.loc[1] #creates Series
print(sr[0]) #prints first element of Series
print(sr.loc["Title"]) #prints same as before

#Understand Dataframe and Series types
print(type(art.loc[:,"Title"])) #prints type -> Series, similar to list
print(type(art.loc[:,["Title"]])) #prints type -> Dataframe, additional []
print(type(art.loc[:,"Title":"Nationality"])) #prints type -> Dataframe

#Use value_coutns in Series 
nat = art["Nationality"]
nat = nat.value_counts() #returns count of each element in Series
#use count in Series
europe = nat[["(French)","(German)","(British)"]] #returns 3x1 matrix with the counts of each element
print(type(europe)) #dtype64
print(europe)

#create a list of Trues and False from row and column values
t_f_li = art["Nationality"] == "(British)" #returns Series of True's if nationality is British
print(art.loc[t_f_li,"Artist"]) #prints artists with british nationality

#replacing values with np.nan (NAN)
print(europe)
art.loc[art["Nationality"] == "(French)","Nationality"] = np.nan #values of French people is NAN
print(art["Nationality"].value_counts()) #There is no French artists in Series

# #combination of commands
# print(art.loc[:,["Title","Artist","Nationality"]].head(5))


art_2 = pd.read_csv("/Users/John Demetriades/Desktop/artworks.csv")

#Series.isnull() or Series.notnul()
print(art_2.shape)
print(art_2.info())
end_date = art_2["EndDate"].isnull() #return a Series of booleans (True when is null)
not_end_date = art_2["EndDate"].notnull() 
print(type(end_date))
'''
Playing around
print(end_date + not_end_date)
print(end_date * not_end_date)
'''
print(art_2.loc[end_date,["Title","Artist"]]) #prints Title and Name for each row with null end date
test = art_2[art_2["EndDate"].isnull()]
'''
Small Project: Print Name and Age of dead artists
'''
print(art_2.iloc[:5]) #print first five rows of Data with no EndDate
age = art_2.loc[not_end_date,"BeginDate"] - art_2.loc[not_end_date,"EndDate"] #return ages of dead artist
names = art_2.loc[not_end_date,"Artist"] 
ng = {"Artist":names,"Age":age}
name_age = pd.DataFrame(data = ng) #data takes dictionaries, see documentation of DataFrame to see other ways
print(name_age.head())

#Operations
print(end_date & not_end_date) # and, True and False -> False
print(end_date | not_end_date) # or, True or False -> True
print(~end_date) #not, True -> False
'''
Small Project: Print the artists that died between 1950 and 2000
'''
ex = (art_2.loc[not_end_date,"EndDate"] > -2000) & (art_2.loc[not_end_date,"EndDate"] < -1950) 
not_end = art_2[not_end_date]
ng = {"Artist":not_end.loc[ex,"Artist"], "EndDate":not_end.loc[ex,"EndDate"]}
n = pd.DataFrame(data=ng)
print(n.head())

#sort by column
begin = art_2.sort_values("BeginDate", ascending = False) #return dataframe in descending order wt=ith respect to BeginDate column
print(begin.head)
