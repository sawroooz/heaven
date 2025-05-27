class juni:
    def __init__(self,jun,tara):
        self.x=jun
        self.y=tara
        self.homw()
    def homw(self):
        temp=self.x
        self.x=self.y
        self.y=temp 
    def get_values(self):
        return self.x,self.y    
x=juni(1,2)  
print(x.get_values())      