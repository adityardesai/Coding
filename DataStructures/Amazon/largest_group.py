"""

https://leetcode.com/playground/TVDGmmuR

https://leetcode.com/discuss/interview-question/782606/
"""

from collections import defaultdict
from collections import deque

def largest_group(item_association):
    
    item_map = defaultdict(set)
    
    for items in item_association:
        if len(items) == 1: 
            item_map[items[0]] = []
        else:
            item_map[items[0]].add(items[1])
            item_map[items[1]].add(items[0])
        
    large_group=[]
    visited=set()
    
    for k,v in item_map.items():
        if k not in visited:
            group=list()
            q=deque()
            q.append(k)
            
            while q:
                node=q.popleft()
                visited.add(node)
                group.append(node)
                
                for neigh in item_map[node]:
                    if neigh not in visited:
                        q.append(neigh)
                    
                group.sort()
                if len(group)>=len(large_group):
                    large_group=list(group)
                elif len(group)==len(large_group):
                    large_group=min(large_group, group)
    
    res=sorted(large_group)
    return res


print(largest_group([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
print(largest_group([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))

print(largest_group([['A', 'B'], ['D', 'E'], ['C', 'D']]))
print(largest_group([['A', 'B'], ['C', 'D'], ['F', 'E']]))
print(largest_group([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]))
print(largest_group([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]))
print(largest_group([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'], 
            ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
            ['A', 'C'],]))
print(largest_group([['i1', 'i2'], ['i2', 'i5'], ['i3']]))
print(largest_group([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]))

print(largest_group([["item1","item2"], ["item1","item3"], ["item2","item7"], ["item3","item7"], ["item5","item6"], ["item3","item7"]]))
