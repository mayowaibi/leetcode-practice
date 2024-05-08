class Solution:
    # Sorting Solution - TC: O(nlogn), SC: O(n)
    def findRelativeRanks(self, score: List[int]) -> List[str]: 
        result = []
        # create a copy of score that is sorted, while leaving score in its original order
        sortedScore = score.copy()
        sortedScore.sort(reverse=True)

        for i in range(len(score)):
            if score[i] == sortedScore[0]:
                result.append("Gold Medal")
            elif score[i] == sortedScore[1]:
                result.append("Silver Medal")
            elif score[i] == sortedScore[2]:
                result.append("Bronze Medal")
            else:
                result.append(str((sortedScore.index(score[i])) + 1))

        return result

    # Heap Solution - TC: O(nlogn), SC: O(n)
