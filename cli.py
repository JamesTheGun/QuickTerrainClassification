import argparse
import sys
from pathlib import Path

from core import run_model

def main():
    """Main entry point for the terrain classification CLI."""
    parser = argparse.ArgumentParser(
        description="Terrain classification using TIFF files and trained models"
    )
    
    parser.add_argument(
        "target_tiff_dir",
        type=str,
        help="Directory containing target TIFF files"
    )
    
    parser.add_argument(
        "model_dir",
        type=str,
        help="Directory containing trained model files"
    )
    
    parser.add_argument(
        "output_shape_dir",
        type=str,
        help="Directory where output shapefiles will be written"
    )
    
    args = parser.parse_args()
    
    # Validate directories exist
    target_tiff_path = Path(args.target_tiff_dir)
    model_path = Path(args.model_dir)
    
    if not target_tiff_path.exists():
        print(f"Error: target_tiff_dir '{args.target_tiff_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not model_path.exists():
        print(f"Error: model_dir '{args.model_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    output_path = Path(args.output_shape_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    run_model(input_path=target_tiff_path, model_path=model_path, output_path=output_path)
    
    print(f"Processing TIFF files from: {args.target_tiff_dir}")

    print(f"Using model from: {args.model_dir}")

    print(f"Output will be saved to: {args.output_shape_dir}")



if __name__ == "__main__":
    main()
