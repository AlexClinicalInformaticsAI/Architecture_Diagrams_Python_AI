# Comprehensive Diagram Specification

This document defines the YAML-based specification for creating rich and detailed diagrams using the `drawio_generator.py` script. This format is designed to be comprehensive, supporting a wide range of Draw.io's features to create diagrams for any domain, not just Azure.

## Core Concepts

The specification is structured around a few core concepts:

- **Nodes:** The basic building blocks of your diagram (e.g., servers, databases, users).
- **Connectors:** The lines that connect nodes, representing relationships or data flow.
- **Containers:** Special nodes that can contain other nodes, used for grouping and creating logical boundaries (e.g., VNet, Subnet, Region).
- **Layout:** Optional hints to guide the automated placement of elements.

---

## YAML Specification

Below is a template for the diagram specification. Each section is explained in detail.

```yaml
# diagram-spec.yaml

# Metadata for the diagram
metadata:
  name: "Multi-Cloud Architecture"
  author: "Jules"

# Definitions for nodes, containers, and groups
elements:
  # User node definition
  user:
    type: node
    label: "User"
    style:
      shape: "actor"
      fillColor: "#cce5ff"
      strokeColor: "#6c8ebf"
    size:
      width: 40
      height: 60
    # You can reference Draw.io's built-in icon libraries
    # icon: "mxgraph.aws4.user"

  # Web Server (example with a specific icon)
  web_server:
    type: node
    label: "Web Server"
    style:
      shape: "image"
      image: "data:image/svg+xml;base64,..." # Base64 encoded SVG or PNG
      verticalLabelPosition: "bottom"
      verticalAlign: "top"
    size:
      width: 50
      height: 50

  # Generic Database
  database:
    type: node
    label: "Database"
    style:
      shape: "cylinder"
      fillColor: "#ffe6cc"
      strokeColor: "#d79b00"
    size:
      width: 60
      height: 80

  # VNet container
  vnet_container:
    type: container
    label: "Virtual Network"
    style:
      shape: "swimlane"
      fillColor: "#f5f5f5"
      strokeColor: "#666666"
      dashed: 1
    # This container will hold other elements
    children:
      - web_server
      - database

# Definitions for the connections between elements
connectors:
  - from: user
    to: web_server
    label: "HTTPS"
    style:
      edgeStyle: "orthogonalEdgeStyle"
      endArrow: "classic"
      strokeColor: "#000000"
  - from: web_server
    to: database
    label: "SQL"
    style:
      edgeStyle: "entityRelationEdgeStyle"
      endArrow: "classic"
      strokeColor: "#000000"

# Optional layout hints
layout:
  - name: user
    position:
      x: 50
      y: 150
  - name: vnet_container
    position:
      x: 200
      y: 50
```

---

## Specification Details

### Nodes (`elements`)

Each node is defined by a unique name (e.g., `web_server`).

- `type`: Can be `node` or `container`.
- `label`: The text displayed on the node.
- `style`: A map of Draw.io style properties.
    - `shape`: The shape of the node (e.g., `rectangle`, `ellipse`, `cylinder`, `actor`, `image`).
    - `fillColor`: Background color.
    - `strokeColor`: Border color.
    - `dashed`: `1` for dashed, `0` for solid.
    - `image`: For `shape: image`, you can use a base64 encoded image string or a URL.
    - `verticalLabelPosition`: `top`, `middle`, `bottom`.
- `size`:
    - `width`: Width of the node.
    - `height`: Height of the node.
- `icon`: (Optional) A string referencing a shape from Draw.io's built-in libraries. This provides access to thousands of icons (e.g., `mxgraph.aws4.ec2`, `mxgraph.gcp.compute.container_optimized_os`).

### Connectors (`connectors`)

Each connector defines a link between two elements.

- `from`: The unique name of the source element.
- `to`: The unique name of the target element.
- `label`: Text to display on the connector.
- `style`:
    - `edgeStyle`: `orthogonalEdgeStyle`, `elbowEdgeStyle`, `straight`, `entityRelationEdgeStyle`.
    - `endArrow`: `classic`, `block`, `oval`.
    - `strokeColor`: Color of the line.

### Containers (`elements` with `type: container`)

Containers are special nodes that can have children.

- `type`: Must be `container`.
- `label`, `style`, `size`: Same as nodes.
- `children`: A list of unique names of the elements to be placed inside this container.

### Layout (`layout`)

This section is optional and allows you to specify the exact position of elements.

- `name`: The unique name of the element.
- `position`:
    - `x`: The x-coordinate.
    - `y`: The y-coordinate.

This comprehensive format will serve as the foundation for the `drawio_generator.py` script, enabling the creation of highly customized and detailed diagrams.
