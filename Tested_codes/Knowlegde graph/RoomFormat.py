# Initialize variables to store user inputs
in_front = input("In Front: Directly in front of you as you enter, you see ")
to_the_left = input("To the Left: The first object to your immediate left is ")
far_left = input("In the far left corner or section, you can find ")
to_the_right = input("To the Right: On your immediate right, there is ")
far_right = input("Further to the far right, the area is occupied by ")
behind_you = input("Behind You: Turning around, the space behind you includes ")
center = input("Center of the Room: The central area of the room is dominated by ")

window_near_door = input("Is there a window near the door? (yes/no) ")
window_on_left_wall = input("Is there a window on the left wall? (yes/no) ")
window_on_right_wall = input("Is there a window on the right wall? (yes/no) ")
window_on_front_wall = input("Is there a window on the front wall, opposite the door? (yes/no) ")


# Display the filled-in description of the room
print("\nRoom Description:")
print(f"In Front: {in_front}")
print(f"To the Left: {to_the_left}")
print(f"Far Left: {far_left}")
print(f"To the Right: {to_the_right}")
print(f"Far Right: {far_right}")
print(f"Behind You: {behind_you}")
print(f"Center of the Room: {center} (serving as a focal point)")


print(f"Window Near Door: {window_near_door}")
print(f"Window on Left Wall: {window_on_left_wall}")
print(f"Window on right Wall: {window_on_right_wall}")
print(f"Window on Front Wall: {window_on_front_wall}")


from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import  XSD
from rdflib.namespace import Namespace

MYNS = Namespace("http://example.org/mynamespace/")
# Create a new graph
g = Graph()

# Namespace for our room ontology
ROOM = URIRef("http://example.org/room/")

# Define URIs for room features and objects
inFront = URIRef(ROOM + "inFront")
toTheLeft = URIRef(ROOM + "toTheLeft")
farLeft = URIRef(ROOM + "farLeft")
toTheRight = URIRef(ROOM + "toTheRight")
farRight = URIRef(ROOM + "farRight")
behindYou = URIRef(ROOM + "behindYou")
centerOfRoom = URIRef(ROOM + "centerOfRoom")
windowNearDoor = URIRef(ROOM + "windowNearDoor")
windowOnLeftWall = URIRef(ROOM + "windowOnLeftWall")
windowOnRightWall = URIRef(ROOM + "windowOnRightWall")
windowOnFrontWall = URIRef(ROOM + "windowOnFrontWall")

# Add objects and features to the graph with their descriptions
g.add((inFront, RDF.type, MYNS.Object))
g.add((inFront, MYNS.description, Literal(in_front, datatype=XSD.string)))

g.add((toTheLeft, RDF.type, MYNS.Object))
g.add((toTheLeft, MYNS.description, Literal(to_the_left, datatype=XSD.string)))

g.add((farLeft, RDF.type, MYNS.Object))
g.add((farLeft, MYNS.description, Literal(far_left, datatype=XSD.string)))

g.add((toTheRight, RDF.type, MYNS.Object))
g.add((toTheRight, MYNS.description, Literal(to_the_right, datatype=XSD.string)))

g.add((farRight, RDF.type, MYNS.Object))
g.add((farRight, MYNS.description, Literal(far_right, datatype=XSD.string)))

g.add((behindYou, RDF.type, MYNS.Object))
g.add((behindYou, MYNS.description, Literal(behind_you, datatype=XSD.string)))

g.add((centerOfRoom, RDF.type, MYNS.Object))
g.add((centerOfRoom, MYNS.description, Literal(center, datatype=XSD.string)))

# Adding window information
g.add((windowNearDoor, RDF.type, MYNS.Object))
g.add((windowNearDoor, MYNS.description, Literal(window_near_door, datatype=XSD.string)))

g.add((windowOnLeftWall, RDF.type, MYNS.Object))
g.add((windowOnLeftWall, MYNS.description, Literal(window_on_left_wall, datatype=XSD.string)))

g.add((windowOnRightWall, RDF.type, MYNS.Object))
g.add((windowOnRightWall, MYNS.description, Literal(window_on_right_wall, datatype=XSD.string)))

g.add((windowOnFrontWall, RDF.type, MYNS.Object))
g.add((windowOnFrontWall, MYNS.description, Literal(window_on_front_wall, datatype=XSD.string)))



# Extending the existing graph definition

# Define a namespace for our spatial and navigation properties
SPATIAL = Namespace("http://example.org/spatial/")


# Define spatial relations
adjacentTo = SPATIAL.adjacentTo
oppositeOf = SPATIAL.oppositeOf
near = SPATIAL.near

# Define a navigation path property
safePath = SPATIAL.safePath

# Add spatial relations between objects and features in the room
# Example relations based on hypothetical room layout
g.add((toTheLeft, adjacentTo, windowOnLeftWall))
g.add((toTheRight, adjacentTo, windowOnRightWall))
g.add((inFront, oppositeOf, behindYou))
g.add((centerOfRoom, near, inFront))
g.add((centerOfRoom, near, toTheLeft))
g.add((centerOfRoom, near, toTheRight))
g.add((centerOfRoom, near, farLeft))
g.add((centerOfRoom, near, farRight))

# Define safe navigation paths
# Example: Define a safe path from the door (behindYou) to the center of the room
g.add((behindYou, safePath, centerOfRoom))
# Additional paths can be defined similarly based on the room's layout and obstacles

print(g.serialize(format='turtle'))

from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
import networkx as nx
from pyvis.network import Network

# Assuming 'g' is your RDFLib graph
G = rdflib_to_networkx_graph(g)

# Initialize a PyVis network object
nt = Network(notebook=True)
nt.from_nx(G)
nt.show("rdf_graph.html")






