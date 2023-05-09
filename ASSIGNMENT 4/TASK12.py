class TaxiLagbe:

    def __init__(self, reg_number, covered_area):

        self.reg_number = reg_number
        self.covered_area = covered_area
        self.passenger_list = []
        self.total_fare = 0
        self.passenger_count = 0
        
    def addPassenger(self, *passenger_detail):
        
        if len(self.passenger_list) < 4:

            for passenger in passenger_detail:
            
                passenger_name, passenger_fare = passenger.split("_")
                self.passenger_list.append(passenger_name)
                self.passenger_count += 1
                self.total_fare += int(passenger_fare)
                print(f'Dear {passenger_name}! Welcome to TaxiLagbe.')
        else:

            print("Taxi Full! No more passengers can be added.")

    def printDetails(self):

        print(f"Trip info for Taxi number: {self.reg_number}")
        print(f"This taxi can cover only {self.covered_area} area.")
        print(f"Total Passengers: {self.passenger_count}")
        print(f"Passenger lists:")
        print(", ".join(self.passenger_list))
        print(f"Total Collected Fare: {self.total_fare} Taka.")


taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
