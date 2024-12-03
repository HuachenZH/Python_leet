from day2_2_PROTOTYPE import prototype



def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

data = [[int(y) for y in x.split(' ')] for x in open('data.txt').read().split('\n') if x]

safe_count = sum([is_safe(row) for row in data])
#print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)


list_correct_bool = [any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data]
list_correct =[data[i]  for i in range(len(data)) if list_correct_bool[i]] 
list_correct = ["_".join([str(elem) for elem in row]) for row in list_correct]


list_mine = prototype()

analysis = set(list_correct) - set(list_mine)

# 51_51_50_49_48
breakpoint()