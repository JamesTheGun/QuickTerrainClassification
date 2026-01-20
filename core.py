from data_managment import standardise_geotiff, standardised_path, load_datam, save_output
from model_managment import load_model, predict

def run_model(input_path: str, model_path: str, output_path: str):
    standardise_geotiff(input_path, standardised_path(input_path), force=False)
    model = load_model(model_path)
    data = load_data(standardised_path(input_path))
    prediction = predict(model, input_path)
    save_output(standardised_path(input_path), output_path)
