import yaml
from crewai import Agent, Task

class AgentTaskBuilder:
    def __init__(self, llm, agents_yaml='crew_config/agents.yaml', tasks_yaml='crew_config/tasks.yaml'):
        self.llm = llm
        self.agents_config = self._load_yaml(agents_yaml)["agents"]
        self.tasks_config = self._load_yaml(tasks_yaml)["tasks"]
        self.agents = {}

    def _load_yaml(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def build_agents(self):
        for agent_def in self.agents_config:
            print(f"Building agent: {agent_def['id']}")
            agent = Agent(
                role=agent_def["role"],
                goal=agent_def["goal"],
                backstory=agent_def["backstory"],
                verbose=True,
                llm=self.llm
            )
            self.agents[agent_def["id"]] = agent
        return self.agents

    def build_tasks(self):
        tasks = []
        for task_def in self.tasks_config:
            print(f"Building task: {task_def['id']}")
            agent = self.agents[task_def["agent"]]
            task = Task(
                description=task_def["description"],
                expected_output=task_def["expected_output"],
                agent=agent
            )
            tasks.append(task)
        return tasks
