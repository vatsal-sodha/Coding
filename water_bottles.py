def numWaterBottles(numBottles, numExchange):
        output = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            q = emptyBottles // numExchange
            r = emptyBottles % numExchange
            output += q
            # print(output)
            emptyBottles = q + r
        return output

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            q = emptyBottles // numExchange
            r = emptyBottles % numExchange
            
            emptyBottles = q + r
        return output

# print(numWaterBottles(9,3))
print(Solution.numWaterBottles(9,3))