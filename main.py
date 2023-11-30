"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


# Create the app while ensuring the counter is reset.
carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0}
)


@carousel_app.transition("card1", "click", "Card1A")
def reset(app, card):
    return "card1A"

@carousel_app.transition("card1", "click", "Wakeup")
def onward(app, card):
    return "card1B"

@carousel_app.transition("card1A", "click", "You are late, dress up and go to school")
def forward(app, card):
    return "card0C"

@carousel_app.transition("card1A", "click", "Another 5 minutes")
def go_back(app, card):
    return "card2A"

@carousel_app.transition("card2A", "click", "your mom finds out you are still sleeping and beats you up")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1B", "click", "Go to school early for no reason")
def reset(app, card):
    return "card0C"

@carousel_app.transition("card1B", "click", "Go eat breakfast")
def reset(app, card):
    return "card2B"

@carousel_app.transition("card2B", "click", "Go to school")
def reset(app, card):
    return "card1C"

@carousel_app.transition("card2B", "click", "Skip school for the convenience store")
def reset(app, card):
    return "card3B"

@carousel_app.transition("card3B", "click", "As you are buying your items you mom finds you and beats you")
def reset(app, card):
    return "card1"

@carousel_app.transition("card0C", "click", "reset")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1C", "click", "Go to physical education")
def reset(app, card):
    return "card1D"

@carousel_app.transition("card1C", "click", "Go to a random class")
def reset(app, card):
    return "card2C"

@carousel_app.transition("card2C", "click", "Back to class")
def reset(app, card):
    return "card2DB"

@carousel_app.transition("card1D", "click", "Go eat lunch")
def reset(app, card):
    return "card2D"

@carousel_app.transition("card1D", "click", "Go and talk to our friends and completely neglect your stomach")
def reset(app, card):
    return "card3D"

@carousel_app.transition("card2D", "click", "Go steal lunch money from a small kid")
def reset(app, card):
    return "card2DA"

@carousel_app.transition("card2D", "click", "Ask a friend who might think lowly of you since you asked them for	money")
def reset(app, card):
    return "card4D"

@carousel_app.transition("card2D", "click", "Do not eat and wait lunch out")
def reset(app, card):
    return "card3D"

@carousel_app.transition("card2DA", "click", "Pass till after detention")
def reset(app, card):
    return "card2DB"

@carousel_app.transition("card2DB", "click", "reset")
def reset(app, card):
    return "card1"
    
@carousel_app.transition("card4D", "click", "Next")
def reset(app, card):
    return "card1E"

@carousel_app.transition("card1E", "click", "Go wander the halls for no reason")
def reset(app, card):
    return "card2E"

@carousel_app.transition("card3D", "click", "Go to next class")
def reset(app, card):
    return "card1F"

@carousel_app.transition("card2E", "click", "reset")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1F", "click", "Another day")
def reset(app, card):
    return "card1"

carousel_app.start("card1")
