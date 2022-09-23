# Ex2 : codage par substitution

import pandas as pd
import numpy as np
import collections
#%% ****************** fct df2dict **********************
def df2dict(df) -> dict :
    dict_df={}
    for index, row in df.iterrows():
        # print(index)
        # print(row)
        for index2, value in row.items():
            # print(index2)
            # print(value)
            dict_df[ index[0]+index2[1] ] = value
    return dict_df
# del(index)
# del(index2)
# del(row)
# del(value)

#%% ******************* fct resizedf ****************
def resizedf(df):
    arr=[[],[]]
    for index, row in df.iterrows():
        for i,v in row.items():
            # print(index[0]+i[1])
            arr[0].append(index[0]+i[1])
            arr[1].append(v)
    df_new=pd.DataFrame(arr)
    df_new=df_new.T # transpose, swap row and column
    df_new.columns=["doublet", "probability"]
    return df_new

#%% ********************* df : standard *************************
# q1, creer un dictionnaire ... 
df = pd.read_csv('bigrammes.txt',  sep="\t", header=0)
df.set_index('10.5M', inplace=True) # put first column to meta data
sumAllElements=df.to_numpy().sum() # sum of all elements of dataframe
df=df/sumAllElements # standardize dataframe
del(sumAllElements)

str_subs="kinrqievxienirzitywryerygfbfjjehiyjgyrrinlirbftirgfnrseigijyhwtywbifeknwtgyhfntiithynetzigirygeywwglinibqwtebrygethnirseiwlhinjihtwmgirybrlyqnirringyhynfgizilinilwrylfbtnykywgirhinybtsewgliqfbbinywthietitniqirivhgwjytwfbrrengirikibilibtrsewykywibtlynseigybewthnijiqibtiwgbibawtnwibziginipynqywryawpenilihynetaytwpeiiriroievnfepwrbykywibthyritinyanyjxwrhyngirflliwgryhxorwfbflwiivhnwlywtebitnwrtirrihnfafbqiebniigjxypnwbwgyggywtitkibywtryrrioywtitrinigikywthnibywtebgwkniyexyrynqgymybqfbbywtyerrwtftjfbregtywtrirwbrtnelibtrrybrhnibqnirirbftirxymwteiggiritrilmgywtbihfekfwntibwnebwbrtybtibhgyji"
# len(str_subs) gives 592



#%% ******************* df2 : of our string ************************
# create another data frame with zeros and the same meta data
df2=df.copy()
for col in df2.columns:
    df2[col].values[:]=0
del(col)
# count bigrammes in str_subs
for i in range(len(str_subs)-1):
    bigramme_actual = str_subs[i:i+2]
    df2.iloc[ord(bigramme_actual[0])-97 , ord(bigramme_actual[1])-97]+=1
del(i)
del(bigramme_actual)
# standardize df2
df2=df2/df2.to_numpy().sum()


#%% ******************** dicts **************************
dict_st=df2dict(df) # st stands for standard
dict2=df2dict(df2)

#%% ********* df two cols ***************
df_new=resizedf(df)
df2_new=resizedf(df2)

df_new.sort_values('probability', ascending=False, inplace=True)
df2_new.sort_values('probability', ascending=False, inplace=True)

