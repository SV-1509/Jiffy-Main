import gensim
from d import nltk_tag_to_wordnet_tag, lemmatize_sentence
import csv
import pandas as pd


import re
model = gensim.models.KeyedVectors.load_word2vec_format('glove.txt', binary = False)

reader = csv.reader(open('dict.csv', 'r'))
dictionary = {}
for row in reader:
   k, v = row[0],row[1:]
   dictionary[k] = v
df = pd.read_csv('file.csv')
functions = df['func'].tolist()
syntax = df['arg'].tolist()
description = df['desc'].tolist()

def findFunction(word):
	word = lemmatize_sentence([word])[0]
	if word in dictionary:
		print('here are the results \n')
		for i in range(len(dictionary[word])):
			print(str(i) + ' - '+dictionary[word][i])
		a = input('\nwant to get more details?(y/n) ')
		if a.lower() == 'y':
			n = int(input('\nenter the function:'))
			index = functions.index(dictionary[word][n])
			print('\n')
			print("SYNTAX: ")
			print(syntax[index])
			print('\n')
			print('DESCRIPTION: ')
			print(description[index])

	else:
		print('not found')
