class Hotel:

    def __init__(self, hotel_name):

        self.hotel_name = hotel_name
        self.staff_members = []
        self.guests = []

    def addStuff(self, name, age, phone_number='000'):

        staff_id = len(self.staff_members) + 1
        self.staff_members.append({
            'id': staff_id,
            'name': name,
            'age': age,
            'phone_number': phone_number
        })

        print(f"Staff With ID {staff_id} is added.")

    def getStuffById(self, id_no):

        for staff in self.staff_members:

            if staff['id'] == id_no:

                summary = ""
                summary += f"Staff ID: {staff['id']}\n"
                summary += f"Name: {staff['name']}\n"
                summary += f"Age: {staff['age']}\n"
                summary += f"Phone no.: {staff['phone_number']}"

                return summary

    def addGuest(self, name, age, phone_number):

        guest_id = len(self.guests) + 1
        self.guests.append({
            'id': guest_id,
            'name': name,
            'age': age,
            'phone_number': phone_number
        })
        print(f"Guest With ID {guest_id} is added.")

    def getGuestById(self, id_no):

        for guest in self.guests:
            if guest['id'] == id_no:
                summary = ""
                summary += f"Guest ID: {guest['id']}\n"
                summary += f"Name: {guest['name']}\n"
                summary += f"Age: {guest['age']}\n"
                summary += f"Phone no.: {guest['phone_number']}"
                return summary

    def allStaffs(self):

        print("All Staffs:")
        print(f"Number of Staff: {len(self.staff_members)}")

        for staff in self.staff_members:
            print(
                f'Staff ID: {staff["id"]} Name: {staff["name"]} Age: {staff["age"]} Phone no: {staff["phone_number"]}')

    def allGuest(self):

        print("All Guests:")
        print(f"Number of Guests: {len(self.guests)}")

        for guest in self.guests:
            print(
                f'Guest ID: {guest["id"]} Name: {guest["name"]} Age: {guest["age"]} Phone no: {guest["phone_number"]}')

        
# Do not change the following lines of code.
h = Hotel("Lakeshore")
h.addStuff("Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest('Carol', 35, '123')
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, '431')
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()
