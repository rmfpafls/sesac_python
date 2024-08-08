# 강사님 : 오늘은 "매직매소드" 예제입니다.
class MyDate:

    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, sec = 0):
    # d = Mtdate()는 My_date.__init__(...d..) 와 같은 것 
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec

        if self.month > 12 :
            raise ValueError("1월부터 12월까지 존재합니다.")
        elif self.year % 4 != 0 and self.month == 2 and self.day >= 29: 
            # 윤년이 아닌 2월에 day가 29일이 넘어가는 경우 
            raise ValueError("윤년에만 29일이 존재합니다.")
        elif self.year % 4 == 0 and self.month == 2 and self.day >= 30:
            #윤년이고 2월이면서 30일 이상인경우
            raise ValueError("윤년, 2월에는 29일까지 존재합니다.")
        elif self.month in [1,3,5,7,8,10,12] and self.day > 31: 
            raise ValueError(f"{self.month}월은 31일까지 존재합니다.")
        elif self.month not in [1,3,5,7,8,10,12] and self.day > 30:
            raise ValueError(f"{self.month}월은 30일까지 존재합니다.")
        elif self.hour > 24 or minute > 60 or sec > 60: 
            raise ValueError(f"하루는 24시간, 1시간은 60분, 1분은 60초입니다.")


    def __add__(self, other): #더할 때 쓰는 애 
        #그러면 이 other에 (2022,4,1,14,30)(2024, 2, 1)이런 식으로 들어올 거임
        # MyDate.__add__(MyDate(2022, 4, 1, 14, 30),  MyDate(2024, 2,1)) 꼴로 들어옴 
        
        #1) 월 더하기 (그럼 초부터 더해야겠네!)
        # 초
        # 60분이 넘으면 시간에 1을 더하고 0부터 다시시작
        # 24시간이 넘으면 day에 1을 더하고 0부터 다시시작
        # case 1) self.day + self.other를 했을 때 self의 달이 [1,3,5,7,8,10,12]였다면 day는 31일이 넘었을때 달에 1을 더하고 초기화
        # case 2) self.day + self.other를 했을 때 self의 달이 [1,3,5,7,8,10,12,2]가 아니고 day는 30일이 넘었을때 달에 1을 더하고 초기화
        # case 3) self.day + self.other를 했을 때 self의 달이 2였고 윤년인경우 day는 29일까지
        # case 4) self.day + self.other를 했을 때 self의 달이 2였고 윤년이 아닌경우 day는 28일까지
        # month가 12가 넘어가면 year에 1을 더하고 self.year + other.year
        
        ## 어떻게?? 빈 리스트를 만들어서 일단 더한다음에 정리 
        result_date = [self.year+other.year, self.month+other.month,self.day+other.day, self.hour+other.hour,self.minute+other.minute, self.sec+other.sec]
        
        if result_date[5] > 60: #60초가 넘어가면 
            result_date[4] += 1 # 1분을 올리고 
            result_date[5] -= 60 # 60초를 빼
        if result_date[4] > 60: #60분이 넘어가면
            result_date[3] += 1 # 1시간을 올리고
            result_date[4] -= 60 # 60분을 빼
        if result_date[3] > 24: #12시가 넘어가면
            result_date[2] += 1 #1일을 올리고 
            result_date[3] -= 24 # 12시간을 빼
        

        # 일계산
        if result_date[1] > 12: #일을 고려하지 않은 상태에서 self와 other의 월을 더한 값이 12가 넘는 경우
            result_date[1] -= 12 # 13월이면 12를 빼고
            result_date[0] += 1  # 년에 1을 더함
        
        while result_date[2] > 28:
            if result_date[1] in [1,3,5,7,8,10,12] and result_date[2] > 31: # 더한 달이 [1,3,5,7,8,10,12]이고 day가 31일이 넘어가는경우
                result_date[1] += 1
                result_date[2] -= 31
            elif result_date[1] not in [1,3,5,7,8,10,12] and result_date[2] > 30:
                result_date[1] += 1
                result_date[2] -= 30
            elif result_date[0] % 4 == 0 and result_date[1] == 2 and result_date[2] > 29: #윤년이고 계산한 달이 2월이고 합한 day가 29이 넘어가면 
                result_date[1] += 1
                result_date[2] -= 29
            elif result_date[0] %4 != 0 and result_date[1] == 2 and result_date[2] > 28: #윤년아니고 계산한 달이 2월이고 합한 day가 28이 넘어가면 
                result_date[1] += 1
                result_date[2] -= 28
            else: 
                break

        if result_date[1]  > 12: #월이 12월을 넘어가면
            result_date[0] += 1 #년에 1을더하고 
            result_date[1] -= 12 
            
        print(f"더한 값은 {result_date[0]}년 {result_date[1]}월 {result_date[2]}일 {result_date[3]}시 {result_date[4]}분 {result_date[5]}초 ")
        return MyDate(result_date[0],result_date[1],result_date[2],result_date[3],result_date[4],result_date[5])

        

    def __sub__(self, other):# 뺄 때 쓰는 애 
    # assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 
        result_date = [self.year-other.year, self.month-other.month,self.day-other.day, self.hour-other.hour,self.minute-other.minute, self.sec-other.sec]

        if result_date[5] < 0: # - 초가 되면
            result_date[4] -= 1 # 1분을 내리고
            result_date[5] = 60 + result_date[5] # 60초에서 빼
        elif result_date[4] < 0: # - 분이 되면 
            result_date[3] -= 1 # 1시간을 내리고
            result_date[4] = 60 + result_date[4] # 60분에서 빼
        elif result_date[3] < 0: # - 시가 되면 
            result_date[2] -= 1 #1일을 내리고
            result_date[3] = 24 + result_date[3] # 12시간을 빼
        
        # 일 계산
        if result_date[1] <= 0: #월의 뺀 값이 -값이면
            result_date[1] = 12 + result_date[1]  # 1년을 빌려와서 거기다가 -값 계산 ㄱㄱ 
            result_date[0] -= 1


        if (result_date[0] % 4 == 0) and result_date[1] == 3 and result_date[2] <= 0: # 윤년이고 2월이고 day가 마이너스이면 
            result_date[2] += 29
            result_date[1] -= 1      
        elif (result_date[0] % 4 != 0) and result_date[1] == 3 and result_date[2] <= 0: # 윤년아니고 2월이고 day가 마이너스이면 
            result_date[2] += 28
            result_date[1] -= 1      
        elif (result_date[1] not in [1,3,5,7,8,10,12] ) and result_date[1] != 3 and result_date[2] <= 0: # 윤년이 아니고 2월도 아니면서 day가 마이너스이면 
            result_date[2] += 31
            result_date[1] -= 1
        elif (result_date[1] in [1,3,5,7,8,10,12] ) and result_date[2] <= 0: 
            result_date[2] += 31
            result_date[1] -= 1

        # 월 계산
        if result_date[1] <= 0: # 계산한 월이 - 값이면
            result_date[0] -= 1  # 계산한 년도에 -값을 하고 
            result_date[1] = 12 + result_date[1] #12개월

        
        print(f"뺀 값은 {result_date[0]}년 {result_date[1]}월 {result_date[2]}일 {result_date[3]}시 {result_date[4]}분 {result_date[5]}초 ")
        return MyDate(result_date[0],result_date[1],result_date[2],result_date[3],result_date[4],result_date[5])

    def __eq__(self, other): # 같을 때
        self_date = [self.year, self.month,self.day, self.hour,self.minute, self.sec]
        other_date = [other.year, other.month,other.day, other.hour,other.minute, other.sec]
        
        if len(self_date) == len(other_date):
            for i in range(len(self_date)):
                if self_date[i] != other_date[i]:
                    return False
            return True
        else:
            return False

    def __lt__(self, other):# d1, d2가 주어졌을 때, d1이 d2보다 작을 때
        result_date = [self.year-other.year, self.month-other.month,self.day-other.day, self.hour-other.hour,self.minute-other.minute, self.sec-other.sec]

        for i in range(result_date):
            if i >= 0:
                return False
        return True

    def __le__(self, other):# d1이 d2보다 같거나 작을 때
        result_date = [self.year-other.year, self.month-other.month,self.day-other.day, self.hour-other.hour,self.minute-other.minute, self.sec-other.sec]

        for i in range(result_date):
            if i > 0:
                return False
        return True
        

    def __gt__(self, other):# d1이 d2보다 클때
        result_date = [self.year-other.year, self.month-other.month,self.day-other.day, self.hour-other.hour,self.minute-other.minute, self.sec-other.sec]

        for i in range(result_date):
            if i <= 0:
                return False
        return True
        

    def __ge__(self, other):# d1가 d2보다 같거나 클때
        result_date = [self.year-other.year, self.month-other.month,self.day-other.day, self.hour-other.hour,self.minute-other.minute, self.sec-other.sec]

        for i in range(result_date):
            if i < 0:
                return False
        return True
        

if __name__ == '__main__':
    d0 = MyDate()
    d1 = MyDate(2022, 1, 31, 14, 30)
    # d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    # 100일이라는게 말인 안되니까 error발생
    # 윤년이면 29일까지있죠 
    # 윤년이면 1년에 366일, 년이 4로 나누어 떨어지면 윤년임 
    # d3 = MyDate(2024, 2, 30)

    d3 = MyDate(day = 30) 
    # d3 = MyDate(2024,2,1)
    assert d1 + d3 == MyDate(2022, 3, 2, 14, 30)# 14시 30분 
    # MyDate.__eq__(MyDate.__add__(d1, d3), MyDate(2022, 4, 2, 14, 30))
    # assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 
    # assert d1 < d2 
    # assert d1 <= d2
    # assert d1 > d2
    # assert d1 >= d2 
    # assert d1 == d2


    
    
