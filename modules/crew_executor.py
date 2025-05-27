from crewai import Crew

class CrewExecutor:
    def __init__(self, agents: list, tasks: list):
        self.agents = agents # list(set(agents))
        self.tasks = tasks

    def run(self):
        crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )
        result = crew.kickoff()
        return result