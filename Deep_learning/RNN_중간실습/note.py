# lr_list = [..] 

# for lr in lr_list:
#     train(lr = lr)

# initial_lr = ... 

# train(lr = lr) 

# plus_or_minus = random.random() > 0.5 

# if plus_or_minus:
#     lr += epsilon 
# else:
#     lr -= epsilon 

a_list = []

b_dict = {} 

for i in range(100): 
    b_dict[i] = i

a_list.append(b_dict)
a_list.append(b_dict)
print(a_list)