class Solution:
    # Sorting Solution - TC: O(plogp+tlogt), SC: O(1)
    # where p = len(players), t = len(trainers)
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = 0
        res = 0

        while i < len(players) and j < len(trainers):
            # inc i only if a match is found
            if players[i] <= trainers[j]:
                i += 1
                res += 1
            # always inc j
            j += 1
    
        return res

    # Brute Force Solution - TC: O(p*t), SC: O(1)
    # where p = len(players), t = len(trainers)
    def matchPlayersAndTrainers2(self, players: List[int], trainers: List[int]) -> int:
        res = 0
    
        for i in range(len(players)):
            for j in range(len(trainers)):
                if players[i] <= trainers[j]:
                    res += 1
                    trainers[j] = 0
                    break
        
        return res