from typing import Dict, List, Optional
from src.agents.base_agent import BaseAgent, Task
from src.memory.memory_manager import MemoryManager

class Orchestrator:
    def __init__(self, memory_manager: MemoryManager):
        self.agents: Dict[str, BaseAgent] = {}
        self.memory = memory_manager
        self.task_history: List[Task] = []

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.role] = agent
        print(f"Agent Registered: {agent}")

    def route_task(self, description: str, role: str, context: Optional[dict] = None) -> Task:
        task_id = f"task_{len(self.task_history) + 1}"
        task = Task(id=task_id, description=description, context=context)

        if role in self.agents:
            print(f"Routing task '{description}' to {role}")
            task.assigned_to = self.agents[role].name
            task.status = "in_progress"

            # Execute agent logic
            result_task = self.agents[role].execute(task)
            result_task.status = "completed"

            self.task_history.append(result_task)
            self.memory.append_log({
                "task_id": result_task.id,
                "agent": result_task.assigned_to,
                "description": result_task.description,
                "result": result_task.result
            })
            return result_task
        else:
            task.status = "failed"
            task.result = f"Error: No agent found for role '{role}'"
            self.task_history.append(task)
            return task

    def get_summary(self):
        return {
            "total_tasks": len(self.task_history),
            "registered_agents": list(self.agents.keys())
        }

# Adding a small correction to Task to include role for routing if needed,
# though description/role pairing usually happens in Orchestrator logic.
