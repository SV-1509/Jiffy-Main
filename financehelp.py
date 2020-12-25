import gensim
import make as m
import csv


import re
model = gensim.models.KeyedVectors.load_word2vec_format('glove.txt', binary = False)

reader = csv.reader(open('dict.csv', 'r'))
finder = {}
for row in reader:
   k, v = row
   finder[k] = v
			
		
def findfunction(x):
	x=x.lower()
	try:
		functions = ""
		for i in finder[x]:
			functions = functions + i + " "
		print("You might be looking for {}".format(functions) )
	except:
		try:
			a = model.most_similar(positive = [x])[:5]
			print(a)
			for j in a :
				functions = ""
				for i in finder[j[0]]:
					functions = functions + i + " "
			print("You might be looking for {}".format(functions) )
		except:
			print("No functions found ! Try a different keyword")

# def helpfunction(x):
# 	x=x.lower()
# 	try :
# 		print(helper[x])
# 	except:
# 		print("No function found")
