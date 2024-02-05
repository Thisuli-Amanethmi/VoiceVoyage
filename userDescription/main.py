import networkx as nx
from rdflib import URIRef
from pyvis.network import Network

def get_floor_information():
    # Collect basic floor information
    floor_info = {
        "Rooms": []
    }

    # Get the number of rooms on the floor
    num_rooms = int(input("Number of rooms on the Floor: "))

    # Iterate over each room
    for j in range(num_rooms):
        room_info = {
            "Room Name": input(f"Room {j + 1} Name: "),
            "Objects": []
        }

        # Get the number of objects in the room
        num_objects = int(input(f"Number of objects in Room {j + 1}: "))

        # Iterate over each object
        for k in range(num_objects):
            object_info = {
                "Object Name": input(f"Object {k + 1} Name in Room {j + 1}: "),
                "Object Type": input(f"Object {k + 1} Type in Room {j + 1}: "),
                "Object Location": {
                    "Relative Position": input(f"Object {k + 1} Relative Position in Room {j + 1}: "),
                    "Landmark Object or Room Feature": input(f"Object {k + 1} Landmark or Feature in Room {j + 1}: ")
                },
                "Object in Left": input(f"Object {k + 1} What is the object in the left side of object {j + 1}: "),
                "Object in Right": input(f"Object {k + 1} What is the object in the right side of object {j + 1}: ")

            }
            room_info["Objects"].append(object_info)

        # Add room information to floor
        floor_info["Rooms"].append(room_info)

    return floor_info


def create_ontology_map(floor_info):
    house_ontology = {
        "Class": {"House": {"Subclass": {"Room": {}}}},
        "Instances": {}
    }

    for room in floor_info["Rooms"]:
        room_name = room["Room Name"]
        house_ontology["Class"]["House"]["Subclass"]["Room"][room_name] = []

        for obj in room["Objects"]:
            object_name = obj["Object Name"]
            left_object = obj["Object in Left"]
            right_object = obj["Object in Right"]

            house_ontology["Instances"][object_name] = {
                "Type": "Object",
                "inRoom": room_name,
                "leftOf": left_object,
                "rightOf": right_object
            }
            house_ontology["Class"]["House"]["Subclass"]["Room"][room_name].append(object_name)

    return house_ontology

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL

def create_owl_ontology(floor_info):
    # Initialize the graph
    g = Graph()

    # Define namespaces
    EX = Namespace("http://example.org/")
    g.bind("ex", EX)

    # Define classes
    House = EX.House
    Room = EX.Room
    Object = EX.Object

    # Add classes to the graph
    g.add((House, RDF.type, OWL.Class))
    g.add((Room, RDF.type, OWL.Class))
    g.add((Room, RDFS.subClassOf, House))
    g.add((Object, RDF.type, OWL.Class))

    # Define properties
    leftOf = EX.leftOf
    rightOf = EX.rightOf
    inRoom = EX.inRoom

    # Add properties to the graph
    g.add((leftOf, RDF.type, OWL.ObjectProperty))
    g.add((rightOf, RDF.type, OWL.ObjectProperty))
    g.add((inRoom, RDF.type, OWL.ObjectProperty))

    # Add rooms and objects to the ontology
    for room in floor_info["Rooms"]:
        room_name = room["Room Name"]
        room_uri = EX[room_name.replace(" ", "_")]

        g.add((room_uri, RDF.type, Room))

        for obj in room["Objects"]:
            object_name = obj["Object Name"]
            object_uri = EX[object_name.replace(" ", "_")]

            g.add((object_uri, RDF.type, Object))
            g.add((object_uri, inRoom, room_uri))

            left_object = obj["Object in Left"]
            if left_object:
                left_object_uri = EX[left_object.replace(" ", "_")]
                g.add((object_uri, leftOf, left_object_uri))

            right_object = obj["Object in Right"]
            if right_object:
                right_object_uri = EX[right_object.replace(" ", "_")]
                g.add((object_uri, rightOf, right_object_uri))

    return g



def visualize_ontology(g):
    # Convert the RDFLib Graph into a NetworkX graph
    G = nx.Graph()
    for subj, pred, obj in g:
        if isinstance(subj, URIRef) and isinstance(obj, URIRef):
            subj_name = str(subj).split('/')[-1]  # Get the last part of the URI
            obj_name = str(obj).split('/')[-1]  # Get the last part of the URI
            pred_name = str(pred).split('/')[-1]  # Get the last part of the URI
            G.add_edge(subj_name, obj_name, label=pred_name)

    # Use pyvis to visualize the NetworkX graph with cdn_resources set to 'in_line'
    nt = Network(notebook=True, height="750px", width="100%", cdn_resources='in_line')
    nt.from_nx(G)
    nt.show("ontology_graph.html")



# Example usage:
floor_info = get_floor_information()
ontology_graph = create_owl_ontology(floor_info)
print(ontology_graph.serialize(format="turtle"))
visualize_ontology(ontology_graph)
