import torch 
import torch.nn.functional as F
import pickle


# 그냥 여기 평가하는 것만 넣어 
def model_evaluate(self, test_data, device, epoch, lr): 
    self.eval() 
    criterion = F.nll_loss 

    loss_list = []
    correct = 0 
    total = 0 
    save_loss = 1
    pickle_loss_and_model = {}

    with torch.no_grad(): 
        for x, y in test_data: 
            y_pred = self(x, device) # batch_size, 32 18
            loss = criterion(y_pred, y)
            loss_mean = torch.mean(loss).item()
            loss_list.append(loss_mean)

            if save_loss > loss_mean: 
                save_loss = loss_mean
                model_state = self.state_dict() # 현재 모델 상태 저장 
                pickle_loss_and_model[save_loss] = model_state
                

            correct += torch.sum(torch.argmax(y_pred, dim = 1) == y)
            total += y.size(0)

    pickle_loss_and_model[f"{save_loss}"] = 'model.pth'
    accuarcy = correct / total
    min_loss = sorted(loss_list)[0]

    with open('loss_history.pkl', 'wb') as file: 
        pickle.dump(pickle_loss_and_model, file)

    print("Accuarcy :", accuarcy.item())
    print("Min_loss :", min_loss)        
    return accuarcy, min_loss
            




    
