from FilteredTwitsBuilder import FilteredTwitsBuilder
from DBPharser import DBPharser
	
def main():
	f = FilteredTwitsBuilder()
	print("starting configuration..")
	Filtered = f.read_from_csv()
	DB = DBPharser(Filtered)
	DB.ConnectToDB()
	

if __name__ == "__main__":
	main()
