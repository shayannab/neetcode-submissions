class Solution:

 def encode(self, strs: List[str]) -> str:
    final = ""
    for i in strs:
        final += str(len(i)) + "#" + i
    return final


 def decode(self, s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":  # find the #
            j += 1
        length = int(s[i:j])  # everything before # is the length
        result.append(s[j+1 : j+1+length])  # slice exactly length chars after #
        i = j + 1 + length  # move pointer to next encoded string
    return result

