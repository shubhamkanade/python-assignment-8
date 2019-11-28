from threading import *
from time import *

def DisplaySmall(string):
	i=0
	#print(getName())
	for i in range(len(string)):
		if(string[i]>='a' and string[i]<'z'):
			print(string[i])

def DisplayCapital(string):
	i=0
	for i in range(len(string)):
		if(string[i]>='A' and string[i]<'Z'):
			print(string[i])
	
def DisplayDigit(string):
	i=0
	for i in range(len(string)):
		if(string[i]>='0' and string[i]<='9'):
			print(string[i])

def main():
	t1=Thread(target=DisplaySmall,args=("HEllo",))
	t2=Thread(target=DisplayCapital,args=("HEllo",))
	t3=Thread(target=DisplayDigit,args=("HellO09",))
	
	t1.start()
	t2.start()
	t3.start()

	print(t1.getName())
	print(t2.getName())
	print(t3.getName())
	
	print(id(t1))
	print(id(t2))
	print(id(t3))
	
if __name__=="__main__":
	main()
