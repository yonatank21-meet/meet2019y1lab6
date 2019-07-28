"""import turtle

num_pts = 5
for i in range(num_pts) :
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()

"""

result = []
for count in range(1, 300):
    if count % 3 == 0:
        result.append("Fizz")
    else:
        result.append(count)
print(result)
