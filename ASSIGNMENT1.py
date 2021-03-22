import random as rd
import matplotlib.pyplot as plt
import numpy as np

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
E = [2, 4, 6, 8, 10]
A = [4, 5, 6, 7, 8, 9, 10]
# "E" is set of even cards
# "A" is set of  cards numbered greater than 3
# "R" is the set of favourable outcomes that is (R=(E intersection A))
#Then P(E^A)=P(R)
R = [4, 6, 8, 10]


def card_pick(n_simulations1 = 1000000):
    count1 = 0
    i=0
    for i in range(n_simulations1):
        i = rd.randint(1,10)
        if i % 2 == 0 and i > 3:
            count1 += 1
    return count1/n_simulations1
print("The probabilty of picking a even numbered card greater than 3,P(R) is:",card_pick(n_simulations1=1000000))
def even_card_pick(n_simulations2 = 1000000):
    count2 = 0
    j=0
    for j in range(n_simulations2):
        j = rd.randint(1,10)
        if j > 3:
            count2 += 1
    return count2/n_simulations2
print("The probabilty of picking a card numbered greater than 3,P(E) is:",even_card_pick(n_simulations2 = 1000000))
print("The probability that the card is even, if it is known that the number on card is greater than 3 is:\n P(E/A)=P(E^A)/P(A)")
print("       =P(R)/P(A)\nTherefore,P(E/A) =",card_pick(n_simulations1=1000000)/even_card_pick(n_simulations2 = 1000000))
N_Sim = [10**3,10**4,10**5,10**6,10**7]
Prob = []
for n in N_Sim :
  Prob.append(card_pick(n)/even_card_pick(n))
fig, ax = plt.subplots()
index = np.arange(len(N_Sim))
bar_width = 0.4
x_ax = np.arange(len(N_Sim))
th_prob = [4/7]*len(N_Sim)
rects1 = plt.bar(x_ax,Prob,bar_width,label ='experimental')
rects2 = plt.bar(x_ax+bar_width,th_prob,bar_width,label ='theoritical')
plt.tight_layout()
plt.xticks(x_ax+bar_width,N_Sim)
plt.title("Graph plot of actual versus simulated probabilities")
plt.ylim(0,0.8)
plt.legend()
plt.show()