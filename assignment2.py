s = """Imagine a vast sheet of paper on which straight Lines, 
Triangles, Squares, Pentagons, Hexagons, and other figures, 
instead of remaining fixed in their places, move freely about, on
or in the surface, but without the power of rising above or 
sinking below it, very much like shadows - only hard and with 
luminous edges - and you will then have a pretty correct notion 
of my country and countrymen. Alas, a few years ago, I should 
have said "my universe": but now my mind has been opened to 
higher views of things."""

# do not change any code above this line
# your code here
string = s.lower()
print(string)
# do not delete. this list must contain the list of words.
# your code goes here
words = list()
words = string.split()
print(words)
# do not delete
# #do not write any code past here
numberOfWords = len(words)
print(numberOfWords)
Set = set(words)
uniqueWordCount = len(set(words))
print(uniqueWordCount)

freq_occur = dict()
for w in words:
    if w in freq_occur:
        freq_occur[w] = freq_occur[w] + 1
    else:
        freq_occur[w] = 1
print(freq_occur)
print(len(freq_occur))

import string

# import the string module
# use the built-in string.punctuation method to create a list of all punctuation marks
punctuation_list = list(string.punctuation)
# display the punctuation_list
print(punctuation_list)
d = ["haythem!", "is", "eating", "tacos.", ".haythem", "loves", "tacos", "", ":"]
d_clean = list()
# do not change the code above this line.
# your code goes here
for f in d:
    for x in f:
        if x in punctuation_list:
            f = f.replace(x, "")
    d_clean.append(f)
    while '' in d_clean:
        d_clean.remove('')

print(d_clean)
print(len(d_clean))
punctuation_list = list(string.punctuation)
# display the punctuation_list
print(punctuation_list)
r = words
r_clean = list()
# do not change the code above this line.
# your code goes here
for j in r:
    for x in j:
        if x in punctuation_list:
            j = j.replace(x, "")
    r_clean.append(j)
    while '' in r_clean:
        r_clean.remove('')
    while "" in r_clean:
        r_clean.remove("")

print(r_clean)
print(len(r_clean))

freqq_occur = dict()
for y in r_clean:
    if y in freqq_occur:
        freqq_occur[y] = freqq_occur[y] + 1
    else:
        freqq_occur[y] = 1
print(freqq_occur)
print(len(freqq_occur))