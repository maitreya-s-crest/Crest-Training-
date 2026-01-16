from collections import Counter

def ordering(x):
    words = x.split()

    x_counter = Counter(words)
    
    sorted_sen = dict(sorted(x_counter.items() , key=lambda x1 : x1[1],reverse=True))
    print(sorted_sen)
    for i , j in sorted_sen.items():
        print(i , j)


sentence = "Red Green Black Black Red red Orange Pink Pink Red White."

ordering(sentence)