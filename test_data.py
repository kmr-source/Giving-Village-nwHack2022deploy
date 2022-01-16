import app

fridge_data = [
    app.Fridge("Full fridge, freezer, pantry",
               "29 West Hastings Street",
               name="Vancouver Women's Health Collective",
               hrs="11am - 7pm weekdays",
               description="Community fridge located within the building; folks have to be buzzed in"),
    app.Fridge("Full fridge, freezer, pantry, accepts home cooked meals",
               "29 West Hastings Street",
               name="Vancouver Women's Health Collective",
               description="This fridge is located in the alley behind the green house"),
    app.Fridge("Full fridge, freezer, pantry",
               "29 West Hastings Street",
               name="Vancouver Women's Health Collective",
               description="This fridge is located in the alley behind the blue house"
               ),
    app.Fridge("Full fridge, freezer, pantry",
               "340 West 2nd Avenue, Vancouver, BC",
               name="Food Stash Foundation",
               description="This fridge is located in the alley behind the blue house"
               ),
    app.Fridge("Full fridge, freezer, pantry",
               "3718 Main Street, Vancouver, BC",
               name="The Soap Dispensary & Kitchen Staples",
               description="Located in the heart of Main Street!",
               img="https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/215763969_288689355954978_4168483443270479323_n.jpg?"
                   "_nc_cat=103&ccb=1-5&_nc_sid=a26aad&_nc_ohc=AxakfH4qk_oAX9X7fwp&_nc_ht=scontent-sea1-1.xx&oh=00_AT9WT2xN7"
                   "LUFOVRY1e3RePpD1Fq2gX-igzwKqOq97zde0g&oe=61E81965"),
]

pantry_data = [
    app.Pantry(
        "E 6th street, Vancouver, BC",
        social_media="@van.periodpantry",
        description="Located between Commercial & Victoria. E-transfer donations to vancouver.periodpantry@gmail.com",
        name="Vancouver Period Pantry",
        website="https://linktr.ee/van.periodpantry"
    ),
    app.Pantry(
        "1410 W 72nd Ave, Vancouver, BC V6P 3C7",
        social_media="@freepantrymarpole",
        description="Take What You Need, Give What You Can",
        name="Marpole Little Free Pantry",
        website="https://connect4219.wixsite.com/marpolemutualaid"
    ),
    app.Pantry(
        "2125 Victoria Dr, Vancouver, BC V5N 5Y4",
        social_media="@little_free_pantry",
        description="Take What You Need, Give What You Can",
        name="McSpadden Little Free Pantry",
        website="https://www.flyingzucchini.ca/"
    )
]
