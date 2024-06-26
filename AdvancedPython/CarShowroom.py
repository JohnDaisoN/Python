class CarShowroom:
    
    def __init__(self):
        self.users = {}
        self.INSURANCE = 100000
        self.price = 0
        self.intermediateprice = 0
        self.company = ''
        self.model = ''
        self.variant = ''
        self.companies = ['Toyota','Nissan','BMW']
        self.models = {'Toyota':['Innova','Etios'], 'Nissan':['Sunny','Magnite'],'BMW':['X5','X3']}
        self.variants = {'petrol':100000,'diesel':75000}
        self.prices = {'Innova':1000000,'Etios':800000,'Sunny':800000,'Magnite':1200000,'X5':2000000,'X3':1800000}
        while 1:
            # print('')
            print('1. Register   2. Login')
            selectedOption = int(input('Select one of the two options'))
            if selectedOption == 1:
                username = input('Enter name')
                password = input('Enter password')
                print('Ok ' + username + ' has login previleges')
                self.users[username] = password
                
            elif selectedOption == 2:
                username = input('Enter name')
                if username not in self.users:
                    print('The username is invalid, register please')
                    continue
                password = input('Enter password')
                if self.users[username] == password:
                    print('Successfully verified')
                    break
                else:
                    print('The username is not present, please register')
        while 1:
            print(self.companies)
            option = input('Select any of the above companies: ')
            if option in self.companies:
                self.company = option
                break
            else:
                print('Please select any of the companies')
        while 1:
            print(self.models[self.company])
            op = input('enter model name from above options: ')
            if op in self.models[self.company]:
                self.model = op
                break
            else:
                print('Please select any of the models')
        while 1:

            i = input('select a variant by writing it -  1.petrol 2.diesel: ')
            if i in self.variants.keys():
                self.variantprice = self.variants[i]
                break
            else:
                print('Select a valid variant type')


    def pricedetails(self):
        self.intermediateprice = self.variantprice + self.prices[self.model]
        self.price = self.intermediateprice + 0.18 * self.intermediateprice + 0.18 * self.intermediateprice + self.INSURANCE
        print('The price of your car is ' + self.price + ' Rs')





            
                



car = CarShowroom()
car.pricedetails()




        



