class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        coordinates=[[pos,sp] for pos,sp in zip(position,speed)]
        stack=[]
        for pos, sp in sorted(coordinates)[::-1]:
           stack.append((target-pos)/sp)
           if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
        return len(stack)    
        