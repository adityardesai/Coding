"""
"""

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def get_factors(num):
            factors = []
            for i in range(2, num):
                if num % i == 0:
                    factors.append(i)
            return factors

        def get_combinations(factors, comb, product, target, start):
            if product > target:
                return
            
            if product == target:
                combinations.append(list(comb))
                return
            
            for i in range(start, len(factors)):
                comb.append(factors[i])
                get_combinations(factors, comb, product * factors[i], target, i)
                comb.pop()
            
        
        if n == 1:
            return []
        
        factors = get_factors(n)
        factors.sort()
        print(factors)
        combinations = []
        get_combinations(factors, [], 1, n, 0)
        return combinations
