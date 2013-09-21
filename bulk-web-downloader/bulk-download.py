import sys
import urllib.request

def fop(filename):
  f=open(filename,"r")
  a=0
  for line in f:
   a=a+1
   saveto = 'home_page/'+str(a)+'.html' 
   print(line) #print url
   urllib.request.urlretrieve(line, saveto) 
  f.close()
  
def main():
 fop(sys.argv[1])
 
#standard boilerplate
if __name__=='__main__':
 main()