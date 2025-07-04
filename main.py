import os
import base64
import requests
import csv
from datetime import datetime, timezone
from tqdm import tqdm
import json

# === Config ===
# Load configuration from config.json
with open("config.json") as config_file:
    config = json.load(config_file)
API_URL = config["API_URL"]
AI_FOLDER = "ai"
NON_AI_FOLDER = "non_ai"
OUTPUT_CSV = "results.csv"
CONFIDENCE_THRESHOLD = 0.5

def encode_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def build_payload(base64_string):
    return {
        "task_id": "test_task_base64",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "data": {
            "type": "image",
            "payload": base64_string
        }
    }

def send_request(image_b64):
    try:
        res = requests.post(API_URL, json=build_payload(image_b64))
        return res.json()
    except Exception as e:
        print(f"[ERROR] Request failed: {e}")
        return None

def process_folder(folder_path, true_label):
    results = []
    files = [fname for fname in os.listdir(folder_path) if fname.lower().endswith((".png", ".jpeg", ".jpg"))]
    for fname in tqdm(files, desc=f"Processing {folder_path}"):
        path = os.path.join(folder_path, fname)
        b64 = encode_image_base64(path)
        response = send_request(b64)

        if not response or "result" not in response:
            results.append([fname, true_label, "error", "N/A", False])
            continue

        score = response["result"].get("confidence_score", 0)
        predicted_label = "AI" if score >= CONFIDENCE_THRESHOLD else "Non-AI"
        is_correct = (predicted_label == true_label)

        results.append([fname, true_label, predicted_label, score, is_correct])

    return results

def main():
    all_results = []
    all_results += process_folder(AI_FOLDER, "AI")
    all_results += process_folder(NON_AI_FOLDER, "Non-AI")

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "source_label", "predicted_label", "confidence_score", "is_correct"])
        writer.writerows(all_results)

    total = len(all_results)
    correct = sum(1 for r in all_results if r[4])
    print(f"\n✅ Accuracy: {correct}/{total} = {correct / total:.2%}")

if __name__ == "__main__":
    main()
