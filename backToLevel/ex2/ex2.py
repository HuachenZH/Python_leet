# Ex2 : codage par substitution

import pandas as pd
import numpy as np
import random
import time

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


def plausibilite(str_subs:str, dict_st:dict) -> float :
    '''
    Compute the plausibilite of a string.
    Parameters
    ----------
    str_subs : str
        The encryted string after random swapping.
    dict_st : dict
        The dictionary of scores of doublets.
    Returns
    -------
    float
        The score of the string.
    '''
    score=0
    for i in range(len(str_subs)-1):
        score += dict_st.get(str_subs[i:i+2].upper())
    return score


def swap(swap1:str, swap2:str, str_subs:str) -> str:
    '''
    Swap two alphabets in a string. For example, all "a" become "b", all "b" become "a"

    Parameters
    ----------
    swap1 : str
        first alphabet.
    swap2 : str
        second alphabet.
    str_subs : str
        The string which will be operated.

    Returns
    -------
    str
        Swapped string.

    '''
    
    str_subs=str_subs.replace(swap1,"%")
    str_subs=str_subs.replace(swap2,swap1)
    str_subs=str_subs.replace('%', swap2)
    return str_subs
#%% ********************* df : standard *************************
# q1, creer un dictionnaire ... 
df = pd.read_csv('bigrammes.txt',  sep="\t", header=0)
df.set_index('10.5M', inplace=True) # put first column to meta data

# log stuffs
for c in df.columns:
    df[c]=df[c]+2 # add one to all elements so that there wont be zero nor one
    # log 0 does not exist. log 1 is 0
    df[c]=np.log10(df[c])

# resize them to 0 ~ 1.
# if not, value too small,  RuntimeWarning: overflow encountered in double_scalars RuntimeWarning: overflow encountered in double_scalars
# for c in df.columns:
#     df[c]=(df[c]-df.min().min())/(df.max().max()-df.min().min())
del(c)

dict_st=df2dict(df) # st stands for standard
# dict2=df2dict(df2)


str_subs="kinrqievxienirzitywryerygfbfjjehiyjgyrrinlirbftirgfnrseigijyhwtywbifeknwtgyhfntiithynetzigirygeywwglinibqwtebrygethnirseiwlhinjihtwmgirybrlyqnirringyhynfgizilinilwrylfbtnykywgirhinybtsewgliqfbbinywthietitniqirivhgwjytwfbrrengirikibilibtrsewykywibtlynseigybewthnijiqibtiwgbibawtnwibziginipynqywryawpenilihynetaytwpeiiriroievnfepwrbykywibthyritinyanyjxwrhyngirflliwgryhxorwfbflwiivhnwlywtebitnwrtirrihnfafbqiebniigjxypnwbwgyggywtitkibywtryrrioywtitrinigikywthnibywtebgwkniyexyrynqgymybqfbbywtyerrwtftjfbregtywtrirwbrtnelibtrrybrhnibqnirirbftirxymwteiggiritrilmgywtbihfekfwntibwnebwbrtybtibhgyji"
dictMapping={chr(i):chr(i) for i in range(97, 123)}

#%% HAL 9000

score=plausibilite(str_subs, dict_st)
print('initial score is : '+str(score))


dictMappingSpare=dictMapping.copy()


t = time.time()
nbrWithoutUpgrade=0
countIteration=0
nbrUpgrade=0
while nbrWithoutUpgrade < 6000 :
    countIteration+=1
    # remap stuffs
    # remap the string with the current mapping dictionary
    # for key, value in dictMapping.items():
    #     str_subs = swap(key, value, str_subs)
    
    # swap... new possibility
    swap1=chr(random.randrange(97,123))
    swap2=chr(random.randrange(97,123))
    str_subs_spare = str_subs # make a spare copy
    str_subs=swap(swap1,swap2,str_subs)
    
    
    # new score
    new_score = plausibilite(str_subs, dict_st)
    if new_score > score:
        # str_sub is already updated
        score = new_score # upgrade the score
        dictMapping[swap1],dictMapping[swap2]=dictMapping[swap2],dictMapping[swap1] # upgrade the mapping dictionary
        print("swapped at iteration "+str(countIteration))
        print(str_subs)
        print('\n')
        nbrWithoutUpgrade=0
        nbrUpgrade+=1
    else:
        str_subs = str_subs_spare # discard the upgrade of str_subs
        # do not upgrade the mapping dictionary
        # do not upgrade the score
        nbrWithoutUpgrade+=1
    
print("end score is "+str(score))
elapsed = time.time() - t
print("time elapsed: "+str(elapsed))
print('nbr mise a jour : '+str(nbrUpgrade))
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



#%% ********* df two cols ***************
df_new=resizedf(df)
# df2_new=resizedf(df2)

df_new.sort_values('probability', ascending=False, inplace=True)
# df2_new.sort_values('probability', ascending=False, inplace=True)



#%% test

    
