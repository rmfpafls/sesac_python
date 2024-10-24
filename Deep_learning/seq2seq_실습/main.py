from preprocessing import generate_dataset
from modeling import RNNManual, RNNEncoder

if __name__ == "__main__":
    train_dataloader, valid_dataloader, test_dataloader, eng_max_length, fra_max_length, eng_word2idx, fra_word2idx, eng_idx2word, fra_idx2word, eng_idx_sentence, fra_idx_sentence = generate_dataset() 
    rnn_model = RNNEncoder(train_dataloader, hidden_dim = 32, embedding_dim = 30)



