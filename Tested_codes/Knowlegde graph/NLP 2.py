import spacy

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# User-provided description of home layout
user_description = "The table is in the center of the living room, and the couch is to the left of the Chair. Sofa is next to window."

# Process the user's description using the NLP model
doc = nlp(user_description)

# Initialize a dictionary to store object locations
object_locations = {}

# Iterate over noun phrases (for objects) and their children (for spatial relationships)
for chunk in doc.noun_chunks:
    # The noun phrase itself is an object
    object_name = chunk.text
    # Check if the chunk has children (i.e., related prepositions)
    for child in chunk.root.children:
        if child.dep_ == "prep":
            # For each prepositional phrase, we find its object
            for obj in child.children:
                if obj.dep_ == "pobj":
                    # Map the object of the preposition to the noun phrase
                    object_locations[obj.text] = f"{child.text} {chunk.text}"

# Print the results
print("Object Locations:", object_locations)
