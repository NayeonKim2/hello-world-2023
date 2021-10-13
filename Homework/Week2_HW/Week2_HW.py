# Assignment 1
myList = ["hand sanitizer", "student ID", "airpods"], ["keys"]
myBag = ["hand sanitizer", "student ID", "airpods"]
myPocket =  ["keys"]

myHandSanitizer = {
    "color" : "green",
    "scent" : "apple",
    "quantity" : 1
}

myStudentID = {
    "color" : "red-orange",
    "forHome" : False
}

myAirpods = {
    "cost" : 1100,
    "size" : "small",
    "expensive" : True
}

myKeys = {
    "quantity" : 2,
    "color" : ["gold", "black"],
    "heavy" : False
}

myObjectsInEverydayLife = (myBag + myPocket)
print(myObjectsInEverydayLife)
print("The most expensive object is: " + myList[0][2])


# Assignment 2
{
  "name": "iPad",
  "generation": 8,
  "color": "space-gray",
  "homebutton": False,
  "Squared": True,
}


# Assignment 3

# let the user know what's going on
print ("Hey, nice to meet you. I am Alexa.")
print ("Please answer the questions below")
print ("-----------------------------------")

yourName = input ("What's your name?:  ")
yourHair = input ("What color is your hair?:  ")
location1 = input ("Where do you live?:  ")
restaurant = input ("What is your favorite restaurant near your house?: ")
hometown = input ("Where are you from?: ")
netflix = input ("What is your favorite Netflix show?: ")
adjective1 = input ("Enter an positive adjective:  ")
famousPerson = input ("A famous person you like: ")

story = "Hi, you must be " + yourName + "! Oh, I like  your " + yourHair + "hair. Oh my god, I am also live in " + location1 + ". " \
"I like " + restaurant + ", too! By the way, I heard that you are from " + hometown + ". " \
"I've never been to " + hometown + ". Actually, my favorite Netflix show is also  " + netflix + "! I watched that twice. " \
"You look so " + adjective1 + ". I really like you! Do you have any plan tomorrow? " "If you are available, let's hang out with " \
+ famousPerson + " in Brooklyn." + " Okay, bye, " + yourName + "! See you."

print (story)





