from typing import  *
    

class Task():
    
    def __init__(self, func)->None:
        self.func = func
        self.queue:List = []
        

    def execute(self ) -> None:
        task:Any = self.queue.pop()
        task()


    def appendtask(self,func)->None:
        self.queue.append(func)
        print("appended")

    def execute(self):
        task : Any= self.queue.pop()
        task()
    

    

    
        
def p():
    print(5)


t = Task(p)
t.appendtask(p)
t.execute()

        
