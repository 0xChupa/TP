import array
import random

arr=[[1,2,3],[4,5,6],[7,8,9]]

for _ in arr:
    for i in _:
        i = random.randint(1,90)
        print(i,end=" ")
    print()

while True:
    numberToFind = random.randint(1,90)

    for _ in arr:
        for i in _:
            if i == numberToFind:
                print("GOOD")
                break
            else:
                continue
        break
