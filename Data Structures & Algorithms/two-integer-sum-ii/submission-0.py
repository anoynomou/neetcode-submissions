class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1,index2 = numbers[0] , numbers[1]

        for f in range(len(numbers)):
            index1 = numbers[f]
            for s in range(len(numbers)):
                index2 = numbers[s]
                if index1 + index2 == target :
                    return [f+1,s+1]
        return []
        