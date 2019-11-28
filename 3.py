from threading import *

def Evenlist(list):
	i=0
	Evensum=0
	for i in list:
		if(i%2==0):	
			Evensum+=i
	print("Even list sum {}".format(Evensum))

def Oddlist(list):
	i=0
	Oddsum=0
	for i in list:
		if(i%2!=0):
			Oddsum+=i
	print("Odd list sum {}".format(Oddsum))

def main():
	arr=list()
	print("Enter n numbers")
	n=int(input())
	print("Enter list elements")
	i=0
	for i in range(n):
		arr.append(int(input()))
	t1=Thread(target=Oddlist,args=(arr,))
	t2=Thread(target=Evenlist,args=(arr,))
	
	t1.start()
	t2.start()

			

if __name__=="__main__":
	main() 			






