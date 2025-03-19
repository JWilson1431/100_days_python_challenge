import turtle
import pandas
import Score

#set up the screen and the title of the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

#setup new score
score = Score.Score()

#set up the map on the screen
screen.screensize(canvheight=600, canvwidth=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read the 50 states csv with pandas
data = pandas.read_csv("50_states.csv")

keep_guessing = True
guessed_states = []
states = data.state.to_list()

while len(guessed_states) < 50:
    #get the user's input for the state
    answer_state = screen.textinput(title=  f"{len(guessed_states)}/50 guessed correct", prompt= "Type in a state" )
    normalized_answer_state = answer_state.title()
    if normalized_answer_state == "Exit":
        # create a list of states the user missed states using list comprehension
        missed_states = [state for state in states if state not in guessed_states]
        # output the list of missed states to a csv so the user can review them
        data_frame = pandas.DataFrame(missed_states)
        data_frame.to_csv("missed_states.csv")
        break
    if normalized_answer_state in states and normalized_answer_state not in guessed_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == normalized_answer_state]
        x_coord = state_data.x.values[0]
        y_coord = state_data.y.values[0]
        t.goto(x_coord, y_coord)
        t.write(answer_state, font=("Arial", 10, "normal"))
        score.increment_score()
        guessed_states.append(normalized_answer_state)

screen.exitonclick()