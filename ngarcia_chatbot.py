# Importing random module to pick random motivational quote based on the number generated
import random 

# Simple welcome message when the program starts
print("Hello! I am your Health and Fitness Coach. ") 
# Get user's name and store it as a global variable for all the other functions to use
name = input("What is your name? ") 

recommendations = {
        "chest" :[
            "Incline Smith Machine Or Dumbell Press",
            "A Cable Fly Variant either machine or with Cable Stack",
            "Dips"
        ],
        "back" :[
            "Lat Pulldown",
            "Chest-supported Rows",
            "Pullups"
        ],
        "shoulders" :[
            "Lateral Raises",
            "Shrugs",
            "Rear Delt Cable Fly"
        ],
        "bicep" :[
            "Bayesian Cable Curl",
            "Hammer Curls",
            "EZ-Bar Curls"
        ],
        "tricep" :[
            "Overhead Cable Tricep Extension",
            "Skull Crushers",
            "Tricep Pushdowns"
        ],
        "legs" :[
            "Squats",
            "Leg Extensions",
            "Hamstring Curls"
        ],
        "core" :[
            "Situps",
            "Leg Raises",
            "Rope Ab Crunches"
        ],
        "forearms" :[
            "Straight Bar Cable Wrist Curl",
            "Reverse EZ-Bar Curls"
        ]
    }

food_options = {
        "fruits": [
            "apples",
            "avocados",
            "bananas",
            "berries",
            "oranges"
        ],
        "vegetables": [
            "watercress",
            "spinach",
            "kale",
            "broccoli",
            "Brussels sprouts"
        ],
        "grains": [
            "quinoa",
            "oats",
            "barley",
            "brown rice",
            "millet"
        ],
        "protein": [
            "chicken",
            "turkey",
            "beef",
            "pork"
        ],
        "dairy": [
            "whole or low-fat milk",
            "yogurt",
            "cheese"
        ]
    }

'''
    Main menu function that provides options for the user to choose from.
    Options include workout recommendations, dietary recommendations, motivational quotes, or exiting the chatbot.
'''
def print_header(message):
    """Prints a formatted header for better visibility"""
    print("\n" + "="*50)
    print(f"  {message}")
    print("="*50 + "\n")

def main_menu(): 
    while True:    
       
        print_header("MAIN MENU")
       # Display options to the user and get their choice
        request = input(f"Hi {name} ! Choose one of the options below so I can further assist you. 'Workout', 'Diet', 'Quotes', 'Water' or 'end' to close the chatbot.  :") 
        #Checks user input and calls the corresponding function (case insensitive due to .lower() method)
        if request.lower() == 'workout': 
            exercises() #calling exercise function
        elif request.lower() == 'diet': 
            dietary() #calling dietary function
        elif request.lower() == 'quotes': 
            motivational_quotes() #calling motivational quotes function
        elif request.lower() == 'water':
            water_intake()
        elif request.lower() == 'end': 
            # Closes the chatbot with a goodbye message
            print("Thank you for using the Health and Fitness Coach Chatbot. Stay healthy and fit! Goodbye!")
            break
        else: 
            print("That is not a valid option. Please try again.")

'''
    Exercise Recommendations Function
    Provides different recommendations based on the muscle group the user wants to target
'''
def exercises(): 
    while True:
        
        print_header("WORKOUT RECOMMENDATIONS")
        #Ask user what muscle group they want to target
        muscle = input("What muscle group are you targeting? 'Chest', 'Back', 'Shoulders', 'Bicep', 'Tricep', 'Legs', 'Core', 'Forearms' OR type 'exit' to go back: ") 
        # Dictionary containing muscle groups as keys and list of exercises as values
        
        # Check if the muscle group is valid and provide recommendations or handle exit/invalid input
        if muscle.lower() in recommendations:
            # Using .join allows the program to print the list without the brackets (Better user experience)
            print('------------------------------------') # Visual separator for better readability
            print(f"What I recommend, {name}, is: {', '.join(recommendations[muscle.lower()])}")
            print('------------------------------------') # Visual separator for better readability
        elif muscle.lower() == 'exit':
            print("Returning to main menu.")
            break
        else:
            print("That is not a valid option. Please try again.") 

