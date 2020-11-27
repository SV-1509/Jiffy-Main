
helper = {"hist()":"Syntax = matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs) \nDetails = Plot a histogram. \nCompute and draw the histogram of x. The return value is a tuple (n, bins, patches) or ([n0, n1, ...], bins, [patches0, patches1, ...]) if the input contains multiple data. See the documentation of the weights parameter to draw a histogram of already-binned data.\nMultiple data can be provided via x as a list of datasets of potentially different length ([x0, x1, ...]), or as a 2-D ndarray in which each column is a dataset. Note that the ndarray form is transposed relative to the list form.\nMasked arrays are not supported."}
finder = {"label":["xlabel()","ylabel()","title()","legend()"],
		  "labels":["xlabel()","ylabel()","title()","legend()"],
		  "title":["xlabel()","ylabel()","title()","legend()"],
		  "titles":["xlabel()","ylabel()","title()","legend()"],
		  "pie":["pie()"],
		  "histograms":["hist()"],
		  "log":["semilogx()","semilogy()","loglog()"],
		  "semilog":["semilogx()","semilogy()","loglog()"],
		  "log plot":["semilogx()","semilogy()","loglog()"],
		  "semilog plot":["semilogx()","semilogy()","loglog()"],

			
		 }
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
