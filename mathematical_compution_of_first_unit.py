# approximate PI

PI=4*(1.0-(1.0/3.0)+(1.0/5.0)-(1.0/7.0)+(1.0/9.0)-(1.0/11.0)+(1.0/13.0)-\
      (1.0/15.0)+(1.0/17.0)-(1.0/19.0))

# area and perimeter of rectangle
radius = float(input("Enter vlaue for circle radius:"))

# Compute area
area = round(PI * radius**2,4)

# Compute perimeter
perimeter = round(radius * PI * 2,4)

# Print the result
print(f"The area of the circle with the radius,{radius} is {area}, and it's perimter is {perimeter}")

# Area and perimter of rectangle

width = float(input("enter width of rectangle:"))
height = float(input("enter height of rectangle:"))

# computing area
area = round(height*width,3)

# computing perimeter
perimeter = round(2*height+2*width,3)

# printing the result
print(f"The area of rectangle with width {width} and {height} is {area} and it's perimeter is {perimeter}")

'''average speed compution'''

# converting kilometer to mile
kilometer = 14
mile = 1.6 * kilometer

# converting minute and second to hour
second = 30
minute = 45
total_second = 45*60+30
hour = total_second / 3600

# compute speed average in miles per hour
averageSpeed = mile / hour

# printing the out put
print(f"The average speed of the runner, who ran {kilometer} kilometer \
in {minute} minute and {second} second is {round(averageSpeed,3)} miles/hour")

