# elements = 45,4,8,5,87,5
# elements_list = list(elements) # self.list = [1,2,3,4]
# lst = []

# for i in range(len(elements_list)):
#     if elements_list[i+1]: #다음값이 존재한다면
#         node = self.LinkedNode(node_id = i, datum = elements[i], next = elements[i+1])
#         lst.append(node)
#     else: # 마지막값이면 next는 none
#         node = self.LinkedNode(node_id = i, datum = elements[i])
#         lst.append(node)

# print(lst)


lst = [43,46,123]


def sum(): 
    lst.pop()
    return lst

sum()
print(lst)