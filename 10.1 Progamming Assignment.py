#File: 10.1 Programming Assignment
#Name: David Suffolk
#Date: May 19th, 2019
#Course: DSC510-T303 Introduction to Programming (2195-1)
#Assignment Number: 10.1
#Purpose: Create a program that lets a user request as many new Chuck Norris jokes. Jokes are data pulled through an API call


#import requests and JSON libraries for program
import requests
import json

#create url variable for api calls
url = "https://api.chucknorris.io/jokes/random"

#create function for the api call
def api_call():
    response = requests.request("GET", url) #GET request for new joke
    data = response.text #create a variable for the text of the response
    info = json.loads(data) #load data variable as JSON and assign to new variable
    print('Joke: ', info['value'], '\n') #output of joke to user


#create function to open the program
def open_operation():
    print("Welcome to the Chuck Norris Joke Provider") #print Welcome message
    user_input=input("Would you like a joke? Enter Y for new joke\n") #request for user to call for joke or end program
    user_response = user_input.lower() #convert response to lower case for error handling
    if user_response == 'y':
        api_call() #api call if user requests joke
        follow_up() #call the follow-up function for user's next request
    else:
        print("Thank you. The program is closing.") #user does not want a new joke. End program with exit message
        exit()

#create function for any follow-up joke requests from the user
def follow_up():
    next_input = input("Would you like another joke? Enter Y for new joke\n") #request for user to call for joke or end program
    next_response = next_input.lower() #convert response to lower case for error handling
    if next_response == 'y':
        api_call() #api call if user requests joke
        follow_up() #call the follow-up function for user's next request
    else:
        print("Thank you. The program is closing.") #user does not want a new joke. End program with exit message
        exit()

#call the open function to begin program
open_operation()

