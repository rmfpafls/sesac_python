
# -------------------------------------------------
# initial_rating : 계정을 처음 만든 플레이어에게 주어지는 레이팅 값
# actual_rating : 실제 레이팅 값 : 이기면 오르고 지면 내려가고 
# match_player는 현재 레이팅 값을 기반으로 잡아줌. 현재 레이팅 차이 값x기다린 시간으로 높은 티어랑 잡아줄 수도 있고
# 어떤식으로든 상관x 오픈된 문제임

# 단, 시뮬레이션을 돌렸을 때, 결과값이 self.current_rating = initial_rating에 반영되는게 보이기만 하면 됨!!!
# -------------------------------------------------

import random 

class Game:
    def __init__(self, players):
        self.players = players # 들어오는 값은 player_list
    

    def play_match(self, player1, player2): 
        # win_lose_history를 update
        # player1, player2의 win_lose_history를 update하고 
        # elo rating 알고리즘에 따라 각자의 current_rating을 update할 것 
        # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 참고


    def match_players(self): # 5명 중에 2명을 골라줘
        # match_player는 현재 레이팅 값을 기반으로 잡아줌. 현재 레이팅 차이 값x기다린 시간으로 높은 티어랑 잡아줄 수도 있고
        # player들을 current_rating을 기반으로 
        simulate([player1,player2])
        
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
    

player_list = [Player(player_id = f"player_id_{i}", actual_rating = 1000 + 50*random.randint(0,7)) for i in range(1,7)] # Player의 인스턴스 생성

print("dfdfdfd",player_list[0])


for z in range(len(player_list)):# 플레이어들의 actual_rating 보여주기 
    print( player_list[z],"의 actual_rating : ", player_list[z].actual_rating)

# match_players(player_list)
print("확인하려는거", player_list[0])
simulate([player_list[0],player_list[1]])
