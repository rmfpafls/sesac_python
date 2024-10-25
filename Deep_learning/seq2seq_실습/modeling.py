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
    
    def init_hidden(self):
        return torch.zeros(self.hidden_dim)    
    
class RNNEncoder(nn.Module): 
    def __init__(self, voca, max_length, hidden_dim = 32, embedding_dim = 200):
        super(RNNEncoder, self).__init__()
        self.cell = RNNManual(embedding_dim, hidden_dim)
        self.embedding = nn.Embedding(len(voca), embedding_dim)

    def forward(self, x): 
        batch_size, x_max_length = x.size() 
        # print("x.size() : " , x.size()) [32, 15]
        hidden = self.cell.init_hidden()

        for i in range(x_max_length): 
            char = x[:, i] # 각 시퀀스의 i번째 단어

            embedded = self.embedding(char).unsqueeze(1)
            # 지금 [batch_size, x_max_legnth]라서 계산하려면 [,,]로 바꿔줘야되므로
            hidden = self.cell(embedded, hidden)
        return hidden

class RNNDecoder(nn.Module): 
    def __init__(self, voca, max_length, hidden_dim = 32, embedding_dim = 200): 
        super(RNNDecoder, self).__init__()
        voca_size = len(voca)
        self.cell = RNNManual(embedding_dim, hidden_dim)
        self.embedding = nn.Embedding(voca_size, embedding_dim)
        self.h2o = nn.Linear(hidden_dim, voca_size)
        self.softmax = nn.LogSoftmax(dim = -1)
        self.hidden_dim = hidden_dim
        

    def forward(self, y, encoder_last_hidden, teacher_forcing_ratio = 0.5): 
        # print(encoder_last_hidden.size()) # 32 19 
        batch_size = encoder_last_hidden.size(0) # 32 19
        fra_max_length = encoder_last_hidden.size(1)
        hidden_dim = self.hidden_dim 
        outputs = []
        hidden = encoder_last_hidden

        decoder_input = y[:, 0] if y is not None else torch.tensor(1*batch_size)
        # 1은 SOS index 
        # target이 주어진 경우 : 정답 문장의 첫번째 단어를 사용해 시작할 수 있다. target이 주어진 것을 알 수 있다. 
        # target이 주어지지 않은 경우 : 정답 문장이 없어서 디코더가 예측한 단어들만을 보고 번역해야한다. [SOS] 토큰으로 시작하게 설정해 디코더가 첫 단어를 예측할 수 있게 해준다. 
        # 1*batch_size인 이유 : [SOS] 토큰을 batch_size만큼 만들어서 각 문장에 대해 디코더가 시작될 수 있도록 설정한다. 
        
        for i in range(fra_max_length): 
            embedded = self.embedding(y)
            hidden = self.cell(embedded, hidden_dim)
            output = self.h2o(hidden)
            output = self.softmax(output)
            outputs.append(output)

            pred = torch.argmax(self.softmax(y), dim = 1)

            # teacher forcing 적용 여부 
            if y is not None and random() < teacher_forcing_ratio: 
                decoder_input = y[:, i] # 실제 정답을 다음 입력으로 사용
            else: 
                decoder_input = pred # 예측한 단어를 다음 입력으로 사용 

            outputs = torch.cat(outputs, dim = 1)
            return outputs
            
    
class Seq2seq(nn.Module): 
    def __init__(self, encoder, decoder): 
        super(Seq2seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x): 
        encoder_last_hidden = self.encoder(x)
        output = self.decoder(encoder_last_hidden)
        return output

     







        