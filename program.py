# number of words in asentence
def words(txt):
    return len(txt.split())
print(words('Python is a programming language'))


# number of sentences in a string
import re
def sentence_count(txt):
    return len(re.split('\.|\?',txt))
string="I am a programmer. What do I do? I program. Which language do I program in? Why, Python of course!"
print(sentence_count(string))

# function to return most frequent number
def most_frequent(List):
    return max(set(List), key = List.count)
 
List = [1, 4, 2, 4, 1, 4,2]
print(most_frequent(List))
