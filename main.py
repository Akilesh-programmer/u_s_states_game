import turtle
import pandas

# Creating a screen object.
screen = turtle.Screen()
# Giving the heading for the popup screen. 
screen.title("U.S. States Game")


# Displaying the image in the screen.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()


# Extracting the needed data into specific list from the csv file.
# First extracting data.
data = pandas.read_csv("50_states.csv")
# Getting all the states name into a list.
states = data.state.to_list()
# Getting the x coordinates into a list.
x = data.x.to_list()
# Getting the y coordinates into a list.
y = data.y.to_list()



# Main code for the game.
game_is_on = True
correct_answers = 0
guessed_answers = []

while game_is_on:
# Creating a popup in the screen for guessing.
    # Showing the prompt. Gettint input and storing it in a variable.
    user_input = screen.textinput(title=f"{correct_answers}/50    States correct", prompt="What's another state's name?")
    
    # Lowering the input.
    l_user_input = user_input.lower()

    # Checking if the user guessed any answer correct with the help of a for loop.
    for state in states:
        # Lowering the state name also in the list.
        l_state = state.lower()

        # checking if correct.
        if l_state not in guessed_answers:
            if l_user_input == l_state:
                correct_answers += 1
                guessed_answers.append(l_state)
                
                # Getting the position of the state in the states list so that we can get the x and y coordinates easily.
                index = states.index(state)
                current_x = x[index]
                current_y = y[index]
                turtle.goto(current_x, current_y)

                # Writing the state name in the map.
                turtle.write(state, move=True, align='left', font=('Courier', 8, 'normal'))
                
                
            

            
            
    
            
            



# With the below method the screen will only turn off after our clicking on it.
screen.exitonclick()