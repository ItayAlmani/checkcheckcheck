import pprint


pp = pprint.PrettyPrinter(indent=4, width=5)



class Dictionnaires():

	def __init__(self, txtName):
		self.txtName = txtName


	def getTxtName(self):

		pathName = r'C:\Users\itaia\Desktop\School\SemesterA\FinalProject\Dictionaries\RonDict\*' + self.txtName + '.txt'
		return pathName.replace("*", "", 1)

	def getTxt(self, txtName):
		fileRead = None
		try:
			with open(txtName, "rt") as fileRead:
				fileRead = fileRead.read().split("\n")
		except FileNotFoundError:
			print("FDictionaryile not found")
			raise
		return fileRead


class Dictionary(Dictionnaires):
	def __init__(self, txtName, dico={}):
		Dictionnaires.__init__(self, txtName)
		self.dico = None

	def preparingTheDico(self, txtFile):
		tempDic = {}
		for word in txtFile:
			if word.split() == []:
				break
			word = word.replace("\t", " ", 1)
			word = word.replace("\t", "", len(word))
			tempDic[word.split()[0]] = word.partition(" ")[2]
		self.dico = tempDic


class listDictionary(Dictionnaires):
	def __init__(self, txtName, listDico=[]):
		Dictionnaires.__init__(self, txtName)
		self.listDico = None

	def preparingTheListDico(self, txtFile):
		self.listDico = txtFile


class nrcDictionary(Dictionnaires):
	def __init__(self, txtName, nrcDico={}):
		Dictionnaires.__init__(self, txtName)
		self.nrcDico = None

	def preparingTheNrcDico(self, txtFile):
		mainDic = {}
		secondary = {}
		for line in txtFile:
			tempKey = line.partition(" ")[0]
			tempValue = line.partition(" ")[2]
			plut = tempValue.split()
			for word in plut:
				#secondary[word.partition(":")[0]] = word.partition(":")[2]
				key = word.partition(":")[0]
				val = word.partition(":")[2]
				secondary[key] = val
			mainDic[tempKey] = secondary
			secondary = {}
		self.nrcDico = mainDic

	def Catagorise (self, dico):
		tempDict = {}
		tempList = []
		abc = ('a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
		for letter in abc:
			for key,val in dico.items():
				if (key[0] == letter):
					tempList.append({key:val})
				else:
					continue
			tempDict[letter] = tempList
			tempList = []
			
		return tempDict
				




class nickNamesDictionary(Dictionnaires):

	def __init__(self, txtName, nickDico={}):
		Dictionnaires.__init__(self, txtName)
		self.nickDico = None

	def preparingTheNickDico(self, txtFile):
		tempDico = dict()
		newList = list()
		tempList = list()

		newList = txtFile.copy()
		tempList = txtFile.copy()
		while True:
			if len(tempList)==0:
				break
			tempList.pop(0)
			tempList.pop(0)
			tempKey = newList.pop(0)
			tempValues = list()
			tempValues.insert(0, newList.pop(0))
			for line in newList:
				if line == '':
					newList = tempList.copy()
					newList.pop(0)
					tempList.pop(0)
					break

				tempVal = tempList.pop(0)
				tempValues.append(tempVal)
			tempDico[tempKey] = tempValues
		self.nickDico = tempDico.copy()

































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































