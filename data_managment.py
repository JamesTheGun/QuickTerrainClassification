
import os
import torch
from typing import List, Tuple
from constants import ESPSG, RES
import subprocess
import rasterio

def save_output_as_shape(model_results: torch.Tensor, output_path: str):
    pass

def load_data(geotiff_path: str) -> torch.Tensor:
    with rasterio.open(geotiff_path) as reader:
        data = reader.read(masked=True)
    data = data[0]
    tensor = torch.from_numpy(data).float()
    return tensor

def standardised_path(path: str) -> str:
    return path.replace(".tif", "_STANDARDISED.tif")

def standardise_geotiff(target_path: str, write_path: str, force: bool = False):
    if os.path.exists(write_path) and not force:
        print(f"Standardised file already exists at {write_path}. Skipping. Use force=True to override.")
        return
    
    p = subprocess.run(
        [
            "gdalwarp",
            "-t_srs", ESPSG,
            "-tr", RES, RES,
            "-tap",
            "-r", "bilinear",
            "-of", "GTiff",
            "-overwrite",
            target_path,
            write_path,
        ],
        capture_output=True,
        text=True,
    )

    if p.returncode != 0:
        raise RuntimeError(p.stderr)