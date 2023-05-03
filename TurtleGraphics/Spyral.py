import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("arrow")

sum_n = 0
n = 10
for i in range(0, 19):

    my_turtle.color("black")
    my_turtle.right(60)
    sum_n += n
    my_turtle.forward(sum_n)

turtle.done()
