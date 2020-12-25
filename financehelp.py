
import make as m
import csv
finder = m.makedict()
# import csv
# reader = csv.reader(open('filename.csv', 'r'))
# finder = {}
# for row in reader:
#    k, v = row
#    finder[k] = v
			
		
def findfunction(x):
	x=x.lower()
	try:
		functions = ""
		for i in finder[x]:
			functions = functions + i + " "
		print("You might be looking for {}".format(functions) )
	except:
		print("No functions found ! Try a different keyword")

def helpfunction(x):
	x=x.lower()
	try :
		print(helper[x])
	except:
		print("No function found")
