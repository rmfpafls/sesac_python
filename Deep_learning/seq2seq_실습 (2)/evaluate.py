import torch 
import torch.nn.functional as F
import math

from bleu import bleu

def vetor2word(x, y, y_pred, eng_idx2word, fra_idx2word): 
    eng_dict = dict(eng_idx2word)
    fra_dict = dict(fra_idx2word) 

    x.tolist()
    y.tolist() 

    x = [[e.item() for e in tensor if e.item() != 0] for tensor in x]
    y = [[e.item() for e in tensor if e.item() != 0] for tensor in y]
    y_pred = torch.argmax(y_pred, dim = -1)
    y_pred = [[fra_dict.get(idx.item(), "[OOV]") for idx in tensor if idx.item() in fra_dict] for tensor in y_pred]

    x = [[eng_dict[lst_lst] for lst_lst in lst ] for lst in x]
    y = [[fra_dict[lst_lst] for lst_lst in lst ] for lst in y]

    for i in range(len(y)): 
        print(f"y[{i}] : " , y[i], '\n\n')
        print(f"y_pred[{i}]", y_pred[i], '\n\n')
        print("DONE\n\n")

        bleu = bleu(y[i], y_pred[i])
        print(f"BLEU score: {bleu:.4f}")

    # print(f"{x[0]}\n\n{y[0]}\n\n{y_pred[0]}\n\n")




def model_evaluate(self, eng_voca, fra_voca, test_data, lr): 
    self.eval() 
    criterion = F.nll_loss 

    loss_list = []
    correct = 0 
    total = 0 
    save_loss = math.inf
    pickle_loss_and_model = {}


    with torch.no_grad(): 
        for x, y in test_data: 
            y_pred = self(x, y) # batch_size, 32 18
            # print("y_pred : ", y_pred.size()) # torch.Size([32, 51, 2380])
            # print(y_pred.shape)
            # print(y.shape)
            # y_pred = torch.argmax(y_pred, dim = -1)
            vetor2word(x, y, y_pred, eng_voca, fra_voca)

            y_pred = y_pred.view(y_pred.size(0) * y_pred.size(1), -1)  #torch.Size([32, 51])
            y = y.view(-1)

            loss = criterion(y_pred, y)
            loss_mean = torch.mean(loss).item()
            
            if save_loss > loss_mean: 
                save_loss = loss_mean
                # model_state_path = f'{save_loss}_model.ckpts'
                state_dict = self.state_dict()  # 현재 모델 상태 저장
                loss_list.append(loss_mean)
            
            correct += torch.sum(torch.argmax(y_pred, dim = 1) == y)
            total += y.size(0)

    accuarcy = (correct / total).item()
    min_loss = sorted(loss_list)[0]
    pickle_loss_and_model[(lr, save_loss, accuarcy)] = state_dict

    return accuarcy, min_loss, pickle_loss_and_model, loss_list

