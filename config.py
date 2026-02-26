"""
LoxieSockie Configuration
"""

from pathlib import Path
import os

# paths
BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / "models" / "best_ncnn_model"
SNAPSHOT_DIR = BASE_DIR / "snapshots"
DB_PATH = BASE_DIR / "loxiesockie.db"

SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

# model
CONFIDENCE_THRESHOLD = 0.6
CONTAINMENT_THRESHOLD = 0.7 # how much % of the sock box needs to be inside the dog box to trigger an alert
DOG_CLASS_ID = 16 # in the standard COCO dataset, dog is class 16
SOCK_CLASS_ID = 0 # tbd

# alert
COOLDOWN_SECONDS = 30
NTFY_TOPIC = "loxiesockie"
NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}" #tbd

# camera + photos
CAMERA_RESOLUTION = (640, 480) # from yolo input size
CAMERA_FORMAT = "RGB888"
MAX_SNAPSHOTS = 500
INPUT_SIZE = 640