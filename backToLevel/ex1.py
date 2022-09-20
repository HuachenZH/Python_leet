import numpy
class Solution:
    # décaler chq caractere de la valeur de key
    def shift(self, key: int, texte: str) -> str:
        listord=''
        for alphabet in texte:
            newVal=ord(alphabet)+key
            if newVal>122:
                # newVal=newVal-122+97-1
                newVal=(newVal-122)%26+97-1
            listord+=chr(newVal)
        return listord
    # decaler chq caractere, avec tous les decodagge possibles
    def multishift(self, texte:str) -> list:
        out=[]
        for i in range(1,26):
            out.append(self.shift(i,texte))
            print('the value is '+str(i))
            print(out[i-1])
            print('--               --')
            # notice : can use enumerate() to print this
        return out
    # donner un score de vraisemblance a partir de la frequence des lettres
    def value(self, key:int, texte: str) -> dict:
        outdict={}

        newText=self.shift(key,texte)
        for i in range(97,123):
            #
            outdict[chr(i)]=newText.count(chr(i))/len(texte)*100
        return outdict

    # donne le decodage le plus vraisemblable vis a vis de la frequence des lettres
    
    def decode_cesar(self, texte:str) -> int:
        #
        valueDict={}
        scorelist=[]
        # sorted by a to z
        vectStandard=numpy.array([7.68,0.80,3.32,3.60,17.76,1.06,1.10,0.64,7.23,0.19,0.00,5.89,2.72,7.61,5.34,3.24,1.34,6.81,8.23,7.30,6.05,1.27,0.0,0.54,0.21,0.07])
        for i in range(1,26):
            valueDict=self.value(i, texte)
            vectThis=[]
            for key in sorted(valueDict):
                # print (key, valueDict[key])
                vectThis.append(valueDict[key]) # score of each letter, sorted by a to z
            vectThis=numpy.array(vectThis)
            score=(numpy.sum((vectStandard[:]-vectThis[:])**2))**0.5
            scorelist.append(score)
            # print(score)
        print('min score is : '+str(min(scorelist)))
        scorelist=numpy.array(scorelist)
        return numpy.where(scorelist == scorelist.min())[0][0]+1


epsilon=Solution()
texte="hqdepqgjtqgdqevqfmuemgemxazaoogbqmoxmeeqdyqezafqexadecgqxqombufmuzqaghdufxmbadfqqfbmdgfvqxqemxgmuuxyqdqzpufgzemxgfbdqecgquybqdoqbfunxqemzeympdqeeqdxmbmdaxqvqyqdqyuemyazfdmhmuxqebqdmzfcguxyqpazzqdmufbqgfqfdqpqeqjbxuomfuazeegdxqeqhqzqyqzfecgumhmuqzfymdcgqxmzgufbdqoqpqzfquxzqzrufduqzvqxqdqsmdpmuemrusgdqyqbmdgfrmfusgqqeqekqgjdagsuezmhmuqzfbmeqfqdmrdmotuebmdxqeayyquxembtkeuazayuqqjbduymufgzqfduefqeeqbdarazpqgzdqqxotmsduzuxmxxmufqfhqzmufemeeqkmufqfeqdqxqhmufbdqzmufgzxuhdqmgtmemdpxmnmzpazzmufmgeeufafoazegxfmufeqeuzefdgyqzfeemzebdqzpdqeqezafqetmnufgqxxqeqfeqynxmufzqbaghaudfqzudgzuzefmzfqzbxmoq"
epsilon.multishift(texte)
print('--------------')
# print(epsilon.value(1,texte))
# print('--------------')
print(epsilon.decode_cesar(texte))

# a to z
# 97 to 122


