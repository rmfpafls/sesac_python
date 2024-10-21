plot_x = []
plot_y = []
for loss_histrory in train_loss_history: 
    plot_x = []
    plot_y = []
    for key, value in loss_histrory.items():
            plot_x.append(key[0])
            plot_y.append(value)
            plot_learning_rate = key[1]
            print(key, value)
    plt.plot(plot_x, plot_y, label = f'{plot_learning_rate}_valid_loss')


for loss_histrory in vaild_loss_history: 
    plot_x = []
    plot_y = []
    for key, value in loss_histrory.items():
            plot_x.append(key[0])
            plot_y.append(value)
            plot_learning_rate = key[1]
            print(key, value)
    plt.plot(plot_x, plot_y, label = f'{plot_learning_rate}_valid_loss')

plt.legend()
plt.show()