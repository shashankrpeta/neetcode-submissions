from typing import List

def read_integers() -> List[int]:
    list=input().split(",")
    for i in range(len(list)):
        list[i]=int(list[i])
    return list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
