class ParcelKoro:

    def __init__(self, customer_name="No name set", product_weight=0):

        self.customer_name = customer_name
        self.product_weight = product_weight
        self.total_fee = 0

    def calculateFee(self, delivery_location=None):

        if self.product_weight == 0:
            total_fee = 0
        else:
            total_weight = self.product_weight
            location_charge = 50 if delivery_location is None else 100
            total_fee = (total_weight * 20) + location_charge

        self.total_fee = total_fee

    def printDetails(self):

        summary = ""

        summary += "Customer Name: {}\n".format(self.customer_name)
        summary += "Product Weight: {}\n".format(self.product_weight)
        summary += "Total Fee: {}".format(self.total_fee)

        print(summary)


print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()
