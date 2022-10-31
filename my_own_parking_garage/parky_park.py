from random import randint
from time import sleep
from IPython.display import Image

fire_show = 'explosion.png'
garage_demo = 'garage_demolition.png'

class Garage():

    def __init__(self):
        self.customerInfo = {}
        self.all_time_customer_info = {}
        self.link = fire_show
        self.link2 = garage_demo
        self.regular = 0
        self.valet = 0
        self.money = 0

    def show_space(self):
        all_space_available = 20 - (self.regular + self.valet)
        reg_space = 12 - self.regular
        all_valet = 8 - self.valet

        if all_space_available == 0:
            print("I am sorry all of our spaces and services are currently sold out. Please try again later.\n")
        else:
            print(f"We have {abs(reg_space)} regular and {abs(all_valet)} valet spots available.\n")

    def add_car(self):
        self.licensePlate = (input("What is your license plate number? If admin, please enter admin. "))
        self.customerInfo[self.licensePlate] = {}

    def basic(self): 
        parking_time = randint(1, 4) * 20

        if self.regular < 12:
            print("We have space for your car today. Remember you will be charged an hourly rate" \
                " for your time spent with us.\n")
            self.money += parking_time
            self.regular += 1
            self.customerInfo[self.licensePlate] = {"Service" : "Basic", "Cost": parking_time}
            self.all_time_customer_info[self.licensePlate] = {"Service" : "Basic", "Cost": parking_time}

        else:
            print("I am sorry we are sold out. Please choose a different service if available.")

    def valet_service(self):
        parking_timev = randint(1, 4) * 40
        prem_parking_time = randint(1, 4) * 40 + 20
        if self.valet < 8:
            print("We have space for your car today. Remember you will be charged an hourly rate" \
                " for your time spent with us. Please pull forward.")
            
            premuium_v_prompt = input("Would you like to upgrade to Premium Valet? (includes a full service car wash?) ")
            
            if premuium_v_prompt.lower().strip() in ('yes', 'y'):
                print("You will be charged an additional fee of $20 on top of your valet fee.\n")
                self.money += prem_parking_time
                self.valet += 1
                self.customerInfo[self.licensePlate] = {"Service": "Premium Valet", "Cost": prem_parking_time}
                self.all_time_customer_info[self.licensePlate] = {"Service": "Premium Valet", "Cost": prem_parking_time}

            else:
                print("You have chosen the standard valet service today. You will be charged an hourly rate" \
                " for your time spent with us today.")
                self.money += parking_timev
                self.valet += 1
                self.customerInfo[self.licensePlate] = {"Service": "Valet", "Cost": parking_timev}
                self.all_time_customer_info[self.licensePlate] = {"Service": "Valet", "Cost": parking_timev}

        else:
            print("I am sorry we are sold out. Please choose a different service if available.")

    def pay(self):
        locate = input("Please provide your license plate number. ")
        paid = input(f'Your total for today is {self.customerInfo[locate]["Cost"]}. Please type pay to pay. ')

        if self.customerInfo[locate]['Service'] == 'Basic':
            self.regular -= 1
        else:
            self.valet -= 1

        if paid.lower().strip() == 'pay' or 'paid':
            print("Thank you please exit the garage.\n")
            del(self.customerInfo[locate])
        else:
            pass
        
    def admin(self):
        moolah = self.money
        password = input("Welcome Admin, please enter your password. \n")

        if password.lower().strip() == 'easy':
            
            print("""
            Admin Options
            [1] See Active Customers
            [2] See All Time Customers
            [3] See Total Revenue
            [4] Exit""")

            while True:
                
                access_info = input("\nWhat would you like to do today Admin? ")

                if access_info == '1':
                    print(f'These are the active customers in the garage right now: {self.customerInfo}')
                elif access_info == '2':
                    print(f'These are the all time customers: {self.all_time_customer_info}')
                elif access_info == '3':
                    print(f'The total made for today is {moolah}. That is both regular and valet services combined.')
                elif access_info == '4':
                   break
                else:
                    print("That is not a valid option. Please try again.")

        else:
            print("You do not have permission to access this information or you have entered your password incorrectly.")
        print("Have a wonderful day.")
        exit()

    # def explosion_display(self):
    #     display(Image(url = self.link)) #in case you want to experience the explosion in juptyer notebook

    # def demo_display(self):
    #     display(Image(url = self.link2)) #in case you want to experience the explosion in juptyer notebook

    def exit_garage(self):
        plate = input("What is your license plate number? ")

        if plate not in self.customerInfo.keys():
            print("Thank you for your patronage.")
            print("This message and the garage will self destruct in 5 minutes, please exit")
            print('.............')
            sleep(5)
            print("You have 3 minutes before this message and the car park self destruct")
            sleep(5)
            print(".......................")
            sleep(2)
            print("You have 10 second before self destruction")
            sleep (1)
            # self.explosion_display()
            sleep(2)
            print(".......................")
            # self.demo_display()
            print("KABOOOM")
            exit()
        else:
            print("You have not paid yet. As a penalty for tyring to leave before paying, we've added $20. \n")
            self.money += 20
            self.customerInfo[plate]["Cost"] += 20
                

#-------------------------------following used for control flow-------------------------------------------

class Main():

    def instructions():
        print("""
        Please read the following prompts carefully, as you may be asked to recall them on a 
        further page. 

        Please note that where basic parking is mentioned, this is a self-service feature that 
        requires you to park your own car. The service is $20 per hour for a maximum of four hours.

        For valet, this in for the valet service only and does not include any additional services. 
        This service is $40 an hour for a maximum of four hours.

        For premium valet, this includes the valet service as well as a full detailed car wash. This 
        service is $60 an hour for a maximum of four hours.

        Please make sure to pay before attempting to exit or you will be assessed a $20 penalty.

        [1] Show Instructions
        [2] Basic 
        [3] Valet 
        [4] Pay
        [5] Show spots/service availability (basic, valet, and premium valet)
        [6] Admin
        [7] Exit
        
        Thank you for choosing BTM Parking.

        pssst....if you're the admin, don't forget the password is the word easy. 
        """)

    def run():
        Main.instructions()
        my_jaguar = Garage()
        Drive = True

        while Drive:
            
            prompt_screen = input("What option would you like to choose from the above menu? ")

            if prompt_screen.strip() == '1':
                Main.instructions()

            elif prompt_screen.strip() == '2':
                my_jaguar.add_car()
                my_jaguar.basic()

            elif prompt_screen.strip() == '3':
                my_jaguar.add_car()
                my_jaguar.valet_service()

            elif prompt_screen.strip() == '4':
                my_jaguar.pay()

            elif prompt_screen.strip() == '5':
                my_jaguar.show_space()
            
            elif prompt_screen.strip() == '6':
                my_jaguar.admin()
        
            elif prompt_screen.strip() == '7':
                my_jaguar.exit_garage()
                
            else:
                print("That is not a valid option. Please try again.")

Main.run()