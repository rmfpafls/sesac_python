# --------------------------------------------
# 1. 패턴 찍는 함수들 만들어보기 
# 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid1를 짜 보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

# write your code here 
star ="*"
blank = " "
how_many_star = int(input("피라미드를 몇 층 만들까요? : "))

def pyramid1(n):
    for i in range(n): 
        print(blank*(n-i)+star*(2*i-1))

pyramid1(how_many_star)

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid2를 짜 보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 
star_and_blank = star+blank
def pyramid2(n):
    for i in range(n): 
        print(blank*(n-i)+star_and_blank*i)

pyramid2(how_many_star)

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid3를 짜 보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 
large_letter = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def pyramid3(n):
    for i in range(n):
        print(blank*((n-1)-i), end ="")
        for j in range(i):
            print(large_letter[j]+blank, end ="")
        print()

pyramid3(how_many_star)

# -------------------------------------------- 
# 4) 피라미드 찍어보기 - 4 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid4를 짜 보세요. 
# 
#       1 
#      1 1 ##0 i = 0 여기서부터 만약 input이 10이라면 중간값은 print x
#     1 2 1 ##1 i = 1 // 
#    1 3 3 1 ##2
#   1 4 6 4 1 ##3
# --------------------------------------------

# write your code here 
def pyramid4(n):
    number_list = []
    temp = []

    for i in range(n): 
        number_list.append(1)
        temp.append(1)
        
        if i < 2:
            pass
        else: 
            for j in range(1,len(number_list)-1):
                temp[j] = number_list[j-1]+number_list[j]
        
        print(blank*(n+2-i), end="")

        for j in range(len(number_list)):
                number_list[j] = temp[j]
                print(str(number_list[j]), blank, end ="")
        print()
 
pyramid4(how_many_star)


# --------------------------------------------
# 5) 다음 패턴을 찍는 함수 sierpinski_triangle을 짜 보세요. 

# n = 2
#         * 
#        * * 
#       *   *
#      * * * *

# 
# n = 3 
#                 * 
#                * *
#               *   *
#              * * * *
#             *       * 
#            * *     * *
#           *   *   *   * 
#          * * * * * * * *
#         *               *   
#        * *             * *  
#       *   *           *   * 
#      * * * *         * * * *
#     *       *       *       *  
#    * *     * *     * *     * *
#   *   *   *   *   *   *   *   * 
#  * * * * * * * * * * * * * * * *
# --------------------------------------------

