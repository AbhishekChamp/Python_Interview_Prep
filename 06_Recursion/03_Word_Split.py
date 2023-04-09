# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable

# Input 1: word_split('themanran', ['the', 'ran', 'man'])
# Output 1: ['the', 'man', 'ran']

# Input 2: word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
# Output 2: ['i', 'love', 'dogs', 'John']

# Input 3: word_split('themanran', ['clown', 'ran', 'man'])
# Output 3: []

def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output

# Testing Solution
result = word_split('themanran', ['the', 'ran', 'man'])
print(result)