class Pycharm:
    def execute(self):
        print('compile')

class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()

l1 = Laptop()
l1.execute(ide)