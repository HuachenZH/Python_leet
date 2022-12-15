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
    for index, row in df.iterrows(): # .iterrows: une méthode pour pandas dataframe, pour itérer les lignes
        for index2, value in row.items():
            dict_df[ index[0]+index2[1] ] = value
            # index est A_, B_, C_ ...
            # index2 est _A, _B, _C ...
    return dict_df


def resizedf(df): # cette fonction n'est pas utilisée
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
#%% ********************* préparer dataframe et dictionnaire *************************
# q1, creer un dictionnaire ... 
# dans ma solution j'utilise la librairie Pandas pour traiter le tableaux.
# Pandas est dédié pour la data science, il est puissant quand il s'agit une grande quantité de donnée
df = pd.read_csv('bigrammes.txt',  sep="\t", header=0)
# pd veut dire pandas, j'avais fait import pandas as pd, pd est l'alias que je donne à pandas
# pour les développeur python, souvent on appelle pandas pd, numpy np, c'est comme une convention

df.set_index('10.5M', inplace=True) 
# put first column to meta data
# dans bigrammes.txt, la premiere colonne est A_, B_, C_ ... etc. On le met dans meta data (=nom de colonne)

# log stuffs
# pour faciliter le calcul du score plus tard, on met le tableau en échelle logarithme
for c in df.columns:
    df[c]=df[c]+1 # add one to all elements so that there wont be zero, cuz log 0 does not exist. 
    df[c]=np.log10(df[c])


del(c) # nettoyage, enlever la variable temporaire que je n'ai pas besoin plus tard

dict_st=df2dict(df) # st stands for standard
# j'ai fait une fonction df2dict, dataframe to dictionary
# j'ai trouvé qu'avec dataframe de pandas, ça peut marcher mais il prend bcp de temps,
# donc finalement je dois transformer à dictionnaire
# apres on va travailler avec ce dictionnaire

# le string à décoder :
str_subs="kinrqievxienirzitywryerygfbfjjehiyjgyrrinlirbftirgfnrseigijyhwtywbifeknwtgyhfntiithynetzigirygeywwglinibqwtebrygethnirseiwlhinjihtwmgirybrlyqnirringyhynfgizilinilwrylfbtnykywgirhinybtsewgliqfbbinywthietitniqirivhgwjytwfbrrengirikibilibtrsewykywibtlynseigybewthnijiqibtiwgbibawtnwibziginipynqywryawpenilihynetaytwpeiiriroievnfepwrbykywibthyritinyanyjxwrhyngirflliwgryhxorwfbflwiivhnwlywtebitnwrtirrihnfafbqiebniigjxypnwbwgyggywtitkibywtryrrioywtitrinigikywthnibywtebgwkniyexyrynqgymybqfbbywtyerrwtftjfbregtywtrirwbrtnelibtrrybrhnibqnirirbftirxymwteiggiritrilmgywtbihfekfwntibwnebwbrtybtibhgyji"

dictMapping={chr(i):chr(i) for i in range(97, 123)}
# c'est une ligne de code permettant de créer un dictionanire comme ça: {'a':'a', 'b':'b', 'c':'c'.... 'z':'z'}
# le key est pour plaintext, value est pour ciphertext
# le contenu de ce dictionnaire va changer au fur et à mesure
# par ex si je trouve le 'k' de ciphertext correpond à 'v' de plaintext, le dictionnaire sera:
# {...'v': 'k'.....}

#%% HAL 9000

score=plausibilite(str_subs, dict_st)
print('initial score is : '+str(score))


dictMappingSpare=dictMapping.copy()
# faire un copy au cas où j'ai besoin
# dans python, si je fais dict2 = dict1, puis je change dict1, dict2 va aussi etre changé
# c'est pour ça jai fait .copy()


t = time.time()
nbrWithoutUpgrade=0
countIteration=0
nbrUpgrade=0
while nbrWithoutUpgrade < 6000 :
# la condition pour stopper le while:
# si pour 6000 essaie enchainé, le score n'est pas amélioré, on sort la boucle while
    countIteration+=1
    
    # swap... new possibility
    # selon la méthode du prof, on va prendre deux lettre aléatoirement et tester
    # si le score est mieux, on garde le changement
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
elapsed = time.time() - t # calculer ça prend combien de temps pour finir la boucle while
print("time elapsed: "+str(elapsed))
print('nbr mise a jour : '+str(nbrUpgrade))








#%% test
