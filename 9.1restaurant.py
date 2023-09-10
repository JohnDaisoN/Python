class Restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.res_name}")
        print(f"The cuisine of the restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.res_name} is now declared open guys")

res1 = Restaurant("Apsara","Indian")
print(res1.res_name)
print(res1.cuisine_type)

res1.describe_restaurant()
res1.open_restaurant()

res2 = Restaurant("Dominos", "AmericanPizza")
res3 = Restaurant("Stevenhe", "chinese")

res2.describe_restaurant()
res3.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, age, sex, salary):
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
         self.sex = sex
         self.salary = salary

    def describe_user(self):
        print(f"The user's name is {self.first_name+self.last_name}")
        print(f"The user's age is {self.age}")
        print(f"The user's sex is {self.sex}")
        print(f"the user's salary should be {self.salary}")
    
    def greet_user(self):
        print(f"Greetings, Mr {self.first_name + self.last_name}")

user1 = User("John", "Daison", 20, "M", 2000000)
user2 = User("Maria", "Thomas", 21, "F", 60000)

user1.describe_user()
user2.describe_user()
user2.greet_user()
user1.greet_user()
