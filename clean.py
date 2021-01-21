from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import re
import string
from nltk.corpus import stopwords, wordnet
import nltk



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


def clean(doc):
	doc = ''.join([i for i in doc if not i.isdigit()])
	doc = doc.lower()
	doc = re.sub(r'[^\w\s]', ' ', doc)
	
	word_list = doc.split()
	filtered_words = [word for word in word_list if word not in stopwords and len(word)>2]
	lem_text = lemmatize_sentence(filtered_words)
	return lem_text
#print(clean('Bootstrap.caplet volatilities from cap volatilities using similar notation to Hull’s book (page 32.11). The first volatility in the vector of caplet vols is zero.'))
