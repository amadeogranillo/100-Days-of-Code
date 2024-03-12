import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

all_states = data["state"].to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                                    prompt="What is another state name").title()

    if answer_state == "Exit":
        for states in all_states:
            if states not in guessed_states:
                missed_states.append(states)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
