def myForEach(listToIterate, callbackFunction):
	if len(listToIterate) == 0:
		return
	element = listToIterate.pop(0)
	callbackFunction(element)
	myForEach(listToIterate, callbackFunction)

def printPlus(elem):
	print(elem + 1)

def main(args):
	myList = [1,2,3,4,5]
	
	myForEach(myList, printPlus)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
