import torch 
import torch.nn as nn 

class EncoderState:
    def __init__(self, **kargs):
        for k, v in kargs.items():
            exec(f'self.{k} = v')

    def initialize(self):
        assert 'model_type' in dir(self)
        return self.model_type.initialize()

class Encoder(nn.Module):
    def __init__(self, source_vocab, embedding_dim, hidden_dim, model_type, ):
        super(Encoder, self).__init__()
        self.source_vocab = source_vocab 
        self.embedding_dim = embedding_dim 
        self.hidden_dim = hidden_dim 

        self.embedding = nn.Embedding(source_vocab.vocab_size, embedding_dim)
        self.cell = model_type(embedding_dim, hidden_dim)

    def forward(self, source):
        # example = [ [1, 3, 2, 1, 1], 
        #             [2, 3, 1, 3, 1], ]
        # batch_size: 2 / seq_length: 5 / vocab_size: 3
        batch_size, seq_length = source.size()
        
        # embedded: batch_size, seq_length, embedding_dim 
        # e: nn.Embedding 
        # e(1) = [1.5, 1.2, 3.2], e(2) = [2.5, -0.7], e(3) = [-1.7, 0.2]
        # self.embedding(example): batch_size, seq_length, embedding_dim 
        # = [ [[1.5, 1.2], e(3), e(2), [1.5, 1.2], [1.5, 1.2]], 
        #     [e(2), e(3), [1.5, 1.2], e(3), [1.5, 1.2]], ]
        # = [ [[1.5, 1.2], e(3), e(2), [1.5, 1.2], [1.5, 1.2]], 
        #     [e(2), e(3), [1.5, 1.2], e(3), [1.5, 1.2]], ] 
        embedded = self.embedding(source)
        encoder_state = EncoderState(model_type = self.model_type).initialize()

        for t in range(seq_length):
            x_t = embedded[:, t, :]
            encoder_state = self.cell(x_t, *encoder_state)

        return encoder_state 

class Decoder(nn.Module):
    pass 

class Seq2Seq(nn.Module):
    def __init__(self, encoder, decoder):
        super(Seq2Seq, self).__init__() 
        self.encoder = encoder 
        self.decoder = decoder 

    def forward(self, source, target):
        encoder_hidden = self.encoder(source) 
        outputs = self.decoder(target, encoder_hidden)

        return outputs 

if __name__ == '__main__':
    encoder = Encoder(source_vocab, embedding_dim, hidden_dim, RNNCellManual)
    model = Seq2Seq(encoder = encoder, 
                    decoder = ...)
    train, valid, test = parse_file(...) 

    for source_batch, target_batch in train:
        model(source_batch)