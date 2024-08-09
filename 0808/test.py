import random

def play_match(self, player1, player2): 
    # win_lose_history를 update
    # player1, player2의 win_lose_history를 update하고 
    # elo rating 알고리즘에 따라 각자의 current_rating을 update할 것 
    # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 참고
    
    pass

def match_players(self): # 7명 중에 2명을 골라줘 self = list 값이 들어옴 
#self = ['player_0', 'player_1', 'player_2', 'player_3', 'player_4', 'player_5', 'player_6']
    empty_room = []

    for i in range(len(self)):#플레이어 7명이 순서대로 게임을 실행하는 경우
        if not len(empty_room): # 빈방이면
            empty_room.append(self[i])
        else: # 방에 누군가 있을때
            for j in range(len(empty_room)):
                if empty_room[j].current_rating - self[i].current_rating < 100: # rating 차이가 110 이하이면 
                    player1 = empty_room.pop(j)
                    player2 = self[i]
                    simulate([player1,player2])
                    break # for 문 나가기 
                else: # rating 차이가 100 이상이면 
                    empty_room.append(self[i]) #빈 방에 가서 기다려라 
            
    while len(empty_room): 
        # 방에 한명이라도 남아있는 경우
        # 정렬을 해서 가장 rating 차이가 적은 애들끼리 붙여줘야지 뭐
        
        for i in range(len(empty_room)): # 레이팅 순으로 정렬 
            for j in range(i+1, len(empty_room)): 
                if empty_room[i].current_rating > empty_room[j].current_rating:
                    empty_room[i], empty_room[j] = empty_room[j], empty_room[i]

        while not len(empty_room) == 1: # 둘 둘 짝지어서 simulate()돌려
            for i in range(len(empty_room)%2):
                    player1 = empty_room.pop(i)
                    player2 = empty_room.pop(i+1)
        
        if len(empty_room) == 1: 
            waiting_raitng = empty_room[0].current_rating - 50
            # 가상의 인스턴스를 만들어서 계산하고 다시 넣어 
            waiting_actual_raiting = empty_room[0].actual_rating
            player_waiting = Player(player_id = 'waiting_player', actual_rating = waiting_actual_raiting)
            player_waiting.current_rating = waiting_raitng
            print("확인하려는     거 ", player_waiting.current_rating)

        print(empty_room)




def simulate(self): # 누가 이기나//어쨌든 플레이어2명이 self로 들어올거임
    # self = ['player_0', 'player_6'] 이런꼴
    # 비겼을 때 생각안할거임 히히 승부의 세계는 그런거임  
    sum_rating = self[0].actual_rating + self[1].actual_rating # 1000 1020 =  2020
    player_A_float = self[0].actual_rating / sum_rating # 0.5
    player_B_float = self[1].actual_rating  # 0.495
    random_winner = random.uniform(0,player_A_float+player_B_float) 

    def calculator(winner,loser):
        winner_winning_percentage = 1 / (10**((loser.current_rating - winner.current_rating) / 400) + 1)
        loser_winning_percentage= 1 / (10**((winner.current_rating - loser.current_rating)/400)+1)
        winner.current_rating = winner.current_rating + 20*(1-winner_winning_percentage)
        loser.current_rating = loser.current_rating + 20*(0-loser_winning_percentage) 

    if (random_winner - player_A_float) > (random_winner - player_B_float):
        print(f"{self[0].player_id} win")
        self[0].win_lose_history.append("win")
        self[1].win_lose_history.append("lose")
        calculator(self[0],self[1])

    else: 
        print(f"{self[1]} win")
        self[0].win_lose_history.append("lose")
        self[1].win_lose_history.append("win")
        calculator(self[1],self[0])
    
    print(self[0].player_id, ":  승리!" )
    print(self[0].player_id, "의 전적입니다.", self[0].win_lose_history)
    print(self[0].player_id, "의 current_rating입니다.", self[0].current_rating)
    print(self[1].player_id, ":  패배!" )
    print(self[1].player_id, "의 전적입니다.", self[1].win_lose_history)
    print(self[1].player_id, "의 current_rating입니다.", self[1].current_rating)   
    

class Player:
    def __init__(self, player_id, initial_rating = 1000, actual_rating = 1000):
        self.player_id = player_id
        self.win_lose_history = []
        self.current_rating = initial_rating
        self.actual_rating = actual_rating

    def __str__(self):# 객체 자체를 출력할 때 넘겨주는 형식을 지정해주는 메서드 
        return str(self.player_id)
    

player_list = [Player(player_id = f"player_id_{i}", actual_rating = 1000 + 50*random.randint(0,7)) for i in range(0,7)] # Player의 인스턴스 생성


for z in range(len(player_list)):# 플레이어들의 actual_rating 보여주기 
    print( player_list[z],"의 actual_rating : ", player_list[z].actual_rating)

# match_players(player_list)
# print("확인하려는거", player_list[0])

# simulate([player_list[0],player_list[1]])

match_players(player_list)
