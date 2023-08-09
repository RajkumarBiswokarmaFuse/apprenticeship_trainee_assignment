# Given an array of strings (str), group the anagrams together. 
# You can return the answer in any order. 
# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

def group_anagrams(words):
    """
    Group anagrams together from an array of strings.

    An anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    Args:
        words (List[str]): The array of strings containing words to be grouped.

    Returns:
        List[List[str]]: A list of lists, where each inner list represents a group
                         of anagrams.

   """
    grouped_anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped_anagrams:
            grouped_anagrams[sorted_word].append(word)
        else:
            grouped_anagrams[sorted_word] = [word]

    
    return list(grouped_anagrams.values())


def main():
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams(["apple","tea",'eat','america']))

if __name__ == "__main__":
    main()