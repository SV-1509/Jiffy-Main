import csv
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from make_helper_dictionary import nltk_tag_to_wordnet_tag, lemmatize_sentence
import gensim
import os


#function to print the results in the required format
def print_format(dictionary,word):
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
#get user input word as a string
word = input('enter word: ')
word = lemmatize_sentence([word])[0]

#load the primary helper dictionary
reader = csv.reader(open(cwd + '/csv/helper_dictionary_3.csv', 'r'))
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


#check if word is in dictionary
if word in dictionary:
	print_format(dictionary,word)
#check for function name matches with input string
else :
	func = []
	for i in functions:
		func.append(i.split('.')[-1])
	suggestions = []
	for i in func:
		if word in i:
			suggestions.append(i)
	if len(suggestions) > 0:
		print('here are the results \n')
		for i in range(len(suggestions)):
			index = func.index(suggestions[i])
			print(str(i) + ' - '+functions[index])
		a = input('\nwant to get more details?(y/n) ')
		if a.lower() == 'y':
			if len(suggestions) == 1:
				index = func.index(suggestions[0])
				print('\n')
				print("SYNTAX: ")
				print(syntax[index])
				print('\n')
				print('DESCRIPTION: ')
				print(description[index])
			else:
				n = int(input('\nenter the function:'))
				index = func.index(suggestions[n])
				print('\n')
				print("SYNTAX: ")
				print(syntax[index])
				print('\n')
				print('DESCRIPTION: ')
				print(description[index])
	else:
		print("not found")
	
