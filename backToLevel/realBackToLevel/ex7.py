
def grow_list(listt : list) -> list:
    listt.append((listt[len(listt)-1] * listt[len(listt)-2] + 1) / listt[len(listt)-3])
listt=[1,2,3]
for i in range(10):
    grow_list(listt)
print(listt)
