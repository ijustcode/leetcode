from collections import deque
from typing import List

def deque_play(q: deque) -> deque:
    print(q)
    print(type(q))
    q.append(3)
    q.append(5)
    q.append(-1)
    print(q)
    q.appendleft(11)
    print(q)
    li = list(q)
    print(type(li))
    print(li)
    print(li[2])    

deque_play(deque([25,33]))
    
