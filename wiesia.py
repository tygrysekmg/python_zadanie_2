from collections import Counter
from pip._vendor.progress import counter
class Grzegorz:
    """Main class"""
    
    def __init__(self):
        print("zadanie staz")
    def read(self,total,dictp,kop,bruce,w,s,uni_data):
        self.total = 0
        self.dict = {}
        self.kop = []
        self.bruce = 0
        self.w = []
        self.s = -1;
        self.uni_data=[]
        print("otwieranie i zamykanie pliku")
        text_file = open("piotr.txt","r")
        lines = text_file.readlines()
        for line in lines:
            for word in line.split():
                
                total += 1
                
                
                
                kop.append(word)

            
        
        print(len(kop))
        
        
        
        
        
        for k in kop:
            print(k)
            s += 1
            print(kop[s])
        print("Nowa Dęba")    
        j = Counter(kop)      
        for z in j:
            print(j[z])
            print(z)
              
        
            
            
            
            
            
        
        
            
            
            
            
            
            
            
                
                    
        print(str(dictp))
        
        
piotr = Grzegorz()
piotr.read(0,{},[],1,[],-1,[])

