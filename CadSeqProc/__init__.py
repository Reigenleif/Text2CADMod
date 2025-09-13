# __init__.py for CadSeqProc
# Import functions/classes needed for:
# 1. Generating a displayable 3D model from defined JSON 3D model
# 2. Evaluating diff between two 3D models
# 3. Modifying a 3D model defined in JSON

from .cad_sequence import (
    CADSequence,
    json_to_vec,
    from_dict,
    from_minimal_json,
    json_to_NormalizedCAD,
    json_to_pc,
    create_cad_model,
    create_mesh,
    sample_points,
    save_points,
    save_stp,
    save_mesh_vertices_as_point_cloud,
    mask_point_cloud_in_bbox,
    get_bounding_box_per_model,
    get_skt_pc_mask,
    create_cumulative_model,
    create_intermediate_model,
    get_cumulative_bounding_box,
    create_bbox_from_ext_vec,
    accuracyReport,
    generate_report,
    # ... add more as needed for 3D model ops
)
from .utility.utils import (
    chamfer_dist,
    point_distance,
    write_ply_colors,
    write_ply_with_binary_values,
    normalize_pc,
    random_sample_points,
    # ... add more as needed for diff/eval
)
from .sequence.transformation.extrude_sequence import ExtrudeSequence
from .sequence.sketch.sketchsequence import SketchSequence

# Optionally import geometry, OCCUtils, etc. as needed for advanced ops
