import os
import pandas as pd
from sklearn.model_selection import train_test_split

# === Config ===
DATASET = "alexteboul/diabetes-health-indicators-dataset"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAWDATA_DIR = os.path.join(SCRIPT_DIR, "raw")
SPLIT_DATA_DIR = os.path.join(SCRIPT_DIR, "split")
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
api.dataset_download_files(dataset=DATASET, path=RAWDATA_DIR, unzip=True)

print(f"✅ Downloaded: '{DATASET}' into '{RAWDATA_DIR}'")


os.makedirs(SPLIT_DATA_DIR, exist_ok=True)

df_raw = pd.read_csv(
    os.path.join(RAWDATA_DIR, "diabetes_012_health_indicators_BRFSS2015.csv")
)

X_train, X_temp = train_test_split(df_raw, random_state=42, test_size=0.15)
X_val, X_test = train_test_split(X_temp, random_state=42, test_size=0.33)


X_train.to_csv(os.path.join(SPLIT_DATA_DIR, "train_raw_split.csv"), index=False)
X_val.to_csv(os.path.join(SPLIT_DATA_DIR, "validation_raw_split.csv"), index=False)
X_test.to_csv(os.path.join(SPLIT_DATA_DIR, "test_raw_split.csv"), index=False)
