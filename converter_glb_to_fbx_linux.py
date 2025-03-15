import os
import sys

import glob
import bpy

def substring_between(s, delim1, delim2):
    return s.partition(delim1)[2].partition(delim2)[0]

def converter(sourcefolder, targetfolder):
    outputdir = f"{targetfolder}"
    os.makedirs("gltf", exist_ok=True)
    os.makedirs(outputdir, exist_ok=True)

    files = glob.glob(f"{sourcefolder}/*.{sourcefolder}")

    for file in files:
        print(file)

        filename = substring_between(file, "/", ".")
        print(filename)
        
        bpy.ops.import_scene.gltf(filepath=f"{sourcefolder}/{filename}.{sourcefolder}",
            filter_glob="*.glb;*.gltf", 
            import_pack_images=True,
            merge_vertices=False,
            import_shading="NORMALS",
            bone_heuristic="BLENDER",
            disable_bone_shape=False,
            bone_shape_scale_factor=1.0,
            guess_original_bind_pose=True,
            import_webp_texture=False)
        bpy.ops.export_scene.fbx(filepath=f"{targetfolder}/{filename}.{targetfolder}",
            use_selection=True,            
            apply_unit_scale=True,         
            apply_scale_options='FBX_SCALE_NONE',  
            use_mesh_modifiers=True, 
            use_tspace=True,
            add_leaf_bones=False,
        )


converter(sys.argv[1], sys.argv[2])