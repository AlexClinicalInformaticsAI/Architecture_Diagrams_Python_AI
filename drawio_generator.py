import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom
import base64
import argparse

def generate_drawio_xml(spec):
    """
    Generates a Draw.io XML structure from a dictionary specification.
    """
    mxfile = ET.Element("mxfile", host="app.diagrams.net", modified="2023-10-27T10:00:00Z", agent="drawio-generator")
    diagram = ET.SubElement(mxfile, "diagram", id="diagram-1", name="Page-1")
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="600", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="850", pageHeight="1100", math="0", shadow="0")
    root = ET.SubElement(mxGraphModel, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    elements = spec.get("elements", {})
    id_map = {}
    next_id = 2

    # Create all elements first
    for name, el in elements.items():
        style_str = ";".join([f"{key}={value}" for key, value in el.get("style", {}).items()])
        el_id = str(next_id)
        id_map[name] = el_id
        next_id += 1

        label = el.get("label", "")
        width = el.get("size", {}).get("width", "120")
        height = el.get("size", {}).get("height", "60")
        x = "0"
        y = "0"

        ET.SubElement(root, "mxCell", id=el_id, value=label, style=style_str, vertex="1", parent="1")
        ET.SubElement(root.find(f".//mxCell[@id='{el_id}']"), "mxGeometry", x=x, y=y, width=str(width), height=str(height), a="geometry")

    # Apply layout
    layout = spec.get("layout", [])
    for item in layout:
        name = item["name"]
        el_id = id_map.get(name)
        if el_id:
            el = root.find(f".//mxCell[@id='{el_id}']/mxGeometry")
            if el is not None:
                el.set("x", str(item["position"]["x"]))
                el.set("y", str(item["position"]["y"]))

    # Set up containers
    for name, el in elements.items():
        if el.get("type") == "container":
            parent_id = id_map[name]
            for child_name in el.get("children", []):
                child_id = id_map.get(child_name)
                if child_id:
                    child_el = root.find(f".//mxCell[@id='{child_id}']")
                    if child_el is not None:
                        child_el.set("parent", parent_id)

    # Create connectors
    for conn in spec.get("connectors", []):
        style_str = ";".join([f"{key}={value}" for key, value in conn.get("style", {}).items()])
        conn_id = str(next_id)
        next_id += 1

        from_id = id_map.get(conn["from"])
        to_id = id_map.get(conn["to"])
        label = conn.get("label", "")

        ET.SubElement(root, "mxCell", id=conn_id, value=label, style=style_str, edge="1", parent="1", source=from_id, target=to_id)
        ET.SubElement(root.find(f".//mxCell[@id='{conn_id}']"), "mxGeometry", relative="1", a="geometry")
        ET.SubElement(root.find(f".//mxCell[@id='{conn_id}']/mxGeometry"), "mxPoint", a="sourcePoint")
        ET.SubElement(root.find(f".//mxCell[@id='{conn_id}']/mxGeometry"), "mxPoint", a="targetPoint")

    return mxfile

def main():
    parser = argparse.ArgumentParser(description="Generate a Draw.io file from a YAML specification.")
    parser.add_argument("--spec", required=True, help="Path to the diagram specification YAML file.")
    args = parser.parse_args()

    try:
        with open(args.spec, "r") as f:
            spec = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: {args.spec} not found.")
        return

    xml_tree = generate_drawio_xml(spec)

    # Pretty print the XML
    xml_str = ET.tostring(xml_tree, 'utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")

    output_filename = f"{spec.get('metadata', {}).get('name', 'diagram').replace(' ', '_')}.drawio"
    with open(output_filename, "w") as f:
        f.write(pretty_xml)

    print(f"Draw.io file generated successfully: {output_filename}")

if __name__ == "__main__":
    main()
