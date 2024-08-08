class Game:
    def __init__(self, players):
        self.players = players 

    def play_match(self, player1, player2):
        # player1, player2의 win_lose_history를 update하고 
        # elo rating 알고리즘에 따라 각자의 current_rating을 update할 것 
        # https://namu.wiki/w/Elo%20%EB%A0%88%EC%9D%B4%ED%8C%85 참고 
        


    def match_players(self):
        # player들을 current_rating을 기반으로 
        
    def simulate(self):
        pass 

class Player:
    def __init__(self, player_id, initial_rating = 1000, actual_rating = 1000):
        self.win_lose_history = []
        self.current_rating = initial_rating
        self.actual_rating = actual_rating

    def __str__(self):
        return str(self.player_id)

    
# initial_rating : 계정을 처음 만든 플레이어에게 주어지는 레이팅 값
# actual_rating : 실제 레이팅 값 : 이기면 오르고 지면 내려가고 
# match_player는 현재 레이팅 값을 기반으로 잡아줌. 현재 레이팅 차이 값x기다린 시간으로 높은 티어랑 잡아줄 수도 있고
# 어떤식으로든 상관x 오픈된 문제임


# 단, 시뮬레이션을 돌렸을 때, 결과값이 self.current_rating = initial_rating에 반영되는게 보이기만 하면 됨!!!
