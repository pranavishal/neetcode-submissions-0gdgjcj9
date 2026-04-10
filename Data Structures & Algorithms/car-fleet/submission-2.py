class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carsWithPosAndIndex = []

        for i in range(len(position)):
            carsWithPosAndIndex.append((position[i], i))
        
        descendingPos = sorted(carsWithPosAndIndex, key=lambda x: x[0], reverse=True)

        print(descendingPos)

        uniqueFleets = 1
        currentTime = (target - descendingPos[0][0]) / speed[descendingPos[0][1]]

        for i in range(1, len(descendingPos)):
            timeToReach = (target - descendingPos[i][0]) / speed[descendingPos[i][1]]
            if timeToReach > currentTime:
                uniqueFleets += 1
                currentTime = timeToReach

        return uniqueFleets