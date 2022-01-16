from app import Resource, Fridge, Pantry

fridge_data = [
    Fridge("Full fridge, freezer, pantry",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           hrs="11am - 7pm weekdays",
           description="Community fridge located within the building; folks have to be buzzed in"),
    Fridge("Full fridge, freezer, pantry, accepts home cooked meals",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           description="This fridge is located in the alley behind the green house"),
    Fridge("Full fridge, freezer, pantry",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           ),
]

pantry_data = [
    Pantry(
        "E6th street between commercial & victoria",
        social_media="@van.periodpantry",
        description="e-transfer donations to vancouver.periodpantry@gmail.com",
        name="vancouver period pantry",
        website="https://linktr.ee/van.periodpantry"
    ),
    Pantry(
        "1410 W 72nd Ave, Vancouver, BC V6P 3C7",
        social_media="@freepantrymarpole",
        description="Take What You Need, Give What You Can",
        name="Marpole Little Free Pantry",
        website="https://connect4219.wixsite.com/marpolemutualaid"
    ),
    Pantry(
        "2125 Victoria Dr, Vancouver, BC V5N 5Y4",
        social_media="@little_free_pantry",
        description="Take What You Need, Give What You Can",
        name="McSpadden Little Free Pantry",
        website="https://www.flyingzucchini.ca/"
    )
]
