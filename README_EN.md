# Directory Structure Generator: Comprehensive Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Feature Overview](#feature-overview)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Code Details](#code-details)
6. [Error Handling](#error-handling)
7. [Troubleshooting](#troubleshooting)

## Introduction

The Directory Structure Generator is a GUI application written in Python that allows users to visualize and generate specified directory structures on the actual file system. This tool is particularly useful for planning project structures or quickly implementing directory structures proposed by generative AI.

## Feature Overview

1. **File System Tree View**: Graphically displays the current directory structure
2. **Directory Structure Input**: Define custom structures in a text area
3. **Structure Generation**: Create directories and files based on the specified structure
4. **Real-time Updates**: Reflect changes in the file system in real-time after generation

## Installation and Setup

### Requirements
- Python 3.6 or higher
- tkinter (usually included with Python by default)

### Setting up a Virtual Environment

```bash
# Create project directory
mkdir directory_structure_generator
cd directory_structure_generator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For Unix-based systems
venv\Scripts\activate  # For Windows

# Install necessary packages (if tkinter needs to be installed separately)
pip install tk
```

### Application Installation

```bash
# Clone the repository (replace with actual repository URL)
git clone https://github.com/yourusername/directory-structure-generator.git

# Move to the project directory
cd directory-structure-generator

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt
```

## Usage

1. Launch the application:
   ```bash
   python directory_generator.py
   ```

2. The GUI window will open. You'll see a file system tree view on the left and a directory structure input area on the right.

3. Input the directory structure:
   ```
   project/
       src/
           main.py
       tests/
           test_main.py
       docs/
           README.md
   ```

4. Click the "Generate" button to create the structure.

5. Use the "Refresh" button to update the tree view and confirm the new structure.

## Code Details

### Class: FileTreeApp

#### __init__(self)
- Initialize the application window
- Create widgets and set initial directory

#### create_widgets(self)
- Create main frame, tree frame, and input frame
- Place each widget (tree view, input area, buttons, path input field)

#### create_tree_view(self)
- Create a tree view to display the file system
- Add scrollbars

#### create_input_area(self)
- Create a text area for directory structure input

#### generate_structure(self)
- Validate the input directory structure
- Call the `create_directory_structure` method
- Display success or error messages

#### create_directory_structure(self, structure, base_path='.')
- Recursively create directories and files based on the specified structure
- Parse the hierarchical structure using indentation

## Error Handling

1. **Invalid Input**: Display error message for empty input or input containing invalid characters
2. **Permission Error**: Show specific error message when lacking permissions to create directories
3. **Existing Files/Directories**: Display warning message if items with the same name already exist (optional)

## Troubleshooting

1. **GUI Doesn't Display**
   - Verify that Tkinter is correctly installed
   - If using a virtual environment, ensure it's activated

2. **Directory Generation Fails**
   - Check for write permissions
   - Ensure path length doesn't exceed OS limitations

3. **Tree View Doesn't Update**
   - Click the "Refresh" button
   - Restart the application
