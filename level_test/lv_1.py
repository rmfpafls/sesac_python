all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letter ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

# write your code here 
a = (1,2,3)
b = list(all_smallcase_letters)
# print(b)

# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
# 2) lower_to_upper
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 
# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1
# 
# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
# --------------------------------------------

# write your code here 
# 1)
upper_to_lower = {}
all_large_letters = all_smallcase_letters.upper()

for i in range(len(all_large_letters)):
    upper_to_lower[all_large_letters[i]] = all_smallcase_letters[i]
# print(upper_to_lower)

# 2) 
lower_to_upper = {}
for i in range(len(all_large_letters)):
    lower_to_upper[all_smallcase_letters[i]] = all_large_letters[i]
# print(lower_to_upper)

# 3) 
alpha_to_number = {}

for i, letters in enumerate(all_smallcase_letters):
    alpha_to_number[all_smallcase_letters[i]] = i+1
# print(alpha_to_number)

# 4)  
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 

number_to_alphabet = []
number_to_alphabet_dict = {}
for i in range(0,26): 
    number_to_alphabet_dict[i] = (all_smallcase_letters[i], large_letter[i])
print(number_to_alphabet_dict)

# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
#  
# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요. 
# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요. 
# --------------------------------------------

a = 'absdf123SAFDSDF'

# upper_to_lower # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
# lower_to_upper # {'a' :'A' }

# 1) #upper을 쓰지말고??? 
a_list = []

for i in a: 
    if i in all_smallcase_letters:
        a_list.append(lower_to_upper[i])
    else: 
        a_list.append(i)
print(''.join(a_list))
    
# 2) 
b_list = []
for i in a: 
    if i in large_letter:
        b_list.append(upper_to_lower[i])
    else: 
        b_list.append(i)
print(''.join(b_list))

# 3) 
c_list =[]
for i in a: 
    if i in all_smallcase_letters:
        c_list.append(lower_to_upper[i])
    elif i in large_letter:
        c_list.append(upper_to_lower[i])
    else: 
        c_list.append(i)

print(''.join(c_list))

# 4) 
for i in a: 
    if i not in all_smallcase_letters or  i not in large_letter:
        print("False")
        break
    else: 
        print("True")
        pass


# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
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

for i in range(6): 
    print(blank*(6-i)+star*(2*i-1))


# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 
star_and_blank = star+blank

for i in range(6): 
    print(blank*(6-i)+star_and_blank*i)


# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 
alpha_list = ['A','B','C','D','E']

for i in range(6): 
    print(blank*(5-i), end ="")
    for j in range(i):
        print(alpha_list[j]+blank, end ="")
    print()



# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------
# 1 5 10 10 5 1 

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# 패턴은 알겠는데 어떻게 print()할지 모르겠음...히히...
# write your code here 
number_list = []
temp = []

for i in range(5): 
    number_list.append(1)
    temp.append(1)
    
    if i < 2:
        pass
    else: 
        for j in range(1,len(number_list)-1):
            temp[j] = number_list[j-1]+number_list[j]
    
    print(blank*(5+2-i), end="")

    for j in range(len(number_list)):
            number_list[j] = temp[j]
            print(str(number_list[j]), blank, end ="")
    print()

# solution
def pascal(n):
    def generate_next_line(last_line):
        n = len(last_line) + 1
        
        next_line = [last_line[0]]

        for i in range(n-2):
            next_line.append(last_line[i] + last_line[i+1])

        next_line.append(last_line[n-2])

        return next_line
    
    lines = [[1], [1,1]]
    
    while len(lines) != n:
        lines.append(generate_next_line(lines[-1]))

    space = ' '

    def fill(number, digits, fill_with = '0'):
        number_digit = get_digit(number)
        return (digits - number_digit) * fill_with + str(number)

    def get_digit(number):
        # int(log_10(n))
        # 123 
        digit = 1
        
        while True:
            if number < 10:
                break 
            else:
                digit += 1 
                number = number // 10 
        
        return digit 

    # print(fill(123, 4)) # 0123
    # print(fill(123, 5)) # 00123
    # print(fill(123, 4, '|')) # |123

    max_number = max(lines[-1])
    max_digit = get_digit(max_number)

    space = ' ' * max_digit

    for idx, line in enumerate(lines):
        print((n-1-idx)*space + space.join([\
            fill(e, max_digit, ' ') for e in line]))
    
    return lines 

for line in pascal(12):
    print(line)

# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         *  
#   *       *       *    
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------

# write your code here 

for i in range(0,5):
    print(blank*(2*i+1),star,blank*(9-2*i),star,blank*(9-2*i),star)

print(blank*13, star)

for i in range(0,5):
    print(blank*(9-2*i),star,blank*(2*i+1),star,blank*(2*i+1),star)