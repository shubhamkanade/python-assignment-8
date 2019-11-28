import sys
from threading import *
from os import *
def Even(no):
	i=0
	print("ppid is ",getppid())
	for i in range(1,no+1,1):
		if(i%2==0):
			print(i)

def Odd(no):
	i=0
	print("ppid is ",getppid())
	for i in range(1,no+1,1):
		if(i%2!=0):
			print(i)

def main():
	t1=Thread(target=Even,args=(20,))
	t2=Thread(target=Odd,args=(20,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
if __name__=="__main__":
	main()	
