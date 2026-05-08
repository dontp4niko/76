import json
import os
from typing import Any, Dict, List

class MemoryManager:
    def __init__(self, storage_path: str = "data/memory"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
        self.memory_file = os.path.join(self.storage_path, "shared_memory.json")
        self._initialize_memory()

    def _initialize_memory(self, force: bool = False):
        if force or not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({"logs": [], "knowledge": {}, "project_files": []}, f)

    def store(self, key: str, value: Any):
        data = self.read_all()
        data[key] = value
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=4)

    def append_log(self, log_entry: Dict[str, Any]):
        data = self.read_all()
        data.setdefault("logs", []).append(log_entry)
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=4)

    def read_all(self) -> Dict[str, Any]:
        with open(self.memory_file, 'r') as f:
            return json.load(f)

    def clear(self):
        self._initialize_memory(force=True)
