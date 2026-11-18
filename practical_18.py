#Count words in a sentance


def count_words(s):
    if not s:
        return 0
    words=s.split()
    return len(words)
     

print(count_words("Python is a programming language"))


def most_frequently_word(s):
    words=s.splite()
words=s.split()

frequency={}
for word in words:

