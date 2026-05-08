from src.agents.base_agent import BaseAgent, Task

class CreativeAgent(BaseAgent):
    def __init__(self, name: str, music_path: str):
        super().__init__(name, "creative")
        self.music_path = music_path

    def execute(self, task: Task) -> Task:
        print(f"CreativeAgent {self.name} processing: {task.description}")

        # Prototype logic for using the music path
        if "music" in task.description.lower() or "audio" in task.description.lower():
            task.result = f"Asset found in {self.music_path}. Integrating into {task.description}."
        else:
            task.result = f"Narrative concept for: {task.description}"

        return task
