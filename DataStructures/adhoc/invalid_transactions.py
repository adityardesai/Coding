# https://leetcode.com/problems/invalid-transactions/
# TC: O(N^2)
# SC: O(N)
class Solution:
    def brute_force_helper(self, transactions):
        result = set()
        for i in range(len(transactions)):
            name1, time1, amount1, city1 = transactions[i].split(',')
            if int(amount1) > 1000:
                result.add(transactions[i])

            for j in range(i + 1, len(transactions)):
                name2, time2, amount2, city2 = transactions[j].split(',')
                if city1 != city2 and abs(int(time1) -
                                          int(time2)) <= 60 and name1 == name2:
                    result.add(transactions[i])
                    result.add(transactions[j])
        return result

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions or len(transactions) == 0:
            return None
        return self.brute_force_helper(transactions)
