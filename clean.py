# source https://machinelearningmastery.com/clean-text-machine-learning-python/
# load text
# filename = 'txt/metamorphosis-kafka.txt'
filename = 'input/input.txt'

file = open(filename, 'rt')
text = file.read()
file.close()

# split into words by white space
# words = text.split()
# words = [word.lower() for word in words]

# # remove punctuation from each word
# import string
# table = str.maketrans('', '', string.punctuation)
# stripped = [w.translate(table) for w in words]

# print(stripped[:100])

# from nltk import sent_tokenize
# sentences = sent_tokenize(text)
# print(sentences[0])


from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# print(tokens[:100])

# tokens = word_tokenize(text)
# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
words = [word.lower() for word in words]
# print(words[:100])

from nltk.corpus import stopwords
stop_words = stopwords.words('spanish')
# print(stop_words)


# words = [w for w in words if not w in stop_words]
# print(words[:100])
#

input_clean = " ".join(words)

print(input_clean)


# from nltk.tokenize import word_tokenize
# tokens = word_tokenize(text)
# # stemming of words
# from nltk.stem.porter import PorterStemmer
# porter = PorterStemmer()
# stemmed = [porter.stem(word) for word in tokens]
# print(stemmed[:100])