# write your code here 
def sierpinski_triangle(n):
        if n == 3:
            return ['  *  ',' * * ','*****']

        arr = sierpinski_triangle(n//2)
        stars = []
        for i in arr:
            stars.append(' '*(n//2)+i+' '*(n//2))

        for i in arr:
            stars.append(i + ' ' + i)

        return stars

print('\n'.join(sierpinski_triangle(12)))

# solution
def triangle():
    lines = [\
      '   *    ',
      '  * *   ',
      ' *   *  ',
      '* * * * ',
    ]
    return lines 

def lstsum(l, r):
    assert len(l) == len(r)
    
    res = []
    for i in range(len(l)):
        res.append(l[i] + r[i])

    return [(a+b) for a, b in zip(l, r)]

def big_triangle():
    res = []
    res += [' ' * 4 + line + ' ' * 4 for line in triangle()]
    
    res += lstsum(triangle(), triangle())
    
    return res 

# print('\n'.join(big_triangle()).replace(' ', '0'))

def big_big_triangle():
    res = []
    res += [' ' * 8 + line for line in big_triangle()]
    
    res += lstsum(big_triangle(), big_triangle())
    
    return res 

# print('\n'.join(big_big_triangle()))

def sierpinski_triangle_list(n):
    if n == 1:
        return triangle()
    else:
        res = [' '*2**n + line + ' '*2**n for line in sierpinski_triangle_list(n-1)]
        res += lstsum(sierpinski_triangle_list(n-1), sierpinski_triangle_list(n-1))
        return res 

def sierpinski_triangle(n):
    return '\n'.join(sierpinski_triangle_list(n))

print(sierpinski_triangle(1))
print(sierpinski_triangle(2))
print(sierpinski_triangle(3))
print(sierpinski_triangle(4))




# --------------------------------------------
# 2. 여러 리스트 관련 함수들 구현해보기 
#
# 아래 함수들은 대부분 itertools에 있는 함수들임. 
# itertools를 쓰지 말고 구현해 볼 것.  
#
# 1) accumulate(lst, function = lambda x, y : x+y)
# 
# lst의 각 원소들에 대해서, function을 누적하여 적용한 리스트를 반환. 
# lst -> [lst[0], f(lst[0], lst[1]), f(lst[2], f(lst[1], lst[0])), ...] 
# --------------------------------------------

# write your code here 
def accumulate(lst, function = lambda x, y: x+y):
    new_list = []

    for i in range(len(lst)):
        if i == 0: 
            new_list.append(lst[i])
        else: 
            add_list = function(new_list[-1],lst[i])
            new_list.append(add_list)

    return new_list


print(accumulate([1,2,3,4])) 
    


# --------------------------------------------
# 2) batched(lst, n)
# 
# lst의 원소들을 n개의 인접한 원소들끼리 묶은 리스트를 반환. 

# ex) batched([1,2,3,4,5], 2) 
#     >> [(1,2), (3,4), (5,)]
# ex) batched(['a', 'b', 1, 3, 6, 1, 3, 7], 3) 
#     >> [('a', 'b', 1), (3, 6, 1), (1, 3, 7)]
# --------------------------------------------

# write your code here  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def batched(lst, n):
    new_list = []

    for i in range(0, len(lst),n):
        duo = lst[i:i+n]

        if len(duo) < n:
            duo += [None] * (n - len(duo))
        new_list.append(tuple(duo))

    return new_list

lst = [1,2,3,4,5,6]
n = 4

# print(batched(lst, n))
    

# --------------------------------------------
# 3) product(args)
# 
# list들의 list args를 받아서, 각각의 리스트에서 하나씩의 원소를 뽑은 튜플들의 리스트를 반환. 
# ex) product([[1,2,3], [4,5,6])
#     >> [(1,4), (1,5), (1,6), 
#         (2,4), (2,5), (2,6), 
#         (3,4), (3,5), (3,6),] 
# --------------------------------------------

# write your code here 
def product(args):
    product_list = []

    for i in range(len(args[0])):
        product_list.append((args[0][i], args[1][i]))
    return product_list

args = [1,2,3], [4,5,6]
print(product(args))
# --------------------------------------------
# 4) permutations(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 permutation의 리스트를 반환. 
# permutation이란, 순서를 가지면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 다르고, 1,1은 허용되지 않음. 
# ex) permutations([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,1), (2,3), (2,4), (2,5), 
#         (3,1), (3,2), (3,4), (3,5), 
#         (4,1), (4,2), (4,3), (4,5), 
#         (5,1), (5,2), (5,3), (5,4),]
# --------------------------------------------

# write your code here 
def permutations(lst, r):
    permutations_list = []
    stuff = []

    for i in range(r): 
        stuff.append

        for j in range(len(lst)):

# --------------------------------------------
# 5) combination(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 combination의 리스트를 반환. 
# combination이란, 순서를 가지지 않으면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 같고, 1,1은 허용되지 않음. 
# ex) combination([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,3), (2,4), (2,5), 
#         (3,4), (3,5), 
#         (4,5), ]
# --------------------------------------------

# write your code here 
def combination(lst, r):
    pass

# --------------------------------------------
# 6) combination_with_duplicate(lst, r)
#
# lst 안의 원소들 r개로 이루어진 중복을 허용하는 combination의 리스트를 반환. 
# ex) combination_with_duplicate([1,2,3,4,5], 2)
#     >> [(1,1), (1,2), (1,3), (1,4), (1,5), 
#         (2,2), (2,3), (2,4), (2,5), 
#         (3,3), (3,4), (3,5), 
#         (4,4), (4,5),
#         (5,5), ]
# --------------------------------------------

# write your code here 
def combination_with_duplicate(lst, r):
    pass

    


