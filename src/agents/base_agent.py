from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class Task:
    id: str
    description: str
    context: Optional[Dict[str, Any]] = None
    assigned_to: Optional[str] = None
    status: str = "pending"
    result: Any = None

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def execute(self, task: Task) -> Task:
        pass

    def __str__(self):
        return f"{self.name} ({self.role})"
