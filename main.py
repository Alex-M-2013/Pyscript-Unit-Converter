from pyscript import web, when #type: ignore

# Intialise Global variables to access and update later
selected_conversion = ""
conversion_multiplier = None

# Conversion multiplers
miles_to_kilometers_multipler = 1.60934
kilometers_to_miles_multiplier = 0.621371

# Get HTML elements by their IDs and store them in variables for easy access later on
User_Input = web.page["#User_Input"] 
Convert_Button = web.page["#Convert_Button"] 
Output = web.page["#Output"] 

def handle_select(event):
    # Access the global variables created earlier
    global selected_conversion
    global conversion_multiplier
    global miles_to_kilometers_multipler
    global kilometers_to_miles_multiplier
    
    # Update the selected conversion to the option the user selected
    selected_conversion = event.target.value.strip()

    # Set the correct conversion multiplier based on the conversion that the user selected 
    if selected_conversion == "Miles to Kilometers":
        conversion_multiplier = miles_to_kilometers_multipler
    elif selected_conversion == "Kilometers to Miles":
        conversion_multiplier = kilometers_to_miles_multiplier

@when ("click", Convert_Button) 
def Convert():
    # Store the user input value in a variable and remove surrounding whitespace
    input_value = User_Input.value.strip()
    
    # Prepare validation checks for empty or invalid user inputs
    input_conditions = [str(input_value) == '', not isinstance(input_value, (int, float))]

    # Displays an error if the user forgot to select a conversion type
    if selected_conversion == "":
        Output.innerHTML = "You need to choose a conversion first!"
    # Displays an error based on the checks prepared earlier in the "input_conditions" list
    elif any(input_conditions):
        Output.innerHTML = "You need to enter a valid number!"
    
    # Perfrom the conversion and display the result
    converted_value = float(input_value) * conversion_multiplier
    Output.innerHTML = converted_value
