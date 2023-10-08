import random
# train model
#find greatest energy
def determine_greatest_energy(social_energy, physical_energy, creative_energy, nervous_energy, cognitive_energy):
    energies = {
        "Social": social_energy,
        "Physical": physical_energy,
        "Creative": creative_energy,
        "Nervous": nervous_energy,
        "Cognitive": cognitive_energy
    }

    greatest_energy_category = max(energies, key=energies.get)
    greatest_energy_index = list(energies.keys()).index(greatest_energy_category)

    return greatest_energy_index

#print random option given category
def random_option_from_category(category):
    if category not in categories:
        print("Invalid category. Please choose a valid category.")
        return

    options = categories[category]
    random_option = random.choice(options)
    return random_option
#Lists
categories = {
    1: [ #social
        "Reconnect with friends",
        "Reconnect with family",
        "Go and meet new people"
    ],
    2  : [ #physical
        "Hiking",
        "Go for a walk",
        "Go to a garden",
        "Go for a drive",
        "Cook a meal",
        "Guided meditation",
        "Go to the gym - gym exercises on YouTube → physical",
        "Yoga",
        "Learn a dance"
    ],
    3: [ #creative
        "Crochet - how to crochet … videos on YouTube",
        "Origami - videos",
        "Redecorate the room"
    ],
    4: [ #passive (supports nervous)
        "Listen to music - make a playlist based on mood and artists/genre you like? (Spotify/apple)",
        "Watch TV / movies",
        "Digital detox",
        "Aromatherapy with essential oils",
        "Watch inspirational content, Ted Talks",
        "Clean room with music"
    ],

    5: [ #mentally active (supports cognitive)
        "Read - book suggestions",
        "Puzzle, brain games",
        "Coloring books",
        "Learn some phrases in a new language",
        "Learn about something new, Watch a documentary",
        "Watch a documentary",
        "Do today's wordle"
    ],
    6: [ #self care
        "Go to a spa",
        "Home spa",
        "Take a bath/warm shower"
    ]
}

# Accessing an activity in the "Social" category
# print("A social activity: ", categories["Social"][0])

# Accessing all activities in the "Creative" category
# print("Creative activities: ", categories["Creative"])


# prompt user with question
# store answers
print("Please answer the following with a number from -3 to 3")
social_energy = input("How much social energy do you have? ")
physical_energy = input("How much physical energy do you have? ")
creative_energy = input("How much creative energy do you have? ")
nervous_energy = input("How much nervous energy do you have? ")
cognitive_energy = input("How much cognitive energy do you have? ")

# use answers as input for the predictor
# output activity
bestCategory = determine_greatest_energy(social_energy, physical_energy, creative_energy, nervous_energy, cognitive_energy)
print(bestCategory)
bestOption = random_option_from_category(bestCategory)
print(bestOption)
