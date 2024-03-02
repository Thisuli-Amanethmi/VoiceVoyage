import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    return entities


# Example text (user can replace this with their own description)
user_input = """
Upon entering my home, the main entrance is through a foyer, featuring a coat rack to the right of the door. 
From the entrance, one can access the living room via an open doorway.

The living room is located in an open area with the sofa positioned against the far wall, 
chairs adjacent to the sofa, and the coffee table in front of the sofa. 
Additional features include the TV, which is mounted on the wall.

The dining room, accessible from the living room via a doorway, features a table located in the center of the room, 
surrounded by 6 chairs, with a special feature, the china cabinet, located on the adjacent wall.

In the kitchen, accessible via a hallway, the pantry is to the left of the refrigerator, and a table is in the center 
with 4 chairs around it. Notable appliances include the fridge and stove, positioned side by side.

The bedroom is accessed via a hallway, with the main bedroom featuring a bed against the main wall, 
a cupboard to the right of the door, a studying table next to the window, and a dressing table adjacent to the cupboard.

The bathroom is accessible via a hallway and it features a commode next to the sink and a sink under the mirror, 
with additional details like the shower or bathtub in a separate enclosure along the far wall.
"""

# Extract entities
entities = extract_entities(user_input)

# Print extracted entities
for entity in entities:
    print(f"Entity: {entity[0]}, Type: {entity[1]}")
