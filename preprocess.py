import os
import string
from clean import clean

def preprocess(path):
	letters = list(string.ascii_lowercase)
	data = []
	for letter in letters:
		for file in os.listdir(path+letter):
			f = open(path+letter+'/'+file,'r')
			doc = f.read()
			doc = clean(doc)
			data.append(doc)
	return data