import torch
import torch.nn as nn 
import random 

class RNNManual(nn.Module):
    def __init__(self, input_dim, hidden_dim): 
        super(RNNManual, self).__init__()
        self.i2h = nn.Linear(input_dim, hidden_dim)
        self.h2h = nn.Linear(hidden_dim, hidden_dim)
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim

    def forward(self, x, hidden):
        return torch.tanh(self.i2h(x) + self.h2h(hidden))
    
    def init_hidden(self, batch_size):
        return torch.zeros(batch_size, self.hidden_dim)    
    
class RNNEncoder(nn.Module): 
    def __init__(self, voca, max_length, hidden_dim = 32, embedding_dim = 200):
        super(RNNEncoder, self).__init__()
        self.cell = RNNManual(embedding_dim, hidden_dim)
        self.embedding = nn.Embedding(len(voca), embedding_dim)
        self.hidden_dim = hidden_dim

    def forward(self, x): 
        batch_size, x_max_length = x.size() 
        # print("x.size() : " , x.size()) #[32, 37]
        hidden = self.cell.init_hidden(batch_size)

        for i in range(x_max_length): 
            char = x[:, i] # 각 시퀀스의 i번째 단어

            embedded = self.embedding(char)
            hidden = self.cell(embedded, hidden)
        return hidden

class RNNDecoder(nn.Module): # output = self.decoder(y, encoder_last_hidden)
    def __init__(self, voca, max_length, hidden_dim = 32, embedding_dim = 200): 
        super(RNNDecoder, self).__init__()
        voca_size = len(voca) # print(voca_size) #2380
        self.cell = RNNManual(embedding_dim, hidden_dim)
        self.embedding = nn.Embedding(voca_size, embedding_dim)
        self.h2o = nn.Linear(hidden_dim, voca_size)
        self.softmax = nn.LogSoftmax(dim = -1)
        self.hidden_dim = hidden_dim
        

    def forward(self, y, encoder_last_hidden, teacher_forcing_ratio = 0.8): 
        # print(y.size())   # torch.Size([32, 51])
        # y = torch.transpose(y, 1, 0) 
        # print(y.size())  # torch.Size([51, 32])
        batch_size = encoder_last_hidden.size(0) # [32, 1, 32]
        fra_max_length = y.size(1) 

        # print("hidden.size() : ", hidden.size()) #[32, 1, 32]
    
        decoder_input = y[:, 0] if y is not None else torch.full(batch_size, 1)
        # torch.full(batch, sos_idx) 로 두는게 좋은데 (나중에 볼 때 바로 알 수 있으니까!), 근데 내가 class로 안둬서
        # 내가 sos 인덱스를 1로 둬서 torch.ones로 해도 될 듯? 
        # print(decoder_input)
        # 1은 SOS index 
        # target이 주어진 경우 : 정답 문장의 첫번째 단어를 사용해 시작할 수 있다. target이 주어진 것을 알 수 있다. 
        # target이 주어지지 않은 경우 : 정답 문장이 없어서 디코더가 예측한 단어들만을 보고 번역해야한다. [SOS] 토큰으로 시작하게 설정해 디코더가 첫 단어를 예측할 수 있게 해준다. 
        # 1*batch_size인 이유 : [SOS] 토큰을 batch_size만큼 만들어서 각 문장에 대해 디코더가 시작될 수 있도록 설정한다. 
        
        outputs = torch.zeros(batch_size, fra_max_length, self.h2o.out_features, dtype=torch.float)
        embedded = self.embedding(decoder_input) # x의 형태: (batch_size, embedding_dim
        hidden = encoder_last_hidden
        result = []
        step = 0

        for _ in range(fra_max_length): # fra_max_length = 15
            hidden = self.cell(embedded, hidden) # 32, []
            # print("hidden.size() :", hidden.size()) # [32, 32, 32]
            output = self.h2o(hidden)
            output = output.float()

            pred = torch.argmax(self.softmax(output), dim=-1)  
            result.append(pred)

            # teacher forcing 적용 여부 
            if y is not None and random.random() < teacher_forcing_ratio: 
                if step + 1 < fra_max_length:
                    decoder_input = y[:, step+1] # 실제 정답을 다음 입력으로 사용
            else: 
                decoder_input = pred # 예측한 단어를 다음 입력으로 사용 
                # print('not teacher forcing: ', decoder_input.shape)

            embedded = self.embedding(decoder_input)
            step += 1 
        
        result = torch.stack(result, dim = 1)
        return result
            
    
class Seq2seq(nn.Module): 
    def __init__(self, encoder, decoder): 
        super(Seq2seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x, y): 
        encoder_last_hidden = self.encoder(x) # [32, 1, 32]
        output = self.decoder(y, encoder_last_hidden)
        return output
