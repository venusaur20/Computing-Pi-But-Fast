import math

def fast_pie(accuracy):
    
    positive = sum([
        4/((n-2)*(n-1)*(n))
        for n in range(4,accuracy,4)
    ])
    negative = sum([
        -4/((n-2)*(n-1)*(n))
        for n in range(6,accuracy,4)
    ])

    pi = positive + negative + 3
    return pi

while True:
    accuracy = (int(input("Your preferred accuracy: "))**2)*2
    print(fast_pie(accuracy))