'''
    Dietary Recommendations Function
    Provides different food recommendations based on the type of food the user is interested in
'''
def dietary(): 
    while True:
        print_header("DIETARY RECOMMENDATIONS") 
        food = input("What type of food are you looking for? 'Fruits', 'Vegetables', 'Grains', 'Protein','Dairy', or type 'exit' to go back: ")
        if food.lower() in food_options:
            # Using .join allows the program to print the list without the brackets (Better user experience)
            print('------------------------------------') # Visual separator for better readability
            print(f"What I recommend, {name}, is: {', '.join(food_options[food.lower()])}")
            print('------------------------------------') # Visual separator for better readability
        elif food.lower() == 'exit':
            print("Returning to main menu.")
            break
        else:
            print("That is not a valid option. Please try again.")
            
'''
    Water Intake Recommendation Function
    Calculates and provides daily water intake recommendations based on user's weight
'''

def water_intake():
    while True:
        try:    
            weight = input("Please enter your weight in pounds (or type 'exit' to go back): ")
            if weight.lower() == 'exit':
                print("Returning to main menu.")
                break
                
            weight = float(weight) # Convert weight to float for calculation
            water_ounces = weight / 2  # Weight divided by 2 gives the recommended daily water intake in ounces
            water_cups = water_ounces / 8  # Convert 8oz to 1 cup for easier understanding)
            print(f"\n{name}, based on your weight of {weight} lbs:")
            print(f"You should drink approximately {water_ounces:.1f} ounces of water per day.")
            print(f"That's about {water_cups:.1f} cups of water (8 oz cups).")
            print(f"Tip: Spread this throughout the day for best results!\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight or 'exit' to go back.")


'''
    Motivational Quotes Function
    Provides a random motivational quote related to health and fitness  
'''            

def motivational_quotes(): 
    
    print("\nHere is a motivational quote for you:\n") # Intro message before displaying the quote
    
    quote = random.randint(1, 10)  #generates a random number between 1 and 10 to select a quote

    #checks the random number and prints the corresponding quote
    if quote == 1: 
        print(" â€œI hated every minute of training, but I said, Don't quit. Suffer now and live the rest of your life as a champion.â€ - Muhammad Ali ") 
    elif quote == 2: 
        print("â€œWe are what we repeatedly do. Excellence then is not an act but a habit.â€ -Aristotele ") 
    elif quote == 3: 
        print(" â€œThe body achieves what the mind believes.â€ â€“ Napoleon Hill") 
    elif quote == 4: 
        print("â€œThe hard days are the best because thatâ€™s when champions are made, so if you push through, you can push through anything.â€ â€“ Dana Vollmer") 
    elif quote == 5: 
        print(" â€œIf you donâ€™t find the time, if you donâ€™t do the work, you donâ€™t get the results.â€ â€“ Arnold Schwarzenegger") 
    elif quote == 6: 
        print(" â€œDead last finish is greater than did not finish, which trumps did not start.â€ ") 
    elif quote == 7: 
        print(" â€œPush harder than yesterday if you want a different tomorrow.â€ â€“ Vincent Williams Sr.") 
    elif quote == 8: 
        print("â€œThe real workout starts when you want to stop.â€ â€“ Ronnie Coleman") 
    elif quote == 9: 
        print("â€œTake care of your body. Itâ€™s the only place you have to live.â€ â€” Jim Rohn") 
    elif quote == 10: 
        print("â€œIâ€™ve failed over and over again in my life and that is why I succeed.â€ â€“ Michael Jordan") 



main_menu() #Calling main menu function to start the program    