

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


# function that will remove everything except string ina given list

def string_list(items):
    string = []
    for item in items:
        if type(item) == str:
            string.append(item)
    return string
items = [1,'python','code',3,'pgm']
print(string_list(items))

# function to return 2 most frequent numbers

from statistics import mode
def freq_num(data):
    num1= mode(data)
    data.remove(num1)
    num2 = mode(data)
    return num1,num2

values = [1, 4, 2, 4, 1, 4,2,2]
result =freq_num(values)
print(result)
