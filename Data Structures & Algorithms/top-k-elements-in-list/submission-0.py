class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        for x in nums:
            _count = 0
            if str(x) not in nums_count:
                for y in nums:
                    if x == y:
                        _count += 1
                nums_count[str(x)] = _count
            # only count if it haven't been counted before 

        result = []

        for i in range(k):
            highest = {
                'key':'key',
                'val':0
                }

            for key in nums_count:
                if nums_count[key] > highest['val']:
                    highest['key'] = key
                    highest['val'] = nums_count[key]
            result.append(int(highest['key']))
            nums_count.pop(highest['key'])
        return result
            

            
                    