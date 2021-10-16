#global variables
calculation_to_hours = 24
calculation_to_minutes = 60
name_of_unit_hours = "hours"
name_of_unit_minutes = "minutes"
program_state = True

#fumctions to calculate desired result
def days_to_hours_and_minutes(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours} and" \
               f" {num_of_days * calculation_to_hours * calculation_to_minutes} {name_of_unit_minutes}"

#function to validate user input and then execute the calculation
def validate_then_exec():
    try:
        #try to convert user input/inputs to an integer instead of a string and define it I think?
        user_input_int = int(num_of_days_element)
        if user_input_int > 0:
            #calculated value = the function (days_to_hours) of the user input after converted to an integer
            #but only if it's a value greater than 0
            calculated_value_hours_and_minutes = days_to_hours_and_minutes(user_input_int)
            print(calculated_value_hours_and_minutes)
        elif user_input_int == 0:
            print("You entered 0. Of course the answer is 0 you idiot.")
        else:
            print("Are you a time traveller?")
    #if you can't convert it to an integer (i.e. a string or float) resulting in a value error, do this.
    except ValueError:
        print("You entered something stupid. Try Again.")

#main program loop, linked to global variable for it's state
while program_state == True:
    #give instructions for program use and take input from user
    user_input = input("Enter a number of days as comma seperated values, and this program will convert them to hours"
                       " and minutes. Type exit when finished.\n")
    #if they type "exit", quit the program by setting global variable "program_state" to false
    if user_input == "exit":
        program_state = False
    else:
        #if the program state is still true, split the user input with a "," and run the execute function
        #for each user input
        for num_of_days_element in user_input.split(","):
            validate_then_exec()