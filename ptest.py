import pandas as pd
word = pd.read_csv('https://github.com/rizzaesh/django-learning/blob/master/word.csv')
# word = 'ddd'
print(word)
word = word[["word","mean","syn"]]
wordsample = word.sample(10)
print(wordsample)