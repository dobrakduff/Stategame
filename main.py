import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
print(all_states)

guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="Next state").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        t.goto(x, y)
        t.write(answer_state)


screen.exitonclick()
