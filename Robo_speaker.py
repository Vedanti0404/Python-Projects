# Import the pyttsx3 module for text-to-speech conversion
import pyttsx3
# Import the os module for system-related functionalities
import os

# Initialize the pyttsx3 text-to-speech engine
robo = pyttsx3.init()

# Print a welcome message
print("Welcome to the Robomax. Created by Vedanti")

# Start an infinite loop to continuously take user input and speak it
while True:
    # Prompt the user to enter what they want to speak or '0' to exit
    x = input("Enter what you want to speak:")
    
    # Check if the user input is '0', and if so, break out of the loop
    if x == "0":
        break
    else:
        # Print the user input
        print(x)
        
        # Use the pyttsx3 engine to say the user input
        robo.say(x)
        
        # Run the pyttsx3 engine to wait for the speech to finish
        robo.runAndWait()
