lr_list = [..] 

for lr in lr_list:
    train(lr = lr)

initial_lr = ... 

train(lr = lr) 

plus_or_minus = random.random() > 0.5 

if plus_or_minus:
    lr += epsilon 
else:
    lr -= epsilon 

