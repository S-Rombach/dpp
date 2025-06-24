import os

# === Config ===
DATASET = "alexteboul/diabetes-health-indicators-dataset"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(SCRIPT_DIR, "raw")
KAGGLE_JSON = os.path.expanduser("~/.kaggle/kaggle.json")

# === Check if kaggle.json exists ===
if not os.path.exists(KAGGLE_JSON):
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)
    print(f"✅ Created directory: '{kaggle_dir}'")

    raise FileNotFoundError(
        f"kaggle.json not found at '{KAGGLE_JSON}'\n"
        "Get it via: https://www.kaggle.com → Account → Create New API Token.\n"
        f"Place the file at '{KAGGLE_JSON}'.\n"
    )

# The __init__ of KaggleApi will try to read the kaggle.json file
# and throw an error if it doesn't exist or is not readable.
# The former error is easier to read.
from kaggle.api.kaggle_api_extended import KaggleApi

# === Download dataset ===
api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset=DATASET, path=TARGET_DIR, unzip=True)

print(f"✅ Downloaded: '{DATASET}' → '{TARGET_DIR}'")
