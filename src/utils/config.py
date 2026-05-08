import json
import os

DEFAULT_CONFIG = {
    "project_name": "Amigo/X4ra",
    "asset_paths": {
        "music": "E:\\musica\\x4ra_ara"
    },
    "mode": "hybrid"
}

def load_config(config_path="data/config.json"):
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return DEFAULT_CONFIG

def save_config(config, config_path="data/config.json"):
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
