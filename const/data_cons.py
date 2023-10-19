import os

class Data_Cons():
    def __init__(self):
        self.workpath = ''
    
    @property
    def cons_init(self):
        return self.workpath

    
    @cons_init.setter    
    def cons_init(self):
        self.workpath = os.getcwd()

        
if __name__ == "__main__":
    test_obj = Data_Cons()
    test_obj.cons_init
    print(test_obj.workpath)