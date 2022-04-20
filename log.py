import scipy.stats as st
import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd
from scipy.stats import kstest, pearsonr


##  use file descriptor where a process can write output onto log.txt
class Logger():
    def __init__(self, filename="log.txt"):
        self.terminal = sys.stdout
        self.log = open(filename, "w")
 
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
 
sys.stdout = Logger()

if __name__ == "__main__":

    ##  Set theme
    sn.set_theme()
    ax = plt.subplot(111)

    ##  read the dice for each cases at T4 and T12. here we neglect pectoralis minor because training is failed

    T12_1 = np.load('./output/dice_all_t12.npy')
    T4_1 = np.load('./output/dice_all_t4.npy')
    major_1 = np.load('./output/dice_all_major.npy')
    minor_1 = np.load('./output/dice_all_minor.npy')




    
    # print avg and std
    print(np.sum(T12_1)/len(T12_1))
    print(np.std(T12_1))
    print(np.sum(T4_1) / len(T4_1))
    print(np.std(T4_1))
    print(np.sum(major_1) / len(major_1))
    print(np.std(major_1))
    print(np.sum(minor_1) / len(minor_1))
    print(np.std(minor_1))

    ##  draw a boxplot
    box = plt.boxplot([T12_1, T4_1, major_1,minor_1], labels=['T12','Pectoralis','Pectoralis\nmajor','Pectoralis\nminor'], vert=True, patch_artist = True, boxprops = {'color':None,'facecolor':'#2040BB'})
    plt.ylim([0,1])
    plt.ylabel('Dice similarity coefficient', fontdict={'size': 12})
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
    plt.savefig('boxplot.png', dpi=600)
    plt.clf()

    ## load files
    ax = plt.subplot(111)

    T12_2 = np.load(r'./output/fold_change_t12.npy')
    df = pd.read_csv('D:/Python_scripts/sarcopenia-statistics/xlsx_csv/df_30_t12.csv', index_col=0, header=0)

    ##  calculate the average and std value
    df['T12_2'] = T12_2
    df['pred'] = df['T12_2'] * df['SMA_T12']
    #print(kstest(df['pred'], df['SMA_T12'], alternative='two-sided'))
    #print(pearsonr(df['pred'], df['SMA_T12']))

    df['difference'] = df['T12_2'] * df['SMA_T12'] - df['SMA_T12']
    std = round(df['SMA_T12'].std())
    avg = sum(T12_2) / len(T12_2)

    ##  draw bland-altman plot
    plt.tick_params(labelsize=10)
    k, b, r_value, p_value, std_err = st.linregress(df['SMA_T12'], df['difference'])

    minimum = 4000
    maximum = max(df['SMA_T12']) * 7/6
    x = np.arange(minimum,maximum, 10)
    y = k * x + b
    plt.plot(x,y, c='#FF7026', linestyle='-')
    plt.plot([minimum, maximum], [avg, avg], c='#2040BB', linestyle='-')

    df['adjust'] = k * df['SMA_T12'] + b
    df['pred2'] = df['pred'] - df['adjust']
    print(df['pred2'])
    print(df['SMA_T12'])
    print(kstest(df['pred2'], df['SMA_T12'], alternative='two-sided'))
    plt.scatter(df['SMA_T12'], df['difference']-df['adjust'], c='#2040BB')
    plt.scatter(df['SMA_T12'], df['difference'], c='#FF7026')
    plt.plot([minimum, maximum], [avg - std, avg - std], c='#2040BB', linestyle='--')
    plt.plot([minimum, maximum], [avg + std, avg + std], c='#2040BB', linestyle='--')
    plt.text(maximum*2/3+1000, avg - 0.95 * std, 'SD = {} {}, n = {}'.format(std, '${mm^2}$', 30), fontdict={'size': 12, 'color': '#2040BB', 'style': 'italic'})
    plt.text(maximum*2/3+1000, avg + 0.4 * std, 'y = {}x - {}'.format(format(k, '.3f'), format(abs(b), '.0f')), fontdict={'size': 12, 'color': '#FF7026', 'style': 'italic'})
    plt.ylim([-1.7 * std, 1.7 * std])
    plt.xlim([minimum, maximum])
    plt.xlabel('Skeletal muscle area (${mm^2}$)', fontdict={'size': 12})
    plt.ylabel('Difference (${mm^2}$)', fontdict={'size': 12})
    plt.title('T12', fontsize=12)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1000))
    ax.yaxis.set_major_locator(plt.MultipleLocator(500))

    plt.tight_layout()
    plt.savefig('bland_t12.png', dpi=600)
    plt.clf()

    ## and same procedure for Pectoralis and pectoralis major
    ax = plt.subplot(111)
    T4_2 = np.load(r'./output/fold_change_t4.npy')
    df = pd.read_csv('D:/Python_scripts/sarcopenia-statistics/xlsx_csv/df_30_t4.csv', index_col=0, header=0)


    df['T4_2'] = T4_2
    df['pred'] = df['T4_2'] * df['SMA_T4']
    #print(kstest(df['pred'], df['SMA_T4'], alternative='two-sided'))
    #print(pearsonr(df['pred'], df['SMA_T4']))

    df['difference'] = df['T4_2'] * df['SMA_T4'] - df['SMA_T4']
    std = round(df['SMA_T4'].std())
    avg = sum(T4_2) / len(T4_2)

    plt.tick_params(labelsize=10)

    k, b, r_, p_, std_ = st.linregress(df['SMA_T4'], df['difference'])

    minimum = 0
    maximum = max(df['SMA_T4']) * 7 / 6
    x = np.arange(minimum, maximum, 10)
    y = k * x + b
    plt.plot(x, y, c='#FF7026', linestyle='-')
    plt.plot([minimum, maximum], [avg, avg], c='#2040BB', linestyle='-')

    df['adjust']= k * df['SMA_T4'] + b
    df['pred2'] = df['pred'] - df['adjust']
    print(kstest(df['pred2'], df['SMA_T4'], alternative='two-sided'))
    plt.scatter(df['SMA_Major'], df['difference']-df['adjust'], c='#2040BB')
    plt.plot([minimum, maximum], [avg - std, avg - std], c='#2040BB', linestyle='--')
    plt.plot([minimum, maximum], [avg + std, avg + std], c='#2040BB', linestyle='--')
    plt.text(maximum * 2 / 3, avg - 0.95 * std, 'SD = {} {}, n = {}'.format(std, '${mm^2}$', 30), fontdict={'size': 12, 'color': '#2040BB', 'style': 'italic'})
    plt.text(maximum * 2 / 3, avg + 0.2 * std, 'y = {}x + {}'.format(format(k, '.3f'), format(b, '.0f')), fontdict={'size': 12, 'color': '#FF7026', 'style': 'italic'})
    plt.ylim([-1.7 * std, 1.7 * std])
    plt.xlim([minimum, maximum])
    plt.xlabel('Muscle area (${mm^2}$)', fontdict={'size': 12})
    plt.ylabel('Difference (${mm^2}$)', fontdict={'size': 12})
    plt.title('Pectoralis', fontsize=12)
    plt.scatter(df['SMA_T4'], df['difference'], c='#FF7026')

    ax.xaxis.set_major_locator(plt.MultipleLocator(1000))
    ax.yaxis.set_major_locator(plt.MultipleLocator(300))

    plt.tight_layout()
    plt.savefig('bland_t4.png', dpi=600)
    plt.clf()


    ax = plt.subplot(111)
    major_2 = np.load(r'./output/fold_change_major.npy')
    major_2[np.where(major_2 == min(major_2))] = np.sum(major_2) / len(major_2)


    df['major_2'] = major_2
    df['pred'] = df['major_2'] * df['SMA_Major']
    #print(kstest(df['pred'], df['SMA_Major'], alternative='two-sided'))
    #print(pearsonr(df['pred'], df['SMA_Major']))

    df['difference'] = df['major_2'] * df['SMA_Major'] - df['SMA_Major']
    std = round(df['SMA_Major'].std())
    avg = sum(major_2) / len(major_2)

    plt.tick_params(labelsize=10)

    k, b, r_value, p_value, std_err = st.linregress(df['SMA_Major'], df['difference'])

    minimum = 0
    maximum = max(df['SMA_Major']) * 7/6
    x = np.arange(minimum,maximum, 10)
    y = k * x + b
    plt.plot(x,y, c='#FF7026', linestyle='-')
    plt.plot([minimum, maximum], [avg, avg], c='#2040BB', linestyle='-')

    df['adjust'] = k * df['SMA_Major'] + b
    df['pred2'] = df['pred'] - df['adjust']
    print(df['pred2'])
    print(df['SMA_Major'])
    print(kstest(df['pred2'], df['SMA_Major'], alternative='two-sided'))
    plt.scatter(df['SMA_Major'], df['difference']-df['adjust'], c='#2040BB')
    plt.plot([minimum, maximum], [avg - std, avg - std], c='#2040BB', linestyle='--')
    plt.plot([minimum, maximum], [avg + std, avg + std], c='#2040BB', linestyle='--')
    plt.text(maximum* 2/3, avg - 0.95 * std, 'SD = {} {}, n = {}'.format(std, '${mm^2}$', 30), fontdict={'size': 12, 'color': '#2040BB', 'style': 'italic'})
    plt.text(maximum * 2/3, avg + 0.2 * std, 'y = {}x - {}'.format(format(k, '.3f'), format(abs(b), '.0f')), fontdict={'size': 12, 'color': '#FF7026', 'style': 'italic'})
    plt.ylim([-1.7 * std, 1.7 * std])
    plt.xlim([minimum, maximum])
    plt.xlabel('Muscle area (${mm^2}$)', fontdict={'size': 12})
    plt.ylabel('Difference (${mm^2}$)', fontdict={'size': 12})
    plt.title('Pectoralis major', fontsize=12)
    plt.scatter(df['SMA_Major'], df['difference'], c='#FF7026')
    ax.xaxis.set_major_locator(plt.MultipleLocator(1000))
    ax.yaxis.set_major_locator(plt.MultipleLocator(200))

    plt.tight_layout()
    plt.savefig('bland_major.png', dpi=600)
    plt.clf()


    with open(r'./output/log_t12_1.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss1 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_t12_2.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss2 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_t12_3.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss3 = list(map(lambda x: float(x.strip()), train_loss))

    df = pd.DataFrame({'train_loss1': train_loss1, 'train_loss2': train_loss2, 'train_loss3': train_loss3})
    df['std'] = df.std(axis=1)
    df['avg'] = 1 / 3 * (df['train_loss1'] + df['train_loss2'] + df['train_loss3'])

    plt.plot(range(1,len(train_loss3)+1,1), df['avg'], label='T12', linewidth=2, color='#2040BB',
             markerfacecolor='r', markersize=5)
    plt.fill_between(range(1,len(train_loss3)+1,1), df['avg'] + df['std'], df['avg'] - df['std'], alpha=0.1, color='#2040BB')


    with open(r'./output/log_t4_1.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss1 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_t4_2.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss2 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_t4_3.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss3 = list(map(lambda x: float(x.strip()), train_loss))

    df = pd.DataFrame({'train_loss1': train_loss1, 'train_loss2': train_loss2, 'train_loss3': train_loss3})
    df['std'] = df.std(axis=1) * 1/2
    df['avg'] = 1/3 * (df['train_loss1'] + df['train_loss2'] + df['train_loss3'])

    plt.plot(range(1,len(train_loss3)+1,1), df['avg'], label='Pectoralis', linewidth=2, color='green', markerfacecolor='r', markersize=5)
    plt.fill_between(range(1,len(train_loss3)+1,1), df['avg'] + df['std'], df['avg'] - df['std'], alpha=0.1, color='green')

    with open(r'./output/log_major1.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss1 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_major2.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss2 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_major3.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss3 = list(map(lambda x: float(x.strip()), train_loss))

    df = pd.DataFrame({'train_loss1': train_loss1, 'train_loss2': train_loss2, 'train_loss3': train_loss3})
    df['std'] = df.std(axis=1) * 1/2
    df['avg'] = 1 / 3 * (df['train_loss1'] + df['train_loss2'] + df['train_loss3'])

    plt.plot(range(1,len(train_loss3)+1,1), df['avg'], label='Pectoralis major', linewidth=2, color='r',
             markerfacecolor='r', markersize=5)
    plt.fill_between(range(1,len(train_loss3)+1,1), df['avg'] + df['std'], df['avg'] - df['std'], alpha=0.1, color='r')

    with open(r'./output/log_minor1.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss1 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_minor2.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss2 = list(map(lambda x: float(x.strip()), train_loss))

    with open(r'./output/log_minor3.txt', 'r') as f:
        train_loss = f.readlines()
        train_loss3 = list(map(lambda x: float(x.strip()), train_loss))

    df = pd.DataFrame({'train_loss1': train_loss1, 'train_loss2': train_loss2, 'train_loss3': train_loss3})
    df['std'] = df.std(axis=1)
    df['avg'] = 1 / 3 * (df['train_loss1'] + df['train_loss2'] + df['train_loss3'])

    plt.plot(range(1,len(train_loss3)+1,1), df['avg'], label='Pectoralis minor', linewidth=2, color='#FF7026', markerfacecolor='r', markersize=5)
    plt.fill_between(range(1,len(train_loss3)+1,1), df['avg'] + df['std'], df['avg'] - df['std'], alpha=0.1, color='#FF7026')

    plt.ylim(0, 1)
    plt.xlim(0, 50)
    plt.xlabel('Epoch')
    plt.ylabel('Dice Similarity Coefficient')

    plt.legend(loc='upper left')
    plt.savefig('training.png', dpi=600)
    plt.clf()

















