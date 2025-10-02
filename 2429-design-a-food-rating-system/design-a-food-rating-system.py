from sortedcontainers import SortedSet

# Sorted Set Solution
class FoodRatings:
    # TC: O(n log n), SC: O(n)
    # n == len(foods) == len(cuisines) == len(ratings)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map cuisine -> SortedSet of (-rating, food) for descending sort by rating, then asc/lex food
        self.cuisine_to_food = defaultdict(SortedSet)
        
        # Map food -> cuisine
        self.food_to_cuisine = {}
        
        # Map food -> current rating
        self.food_to_rating = {}

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.cuisine_to_food[cuisine].add((-rating, food))
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating

    # TC: O(log n), SC: O(1)
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        oldRating = self.food_to_rating[food]

        # Remove old rating and insert new rating
        self.cuisine_to_food[cuisine].remove((-oldRating, food))
        self.cuisine_to_food[cuisine].add((-newRating, food))

        # Update rating map
        self.food_to_rating[food] = newRating

    # TC: O(1), SC: O(1)
    def highestRated(self, cuisine: str) -> str:
        # Return food name with highest rating (lowest -rating)
        return self.cuisine_to_food[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)