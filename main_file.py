import json
import difflib
from difflib import get_close_matches
my_data = json.load(open("data.json"))
def give_me_def(word):
	for i in my_data[word]:
		print(i)
	
def main_fun():
	flag = False
	
	while(1):
		p = input('Press "Y" to continue and "N" to exit \n')
		if "n" == p.lower():
			exit()
		elif "y" == p.lower():
			st = input("Enter the word you want \n")
			st=st.lower()
			if st in my_data:
				flag=True
			elif st.title() in my_data:
				st=st.title()
				flag=True
			elif st.upper() in my_data:
				st=st.upper()
				flag=True
			else:
				new_word = get_close_matches(st,my_data.keys(),cutoff=0.7)
				if new_word:
					print("Did you mean {}".format(new_word[0]))
					take=input('Press "Y" if yes')
					if "y"==take.lower():
						st = new_word[0]
						flag=True
					else:
						continue
				else:
					flag = False
			
		if flag == True:
			give_me_def(st)
			continue
		else:
			print("You entered somthing wrong.. Please try again")
			continue
				
if __name__ == "__main__":
		main_fun()