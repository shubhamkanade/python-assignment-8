from threading import *

def EvenFactor(no):
	i=0
	iEvensum=0
	for i in range(1,no+1,1):
		if(i%2==0):
			iEvensum+=i
	print("Even sum is ",iEvensum)
		
def OddFactor(no):
	i=0
	iOddsum=0
	for i in range(1,no+1,1):
		if(i%2!=0):
			iOddsum+=i
	print("ODD sum is",iOddsum)

def main():
	
	t1=Thread(target=EvenFactor,args=(6,))
	t2=Thread(target=OddFactor,args=(6,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	print("Exit from main")

if __name__=="__main__":
	main()	
