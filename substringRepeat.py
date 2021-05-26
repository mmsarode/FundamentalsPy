# Task: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    
    # approach: 
    # find longest ending at i
    # start from i to left

    n = len(s)
    maxLenSoFar = 0

    # O(n)
    unique_ch = set(s)
    m = len(unique_ch)

    # (n*m) ~ n
    for i in range(n-1, -1, -1):
        lenAtCurrIdx = 0
        curr_set = set()
        
        for j in range(i, max(i - m, -1), -1):
            if s[j] in curr_set:
                break
            else:
                lenAtCurrIdx += 1
                curr_set.add(s[j])
        maxLenSoFar = max(maxLenSoFar, lenAtCurrIdx)
        print(maxLenSoFar, i)

    return maxLenSoFar

def lengthOfLongestSubstring02(s: str) -> int:
    
    # approach: 
    # find longest ending at i
    # start from i to left

    n = len(s)
    maxLenSoFar = 0

    # O(n)
    unique_ch = set(s)
    m = len(unique_ch)

  

    curr_set = set()
    

    for i in range(n-1, -1, -1):
        
        curr_set_size = len(curr_set)
        lenAtCurrIdx = curr_set_size
        
        for j in range(i - curr_set_size, max(i - curr_set_size - m, -1), -1):
            if s[j] in curr_set:
                break
            else:
                lenAtCurrIdx += 1
                curr_set.add(s[j])
        maxLenSoFar = max(maxLenSoFar, lenAtCurrIdx)

        curr_set.remove(s[i])
        
        print(maxLenSoFar, i)

    return maxLenSoFar

def lengthOfLongestSubstring03(s: str) -> int:
    
          


if __name__ == "__main__":

    input_00 = "abcabcbb"
    input_01 = "abcadcbb"
    input_02 = "pwwkew"
    input_03 = "abcb"

    # print(lengthOfLongestSubstring(input_00))
    # print(lengthOfLongestSubstring(input_01))
    print(lengthOfLongestSubstring02(input_03))

