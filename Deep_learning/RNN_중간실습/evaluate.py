import torch 
import torch.nn.functional as F
import pickle
import os
import math


def model_evaluate(self, test_data, device, lr): 
    self.eval() 
    criterion = F.nll_loss 

    loss_list = []
    correct = 0 
    total = 0 
    save_loss = math.inf
    pickle_loss_and_model = {}
    file_path = 'loss_history.pkl'

    with torch.no_grad(): 
        for x, y in test_data: 
            y_pred = self(x, device) # batch_size, 32 18
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

    print("Accuarcy :", accuarcy)
    print("Min_loss :", min_loss)      

    return accuarcy, min_loss, file_path, pickle_loss_and_model, loss_list

def save_file(file_path, pickle_loss_and_model):
    if os.path.exists(file_path): # 파일이 있다면 
        with open('loss_history.pkl', 'rb') as file: 
            existing_data = pickle.load(file)
            existing_data.update(pickle_loss_and_model)

        with open(file_path, 'wb') as file: 
            pickle.dump(existing_data, file)
            print("파일 업데이트")
    else: # 파일이 없다면 
        with open('loss_history.pkl', 'wb') as file: 
            pickle.dump(pickle_loss_and_model, file)
            print("새 파일 생성")


