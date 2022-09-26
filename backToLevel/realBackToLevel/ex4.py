nb=1949

nbcp=nb
unities=[500, 200, 100, 50, 20, 10, 5, 2, 1]
value=[]
for unity in unities:
    value.append(nbcp//unity)
    nbcp=nbcp%unity
    # print(nbcp)
print(value)

out=''
for i in range(len(unities)):
    if value[i]!=0:
        out+=str(unities[i])+"*"+str(value[i])+'+'
out=out[:len(out)-1]
print(out)
