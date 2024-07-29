class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        decrease = 0
        increase = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                if not increase:
                    return False
                else:
                    decrease += 1
            elif arr[i] < arr[i+1]:
                if not decrease:
                    increase += 1
                else:
                    return False
        if not decrease:
            return False
        if not increase:
            return False
        return True