class Car:
    
    wheels = 4 #class variable

    def __init__(self, make , model, year, color):
        self.make = make #instance variabe
        self.model = model #instance variabe
        self.year = year #instance variabe
        self.color = color #instance variabe

    def drive(self):
        print('This '+self.model+' is driving')
    
    def stop(self):
        print('This '+self.model+' is stoped')

