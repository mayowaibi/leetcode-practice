class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        text_s = ""
        text_t = ""
        for letter in s:
            if letter != "#":
                text_s += letter
            else:
                text_s = text_s[:-1]
        for letter in t:
            if letter != "#":
                text_t += letter
            else:
                text_t = text_t[:-1]
        return text_s == text_t