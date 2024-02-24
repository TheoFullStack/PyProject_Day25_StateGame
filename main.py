import pandas as pd
import turtle

# Constants
lives = 5
x_value= 0
y_value = 0

# Setting the dataframe
data_file = pd.read_csv("50_states.csv")
df = pd.DataFrame(data_file)

# Setting Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Functions
def state_checker():
    if answer_state in df['state'].values:
        print("Present")
        return True
def go_to_placer():
    global x_value, y_value
    if state_checker():
        selected_row = df[df['state'] == answer_state]
        x_value = selected_row.at[selected_row.index[0],'x']
        y_value = selected_row.at[selected_row.index[0], 'y']

        print(f'This is x: {x_value} , this is y: {y_value}')
def text_sender(text,x,y):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x,y)
    text.write(answer_state, align="center", font=("Arial", 12, "normal"))


# Where fun happens
while lives > 0:
    answer_state = screen.textinput("Guess the state", "Give me a state name!: ").title()
    if state_checker():
        go_to_placer()
        text_sender(answer_state,x_value,y_value)
        print(x_value,y_value)
    else:
        lives -=1
        print(lives)

print("Game over")
screen.bye()








turtle.mainloop()