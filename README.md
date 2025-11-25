# Comprehensive Architecture Diagram Generator

This project provides a powerful and flexible system for generating detailed architecture diagrams using Python and Draw.io. It is designed to be extensible, allowing you to create diagrams for any cloud provider (Azure, AWS, GCP) or even custom on-premise architectures.

## Key Features

- **Comprehensive Specification:** Define your diagrams in a simple, human-readable YAML format.
- **Full Draw.io Support:** The system supports a wide range of Draw.io features, including:
    - Custom shapes, styles, and colors.
    - Icons from any Draw.io library (AWS, GCP, Cisco, etc.).
    - Various connector styles and arrow types.
    - Containers for logical grouping (e.g., swimlanes).
- **Extensible:** The Python-based generation engine is designed to be easily extended to support new Draw.io features and icon libraries.

## How it Works

The diagram generation process is straightforward:

1.  **Define your diagram:** Create a YAML file (e.g., `diagram-spec.yaml`) that describes the components, connections, and layout of your diagram.
2.  **Generate the diagram:** Run the `drawio_generator.py` script to parse the YAML file and generate a `.drawio` file.
3.  **View and edit:** Open the generated `.drawio` file in the Draw.io editor to view, edit, and export your diagram.

## Getting Started

### 1. Setup

Install the required Python dependency:

```bash
pip install pyyaml
```

### 2. Create a Diagram Specification

Create a YAML file that defines your diagram. See `diagram-spec.md` for a detailed explanation of the format and all supported features.

Here is a simple example:

```yaml
# my-diagram.yaml

metadata:
  name: "My Simple Diagram"

elements:
  server:
    type: node
    label: "Web Server"
    style:
      shape: "image"
      image: "data:image/svg+xml;base64,..." # Base64 encoded icon
    size:
      width: 50
      height: 50

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

connectors:
  - from: server
    to: database
    label: "JDBC"
```

### 3. Generate the Draw.io File

Run the `drawio_generator.py` script and provide the path to your YAML file:

```bash
python3 drawio_generator.py --spec my-diagram.yaml
```

This will generate a `My_Simple_Diagram.drawio` file in the root directory.

## Examples

- **Multi-Cloud Diagram:** See `multi-cloud-diagram.yaml` for an example of a diagram that combines components from different cloud providers.
- **Contoso Architecture:** The `contoso-architecture-spec.yaml` file demonstrates how to create a detailed Azure architecture diagram using the new system.

## Watch the Video

For a detailed walkthrough of the original system, you can watch this video:

[![Video Title](https://img.youtube.com/vi/m7EuZ7GhinE/0.jpg)](https://www.youtube.com/watch?v=m7EuZ7GhinE)
