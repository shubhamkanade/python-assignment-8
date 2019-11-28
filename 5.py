from threading import *
from os import *

def Thread1(lobj):
	i=0
	
	lobj.acquire()
	for i in range(1,50+1,1):
		print(i)
	lobj.release()
	
def Thread2(lobj):
	i=0
	lobj.acquire()
	for i in range(50,0,-1):
		print(i)
	lobj.release()

def main():
	
	lobj=Lock()	
	t1=Thread(target=Thread1,args=(lobj,))
	t2=Thread(target=Thread2,args=(lobj,))
	
	t1.start()
	t2.start()
	

if __name__=="__main__":
	main()
