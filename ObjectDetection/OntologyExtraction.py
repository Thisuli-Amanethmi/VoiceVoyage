rdf_file_path = "E:\\2nd year\\Sem2\\DSGP\\MainGitHubRepo\\VoiceVoyage\\OntologyGraph\\mydata.rdf"

# Reading the content of the RDF file into a string
with open(rdf_file_path, 'r', encoding='utf-8') as file:
    root = file.read()

print(root)

import xml.etree.ElementTree as ET


xml_data = root

# Parse the XML content
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

# Define the namespace to avoid specifying it every time
namespaces = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'ns1': 'http://example.org/spatial/',
    'ns2': 'http://example.org/mynamespace/'
}
def Spatial_relationships(relationship):
    # Initialize a list to hold objects with an 'adjacentTo' relationship
    adjacent_objects = []
    Objects_with_spatial_relation=[]

    # Iterate through each object in the XML
    for obj in root.findall('rdf:Description', namespaces):
        # Check if the object has a relationship
        if obj.find('ns1:'+relationship, namespaces) is not None:
            # Extract the object's ID and the ID of the object it is adjacent to
            obj_id = obj.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
            adjacent_to_id = obj.find('ns1:'+relationship, namespaces).get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
            # Extract the object's description
            description = obj.find('ns2:description', namespaces).text if obj.find('ns2:description', namespaces) is not None else 'No description'
            # Add the object's details to the list
            adjacent_objects.append({'id': obj_id, 'adjacent_to': adjacent_to_id, 'description': description})

    # Print or return the list of adjacent objects
    for obj in adjacent_objects:
        #print(f"Object ID: {get_description_by_id(obj['id'])}, {relationship}: {get_description_by_id(obj['adjacent_to'])}, Description: {obj['description']}")
        if get_description_by_id(obj['id'])!="no" and get_description_by_id(obj['adjacent_to'])!="no":
            if get_description_by_id(obj['id'])=="yes":
                Objects_with_spatial_relation.append("Window")
                Objects_with_spatial_relation.append(get_description_by_id(obj['adjacent_to']))
            if get_description_by_id(obj['adjacent_to'])=="yes":
                Objects_with_spatial_relation.append(get_description_by_id(obj['id']))
                Objects_with_spatial_relation.append("Window")
            else:
                Objects_with_spatial_relation.append(get_description_by_id(obj['id']))
                Objects_with_spatial_relation.append(get_description_by_id(obj['adjacent_to']))

    return Objects_with_spatial_relation,relationship

def get_description_by_id(object_id):
    # Find the object by its ID
    obj = root.find(f".//rdf:Description[@rdf:about='{object_id}']", namespaces)
    if obj is not None:
        # Extract the object's description if available
        description = obj.find('ns2:description', namespaces)
        return description.text if description is not None else "No description"
    else:
        return "Object not found"




