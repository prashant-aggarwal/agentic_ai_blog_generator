from crewai import Crew, Agent, Task, LLM, Process
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

@CrewBase
class CrewGenerator:
    def __init__(self) -> None:
        load_dotenv()
        self.llm = LLM(
            model=os.getenv("MODEL_ID"),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_region_name=os.getenv("AWS_REGION_NAME")
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.llm,
        )
    
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            llm=self.llm,
        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            llm=self.llm,
        )
    
    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research'],
            tools=[],
        )
    
    @task
    def summarize(self) -> Task:
        return Task(
            config=self.tasks_config['summarize'],
            tools=[],
        )
    
    @task
    def blog(self) -> Task:
        return Task(
            config=self.tasks_config['blog'],
            tools=[],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )