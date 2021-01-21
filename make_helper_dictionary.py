import gensim
import pandas as pd
import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string

model = gensim.models.KeyedVectors.load_word2vec_format('glove.txt', binary = False)
stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def nltk_tag_to_wordnet_tag(nltk_tag):
	if nltk_tag.startswith('J'):
		return wordnet.ADJ
	elif nltk_tag.startswith('V'):
		return wordnet.VERB
	elif nltk_tag.startswith('N'):
		return wordnet.NOUN
	elif nltk_tag.startswith('R'):
		return wordnet.ADV
	else:          
		return None

def lemmatize_sentence(sentence):
	nltk_tagged = nltk.pos_tag(sentence)
	wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
	lemmatized_sentence = []
	for word, tag in wordnet_tagged:
		if tag is None:
			lemmatized_sentence.append(word)
		else:
			lemmatized_sentence.append(lemmatizer.lemmatize(word,tag))
	return lemmatized_sentence




def cleanup(doc):
	#doc = ''.join([i for i in doc if not isinstance(i, float)])
	doc = ''.join([i for i in doc if not i.isdigit()])

	doc = doc.lower()
	doc = re.sub(r'[^\w\s]', ' ', doc)
	word_list = doc.split()
	filtered_words = [word for word in word_list if word not in stopwords and len(word)>2]
	lem_text = [lemmatizer.lemmatize(i) for i in filtered_words]
	lem_text = list(set(lem_text))
	return lem_text

def create_counter(filename):
	counter = {}
	df = pd.read_csv(filename)
	d = df['desc'].tolist()
	for i in range(len(d)):
		d[i] = cleanup(d[i])
		for ele in d[i]:
			if ele in counter:
				counter[ele] += 1
			else:
				counter[ele] = 1
		
		
	x = dict(sorted(counter.items(), key=lambda item: item[1],reverse=True))	
	return x


'''

def get_description(filename):
	df = pd.read_csv(filename)
	d = df['desc'].tolist()

	
#get_description('file.csv')
#print(create_counter('file.csv'))


def create_keywords(filename):

	df = pd.read_csv(filename)
	funcs = df['func'].tolist()
	func = []
	for i in funcs:
		func.append(i.split('.')[-1])

	f = []
	for term in func:
		if term.count('_')>0:
			w = term.split('_')
			f.append(w)
		else:
			if any(x.isupper() for x in term):
				if len(term) == 1:
					f.append([term.lower()])
				else:
					for i in range(1,len(term)):
						if term[i].isupper():
							break
					w = re.findall('[A-Z][^A-Z]*',term[i:])
					w.append(term[:i])
					w = [q.lower() for q in w]
					counter = 0
					for ele in w:
						if len(ele) == 1:
							counter = counter + 1
					if counter > 1:
						for i in range(len(w)):
							if len(w[i]) == 1:
								ww = ''.join(w[i:counter+i])
								w.append(ww)
								del w[i:counter+i]
								break

					f.append(w)
			else:
				w = []
				w.append(term)
				f.append(w)
	
	for i in range(len(f)):

		f[i] = lemmatize_sentence(f[i])


	return f

def create_dictionary_funcnames(keywords, model, functions):
	di = {}
	exceptions = []
	for i in range(len(keywords)):
		words = []
		for word in keywords[i]:
			if word != 'fin':
				words.append(word)
				try:
					a = model.most_similar(positive = [word])[:5]
					for j in a:
						if j[0] not in words:
							words.append(j[0])
				except:
					if word not in exceptions:
						exceptions.append(word)
		
		words = lemmatize_sentence(words)
		for w in words:

			if w not in di:
				di[w] = []
				di[w].append(functions[i])
			else:
				if functions[i] not in di[w]:
					di[w].append(functions[i])
	return di,exceptions





df = pd.read_csv('file.csv')
functions = df['func'].tolist()
keywords = create_keywords('file.csv')

dictionary,exceptions  = create_dictionary_funcnames(keywords, model, functions)


file = open('dict.csv','w')
writer = csv.writer(file)
for ele in dictionary:
	row = [ele]+dictionary[ele]
	writer.writerow(row)
file.close()


'''