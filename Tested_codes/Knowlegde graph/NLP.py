import spacy

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# User-provided description of home layout
user_description = "The table is in the center of the living room, and the couch is to the left of the table."

# Process the user's description using the NLP model
doc = nlp(user_description)

# Initialize variables to store object locations and names
object_locations = {}
object_names = []

# Extract object locations and names
for token in doc:
    if token.dep_ == "pobj" and token.head.pos_ == "ADP":
        preposition = token.head.text
        object_name = token.text
        object_locations[preposition] = object_name
        object_names.append(object_name)

# Print the results
print("Object Locations:", object_locations)
print("Object Names:", object_names)
