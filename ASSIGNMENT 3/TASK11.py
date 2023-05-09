# Write your code here

class Shape:
    
    def __init__(self, shape_type, property_1, property_2):
        self.shape_type = shape_type
        self.property_1 = property_1
        self.property_2 = property_2
    
    def area(self):
        
        if self.shape_type == "Triangle":
            print("Area: ", (0.5) * (self.property_1) * (self.property_2))
        elif self.shape_type == "Rhombus":
            print("Area: ",(self.property_1 * self.property_2) / 2)
        elif self.shape_type == "Square":
            print("Area: ",(self.property_1 * self.property_2))
        elif self.shape_type == "Rectangle":
            print("Area: ",(self.property_1 * self.property_2))
        else:
            print("Area: Shape Unknown")
triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()

