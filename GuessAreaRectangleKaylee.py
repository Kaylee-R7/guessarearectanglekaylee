#Area of a rectangle
def calculate_rectangle_area():
#Greet the user
    print("---lets calculate the area of a rectangle---")
#Get user input for length and width
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))
#Calculate the area of the rectangle
    area = length*width 
#Ask user for the area
    user_area = float(input("What do you think the area is? "))
#Check if the user's answer is correct
    if user_area == area:
       print("Correct! Great job!")
    else:   
        print(f"Incorrect. The correct area is {area} cm².")
calculate_rectangle_area()