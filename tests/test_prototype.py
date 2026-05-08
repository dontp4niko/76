import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.orchestrator.orchestrator import Orchestrator
from src.agents.base_agent import BaseAgent, Task
from src.memory.memory_manager import MemoryManager

class MockAgent(BaseAgent):
    def execute(self, task: Task) -> Task:
        print(f"MockAgent {self.name} executing task: {task.description}")
        task.result = f"Result of {task.description} by {self.name}"
        return task

def main():
    print("--- Starting Amigo/X4ra Prototype Test ---")

    # Initialize Memory
    memory = MemoryManager(storage_path="data/test_memory")
    memory.clear()

    # Initialize Orchestrator
    orchestrator = Orchestrator(memory)

    # Register Agents
    researcher = MockAgent("Dr. Know", "researcher")
    coder = MockAgent("Bit Buddy", "coder")

    orchestrator.register_agent(researcher)
    orchestrator.register_agent(coder)

    # Route Tasks
    print("\nRouting Task 1...")
    res1 = orchestrator.route_task("Research AAAA game trends", "researcher")
    print(f"Task 1 Status: {res1.status}, Result: {res1.result}")

    print("\nRouting Task 2...")
    res2 = orchestrator.route_task("Write engine initialization script", "coder")
    print(f"Task 2 Status: {res2.status}, Result: {res2.result}")

    print("\nRouting Task 3 (Should Fail)...")
    res3 = orchestrator.route_task("Design character art", "artist")
    print(f"Task 3 Status: {res3.status}, Result: {res3.result}")

    # Verify Memory
    print("\n--- Shared Memory Logs ---")
    history = memory.read_all()
    for log in history.get("logs", []):
        print(f"[{log['task_id']}] {log['agent']}: {log['result']}")

    # Summary
    summary = orchestrator.get_summary()
    print(f"\nSummary: {summary}")
    print("\n--- Prototype Test Complete ---")

if __name__ == "__main__":
    main()
