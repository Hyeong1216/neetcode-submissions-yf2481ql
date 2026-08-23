class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #hashmap -> put arr1 counted
        # iterate throug arr2, adding counted # of arr1

        hashMap = {}
        for i in range(len(arr1)):
            hashMap[arr1[i]] = hashMap.get(arr1[i], 0) + 1
        
        print(hashMap)
        res = []
        for i in range(len(arr2)):
            curr = arr2[i]
            for j in range(hashMap[curr]):
                res.append(curr)
            del hashMap[curr]
        # print(res)
        # print(hashMap)
        for k, v in sorted(hashMap.items()):
            for j in range(v):
                res.append(k)
        return res
        