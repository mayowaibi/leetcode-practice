class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Replace all symbols in the paragraph with spaces
        symbols = "!?',;."
        for c in symbols:
            paragraph = paragraph.replace(c, " ")
        # Convert paragraph to all lowercase
        paragraph = paragraph.lower()

        # Using the Counter method to create a hashmap that maps each word to its number of occurences
        hashmap = Counter(paragraph.split(" "))
        result, hashmap[result] = "", 0

        for word in hashmap:
            if word not in banned and hashmap[word] > hashmap[result]:
                result = word
                hashmap[result] = hashmap[word]
        
        return result