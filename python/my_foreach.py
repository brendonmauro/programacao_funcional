def myForEach(listToIterate, callbackFunction):
	if len(listToIterate) == 0:
		return
	
	newList = list(listToIterate)
	element = newList.pop(0)
	callbackFunction(element)
	myForEach(newList, callbackFunction)

def printPlus(elem):
	print(elem + 1)

def main(args):
	myList = [1,2,3,4,5]
	
	myForEach(myList, printPlus)
	print(myList)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
