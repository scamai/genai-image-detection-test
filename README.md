# AI Image Detection Test

*Note: The API URL is not provided directly in this repository. Please contact us to receive it.*

This project evaluates an AI image detection API by sending images from two folders (`ai/` and `non_ai/`) and recording the results.

## Project Structure

- `ai/` — Folder containing AI-generated images (`.png`, `.jpg`, `.jpeg`)
- `non_ai/` — Folder containing non-AI (real) images (`.png`, `.jpg`, `.jpeg`)
- `main.py` — Main script to run the evaluation
- `results.csv` — Output file with results after running the script

## Setup Instructions

1. **Clone the repository and navigate to the project directory.**

2. **Create a Python virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` does not exist, install manually:
   ```bash
   pip install requests tqdm
   ```

4. **Ensure your image folders are populated:**
   - Place AI-generated images in the `ai/` folder.
   - Place real/non-AI images in the `non_ai/` folder.

5. **Check the API endpoint:**
   - The API URL will be sent to you via email. Please update `config.json` with the provided URL.
   - If you haven't received the API server address, please contact us.

## Running the Script

Activate your virtual environment if not already active:
```bash
source venv/bin/activate
```

Run the script:
```bash
python main.py
```

You will see a progress bar for each folder. When finished, the script prints the overall accuracy and writes detailed results to `results.csv`.

## Output
- **results.csv** — Contains columns: `filename`, `source_label`, `predicted_label`, `confidence_score`, `is_correct`
- **Terminal output** — Shows progress and final accuracy

## Troubleshooting
- **ModuleNotFoundError:**
  - Make sure you installed dependencies in your virtual environment.
- **API errors or timeouts:**
  - Ensure the API endpoint is correct and accessible from your machine.
- **No images processed:**
  - Check that your `ai/` and `non_ai/` folders contain valid image files.

## License
This project is for evaluation and testing purposes only. 