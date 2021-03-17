import random as rd


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


