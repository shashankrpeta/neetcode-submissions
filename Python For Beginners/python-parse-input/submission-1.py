from typing import List

def read_integers() -> List[int]:
    my_list=list(map(int,input().split(",")))
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
