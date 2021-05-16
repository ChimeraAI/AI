import nltk
import numpy as np

rawData = []
for i in range(101):
    for j in range(1,101):
        k = i + j
        l = i - j
        m = round(i / j,3)
        n = i * j
        rawData.append(str(i) + " + " + str(j) + " = " + str(k))
        rawData.append(str(i) + " - " + str(j) + " = " + str(l))
        rawData.append(str(i) + " / " + str(j) + " = " + str(m))
        rawData.append(str(i) + " * " + str(j) + " = " + str(n))

sentence_data = np.array(rawData)
raw_tokens = np.array([nltk.word_tokenize(i) for i in sentence_data])
tokens = np.array([nltk.word_tokenize(i) for i in sentence_data]).flatten()

enum_tokens = dict((c, i) for i, c in enumerate(tokens))

question = []
answer = []
for i in rawData:
    splitData = rawData.split(" =")
    seq_in = splitData[0]
    seq_out = splitData[1]
