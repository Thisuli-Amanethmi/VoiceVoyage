from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import XSD, Namespace
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
import networkx as nx
from pyvis.network import Network

def collect_room_description():
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

    return {
        "in_front": in_front,
        "to_the_left": to_the_left,
        "far_left": far_left,
        "to_the_right": to_the_right,
        "far_right": far_right,
        "behind_you": behind_you,
        "center": center,
        "window_near_door": window_near_door,
        "window_on_left_wall": window_on_left_wall,
        "window_on_right_wall": window_on_right_wall,
        "window_on_front_wall": window_on_front_wall
    }

def create_rdf_graph(room_description):
    g = Graph()
    MYNS = Namespace("http://example.org/mynamespace/")
    ROOM = URIRef("http://example.org/room/")

    for key, value in room_description.items():
        if key.startswith("window"):
            predicate = ROOM + key.capitalize().replace("_", "")
            g.add((predicate, RDF.type, MYNS.Object))
            g.add((predicate, MYNS.description, Literal(value, datatype=XSD.string)))
        else:
            predicate = URIRef(ROOM + key.replace("_", ""))
            g.add((predicate, RDF.type, MYNS.Object))
            g.add((predicate, MYNS.description, Literal(value, datatype=XSD.string)))

    return g

def visualize_rdf_graph(graph):
    G = rdflib_to_networkx_graph(graph)
    nt = Network(notebook=True)
    nt.from_nx(G)
    nt.show("rdf_graph.html")

def main():
    room_description = collect_room_description()
    rdf_graph = create_rdf_graph(room_description)
    print(rdf_graph.serialize(format='turtle'))
    visualize_rdf_graph(rdf_graph)

if __name__ == "__main__":
    main()
