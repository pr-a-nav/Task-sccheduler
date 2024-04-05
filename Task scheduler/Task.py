from collections import namedtuple

class Task:

    def __init__(self, func, args, ):
        self.args = args
        self.func = func

    def execute(self):
        result = self.func(self.args)
        return result





print("starting")

def printh(x):
    return x

task = Task(printh,4)


r = task.execute()

print(r)
