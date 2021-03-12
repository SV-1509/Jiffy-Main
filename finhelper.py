import csv
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from make_helper_dictionary import nltk_tag_to_wordnet_tag, lemmatize_sentence
import gensim
import os


#function to print the results in the required format
def print_format(dictionary):
	print('here are the results \n')
	dictionary[word] = [x for x in dictionary[word] if x != '']
	for i in range(len(dictionary[word])):
		print(str(i) + ' - '+dictionary[word][i])
	a = input('\nwant to get more details?(y/n) ')
	if a.lower() == 'y':
		if len(dictionary[word]) == 1:
			index = functions.index(dictionary[word][0])
			print('\n')
			print("SYNTAX: ")
			print(syntax[index])
			print('\n')
			print('DESCRIPTION: ')
			print(description[index])
		else:
			n = int(input('\nenter the function:'))
			index = functions.index(dictionary[word][n])
			print('\n')
			print("SYNTAX: ")
			print(syntax[index])
			print('\n')
			print('DESCRIPTION: ')
			print(description[index])


lemmatizer = WordNetLemmatizer()
cwd = os.getcwd()

#load the primary helper dictionary
reader = csv.reader(open(cwd + '/csv/helper_dictionary_6.csv', 'r'))
dictionary = {}
for row in reader:
	key = row[0]
	value = row[1:]
	dictionary[key] = value

#load the financepy function names, syntax and description
df = pd.read_csv(cwd + '/csv/financepy.csv')
functions = df['func'].tolist()
syntax = df['arg'].tolist()
description = df['desc'].tolist()

#get user input word as a string
word = input('enter word: ')
word = lemmatize_sentence([word])[0]

#check if word is in primary dictionary
if word in dictionary:
	print_format(dictionary)
else :
	#load the secondary dictionary
	reader2 = csv.reader(open(cwd + '/csv/helper_dictionary_3.csv', 'r'))
	dictionary2 = {}
	for row in reader2:
		key = row[0]
		value = row[1:]
		dictionary2[key] = value

	#check if word is in secondary dictionary
	if word in dictionary2:
		print_function(dictionary2)
	else:
		print("not found")