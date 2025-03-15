# 3D Model Converter

This Python script allows you to convert 3D model files from one format to another. To use it, you need to organize your 3D models into a specific folder structure and provide the source and target folders as input parameters when running the script.

## Folder Structure

Before running the script, ensure that your 3D models are organized as follows:

- Create a folder for each type of 3D object format (e.g., `glb`, `fbx`, `obj`, etc.).
- Place the respective 3D model files inside the corresponding folder.


### Example Folder Structure:

```
project/
├── glb/
│   ├── object1.glb
│   ├── object2.glb
│   └── object3.glb
├── fbx/
│   ├── object1.fbx
│   ├── object2.fbx
│   └── object3.fbx
└── converter.py
```

In this example, all `.glb` files are inside the `glb` folder, and `.fbx` files are inside the `fbx` folder. 

## Running the Script

To run the Python script, follow these steps:

### 1. Organize Your Files

Ensure that your 3D model files are organized inside their respective folders, as described above. For example, if you have `object.glb`, save it inside the `glb/` folder (i.e., `glb/object.glb`).

### 2. Execute the Script

After organizing your files, open a terminal or command prompt, navigate to the folder containing the converter files, such as  `converter_glb_to_fbx_windows.py`, and run the following command:

```bash
python converter_glb_to_fbx_windows.py <source_folder> <target_folder>
```

### Parameters:
- **`<source_folder>`**: The folder where the 3D model files are located. This should be the name of the folder, such as `glb`, `fbx`, `obj`, etc.
- **`<target_folder>`**: The folder where the converted 3D models should be saved. This can be the same format or a different one, such as `fbx`, `obj`, `glb`, etc.

### Example Command:
If you want to convert `.glb` files from the `glb` folder to `.fbx` format and save them in the `fbx` folder, run:

```bash
python converter_glb_to_fbx_windows.py glb fbx
```

The script will read all `.glb` files from the `glb` folder, convert them to `.fbx` format, and save the output in the `fbx` folder.

### Notes:
- Make sure that the **target folder** already exists, or the script will create it for you.
- Ensure the required Python libraries (such as `trimesh`, `glob`, `bpy`, etc.) are installed on your system.
- **Note that you can only import objects in the glb format and export them to formats like fbx or gltf.**

---

## Requirements

To use this script, you need to install the following dependencies:

- **`trimesh`**: For 3D mesh handling.
- **`pyassimp`**: For importing and exporting 3D models in various formats.
- **`bpy`**: If Blender is needed for specific format conversions.
- Other necessary dependencies will be installed automatically when running the script.

To install the required libraries, you can use `pip`:

```bash
pip install trimesh glob bpy
```

---

## `requirements_windows.txt`

If you're using **Windows**, you can install the dependencies from the `requirements_windows.txt` file, which includes all the necessary libraries for this script. You can install the requirements by running the following command in your terminal:

1. First, create a `requirements_windows.txt` file containing the following lines:

```
trimesh
glob
bpy
```

2. Install the dependencies by running:

```bash
pip install -r requirements_windows.txt
```

This will ensure that all required libraries are installed for Windows.
