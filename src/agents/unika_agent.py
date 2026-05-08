from src.agents.base_agent import BaseAgent, Task

class UnikaAgent(BaseAgent):
    """
    UnikaAgent: Specialized Game Developer agent focused on system design,
    combat mechanics, and engine-level implementation.
    """
    def __init__(self, name: str = "Unika"):
        super().__init__(name, "developer")

    def execute(self, task: Task) -> Task:
        print(f"UnikaAgent {self.name} developing: {task.description}")

        # Logic for game development tasks
        desc = task.description.lower()
        if "combat" in desc or "mechanics" in desc:
            task.result = f"Unika implemented advanced combat systems: {task.description}"
        elif "engine" in desc or "system" in desc:
            task.result = f"Unika optimized core engine systems for: {task.description}"
        else:
            task.result = f"Unika completed game development task: {task.description}"

        return task
