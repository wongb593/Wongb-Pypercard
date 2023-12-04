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

@carousel_app.transition("card1", "click", "go_card1A")
def reset(app, card):
    return "card1A"

@carousel_app.transition("card1", "click", "go_card1B")
def onward(app, card):
    return "card1B"

@carousel_app.transition("card1A", "click", "go_card0C")
def forward(app, card):
    return "card0C"

@carousel_app.transition("card1A", "click", "go_card2A")
def go_back(app, card):
    return "card2A"

@carousel_app.transition("card2A", "click", "go_card1")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1B", "click", "go_card0C")
def reset(app, card):
    return "card0C"

@carousel_app.transition("card1B", "click", "go_card2B")
def reset(app, card):
    return "card2B"

@carousel_app.transition("card2B", "click", "go_card1C")
def reset(app, card):
    return "card1C"

@carousel_app.transition("card2B", "click", "go_card3B")
def reset(app, card):
    return "card3B"

@carousel_app.transition("card3B", "click", "go_card1")
def reset(app, card):
    return "card1"

@carousel_app.transition("card0C", "click", "go_card1")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1C", "click", "go_card1D")
def reset(app, card):
    return "card1D"

@carousel_app.transition("card1C", "click", "go_card2C")
def reset(app, card):
    return "card2C"

@carousel_app.transition("card2C", "click", "go_card2DB")
def reset(app, card):
    return "card2DB"

@carousel_app.transition("card1D", "click", "go_card2D")
def reset(app, card):
    return "card2D"

@carousel_app.transition("card1D", "click", "go_card3D")
def reset(app, card):
    return "card3D"

@carousel_app.transition("card2D", "click", "go_card2DA")
def reset(app, card):
    return "card2DA"

@carousel_app.transition("card2D", "click", "go_card4D")
def reset(app, card):
    return "card4D"

@carousel_app.transition("card2D", "click", "go_card3D")
def reset(app, card):
    return "card3D"

@carousel_app.transition("card2DA", "click", "go_card2DB")
def reset(app, card):
    return "card2DB"

@carousel_app.transition("card2DB", "click", "go_card1")
def reset(app, card):
    return "card1"

@carousel_app.transition("card3D", "click", "go_card1")
def reset(app, card):
    return "card1"
    
@carousel_app.transition("card4D", "click", "go_card1E")
def reset(app, card):
    return "card1E"

@carousel_app.transition("card1E", "click", "go_card2E")
def reset(app, card):
    return "card2E"

@carousel_app.transition("card1E", "click", "go_card1F")
def reset(app, card):
    return "card1F"

@carousel_app.transition("card2E", "click", "go_card1")
def reset(app, card):
    return "card1"

@carousel_app.transition("card1F", "click", "go_card1")
def reset(app, card):
    return "card1"

carousel_app.start("card1")
