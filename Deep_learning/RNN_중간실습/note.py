a_dict = {}
b_dict = {}

for i in range(10): 
    a_dict[i] = i

for j in range(10,20): 
    b_dict[i] = j

a_dict.update(b_dict)

for i in range(len(a_dict)): 
    print(a_dict)