import json
def main_fun():
	flag = False
	my_data = json.load(open("data.json"))
	while(1):
		p = input('Press "Y" to continue and "N" to exit \n')
		if "n" == p.lower():
			exit()
		elif "y" == p.lower():
			st = input("Enter the word you want \n")
			for key,value in my_data.items():
				if st == key:
					for i in value:
						print(i)
					flag=True
					break
			if flag == True:
				continue
			else:
				print("You entered somthing wrong.. Please try again")
				continue
				
if __name__ == "__main__":
		main_fun()