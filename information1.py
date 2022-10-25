import math
import numpy as np
a_num = [0 for i in range(26)]
p = [0 for i in range(26)]
infor = [0 for i in range(26)]
def each_infor(P):#平均互信息
    each = 0
    p_y = np.zeros((26))
    px_y = np.zeros((26,26))
    for i in range(26):
        for j in range(26):
            if i==j:
                px_y[i][j] = 1/2
                px_y[i][(j+1)%26] = 1/2
    for i in range(26):
        for j in range(26):
            p_y[i] += px_y[i][j]*P[j]
    for i in range(26):
        for j in range(26):
            if px_y[i][j]==0:
                continue
            each += P[i]*px_y[i][j]*(math.log((px_y[i][j]/p_y[j]),2))
    print(each)
def poo(x):#统计26个小写字母发生概率
    for i in range(len(x[0])):
        a_num[ord(x[0][i])%97] += 1
    for j in range(len(a_num)):
        p[j] = a_num[j] / len(x[0])
    print(p)

def coi(p):#统计26个小写字母的自信息量和信源熵
    sum=0
    for j in range(26):
        infor[j] = -(math.log(p[j], 2))
        sum += -(p[j] * (math.log(p[j], 2)))
    print(infor)
    print(sum)



if __name__ == '__main__':
    with open('./1.txt', encoding='utf-8') as f:
        x = list(f)
    poo(x)
    coi(p)
    each_infor(p)
