from preprocessing import generate_dataset
from modeling import RNNManual, RNNEncoder, RNNDecoder, Seq2seq
from training import train_model

if __name__ == "__main__":
    train_dataloader, valid_dataloader, test_dataloader, eng_max_length, fra_max_length, eng_word2idx, fra_word2idx, eng_idx2word, fra_idx2word, eng_idx_sentence, fra_idx_sentence, eng_voca, fra_voca = generate_dataset() 
    # train_dataloader = [batch_size, 108673, 15]

    encoder = RNNEncoder(eng_voca, eng_max_length, hidden_dim = 32, embedding_dim = 30)
    decoder = RNNDecoder(fra_voca, fra_max_length, hidden_dim = 32, embedding_dim = 30) 
    model = Seq2seq(encoder, decoder)
    train_loss_history, vaild_loss_history = train_model(model, train_dataloader, valid_dataloader, eng_idx2word, fra_idx2word, epochs = 100, learning_rate = 0.001)
    
    # for x, y in train_dataloader:
    #     hidden = encoder(x) 
    #     # print("x.size() : ", x.size()) # torch.Size([32, 15])
    #     # print("encoder's ouput(hidden).size() :", hidden.size()) # torch.Size([32, 1, 32])
    #     # print("y.size():", y.size()) #  torch.Size([32, 19])
    #     output = decoder(y, hidden)
    #     print(output)
