class FirstClass:
    def sample_demo(self,name):
        self.name = name
        print(f"First Class : {name}")



class SecondClass(FirstClass):
    def base_sample(self):
        print("Second class")

    def demo_sample(self):
        print("First Class and Second class")    


val1 = FirstClass()
val2 = SecondClass()

val1.sample_demo( 'Muhammed')
val2.base_sample()
val2.demo_sample()
val1.sample_demo('Yaseen')








