leet 2707:  
```text
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
```

## devlog
```python
# Analysis
# dwm o diz x v v bosxxw
# ___ * *** _ * * ______
# output: 8, incorrect
# split at "o" so that i cannot split again at "wmo", and split at "wmo" is more optimized
# and notice, in this case i need to split "v" two times
# 
# d wmo diz x v v bosxxw
# _ *** *** _ * * ______  
# output: 7, correct

# imagine in "dictionary" you have "wmo" and "o"
# after splitting "wmo", you cannot split the "o" inside again

# maybe one word in "dictionary" has less length but more occurrence
# e.g. s="wawao" , word1="wa" and word2="wao". word1 is more optimal


# solution 3: sort dictionary by length of word
```

### bug 3: due to replace by ""
code with pb:  
```python
    s = s.replace(word, "")
```
```shell
na
______hlwx_____iji___eas____tjqwk_______o_____f
i
______hlwx______j____eas____tjqwk_______o_____f
```
In "dicitonary", there was "xi" between "na" and "i".  
If i replace by "", "xi" will be found and deleted

Solution:  
```python
    s = s.replace(word, "_"*len(word))
    # ... truncated
    # at the end, before return, replace "_" by ""
```
