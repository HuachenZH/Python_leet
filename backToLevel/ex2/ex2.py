# Ex2 : codage par substitution

import pandas as pd
import numpy as np
import collections
#%% ****************** fct df2dict **********************
def df2dict(df) -> dict :
    '''
    Turns a pandas data frame to a dictionary. 

    Parameters
    ----------
    df : pandas dataframe
        The dataframe to be transformed into dictionary.

    Returns
    -------
    dict
        Dictionary based on data of the input data frame. The keys of the dictionary will be like "AA", "AB"... "ZY", "ZZ"

    '''
    dict_df={}
    for index, row in df.iterrows():
        for index2, value in row.items():
            dict_df[ index[0]+index2[1] ] = value
    return dict_df


def resizedf(df):
    '''
    Transform a two-dimension pandas data frame into an one-dimension data frame.

    Parameters
    ----------
    df : pandas data frame
        Two-dimension data frame, row name is like : "A_", "B_"... col name is like "_A", "_B"...

    Returns
    -------
    df_new : pandas data frame
        One dimension, from "AA", "AB", ... til "ZY", "ZZ".

    '''
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


def plausibilite(str_subs:str, df) -> float :
    '''
    Compute the plausibilite of a string.

    Parameters
    ----------
    str_subs : str
        The encryted string after random swapping.
    df : pandas data frame
        The pandas data frame of the score of doublets.

    Returns
    -------
    float
        The score of the string.

    '''
    score=1
    for i in range(len(str_subs)-1):
        score *= df.loc[str_subs[i:i+2].upper()[0]+'_' , '_'+str_subs[i:i+2].upper()[1]] # corresponding score of the doublet
    return score

#%% ********************* df : standard *************************
# q1, creer un dictionnaire ... 
df = pd.read_csv('bigrammes.txt',  sep="\t", header=0)
df.set_index('10.5M', inplace=True) # put first column to meta data


for c in df.columns:
    df[c]=df[c]+2 # add one to all elements so that there wont be zero nor one
    # log 0 does not exist. log 1 is 0
    df[c]=np.log10(df[c])

# sumAllElements=df.to_numpy().sum() # sum of all elements of dataframe
# df=df/sumAllElements # standardize dataframe
# del(sumAllElements)

str_subs="kinrqievxienirzitywryerygfbfjjehiyjgyrrinlirbftirgfnrseigijyhwtywbifeknwtgyhfntiithynetzigirygeywwglinibqwtebrygethnirseiwlhinjihtwmgirybrlyqnirringyhynfgizilinilwrylfbtnykywgirhinybtsewgliqfbbinywthietitniqirivhgwjytwfbrrengirikibilibtrsewykywibtlynseigybewthnijiqibtiwgbibawtnwibziginipynqywryawpenilihynetaytwpeiiriroievnfepwrbykywibthyritinyanyjxwrhyngirflliwgryhxorwfbflwiivhnwlywtebitnwrtirrihnfafbqiebniigjxypnwbwgyggywtitkibywtryrrioywtitrinigikywthnibywtebgwkniyexyrynqgymybqfbbywtyerrwtftjfbregtywtrirwbrtnelibtrrybrhnibqnirirbftirxymwteiggiritrilmgywtbihfekfwntibwnebwbrtybtibhgyji"

plausibilite(str_subs, df)




#%% ******************* df2 : of our string ************************
# create another data frame with zeros and the same meta data

# df2=df.copy()
# for col in df2.columns:
#     df2[col].values[:]=0
# del(col)
# # count bigrammes in str_subs
# for i in range(len(str_subs)-1):
#     bigramme_actual = str_subs[i:i+2]
#     df2.iloc[ord(bigramme_actual[0])-97 , ord(bigramme_actual[1])-97]+=1
# del(i)
# del(bigramme_actual)
# # standardize df2
# df2=df2/df2.to_numpy().sum()


#%% ******************** dicts **************************
dict_st=df2dict(df) # st stands for standard
# dict2=df2dict(df2)

#%% ********* df two cols ***************
df_new=resizedf(df)
# df2_new=resizedf(df2)

df_new.sort_values('probability', ascending=False, inplace=True)
# df2_new.sort_values('probability', ascending=False, inplace=True)






#%% test


